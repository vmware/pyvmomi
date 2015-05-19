.. _int: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.0: ../../vim/version.rst#vimversionversion7

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.storageDrs.IoLoadBalanceConfig
==================================
  Storage DRS configuration for I/O load balancing.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0`_

Attributes:
    ioLatencyThreshold (`int`_, optional):

       Storage DRS makes storage migration recommendations if I/O latency on one (or more) of the datastores is higher than the specified threshold.Unit: millisecond. The valid values are in the range of 5 to 100. If not specified, the default value is 15.
    ioLoadImbalanceThreshold (`int`_, optional):

       Storage DRS makes storage migration recommendations if I/O load imbalance level is higher than the specified threshold.Unit: a number. The valid values are in the range of 1 to 100. If not specified, the default value is 5.
