
vim.vm.device.VirtualDiskOption.VFlashCacheConfigOption
=======================================================
  Options for vFlash cache configuration.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_

Attributes:
    cacheConsistencyType (`vim.option.ChoiceOption <vim/option/ChoiceOption.rst>`_):

       Cache data consistency type. See `VirtualDiskVFlashCacheConfigInfoCacheConsistencyType <vim/vm/device/VirtualDisk/VFlashCacheConfigInfo/CacheConsistencyType.rst>`_ 
    cacheMode (`vim.option.ChoiceOption <vim/option/ChoiceOption.rst>`_):

       Cache mode See `VirtualDiskVFlashCacheConfigInfoCacheMode <vim/vm/device/VirtualDisk/VFlashCacheConfigInfo/CacheMode.rst>`_ 
    reservationInMB (`vim.option.LongOption <vim/option/LongOption.rst>`_):

       Cache reservation
    blockSizeInKB (`vim.option.LongOption <vim/option/LongOption.rst>`_):

       Cache block size
