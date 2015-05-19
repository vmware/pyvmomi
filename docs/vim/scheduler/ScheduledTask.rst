.. _vim.Task: ../../vim/Task.rst

.. _vim.fault.InvalidName: ../../vim/fault/InvalidName.rst

.. _vim.fault.InvalidState: ../../vim/fault/InvalidState.rst

.. _vim.fault.DuplicateName: ../../vim/fault/DuplicateName.rst

.. _vmodl.fault.InvalidArgument: ../../vmodl/fault/InvalidArgument.rst

.. _vim.ExtensibleManagedObject: ../../vim/ExtensibleManagedObject.rst

.. _vim.scheduler.ScheduledTaskInfo: ../../vim/scheduler/ScheduledTaskInfo.rst

.. _vim.scheduler.ScheduledTaskSpec: ../../vim/scheduler/ScheduledTaskSpec.rst


vim.scheduler.ScheduledTask
===========================
  The scheduled task object.


:extends: vim.ExtensibleManagedObject_


Attributes
----------
    info (`vim.scheduler.ScheduledTaskInfo`_):
       Information about the current scheduled task.


Methods
-------


RemoveScheduledTask():
   Removes the scheduled task.


  Privilege:
               ScheduledTask.Delete



  Args:


  Returns:
    None
         

  Raises:

    `vim.fault.InvalidState`_: 
       if the scheduled task is running.


ReconfigureScheduledTask(spec):
   Reconfigures the scheduled task properties.


  Privilege:
               ScheduledTask.Edit



  Args:
    spec (`vim.scheduler.ScheduledTaskSpec`_):
       The new specification for the scheduled task.




  Returns:
    None
         

  Raises:

    `vim.fault.InvalidState`_: 
       if the scheduled task is running.

    `vim.fault.InvalidName`_: 
       if the scheduled task name is empty or too long.

    `vim.fault.DuplicateName`_: 
       if a scheduled task with the name already exists.

    `vmodl.fault.InvalidArgument`_: 
       if the specification is invalid.


RunScheduledTask():
   Runs the scheduled task immediately. The schedule for future runs remains in effect.


  Privilege:
               ScheduledTask.Run



  Args:


  Returns:
    None
         

  Raises:

    `vim.fault.InvalidState`_: 
       if the scheduled task is running already.


