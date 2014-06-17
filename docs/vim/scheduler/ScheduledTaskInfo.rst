.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _object: https://docs.python.org/2/library/stdtypes.html

.. _vim.Task: ../../vim/Task.rst

.. _datetime: https://docs.python.org/2/library/stdtypes.html

.. _taskObject: ../../vim/scheduler/ScheduledTaskInfo.rst#taskObject

.. _vim.ManagedEntity: ../../vim/ManagedEntity.rst

.. _vim.TaskInfo.State: ../../vim/TaskInfo/State.rst

.. _vmodl.ManagedObject: ../../vim.ExtensibleManagedObject.rst

.. _vmodl.LocalizedMethodFault: ../../vmodl/LocalizedMethodFault.rst

.. _vim.scheduler.ScheduledTask: ../../vim/scheduler/ScheduledTask.rst

.. _vim.scheduler.ScheduledTaskSpec: ../../vim/scheduler/ScheduledTaskSpec.rst


vim.scheduler.ScheduledTaskInfo
===============================
  The scheduled task details.
:extends: vim.scheduler.ScheduledTaskSpec_

Attributes:
    scheduledTask (`vim.scheduler.ScheduledTask`_):

       Scheduled task object.
    entity (`vim.ManagedEntity`_):

       The entity on which related events will be logged. If the task is scheduled on a ManagedEntity, this field will also reflect the same ManagedEntity. If task is scheduled on a ManagedObject, this field will have information about the entity on which the events will be logged on behalf of the ManagedObject. ManagedObject itself will be denoted by `taskObject`_ 
    lastModifiedTime (`datetime`_):

       The time the scheduled task is created or modified.
    lastModifiedUser (`str`_):

       Last user that modified the scheduled task.
    nextRunTime (`datetime`_, optional):

       The next time the scheduled task will run.
    prevRunTime (`datetime`_, optional):

       The last time the scheduled task ran.
    state (`vim.TaskInfo.State`_):

       Scheduled task state.
    error (`vmodl.LocalizedMethodFault`_, optional):

       The fault code when the scheduled task state is "error".
    result (`object`_, optional):

       The operation result when the scheduled task state is "success".
    progress (`int`_, optional):

       The task progress when the scheduled task state is "running".
    activeTask (`vim.Task`_, optional):

       The running task instance when the scheduled task state is "running".
    taskObject (`vmodl.ManagedObject`_):

       The object on which the scheduled task is defined. This field will have information about either the ManagedEntity or the ManagedObject on which the scheduled task is defined.
