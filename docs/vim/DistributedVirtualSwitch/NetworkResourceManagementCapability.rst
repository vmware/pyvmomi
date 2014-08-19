
vim.DistributedVirtualSwitch.NetworkResourceManagementCapability
================================================================
  Dataobject representing the feature capabilities of network resource management supported by the vSphere Distributed Switch.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    networkResourceManagementSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether network I/O control is supported on the vSphere Distributed Switch. Network I/O control is supported in vSphere Distributed Switch Version 4.1 or later.
    networkResourcePoolHighShareValue (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       High share level ( `SharesLevel <vim/SharesInfo/Level.rst>`_ . `high <vim/SharesInfo/Level.rst#high>`_ ) for `DVSNetworkResourcePoolAllocationInfo <vim/dvs/NetworkResourcePool/AllocationInfo.rst>`_ . `shares <vim/dvs/NetworkResourcePool/AllocationInfo.rst#shares>`_ .ThenetworkResourcePoolHighshareValueproperty implicitly defines the legal range of share values to be between 1 and this value. This property also defines values for other level types, such as `normal <vim/SharesInfo/Level.rst#normal>`_ being one half of this value and `low <vim/SharesInfo/Level.rst#low>`_ being one fourth of this value. This feature is supported in vSphere Distributed Switch Version 4.1 or later.
    qosSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether Qos Tag(802.1p priority tag)is supported on the vSphere Distributed Switch. Qos Tag is supported in vSphere Distributed Switch Version 5.0 or later.
    userDefinedNetworkResourcePoolsSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether the switch supports creating user defined resource pools. This feature is supported in vSphere Distributed Switch Version 5.0 or later.
