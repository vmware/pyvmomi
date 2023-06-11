#############################################################
# Copyright (c) 2005-2023 VMware, Inc.
#############################################################

# @file task.py
# @brief Task functions
#
# This module provies synchronization of client/server operations
# since many VIM operations return 'tasks' which can have
# varying completion times.
"""
Task functions

This module provies synchronization of client/server operations since
many VIM operations return 'tasks' which can have varying completion
times.
"""

__author__ = 'VMware, Inc'

from pyVmomi import vmodl, vim

import time


#
# @brief Exception class to represent when task is blocked (e.g.:
# waiting for an answer to a question.
#
class TaskBlocked(Exception):
    """
    Exception class to represent when task is blocked
    e.g.: waiting for an answer to a question
    """
    pass


#
# TaskUpdates
#     verbose information about task progress
#
def TaskUpdatesVerbose(task, progress):
    info = task.info
    if isinstance(info.progress, int):
        if not isinstance(progress, str):
            progress = '{:.0f}% ({})'.format(info.progress, info.state)
        print('Task %s (key:%s, desc:%s) - %s' %
              (info.name.info.name, info.key, info.description, progress))


globalTaskUpdate = None


def SetTasksVerbose(verbose=True):
    global globalTaskUpdate
    if verbose:
        globalTaskUpdate = TaskUpdatesVerbose
    else:
        globalTaskUpdate = None


#
# @param raiseOnError [in] Any exception thrown is thrown up to the caller if
# raiseOnError is set to true
# @param si [in] ServiceInstance to use. If set to None, use the default one.
# @param pc [in] property collector to use else retrieve one from cache
# @param maxWaitTime [in] The maximum amount of time the task is allowed to
# run. Throws an exception if raiseOnError is True.
# @param onProgressUpdate [in] callable to call with task progress updates.
#    For example:
#
#    def OnTaskProgressUpdate(task, percentDone):
#       sys.stderr.write('# Task {}: {:.0f}% complete ...\n'
#                        .format(task, percentDone))
#
# Given a task object and a service instance, wait for the task completion
#
# @return state as either "success" or "error". To look at any errors, the
# user should reexamine the task object.
#
# NOTE: This is a blocking call.
#
def WaitForTask(task,
                raiseOnError=True,
                si=None,
                pc=None,
                maxWaitTime=None,
                onProgressUpdate=None,
                log=None,
                getAllUpdates=False):
    """
    Wait for task to complete.

    @type  raiseOnError      : bool
    @param raiseOnError      : Any exception thrown is thrown up to the caller
                                if raiseOnError is set to true.
    @type  si                : ManagedObjectReference to a ServiceInstance.
    @param si                : ServiceInstance to use. If None, use the
                                information from the task.
    @type  pc                : ManagedObjectReference to a PropertyCollector.
    @param pc                : Property collector to use. If None, get it from
                                the ServiceInstance.
    @type  maxWaitTime       : numeric value
    @param maxWaitTime       : The maximum amount of time the task is allowed to
                                run. Throws an exception if raiseOnError is True.
    @type  onProgressUpdate  : callable
    @param onProgressUpdate  : The callable to call with task progress updates.
    @type  log               : Optional logger.
    @param log               : Logging.
    @type  getAllUpdates     : Optional bool value. Default is False.
    @param getAllUpdates     : Get all updates for the task.

        For example::

            def OnTaskProgressUpdate(task, percentDone):
                print 'Task {} is {:.0f}% complete.'.format(task, percentDone)
    """

    if pc is None:
        if si is None: si = vim.ServiceInstance("ServiceInstance", task._stub)
        pc = si.content.propertyCollector

    progressUpdater = ProgressUpdater(task, onProgressUpdate, getAllUpdates)
    progressUpdater.Update('created')

    filter = CreateFilter(pc, task)

    version, state = None, None

    if maxWaitTime:
        waitTime = maxWaitTime + time.time()

    # Loop looking for updates till the state moves to a completed state.
    while state not in (vim.TaskInfo.State.success, vim.TaskInfo.State.error):
        try:
            version, state = GetTaskStatus(task, version, pc)
            progressUpdater.UpdateIfNeeded()

            if maxWaitTime and waitTime < time.time():
                err = "Task exceeded timeout of %d seconds" % maxWaitTime
                progressUpdater.Update(err)
                if raiseOnError is True:
                    raise Exception(err)
                break
        except vmodl.fault.ManagedObjectNotFound as e:
            print("Task object has been deleted: %s" % e.obj)
            break

    DestroyFilter(filter)

    info = task.info
    if state == "error":
        progressUpdater.Update("error: %s" % info.error)
        if raiseOnError:
            raise info.error
        else:
            _LogMsg(log, "Task reported error: %s" % info.error)
    elif state == "success":
        progressUpdater.Update('completed')
    elif state == "queued":
        _LogMsg(log, "Task reports as queued: %s" % info)
        progressUpdater.UpdateIfNeeded()
    else:  # state = running
        _LogMsg(log, "Task reports as still running: %s" % info)
        progressUpdater.UpdateIfNeeded()

    return state


# Wait for multiple tasks to complete
#  See WaitForTask for detail
#
#  Difference: WaitForTasks won't return the state of tasks. User can check
#  tasks state directly with task.info.state
#
#  TODO: Did not check for question pending
def WaitForTasks(tasks,
                 raiseOnError=True,
                 si=None,
                 pc=None,
                 onProgressUpdate=None,
                 results=None,
                 getAllUpdates=False):
    """
    Wait for multiple tasks to complete. Much faster than calling WaitForTask
    N times.
    """

    if not tasks:
        return

    if si is None: si = vim.ServiceInstance("ServiceInstance", tasks[0]._stub)
    if pc is None: pc = si.content.propertyCollector
    if results is None: results = []

    progressUpdaters = {}
    for task in tasks:
        progressUpdater = ProgressUpdater(task, onProgressUpdate, getAllUpdates)
        progressUpdater.Update('created')
        progressUpdaters[str(task)] = progressUpdater

    filter = CreateTasksFilter(pc, tasks)

    try:
        version, state = None, None

        # Loop looking for updates till the state moves to a completed state.
        while len(progressUpdaters):
            update = pc.WaitForUpdates(version)
            for filterSet in update.filterSet:
                for objSet in filterSet.objectSet:
                    task = objSet.obj
                    taskId = str(task)
                    for change in objSet.changeSet:
                        if change.name == 'info':
                            state = change.val.state
                        elif change.name == 'info.state':
                            state = change.val
                        else:
                            continue

                        progressUpdater = progressUpdaters.get(taskId)
                        if not progressUpdater:
                            continue

                        if state == vim.TaskInfo.State.success:
                            progressUpdater.Update('completed')
                            progressUpdaters.pop(taskId)
                            # cache the results, as task objects could expire if one
                            # of the tasks take a longer time to complete
                            results.append(task.info.result)
                        elif state == vim.TaskInfo.State.error:
                            err = task.info.error
                            progressUpdater.Update('error: %s' % str(err))
                            if raiseOnError:
                                try:
                                    raise err
                                finally:
                                    del err
                            else:
                                print("Task %s reported error: %s" %
                                      (taskId, str(err)))
                                progressUpdaters.pop(taskId)
                        else:
                            if onProgressUpdate:
                                progressUpdater.UpdateIfNeeded()
            # Move to next version
            version = update.version
    finally:
        if filter:
            DestroyFilter(filter)
    return


def GetTaskStatus(task, version, pc):
    update = pc.WaitForUpdates(version)
    info = task.info
    state = info.state

    if (state == 'running' and info.name is not None and info.name.info.name
            not in ['Destroy', 'Relocate', 'CreateVm']):
        CheckForQuestionPending(info)

    return update.version, state


def CreateFilter(pc, task):
    """ Create property collector filter for task """
    return CreateTasksFilter(pc, [task])


def CreateTasksFilter(pc, tasks):
    """ Create property collector filter for tasks """
    if not tasks:
        return None

    # First create the object specification as the task object.
    objspecs = [
        vmodl.query.PropertyCollector.ObjectSpec(obj=task) for task in tasks
    ]

    # Next, create the property specification as the state.
    propspec = vmodl.query.PropertyCollector.PropertySpec(type=vim.Task,
                                                          pathSet=[],
                                                          all=True)

    # Create a filter spec with the specified object and property spec.
    filterspec = vmodl.query.PropertyCollector.FilterSpec()
    filterspec.objectSet = objspecs
    filterspec.propSet = [propspec]

    # Create the filter
    return pc.CreateFilter(filterspec, True)


def DestroyFilter(filter):
    try:
        filter.Destroy()
    except vmodl.fault.ManagedObjectNotFound:
        pass


def CheckForQuestionPending(info):
    """ Check to see if VM needs to ask a question, throw exception """

    vm = info.entity
    if vm is not None and isinstance(vm, vim.VirtualMachine):
        qst = vm.runtime.question
        if qst is not None:
            raise TaskBlocked("Task blocked, User Intervention required")


def _LogMsg(log, message):
    """Helper logging a message with logger or print depending on the flag."""
    if log:
        log(message)
    else:
        print(message)


#
# @brief Class that keeps track of task percentage complete and calls
# a provided callback when it changes.
#
class ProgressUpdater(object):
    """
    Class that keeps track of task percentage complete and calls a
    provided callback when it changes.
    """
    def __init__(self, task, onProgressUpdate, getAllUpdates=False):
        self.task = task
        self.onProgressUpdate = onProgressUpdate
        self.getAllUpdates = getAllUpdates
        self.prevProgress = 0
        self.progress = 0

    def Update(self, state):
        global globalTaskUpdate
        taskUpdate = globalTaskUpdate
        if self.onProgressUpdate:
            taskUpdate = self.onProgressUpdate
        if taskUpdate:
            taskUpdate(self.task, state)

    def UpdateIfNeeded(self):
        self.progress = self.task.info.progress

        if self.getAllUpdates or self.progress != self.prevProgress:
            self.Update(self.progress)

        self.prevProgress = self.progress
