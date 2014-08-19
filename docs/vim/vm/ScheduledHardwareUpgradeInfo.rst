
vim.vm.ScheduledHardwareUpgradeInfo
===================================
  Data object type containing settings for the scheduled hardware upgrades.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.1 <vim/version.rst#vimversionversion8>`_

Attributes:
    upgradePolicy (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Scheduled hardware upgrade policy setting for the virtual machine.See `ScheduledHardwareUpgradeInfoHardwareUpgradePolicy <vim/vm/ScheduledHardwareUpgradeInfo/HardwareUpgradePolicy.rst>`_ 
    versionKey (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Key for target hardware version to be used on next scheduled upgrade in the format of `key <vim/vm/ConfigOptionDescriptor.rst#key>`_ .
    scheduledHardwareUpgradeStatus (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Status for last attempt to run scheduled hardware upgrade.See `ScheduledHardwareUpgradeInfoHardwareUpgradeStatus <vim/vm/ScheduledHardwareUpgradeInfo/HardwareUpgradeStatus.rst>`_ 
    fault (`vmodl.LocalizedMethodFault <vmodl/LocalizedMethodFault.rst>`_, optional):

       Contains information about the failure of last attempt to run scheduled hardware upgrade.
