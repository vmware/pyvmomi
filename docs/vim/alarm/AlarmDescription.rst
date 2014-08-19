
vim.alarm.AlarmDescription
==========================
  Static strings for alarms.
:extends: vmodl.DynamicData_

Attributes:
    expr ([`vim.TypeDescription <vim/TypeDescription.rst>`_]):

       Descriptions of expression types for a trigger.
    stateOperator ([`vim.ElementDescription <vim/ElementDescription.rst>`_]):

        `State Operator enum description <vim/alarm/StateAlarmExpression/StateOperator.rst>`_ 
    metricOperator ([`vim.ElementDescription <vim/ElementDescription.rst>`_]):

        `MetricAlarmExpression Metric Operator enum description <vim/alarm/MetricAlarmExpression/MetricOperator.rst>`_ 
    hostSystemConnectionState ([`vim.ElementDescription <vim/ElementDescription.rst>`_]):

        `Host System Connection State enum description <vim/HostSystem/ConnectionState.rst>`_ 
    virtualMachinePowerState ([`vim.ElementDescription <vim/ElementDescription.rst>`_]):

        `Virtual Machine Power State enum description <vim/VirtualMachine/PowerState.rst>`_ 
    datastoreConnectionState ([`vim.ElementDescription <vim/ElementDescription.rst>`_]):

        `accessible <vim/Datastore/Summary.rst#accessible>`_ and `description <vim/host/MountInfo.rst#accessible>`_ 
    hostSystemPowerState ([`vim.ElementDescription <vim/ElementDescription.rst>`_]):

        `Host System Power State enum description <vim/HostSystem/PowerState.rst>`_ 
    virtualMachineGuestHeartbeatStatus ([`vim.ElementDescription <vim/ElementDescription.rst>`_]):

        `Guest Heartbeat Status enum description <vim/ManagedEntity/Status.rst>`_ 
    entityStatus ([`vim.ElementDescription <vim/ElementDescription.rst>`_]):

        `ManagedEntity Status enum description <vim/ManagedEntity/Status.rst>`_ 
    action ([`vim.TypeDescription <vim/TypeDescription.rst>`_]):

       Action class descriptions for an alarm.
