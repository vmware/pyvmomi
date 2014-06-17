.. _int: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../vmodl/DynamicData.rst

.. _vim.SharesInfo.Level: ../vim/SharesInfo/Level.rst


vim.SharesInfo
==============
  Specification of shares.Shares are used to determine relative allocation between resource consumers. In general, a consumer with more shares gets proportionally more of the resource, subject to certain other constraints.
:extends: vmodl.DynamicData_

Attributes:
    shares (`int`_):

       The number of shares allocated. Used to determine resource allocation in case of resource contention. This value is only set if level is set to custom. If level is not set to custom, this value is ignored. Therefore, only shares with custom values can be compared.There is no unit for this value. It is a relative measure based on the settings for other resource pools.
    level (`vim.SharesInfo.Level`_):

       The allocation level. The level is a simplified view of shares. Levels map to a pre-determined set of numeric values for shares. If the shares value does not map to a predefined size, then the level is set as custom.
