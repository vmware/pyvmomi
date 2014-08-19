
vim.dvs.DistributedVirtualPort.Setting
======================================
  The `DVPortSetting <vim/dvs/DistributedVirtualPort/Setting.rst>`_ data object describes the network configuration of a `DistributedVirtualPort <vim/dvs/DistributedVirtualPort.rst>`_ .
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    blocked (`vim.BoolPolicy <vim/BoolPolicy.rst>`_, optional):

       Indicates whether this port is blocked. If a port is blocked, packet forwarding is stopped.
    vmDirectPathGen2Allowed (`vim.BoolPolicy <vim/BoolPolicy.rst>`_, optional):

       Indicates whether this port is allowed to do VMDirectPath Gen2 network passthrough. Direct path capability is defined at host, switch, and device levels. See thevmDirectPathGen2Supportedproperties on the `DVSFeatureCapability <vim/DistributedVirtualSwitch/FeatureCapability.rst>`_ , `HostCapability <vim/host/Capability.rst>`_ , `PhysicalNic <vim/host/PhysicalNic.rst>`_ , and `VirtualEthernetCardOption <vim/vm/device/VirtualEthernetCardOption.rst>`_ objects.
    inShapingPolicy (`vim.dvs.DistributedVirtualPort.TrafficShapingPolicy <vim/dvs/DistributedVirtualPort/TrafficShapingPolicy.rst>`_, optional):

       Network shaping policy for controlling throughput of inbound traffic.
    outShapingPolicy (`vim.dvs.DistributedVirtualPort.TrafficShapingPolicy <vim/dvs/DistributedVirtualPort/TrafficShapingPolicy.rst>`_, optional):

       Network shaping policy for controlling throughput of outbound traffic.
    vendorSpecificConfig (`vim.dvs.DistributedVirtualPort.VendorSpecificConfig <vim/dvs/DistributedVirtualPort/VendorSpecificConfig.rst>`_, optional):

       Opaque binary blob that stores vendor specific configuration.
    networkResourcePoolKey (`vim.StringPolicy <vim/StringPolicy.rst>`_, optional):

       The key of user defined network resource pool to be associated with a port. The default value for this property is "-1", indicating that this port is not associated with any network resource pool.
    filterPolicy (`vim.dvs.DistributedVirtualPort.FilterPolicy <vim/dvs/DistributedVirtualPort/FilterPolicy.rst>`_, optional):

       Configuration for Network Filter Policy.
