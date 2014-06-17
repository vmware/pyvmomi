.. _vim.Task: ../../vim/Task.rst

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.ManagedEntity: ../../vim/ManagedEntity.rst

.. _vmodl.ManagedObject: ../../vim.ExtensibleManagedObject.rst

.. _vim.fault.InvalidName: ../../vim/fault/InvalidName.rst

.. _vim.fault.DuplicateName: ../../vim/fault/DuplicateName.rst

.. _vmodl.fault.InvalidArgument: ../../vmodl/fault/InvalidArgument.rst

.. _vim.scheduler.ScheduledTask: ../../vim/scheduler/ScheduledTask.rst

.. _vim.scheduler.ScheduledTaskSpec: ../../vim/scheduler/ScheduledTaskSpec.rst

.. _vim.scheduler.ScheduledTaskDescription: ../../vim/scheduler/ScheduledTaskDescription.rst


vim.scheduler.ScheduledTaskManager
==================================
  Object manager for scheduled tasks.




Attributes
----------
    scheduledTask (`vim.scheduler.ScheduledTask`_):
      privilege: System.View
       All available scheduled tasks.
    description (`vim.scheduler.ScheduledTaskDescription`_):
      privilege: System.View
       Static descriptive strings used in scheduled tasks.


Methods
-------


CreateScheduledTask(entity, spec):
   Creates a scheduled task.


  Privilege:



  Args:
    entity (`vim.ManagedEntity`_):
       The managed entity (or entities) for which the scheduled task triggers an action. You can schedule tasks on any managed entity. If the scheduled task is associated with a leaf node in the inventory tree, it applies only to a single entity (virtual machine or host). If the task is associated with a folder, a datacenter, a compute resource, or a resource pool, it applies to the virtual machine or host descendants of the entity.


    spec (`vim.scheduler.ScheduledTaskSpec`_):
       The specification for the new scheduled task.




  Returns:
    `vim.scheduler.ScheduledTask`_:
         The scheduled task created by the operation.

  Raises:

    `vim.fault.InvalidName`_: 
       if the scheduled task name is empty or too long.

    `vim.fault.DuplicateName`_: 
       if a scheduled task with the name already exists.

    `vmodl.fault.InvalidArgument`_: 
       if the specification is invalid.


RetrieveEntityScheduledTask(entity):
   Available scheduled tasks defined on the entity.


  Privilege:
               System.View



  Args:
    entity (`vim.ManagedEntity`_, optional):
       The entity. If null, all scheduled tasks are returned for visible entities.




  Returns:
    `vim.scheduler.ScheduledTask`_:
         The scheduled tasks.


CreateObjectScheduledTask(obj, spec):
   Creates a scheduled task.
  since: `vSphere API 4.0`_


  Privilege:



  Args:
    obj (`vmodl.ManagedObject`_):
       The managed object for which the scheduled task triggers an action. You can schedule tasks on any managed object.


    spec (`vim.scheduler.ScheduledTaskSpec`_):
       The specification for the new scheduled task.




  Returns:
    `vim.scheduler.ScheduledTask`_:
         The scheduled task created by the operation.

  Raises:

    `vim.fault.InvalidName`_: 
       if the scheduled task name is empty or too long.

    `vim.fault.DuplicateName`_: 
       if a scheduled task with the name already exists.

    `vmodl.fault.InvalidArgument`_: 
       if the specification is invalid.


RetrieveObjectScheduledTask(obj):
   Available scheduled tasks defined on the object.
  since: `vSphere API 4.0`_


  Privilege:
               System.View



  Args:
    obj (`vmodl.ManagedObject`_, optional):
       The object. If not specified, all scheduled tasks are returned for visible entities and visible ManagedObjects.




  Returns:
    `vim.scheduler.ScheduledTask`_:
         The scheduled tasks.


