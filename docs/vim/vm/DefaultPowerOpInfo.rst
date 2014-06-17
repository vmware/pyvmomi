.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.vm.DefaultPowerOpInfo
=========================
  The DefaultPowerOpInfo data object type holds the configured defaults for the power operations on a virtual machine. The properties indicated whether to do a "soft" or guest initiated operation, or a "hard" operation.
:extends: vmodl.DynamicData_

Attributes:
    powerOffType (`str`_, optional):

       Describes the default power off type for this virtual machine. The possible values are specified by the PowerOpType.
        * hard - Perform power off by using the PowerOff method.
        * soft - Perform power off by using the ShutdownGuest method.
        * preset - The preset value is specified in the defaultPowerOffType section.
        * This setting is advisory and clients can choose to ignore it.
    suspendType (`str`_, optional):

       Describes the default suspend type for this virtual machine. The possible values are specified by the PowerOpType.
        * hard - Perform suspend by using the Suspend method.
        * soft - Perform suspend by using the StandbyGuest method.
        * preset - The preset value is specified in the defaultSuspendType section.
        * This setting is advisory and clients can choose to ignore it.
    resetType (`str`_, optional):

       Describes the default reset type for this virtual machine. The possible values are specified by the PowerOpType.
        * hard - Perform reset by using the Reset method.
        * soft - Perform reset by using the RebootGuest method.
        * preset - The preset value is specified in the defaultResetType section.
        * This setting is advisory and clients can choose to ignore it.
    defaultPowerOffType (`str`_, optional):

       Default operation for power off: soft or hard
    defaultSuspendType (`str`_, optional):

       Default operation for suspend: soft or hard
    defaultResetType (`str`_, optional):

       Default operation for reset: soft or hard
    standbyAction (`str`_, optional):

       Behavior of virtual machine when it receives the S1 ACPI call.
