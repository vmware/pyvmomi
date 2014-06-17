.. _vim.host.LowLevelProvisioningManager: ../../../vim/host/LowLevelProvisioningManager.rst

.. _vim.host.LowLevelProvisioningManager.ReloadTarget: ../../../vim/host/LowLevelProvisioningManager/ReloadTarget.rst

vim.host.LowLevelProvisioningManager.ReloadTarget
=================================================
  The target of the disk reload.
  :contained by: `vim.host.LowLevelProvisioningManager`_

  :type: `vim.host.LowLevelProvisioningManager.ReloadTarget`_

  :name: snapshotConfig

values:
--------

currentConfig
   Specifies the reload of the current config of the virtual machine.

snapshotConfig
   Specifies the reload of the snapshot config of the virtual machine. If the virtual machine has multiple snapshots, all of the snapshot's config will be reloaded.
