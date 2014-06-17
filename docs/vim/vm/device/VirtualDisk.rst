.. _str: https://docs.python.org/2/library/stdtypes.html

.. _long: https://docs.python.org/2/library/stdtypes.html

.. _vim.SharesInfo: ../../../vim/SharesInfo.rst

.. _vim.vm.device.VirtualDevice: ../../../vim/vm/device/VirtualDevice.rst

.. _vim.StorageResourceManager.IOAllocationInfo: ../../../vim/StorageResourceManager/IOAllocationInfo.rst

.. _vim.vm.device.VirtualDisk.VFlashCacheConfigInfo: ../../../vim/vm/device/VirtualDisk/VFlashCacheConfigInfo.rst


vim.vm.device.VirtualDisk
=========================
  This data object type contains information about a disk in a virtual machine.The virtual disk backing object types describe the different virtual disk backings available. The disk format version in each case describes the version of the format that is used.Supported virtual disk backings:Sparse disk format, version 1 and 2The virtual disk backing grows when needed. Supported only for VMware Server.Flat disk format, version 1 and 2The virtual disk backing is preallocated. Version 1 is supported only for VMware Server.Space efficient sparse disk formatThe virtual disk backing grows on demand and incorporates additional space optimizations.Raw disk format, version 2The virtual disk backing uses a full physical disk drive to back the virtual disk. Supported only for VMware Server.Partitioned raw disk format, version 2The virtual disk backing uses one or more partitions on a physical disk drive to back a virtual disk. Supported only for VMware Server.Raw disk mapping, version 1The virtual disk backing uses a raw device mapping to back the virtual disk. Supported for ESX Server 2.5 and 3.x.
:extends: vim.vm.device.VirtualDevice_

Attributes:
    capacityInKB (`long`_):

       Capacity of this virtual disk in kilobytes. Information might be lost when actual disk size is rounded off to kilobytes.
    capacityInBytes (`long`_, optional):

       Capacity of this virtual disk in bytes. Server will always populate this property. Clients must initialize it when creating a new non -RDM disk or in case they want to change the current capacity of an existing virtual disk, but can omit it otherwise.
    shares (`vim.SharesInfo`_, optional):

       Disk shares, used for resource scheduling.
    storageIOAllocation (`vim.StorageResourceManager.IOAllocationInfo`_, optional):

       Resource allocation for storage I/O.
    diskObjectId (`str`_, optional):

       Virtual disk durable and unmutable identifier. Virtual disk has a UUID field but that can be set through VirtualDiskManager APIs. This identifier is a universally unique identifier which is not settable. VirtualDisk can remain in existence even if it is not associated with VM.
    vFlashCacheConfigInfo (`vim.vm.device.VirtualDisk.VFlashCacheConfigInfo`_, optional):

       vFlash cache configuration supported on this virtual disk
