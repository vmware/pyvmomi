.. _vim.Task: ../../vim/Task.rst

.. _vim.alarm.AlarmInfo: ../../vim/alarm/AlarmInfo.rst

.. _vim.alarm.AlarmSpec: ../../vim/alarm/AlarmSpec.rst

.. _vim.fault.InvalidName: ../../vim/fault/InvalidName.rst

.. _vim.fault.DuplicateName: ../../vim/fault/DuplicateName.rst

.. _vmodl.fault.InvalidArgument: ../../vmodl/fault/InvalidArgument.rst

.. _vim.ExtensibleManagedObject: ../../vim/ExtensibleManagedObject.rst


vim.alarm.Alarm
===============
  This managed object type defines an alarm that is triggered and an action that occurs due to the triggered alarm when certain conditions are met on a specific `ManagedEntity`_ object.


:extends: vim.ExtensibleManagedObject_


Attributes
----------
    info (`vim.alarm.AlarmInfo`_):
      privilege: System.View
       Information about this alarm.


Methods
-------


RemoveAlarm():
   Removes the alarm.


  Privilege:
               Alarm.Delete



  Args:


  Returns:
    None
         


ReconfigureAlarm(spec):
   Reconfigures the alarm properties. This operation requires access privileges on the entity with which the alarm is associated.In addition to the Alarm.Edit privilege, may also require the Global.ScriptAction if a RunScriptAction action is specified in the AlarmSpec.


  Privilege:
               Alarm.Edit



  Args:
    spec (`vim.alarm.AlarmSpec`_):
       The new specification for the alarm.




  Returns:
    None
         

  Raises:

    `vim.fault.InvalidName`_: 
       if the alarm name is empty or too long.

    `vim.fault.DuplicateName`_: 
       if an alarm with the name already exists.

    `vmodl.fault.InvalidArgument`_: 
       if the specification is invalid.


