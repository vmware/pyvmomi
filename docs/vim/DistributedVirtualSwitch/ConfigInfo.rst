.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _datetime: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _uplinkPortPolicy: ../../vim/DistributedVirtualSwitch/ConfigInfo.rst#uplinkPortPolicy

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.dvs.HostMember: ../../vim/dvs/HostMember.rst

.. _vim.dvs.ProductSpec: ../../vim/dvs/ProductSpec.rst

.. _vim.dvs.KeyedOpaqueBlob: ../../vim/dvs/KeyedOpaqueBlob.rst

.. _DistributedVirtualSwitch: ../../vim/DistributedVirtualSwitch.rst

.. _vim.dvs.DistributedVirtualPortgroup: ../../vim/dvs/DistributedVirtualPortgroup.rst

.. _vim.dvs.DistributedVirtualPort.Setting: ../../vim/dvs/DistributedVirtualPort/Setting.rst

.. _vim.DistributedVirtualSwitch.ContactInfo: ../../vim/DistributedVirtualSwitch/ContactInfo.rst

.. _vim.DistributedVirtualSwitch.SwitchPolicy: ../../vim/DistributedVirtualSwitch/SwitchPolicy.rst

.. _vim.DistributedVirtualSwitch.UplinkPortPolicy: ../../vim/DistributedVirtualSwitch/UplinkPortPolicy.rst

.. _vim.DistributedVirtualSwitch.HealthCheckConfig: ../../vim/DistributedVirtualSwitch/HealthCheckConfig.rst


vim.DistributedVirtualSwitch.ConfigInfo
=======================================
  Configuration of a `DistributedVirtualSwitch`_ .
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    uuid (`str`_):

       Generated UUID of the switch. Unique across vCenter Server inventory and instances.
    name (`str`_):

       Name of the switch.
    numStandalonePorts (`int`_):

       Number of standalone ports in the switch. Standalone ports are ports that do not belong to any portgroup.
    numPorts (`int`_):

       Current number of ports, not including conflict ports.
    maxPorts (`int`_):

       Maximum number of ports allowed in the switch, not including conflict ports.
    uplinkPortPolicy (`vim.DistributedVirtualSwitch.UplinkPortPolicy`_):

       Uplink port policy.
    uplinkPortgroup ([`vim.dvs.DistributedVirtualPortgroup`_], optional):

       List of uplink portgroups. When adding host members, the server uses the `uplinkPortPolicy`_ to create a number of uplink ports for the host. If portgroups are shown here, those uplink ports will be added to the portgroups, with uplink ports evenly spread among the portgroups.
    defaultPortConfig (`vim.dvs.DistributedVirtualPort.Setting`_):

       Default configuration for the ports in the switch, if the port does not inherit configuration from the parent portgroup or has its own configuration.
    host ([`vim.dvs.HostMember`_], optional):

       Hosts that join the switch.
    productInfo (`vim.dvs.ProductSpec`_):

       Vendor, product, and version information for the implementation module of the switch.
    targetInfo (`vim.dvs.ProductSpec`_, optional):

       Intended vendor, product, and version information for the implementation module of the switch.
    extensionKey (`str`_, optional):

       Key of the extension registered by the remote server that controls the switch.
    vendorSpecificConfig ([`vim.dvs.KeyedOpaqueBlob`_], optional):

       Opaque binary blob that stores vendor specific configuration.
    policy (`vim.DistributedVirtualSwitch.SwitchPolicy`_, optional):

       Usage policy of the switch.
    description (`str`_, optional):

       Description string for the switch.
    configVersion (`str`_):

       Version string of the configuration.
    contact (`vim.DistributedVirtualSwitch.ContactInfo`_):

       Human operator contact information.
    switchIpAddress (`str`_, optional):

       IP address for the switch, specified using IPv4 dot notation. The utility of this address is defined by other switch features.
    createTime (`datetime`_):

       Create time of the switch.
    networkResourceManagementEnabled (`bool`_):

       Boolean to indicate if network I/O control is enabled on the switch.
    defaultProxySwitchMaxNumPorts (`int`_, optional):

       Default host proxy switch maximum port number
    healthCheckConfig ([`vim.DistributedVirtualSwitch.HealthCheckConfig`_], optional):

       VDS health check configuration.
