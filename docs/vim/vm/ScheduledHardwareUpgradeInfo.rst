.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.1: ../../vim/version.rst#vimversionversion8

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vmodl.LocalizedMethodFault: ../../vmodl/LocalizedMethodFault.rst

.. _ScheduledHardwareUpgradeInfoHardwareUpgradePolicy: ../../vim/vm/ScheduledHardwareUpgradeInfo/HardwareUpgradePolicy.rst

.. _ScheduledHardwareUpgradeInfoHardwareUpgradeStatus: ../../vim/vm/ScheduledHardwareUpgradeInfo/HardwareUpgradeStatus.rst


vim.vm.ScheduledHardwareUpgradeInfo
===================================
  Data object type containing settings for the scheduled hardware upgrades.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.1`_

Attributes:
    upgradePolicy (`str`_, optional):

       Scheduled hardware upgrade policy setting for the virtual machine.See `ScheduledHardwareUpgradeInfoHardwareUpgradePolicy`_ 
    versionKey (`str`_, optional):

       Key for target hardware version to be used on next scheduled upgrade in the format of `key`_ .
    scheduledHardwareUpgradeStatus (`str`_, optional):

       Status for last attempt to run scheduled hardware upgrade.See `ScheduledHardwareUpgradeInfoHardwareUpgradeStatus`_ 
    fault (`vmodl.LocalizedMethodFault`_, optional):

       Contains information about the failure of last attempt to run scheduled hardware upgrade.
