
vim.host.VFlashManager.VFlashCacheConfigInfo.VFlashModuleConfigOption
=====================================================================
  
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_

Attributes:
    vFlashModule (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Name of the vFlash module
    vFlashModuleVersion (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Version of the vFlash module
    minSupportedModuleVersion (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Minimum supported version
    cacheConsistencyType (`vim.option.ChoiceOption <vim/option/ChoiceOption.rst>`_):

       Cache data consistency types. See `VirtualDiskVFlashCacheConfigInfoCacheConsistencyType <vim/vm/device/VirtualDisk/VFlashCacheConfigInfo/CacheConsistencyType.rst>`_ 
    cacheMode (`vim.option.ChoiceOption <vim/option/ChoiceOption.rst>`_):

       Cache modes. See `VirtualDiskVFlashCacheConfigInfoCacheMode <vim/vm/device/VirtualDisk/VFlashCacheConfigInfo/CacheMode.rst>`_ 
    blockSizeInKBOption (`vim.option.LongOption <vim/option/LongOption.rst>`_):

       blockSizeInKBOption defines a range of virtual disk cache block size.
    reservationInMBOption (`vim.option.LongOption <vim/option/LongOption.rst>`_):

       reservationInMBOption defines a range of virtual disk cache size.
    maxDiskSizeInKB (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       Maximal size of virtual disk supported in kilobytes.
