.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _Task: ../vim/Task.rst

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _entity: ../vim/TaskInfo.rst#entity

.. _vim.Task: ../vim/Task.rst

.. _ListView: ../vim/view/ListView.rst

.. _TaskInfo: ../vim/TaskInfo.rst

.. _VI API 2.5: ../vim/version.rst#vimversionversion2

.. _vim.TaskInfo: ../vim/TaskInfo.rst

.. _HistoryCollector: ../vim/HistoryCollector.rst

.. _ExtensionManager: ../vim/ExtensionManager.rst

.. _vim.TaskFilterSpec: ../vim/TaskFilterSpec.rst

.. _vmodl.ManagedObject: ../vim.ExtensibleManagedObject.rst

.. _vim.TaskDescription: ../vim/TaskDescription.rst

.. _TaskHistoryCollector: ../vim/TaskHistoryCollector.rst

.. _vim.fault.InvalidState: ../vim/fault/InvalidState.rst

.. _vim.TaskHistoryCollector: ../vim/TaskHistoryCollector.rst

.. _vmodl.fault.InvalidArgument: ../vmodl/fault/InvalidArgument.rst


vim.TaskManager
===============
  The TaskManager managed object provides an interface for creating and managing `Task`_ managed objects. Many operations are non-blocking, returning a `Task`_ managed object that can be monitored by a client application. `Task`_ managed objects may also be accessed through the TaskManager.




Attributes
----------
    recentTask ([`vim.Task`_]):
      privilege: System.View
       A list of `Task`_ managed objects that completed recently, that are currently running, or that are queued to run.The list contains only `Task`_ objects that the client has permission to access, which is determined by having permission to access the `Task`_ object's managed `entity`_ .The completed `Task`_ objects by default include only `Task`_ objects that completed within the past 10 minutes. When connected to vCenter Server, there is an additional default limitation that each of the completed `Task`_ objects in this list is one of the last 200 completed `Task`_ objects.This property should not be used for tracking `Task`_ completion. Generally, a `ListView`_ is a better way to monitor a specific set of `Task`_ objects. In releases after vSphere API 5.0, vSphere Servers might not generate property collector update notifications for this property. To obtain the latest value of the property, you can use PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx. If you use the PropertyCollector.WaitForUpdatesEx method, specify an empty string for the version parameter. Any other version value will not produce any property values as no updates are generated.
    description (`vim.TaskDescription`_):
      privilege: System.View
       Locale-specific, static strings that describe `Task`_ information to users.
    maxCollector (`int`_):
      privilege: System.View
       Maximum number of `TaskHistoryCollector`_ data objects that can exist concurrently, per client.


Methods
-------


CreateCollectorForTasks(filter):
   Creates a `TaskHistoryCollector`_ , a specialized `HistoryCollector`_ that gathers `TaskInfo`_ data objects.A `TaskHistoryCollector`_ does not persist beyond the current client session.


  Privilege:
               System.View



  Args:
    filter (`vim.TaskFilterSpec`_):
       The specification for the task query filter.




  Returns:
    `vim.TaskHistoryCollector`_:
         The task collector based on the filter.

  Raises:

    `vim.fault.InvalidState`_: 
       if there are more than the maximum number of task collectors.

    `vmodl.fault.InvalidArgument`_: 
       if the filter is null or unknown.


CreateTask(obj, taskTypeId, initiatedBy, cancelable, parentTaskKey):
   Creates a new `Task`_ , specifying the object with which the `Task`_ is associated, the type of task, and whether the task is cancelable. Use this operation in conjunction with the `ExtensionManager`_ .
  since: `VI API 2.5`_


  Privilege:
               Task.Create



  Args:
    obj (`vmodl.ManagedObject`_):
       ManagedObject with which Task will be associated


    taskTypeId (`str`_):
       Extension registered task type identifier for type of task being created


    initiatedBy (`str`_, optional):
       The name of the user on whose behalf the Extension is creating the task


    cancelable (`bool`_):
       True if the task should be cancelable, else false


    parentTaskKey (`str`_, optional, since `vSphere API 4.0`_ ):
       Key of the task that is the parent of this task




  Returns:
    `vim.TaskInfo`_:
          `TaskInfo`_ data object describing the new task


