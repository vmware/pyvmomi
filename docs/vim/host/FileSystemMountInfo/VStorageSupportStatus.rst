vim.host.FileSystemMountInfo.VStorageSupportStatus
==================================================
  Status of volume's support for vStorage hardware acceleration. The ESX Server determines the status based on the capabilities of the devices that support the file system volume. When a host boots, the support status is unknown. As the ESX host attempts hardware-accelerated operations, it determines whether the storage device supports hardware acceleration and sets the `vStorageSupport <vim/host/FileSystemMountInfo.rst#vStorageSupport>`_ property accordingly.
  :contained by: `vim.host.FileSystemMountInfo <vim/host/FileSystemMountInfo.rst>`_

  :type: `vim.host.FileSystemMountInfo.VStorageSupportStatus <vim/host/FileSystemMountInfo/VStorageSupportStatus.rst>`_

  :name: vStorageUnknown

values:
--------

vStorageSupported
   Storage device supports hardware acceleration. The ESX host will use the feature to offload certain storage-related operations to the device.

vStorageUnsupported
   Storage device does not support hardware acceleration. The ESX host will handle all storage-related operations.

vStorageUnknown
   Initial support status value.
