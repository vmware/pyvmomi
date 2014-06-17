.. _vSphere API 5.5: ../../../../vim/version.rst#vimversionversion9

.. _vmodl.DynamicData: ../../../../vmodl/DynamicData.rst

.. _vim.option.LongOption: ../../../../vim/option/LongOption.rst

.. _vim.option.ChoiceOption: ../../../../vim/option/ChoiceOption.rst

.. _VirtualDiskVFlashCacheConfigInfoCacheMode: ../../../../vim/vm/device/VirtualDisk/VFlashCacheConfigInfo/CacheMode.rst

.. _VirtualDiskVFlashCacheConfigInfoCacheConsistencyType: ../../../../vim/vm/device/VirtualDisk/VFlashCacheConfigInfo/CacheConsistencyType.rst


vim.vm.device.VirtualDiskOption.VFlashCacheConfigOption
=======================================================
  Options for vFlash cache configuration.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5`_

Attributes:
    cacheConsistencyType (`vim.option.ChoiceOption`_):

       Cache data consistency type. See `VirtualDiskVFlashCacheConfigInfoCacheConsistencyType`_ 
    cacheMode (`vim.option.ChoiceOption`_):

       Cache mode See `VirtualDiskVFlashCacheConfigInfoCacheMode`_ 
    reservationInMB (`vim.option.LongOption`_):

       Cache reservation
    blockSizeInKB (`vim.option.LongOption`_):

       Cache block size
