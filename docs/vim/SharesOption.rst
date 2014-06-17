.. _level: ../vim/SharesInfo.rst#level

.. _shares: ../vim/SharesInfo.rst#shares

.. _SharesInfo: ../vim/SharesInfo.rst

.. _vSphere API 4.1: ../vim/version.rst#vimversionversion6

.. _vmodl.DynamicData: ../vmodl/DynamicData.rst

.. _vim.SharesInfo.Level: ../vim/SharesInfo/Level.rst

.. _vim.option.IntOption: ../vim/option/IntOption.rst


vim.SharesOption
================
  Specification of shares.Object of this class specifies value ranges for object of instance `SharesInfo`_ 
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1`_

Attributes:
    sharesOption (`vim.option.IntOption`_):

       Value range which can be used for share definition in `shares`_ 
    defaultLevel (`vim.SharesInfo.Level`_):

       Default value for `level`_ 
