.. _PhysicalNic: ../../../vim/host/PhysicalNic.rst

.. _DVPortSetting: ../../../vim/dvs/DistributedVirtualPort/Setting.rst

.. _vim.BoolPolicy: ../../../vim/BoolPolicy.rst

.. _HostCapability: ../../../vim/host/Capability.rst

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vim.StringPolicy: ../../../vim/StringPolicy.rst

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _DVSFeatureCapability: ../../../vim/DistributedVirtualSwitch/FeatureCapability.rst

.. _DistributedVirtualPort: ../../../vim/dvs/DistributedVirtualPort.rst

.. _VirtualEthernetCardOption: ../../../vim/vm/device/VirtualEthernetCardOption.rst

.. _vim.dvs.DistributedVirtualPort.FilterPolicy: ../../../vim/dvs/DistributedVirtualPort/FilterPolicy.rst

.. _vim.dvs.DistributedVirtualPort.TrafficShapingPolicy: ../../../vim/dvs/DistributedVirtualPort/TrafficShapingPolicy.rst

.. _vim.dvs.DistributedVirtualPort.VendorSpecificConfig: ../../../vim/dvs/DistributedVirtualPort/VendorSpecificConfig.rst


vim.dvs.DistributedVirtualPort.Setting
======================================
  The `DVPortSetting`_ data object describes the network configuration of a `DistributedVirtualPort`_ .
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    blocked (`vim.BoolPolicy`_, optional):

       Indicates whether this port is blocked. If a port is blocked, packet forwarding is stopped.
    vmDirectPathGen2Allowed (`vim.BoolPolicy`_, optional):

       Indicates whether this port is allowed to do VMDirectPath Gen2 network passthrough. Direct path capability is defined at host, switch, and device levels. See thevmDirectPathGen2Supportedproperties on the `DVSFeatureCapability`_ , `HostCapability`_ , `PhysicalNic`_ , and `VirtualEthernetCardOption`_ objects.
    inShapingPolicy (`vim.dvs.DistributedVirtualPort.TrafficShapingPolicy`_, optional):

       Network shaping policy for controlling throughput of inbound traffic.
    outShapingPolicy (`vim.dvs.DistributedVirtualPort.TrafficShapingPolicy`_, optional):

       Network shaping policy for controlling throughput of outbound traffic.
    vendorSpecificConfig (`vim.dvs.DistributedVirtualPort.VendorSpecificConfig`_, optional):

       Opaque binary blob that stores vendor specific configuration.
    networkResourcePoolKey (`vim.StringPolicy`_, optional):

       The key of user defined network resource pool to be associated with a port. The default value for this property is "-1", indicating that this port is not associated with any network resource pool.
    filterPolicy (`vim.dvs.DistributedVirtualPort.FilterPolicy`_, optional):

       Configuration for Network Filter Policy.
