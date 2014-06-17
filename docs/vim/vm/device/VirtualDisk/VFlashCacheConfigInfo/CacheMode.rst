.. _vim.vm.device.VirtualDisk.VFlashCacheConfigInfo: ../../../../../vim/vm/device/VirtualDisk/VFlashCacheConfigInfo.rst

.. _vim.vm.device.VirtualDisk.VFlashCacheConfigInfo.CacheMode: ../../../../../vim/vm/device/VirtualDisk/VFlashCacheConfigInfo/CacheMode.rst

vim.vm.device.VirtualDisk.VFlashCacheConfigInfo.CacheMode
=========================================================
  Pre-defined constants for cache modes.
  :contained by: `vim.vm.device.VirtualDisk.VFlashCacheConfigInfo`_

  :type: `vim.vm.device.VirtualDisk.VFlashCacheConfigInfo.CacheMode`_

  :name: write_back

values:
--------

write_back
   In write-back mode, writes to the cache do not go to the underlying storage right away. Cache holds data temporarily till it can be permanently saved or otherwise modified.

write_thru
   In write-through cache mode, writes to the cache cause writes to the underlying storage. The cache acts as a facade to the underlying storage.
