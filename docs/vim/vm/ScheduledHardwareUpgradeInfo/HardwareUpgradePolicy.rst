vim.vm.ScheduledHardwareUpgradeInfo.HardwareUpgradePolicy
=========================================================
  The policy setting used to determine when to perform scheduled upgrades for a virtual machine.
  :contained by: `vim.vm.ScheduledHardwareUpgradeInfo <vim/vm/ScheduledHardwareUpgradeInfo.rst>`_

  :type: `vim.vm.ScheduledHardwareUpgradeInfo.HardwareUpgradePolicy <vim/vm/ScheduledHardwareUpgradeInfo/HardwareUpgradePolicy.rst>`_

  :name: always

values:
--------

always
   Always run scheduled upgrades.

never
   No scheduled upgrades.

onSoftPowerOff
   Run scheduled upgrades only on normal guest OS shutdown.
