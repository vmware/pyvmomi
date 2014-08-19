
vim.StorageResourceManager.IOAllocationOption
=============================================
  The IOAllocationOption specifies value ranges that can be used to initialize IOAllocationInfo object.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1 <vim/version.rst#vimversionversion6>`_

Attributes:
    limitOption (`vim.option.LongOption <vim/option/LongOption.rst>`_):

       limitOptions defines a range of values allowed to be used for storage IO limit `limit <vim/StorageResourceManager/IOAllocationInfo.rst#limit>`_ .
    sharesOption (`vim.SharesOption <vim/SharesOption.rst>`_):

       sharesOption defines a range of values allowed to be used to specify allocated io shares `shares <vim/StorageResourceManager/IOAllocationInfo.rst#shares>`_ .
