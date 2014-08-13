.. _accessible: ../../vim/Datastore/Summary.rst#accessible

.. _description: ../../vim/host/MountInfo.rst#accessible

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.TypeDescription: ../../vim/TypeDescription.rst

.. _vim.ElementDescription: ../../vim/ElementDescription.rst

.. _State Operator enum description: ../../vim/alarm/StateAlarmExpression/StateOperator.rst

.. _ManagedEntity Status enum description: ../../vim/ManagedEntity/Status.rst

.. _Guest Heartbeat Status enum description: ../../vim/ManagedEntity/Status.rst

.. _Host System Power State enum description: ../../vim/HostSystem/PowerState.rst

.. _Virtual Machine Power State enum description: ../../vim/VirtualMachine/PowerState.rst

.. _Host System Connection State enum description: ../../vim/HostSystem/ConnectionState.rst

.. _MetricAlarmExpression Metric Operator enum description: ../../vim/alarm/MetricAlarmExpression/MetricOperator.rst


vim.alarm.AlarmDescription
==========================
  Static strings for alarms.
:extends: vmodl.DynamicData_

Attributes:
    expr ([`vim.TypeDescription`_]):

       Descriptions of expression types for a trigger.
    stateOperator ([`vim.ElementDescription`_]):

        `State Operator enum description`_ 
    metricOperator ([`vim.ElementDescription`_]):

        `MetricAlarmExpression Metric Operator enum description`_ 
    hostSystemConnectionState ([`vim.ElementDescription`_]):

        `Host System Connection State enum description`_ 
    virtualMachinePowerState ([`vim.ElementDescription`_]):

        `Virtual Machine Power State enum description`_ 
    datastoreConnectionState ([`vim.ElementDescription`_]):

        `accessible`_ and `description`_ 
    hostSystemPowerState ([`vim.ElementDescription`_]):

        `Host System Power State enum description`_ 
    virtualMachineGuestHeartbeatStatus ([`vim.ElementDescription`_]):

        `Guest Heartbeat Status enum description`_ 
    entityStatus ([`vim.ElementDescription`_]):

        `ManagedEntity Status enum description`_ 
    action ([`vim.TypeDescription`_]):

       Action class descriptions for an alarm.
