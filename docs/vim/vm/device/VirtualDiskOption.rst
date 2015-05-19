.. _vim.option.LongOption: ../../../vim/option/LongOption.rst

.. _StorageIOAllocationInfo: ../../../vim/StorageResourceManager/IOAllocationInfo.rst

.. _vim.vm.device.VirtualDeviceOption: ../../../vim/vm/device/VirtualDeviceOption.rst

.. _vim.StorageResourceManager.IOAllocationOption: ../../../vim/StorageResourceManager/IOAllocationOption.rst

.. _vim.vm.device.VirtualDiskOption.VFlashCacheConfigOption: ../../../vim/vm/device/VirtualDiskOption/VFlashCacheConfigOption.rst


vim.vm.device.VirtualDiskOption
===============================
  The VirtualDiskOption data class contains the options for the virtual disk data object type.
:extends: vim.vm.device.VirtualDeviceOption_

Attributes:
    capacityInKB (`vim.option.LongOption`_):

       Minimum, maximum, and default capacity of the disk.
    ioAllocationOption (`vim.StorageResourceManager.IOAllocationOption`_):

       Minumum, maximum, and default values for Storage I/O allocation.See `StorageIOAllocationInfo`_ 
    vFlashCacheConfigOption (`vim.vm.device.VirtualDiskOption.VFlashCacheConfigOption`_, optional):

       vFlash cache configuration on the disk
