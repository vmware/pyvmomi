.. _limit: ../../vim/StorageResourceManager/IOAllocationInfo.rst#limit

.. _shares: ../../vim/StorageResourceManager/IOAllocationInfo.rst#shares

.. _vSphere API 4.1: ../../vim/version.rst#vimversionversion6

.. _vim.SharesOption: ../../vim/SharesOption.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.option.LongOption: ../../vim/option/LongOption.rst


vim.StorageResourceManager.IOAllocationOption
=============================================
  The IOAllocationOption specifies value ranges that can be used to initialize IOAllocationInfo object.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1`_

Attributes:
    limitOption (`vim.option.LongOption`_):

       limitOptions defines a range of values allowed to be used for storage IO limit `limit`_ .
    sharesOption (`vim.SharesOption`_):

       sharesOption defines a range of values allowed to be used to specify allocated io shares `shares`_ .
