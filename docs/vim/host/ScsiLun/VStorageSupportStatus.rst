.. _vStorageSupport: ../../../vim/host/ScsiLun.rst#vStorageSupport

.. _vim.host.ScsiLun: ../../../vim/host/ScsiLun.rst

.. _vim.host.ScsiLun.VStorageSupportStatus: ../../../vim/host/ScsiLun/VStorageSupportStatus.rst

vim.host.ScsiLun.VStorageSupportStatus
======================================
  Storage array hardware acceleration support status. When a host boots, the support status is unknown. As a host attempts hardware-accelerated operations, it determines whether the storage device supports hardware acceleration and sets the `vStorageSupport`_ property accordingly.
  :contained by: `vim.host.ScsiLun`_

  :type: `vim.host.ScsiLun.VStorageSupportStatus`_

  :name: vStorageUnknown

values:
--------

vStorageSupported
   Storage device supports hardware acceleration. The ESX host will use the feature to offload certain storage-related operations to the device.

vStorageUnsupported
   Storage device does not support hardware acceleration. The ESX host will handle all storage-related operations.

vStorageUnknown
   Initial support status value.
