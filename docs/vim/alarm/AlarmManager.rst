.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vim.Task: ../../vim/Task.rst

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.alarm.Alarm: ../../vim/alarm/Alarm.rst

.. _vim.ManagedEntity: ../../vim/ManagedEntity.rst

.. _vim.alarm.AlarmSpec: ../../vim/alarm/AlarmSpec.rst

.. _vim.alarm.AlarmState: ../../vim/alarm/AlarmState.rst

.. _vim.fault.InvalidName: ../../vim/fault/InvalidName.rst

.. _vim.fault.DuplicateName: ../../vim/fault/DuplicateName.rst

.. _vim.alarm.AlarmExpression: ../../vim/alarm/AlarmExpression.rst

.. _vmodl.fault.InvalidRequest: ../../vmodl/fault/InvalidRequest.rst

.. _vim.alarm.AlarmDescription: ../../vim/alarm/AlarmDescription.rst

.. _vmodl.fault.InvalidArgument: ../../vmodl/fault/InvalidArgument.rst

.. _vmodl.fault.ManagedObjectNotFound: ../../vmodl/fault/ManagedObjectNotFound.rst


vim.alarm.AlarmManager
======================
  The alarm manager is a singleton object for managing alarms within a service instance.




Attributes
----------
    defaultExpression ([`vim.alarm.AlarmExpression`_]):
      privilege: System.View
       The default setting for each alarm expression, used to populate the initial client wizard screen.
    description (`vim.alarm.AlarmDescription`_):
      privilege: System.View
       The static descriptive strings used in alarms.


Methods
-------


CreateAlarm(entity, spec):
   Creates an alarm.In addition to the Alarm.Create privilege, may also require the Global.ScriptAction if a RunScriptAction action is specified in the AlarmSpec.


  Privilege:



  Args:
    entity (`vim.ManagedEntity`_):
       The entity with which the alarm is associated.


    spec (`vim.alarm.AlarmSpec`_):
       The specification for the new alarm.




  Returns:
    `vim.alarm.Alarm`_:
         A reference to the Alarm object created by the operation.

  Raises:

    `vim.fault.InvalidName`_: 
       if the alarm name is empty or too long.

    `vim.fault.DuplicateName`_: 
       if an alarm with the name already exists.

    `vmodl.fault.InvalidArgument`_: 
       if the specification is invalid.


GetAlarm(entity):
   Available alarms defined on the entity. These alarms do not include any inherited alarms; that is, alarms associated with parent entities.


  Privilege:
               System.View



  Args:
    entity (`vim.ManagedEntity`_, optional):
       The entity. If not set, alarms are returned for all visible entities.




  Returns:
    [`vim.alarm.Alarm`_]:
         A reference to the Alarm objects returned by the operation.


AreAlarmActionsEnabled(entity):
   Returns true if alarm actions are enabled on the specified managed entity.
  since: `vSphere API 4.0`_


  Privilege:



  Args:
    entity (`vim.ManagedEntity`_):
       The managed entity to look up.




  Returns:
    `bool`_:
         


EnableAlarmActions(entity, enabled):
   Enables or disables alarms on the specified managed entity.
  since: `vSphere API 4.0`_


  Privilege:



  Args:
    entity (`vim.ManagedEntity`_):
       The managed entity on which to set a schedule.


    enabled (`bool`_):
       true, if alarms are enabled during the schedule.




  Returns:
    None
         


GetAlarmState(entity):
   The state of instantiated alarms on the entity.


  Privilege:



  Args:
    entity (`vim.ManagedEntity`_):
       The entity.




  Returns:
    [`vim.alarm.AlarmState`_]:
         The state of instantiated alarms.

  Raises:

    `vmodl.fault.InvalidRequest`_: 
       if the referenced entity is null.

    `vmodl.fault.ManagedObjectNotFound`_: 
       if the referenced entity is invalid.


AcknowledgeAlarm(alarm, entity):
   Acknowledge the alarm on a managed entity. The actions associated with the alarm will not fire until the alarm's next distinct occurrence; that is, until after the alarm has entered the green or gray states at least once. Calling this method on an acknowledged or non-triggered alarm.
  since: `vSphere API 4.0`_


  Privilege:



  Args:
    alarm (`vim.alarm.Alarm`_):
       The Alarm to acknowledge.


    entity (`vim.ManagedEntity`_):
       The ManagedEntity for which to acknowledge the Alarm.




  Returns:
    None
         

  Raises:

    `vmodl.fault.InvalidRequest`_: 
       if the referenced alarm/entity is null

    `vmodl.fault.InvalidArgument`_: 
       if the tuple doesn't exist.

    `vmodl.fault.ManagedObjectNotFound`_: 
       if the referenced alarm/entity is invalid.


