.. _vim.vm.ToolsConfigInfo: ../../../vim/vm/ToolsConfigInfo.rst

.. _vim.vm.ToolsConfigInfo.UpgradePolicy: ../../../vim/vm/ToolsConfigInfo/UpgradePolicy.rst

vim.vm.ToolsConfigInfo.UpgradePolicy
====================================
  The policy setting used to determine when tools are auto-upgraded for a virtual machine
  :contained by: `vim.vm.ToolsConfigInfo`_

  :type: `vim.vm.ToolsConfigInfo.UpgradePolicy`_

  :name: upgradeAtPowerCycle

values:
--------

manual
   No auto-upgrades for tools will be performed for this virtual machine. Users must manually invoke the UpgradeTools operation to update the tools.

upgradeAtPowerCycle
   When the virtual machine is power-cycled, the system checks for a newer version of tools when the VM comes back up. If it is available, a tools upgrade is automatically performed on the virtual machine and it is rebooted if necessary.
