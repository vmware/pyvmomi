
vim.TaskManager
===============
  The TaskManager managed object provides an interface for creating and managing `Task <vim/Task.rst>`_ managed objects. Many operations are non-blocking, returning a `Task <vim/Task.rst>`_ managed object that can be monitored by a client application. `Task <vim/Task.rst>`_ managed objects may also be accessed through the TaskManager.




Attributes
----------
    recentTask ([`vim.Task <vim/Task.rst>`_]):
      privilege: System.View
       A list of `Task <vim/Task.rst>`_ managed objects that completed recently, that are currently running, or that are queued to run.The list contains only `Task <vim/Task.rst>`_ objects that the client has permission to access, which is determined by having permission to access the `Task <vim/Task.rst>`_ object's managed `entity <vim/TaskInfo.rst#entity>`_ .The completed `Task <vim/Task.rst>`_ objects by default include only `Task <vim/Task.rst>`_ objects that completed within the past 10 minutes. When connected to vCenter Server, there is an additional default limitation that each of the completed `Task <vim/Task.rst>`_ objects in this list is one of the last 200 completed `Task <vim/Task.rst>`_ objects.This property should not be used for tracking `Task <vim/Task.rst>`_ completion. Generally, a `ListView <vim/view/ListView.rst>`_ is a better way to monitor a specific set of `Task <vim/Task.rst>`_ objects. In releases after vSphere API 5.0, vSphere Servers might not generate property collector update notifications for this property. To obtain the latest value of the property, you can use PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx. If you use the PropertyCollector.WaitForUpdatesEx method, specify an empty string for the version parameter. Any other version value will not produce any property values as no updates are generated.
    description (`vim.TaskDescription <vim/TaskDescription.rst>`_):
      privilege: System.View
       Locale-specific, static strings that describe `Task <vim/Task.rst>`_ information to users.
    maxCollector (`int <https://docs.python.org/2/library/stdtypes.html>`_):
      privilege: System.View
       Maximum number of `TaskHistoryCollector <vim/TaskHistoryCollector.rst>`_ data objects that can exist concurrently, per client.


Methods
-------


CreateCollectorForTasks(filter):
   Creates a `TaskHistoryCollector <vim/TaskHistoryCollector.rst>`_ , a specialized `HistoryCollector <vim/HistoryCollector.rst>`_ that gathers `TaskInfo <vim/TaskInfo.rst>`_ data objects.A `TaskHistoryCollector <vim/TaskHistoryCollector.rst>`_ does not persist beyond the current client session.


  Privilege:
               System.View



  Args:
    filter (`vim.TaskFilterSpec <vim/TaskFilterSpec.rst>`_):
       The specification for the task query filter.




  Returns:
    `vim.TaskHistoryCollector <vim/TaskHistoryCollector.rst>`_:
         The task collector based on the filter.

  Raises:

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if there are more than the maximum number of task collectors.

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if the filter is null or unknown.


CreateTask(obj, taskTypeId, initiatedBy, cancelable, parentTaskKey):
   Creates a new `Task <vim/Task.rst>`_ , specifying the object with which the `Task <vim/Task.rst>`_ is associated, the type of task, and whether the task is cancelable. Use this operation in conjunction with the `ExtensionManager <vim/ExtensionManager.rst>`_ .
  since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_


  Privilege:
               Task.Create



  Args:
    obj (`vmodl.ManagedObject <vim.ExtensibleManagedObject.rst>`_):
       ManagedObject with which Task will be associated


    taskTypeId (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       Extension registered task type identifier for type of task being created


    initiatedBy (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       The name of the user on whose behalf the Extension is creating the task


    cancelable (`bool <https://docs.python.org/2/library/stdtypes.html>`_):
       True if the task should be cancelable, else false


    parentTaskKey (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional, since `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_ ):
       Key of the task that is the parent of this task




  Returns:
    `vim.TaskInfo <vim/TaskInfo.rst>`_:
          `TaskInfo <vim/TaskInfo.rst>`_ data object describing the new task


