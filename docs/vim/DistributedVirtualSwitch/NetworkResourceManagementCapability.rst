.. _int: https://docs.python.org/2/library/stdtypes.html

.. _high: ../../vim/SharesInfo/Level.rst#high

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _normal: ../../vim/SharesInfo/Level.rst#normal

.. _shares: ../../vim/dvs/NetworkResourcePool/AllocationInfo.rst#shares

.. _SharesLevel: ../../vim/SharesInfo/Level.rst

.. _vSphere API 5.0: ../../vim/version.rst#vimversionversion7

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _DVSNetworkResourcePoolAllocationInfo: ../../vim/dvs/NetworkResourcePool/AllocationInfo.rst


vim.DistributedVirtualSwitch.NetworkResourceManagementCapability
================================================================
  Dataobject representing the feature capabilities of network resource management supported by the vSphere Distributed Switch.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0`_

Attributes:
    networkResourceManagementSupported (`bool`_):

       Indicates whether network I/O control is supported on the vSphere Distributed Switch. Network I/O control is supported in vSphere Distributed Switch Version 4.1 or later.
    networkResourcePoolHighShareValue (`int`_):

       High share level ( `SharesLevel`_ . `high`_ ) for `DVSNetworkResourcePoolAllocationInfo`_ . `shares`_ .ThenetworkResourcePoolHighshareValueproperty implicitly defines the legal range of share values to be between 1 and this value. This property also defines values for other level types, such as `normal`_ being one half of this value and `low`_ being one fourth of this value. This feature is supported in vSphere Distributed Switch Version 4.1 or later.
    qosSupported (`bool`_):

       Indicates whether Qos Tag(802.1p priority tag)is supported on the vSphere Distributed Switch. Qos Tag is supported in vSphere Distributed Switch Version 5.0 or later.
    userDefinedNetworkResourcePoolsSupported (`bool`_):

       Indicates whether the switch supports creating user defined resource pools. This feature is supported in vSphere Distributed Switch Version 5.0 or later.
