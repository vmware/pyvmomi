
vim.storageDrs.SpaceLoadBalanceConfig
=====================================
  Storage DRS configuration for space load balancing.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    spaceUtilizationThreshold (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Storage DRS makes storage migration recommendations if space utilization on one (or more) of the datastores is higher than the specified threshold.The valid values are in the range of 50 (i.e., 50%) to 100 (i.e., 100%). If not specified, the default value is 80%.
    minSpaceUtilizationDifference (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Storage DRS considers making storage migration recommendations if the difference in space utilization between the source and destination datastores is higher than the specified threshold.The valid values are in the range of 1 (i.e., 1%) to 50 (i.e., 50%). If not specified, the default value is 5%.
