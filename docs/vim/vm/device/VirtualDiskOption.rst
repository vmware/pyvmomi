
vim.vm.device.VirtualDiskOption
===============================
  The VirtualDiskOption data class contains the options for the virtual disk data object type.
:extends: vim.vm.device.VirtualDeviceOption_

Attributes:
    capacityInKB (`vim.option.LongOption <vim/option/LongOption.rst>`_):

       Minimum, maximum, and default capacity of the disk.
    ioAllocationOption (`vim.StorageResourceManager.IOAllocationOption <vim/StorageResourceManager/IOAllocationOption.rst>`_):

       Minumum, maximum, and default values for Storage I/O allocation.See `StorageIOAllocationInfo <vim/StorageResourceManager/IOAllocationInfo.rst>`_ 
    vFlashCacheConfigOption (`vim.vm.device.VirtualDiskOption.VFlashCacheConfigOption <vim/vm/device/VirtualDiskOption/VFlashCacheConfigOption.rst>`_, optional):

       vFlash cache configuration on the disk
