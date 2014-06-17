.. _str: https://docs.python.org/2/library/stdtypes.html

.. _long: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.5: ../../../../vim/version.rst#vimversionversion9

.. _vmodl.DynamicData: ../../../../vmodl/DynamicData.rst

.. _vim.option.LongOption: ../../../../vim/option/LongOption.rst

.. _vim.option.ChoiceOption: ../../../../vim/option/ChoiceOption.rst

.. _VirtualDiskVFlashCacheConfigInfoCacheMode: ../../../../vim/vm/device/VirtualDisk/VFlashCacheConfigInfo/CacheMode.rst

.. _VirtualDiskVFlashCacheConfigInfoCacheConsistencyType: ../../../../vim/vm/device/VirtualDisk/VFlashCacheConfigInfo/CacheConsistencyType.rst


vim.host.VFlashManager.VFlashCacheConfigInfo.VFlashModuleConfigOption
=====================================================================
  
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5`_

Attributes:
    vFlashModule (`str`_):

       Name of the vFlash module
    vFlashModuleVersion (`str`_):

       Version of the vFlash module
    minSupportedModuleVersion (`str`_):

       Minimum supported version
    cacheConsistencyType (`vim.option.ChoiceOption`_):

       Cache data consistency types. See `VirtualDiskVFlashCacheConfigInfoCacheConsistencyType`_ 
    cacheMode (`vim.option.ChoiceOption`_):

       Cache modes. See `VirtualDiskVFlashCacheConfigInfoCacheMode`_ 
    blockSizeInKBOption (`vim.option.LongOption`_):

       blockSizeInKBOption defines a range of virtual disk cache block size.
    reservationInMBOption (`vim.option.LongOption`_):

       reservationInMBOption defines a range of virtual disk cache size.
    maxDiskSizeInKB (`long`_):

       Maximal size of virtual disk supported in kilobytes.
