
vim.vm.device.VirtualDisk.VFlashCacheConfigInfo
===============================================
  Data object describes the vFlash cache configuration on this virtual disk.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_

Attributes:
    vFlashModule (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Name of vFlash module which manages the cache. If not specified, default setting `defaultVFlashModule <vim/host/VFlashManager/VFlashCacheConfigSpec.rst#defaultVFlashModule>`_ will be used.
    reservationInMB (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Amount of vFlash resource that is guaranteed available to the cache. If not specified, default reservation will be used.
    cacheConsistencyType (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Cache data consistency types after a crash. See `VirtualDiskVFlashCacheConfigInfoCacheConsistencyType <vim/vm/device/VirtualDisk/VFlashCacheConfigInfo/CacheConsistencyType.rst>`_ for supported types. If not specified, the default value used is `strong <vim/vm/device/VirtualDisk/VFlashCacheConfigInfo/CacheConsistencyType.rst#strong>`_ 
    cacheMode (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Cache modes. See `VirtualDiskVFlashCacheConfigInfoCacheMode <vim/vm/device/VirtualDisk/VFlashCacheConfigInfo/CacheMode.rst>`_ for supported modes. If not specified, the default value used is `write_thru <vim/vm/device/VirtualDisk/VFlashCacheConfigInfo/CacheMode.rst#write_thru>`_ .
    blockSizeInKB (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Cache block size. This parameter allows the user to control how much data gets cached on a single access to the VMDK. Max block size is 1MB. Default is 4KB.
