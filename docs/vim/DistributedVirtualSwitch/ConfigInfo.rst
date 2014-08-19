
vim.DistributedVirtualSwitch.ConfigInfo
=======================================
  Configuration of a `DistributedVirtualSwitch <vim/DistributedVirtualSwitch.rst>`_ .
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    uuid (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Generated UUID of the switch. Unique across vCenter Server inventory and instances.
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Name of the switch.
    numStandalonePorts (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Number of standalone ports in the switch. Standalone ports are ports that do not belong to any portgroup.
    numPorts (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Current number of ports, not including conflict ports.
    maxPorts (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Maximum number of ports allowed in the switch, not including conflict ports.
    uplinkPortPolicy (`vim.DistributedVirtualSwitch.UplinkPortPolicy <vim/DistributedVirtualSwitch/UplinkPortPolicy.rst>`_):

       Uplink port policy.
    uplinkPortgroup ([`vim.dvs.DistributedVirtualPortgroup <vim/dvs/DistributedVirtualPortgroup.rst>`_], optional):

       List of uplink portgroups. When adding host members, the server uses the `uplinkPortPolicy <vim/DistributedVirtualSwitch/ConfigInfo.rst#uplinkPortPolicy>`_ to create a number of uplink ports for the host. If portgroups are shown here, those uplink ports will be added to the portgroups, with uplink ports evenly spread among the portgroups.
    defaultPortConfig (`vim.dvs.DistributedVirtualPort.Setting <vim/dvs/DistributedVirtualPort/Setting.rst>`_):

       Default configuration for the ports in the switch, if the port does not inherit configuration from the parent portgroup or has its own configuration.
    host ([`vim.dvs.HostMember <vim/dvs/HostMember.rst>`_], optional):

       Hosts that join the switch.
    productInfo (`vim.dvs.ProductSpec <vim/dvs/ProductSpec.rst>`_):

       Vendor, product, and version information for the implementation module of the switch.
    targetInfo (`vim.dvs.ProductSpec <vim/dvs/ProductSpec.rst>`_, optional):

       Intended vendor, product, and version information for the implementation module of the switch.
    extensionKey (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Key of the extension registered by the remote server that controls the switch.
    vendorSpecificConfig ([`vim.dvs.KeyedOpaqueBlob <vim/dvs/KeyedOpaqueBlob.rst>`_], optional):

       Opaque binary blob that stores vendor specific configuration.
    policy (`vim.DistributedVirtualSwitch.SwitchPolicy <vim/DistributedVirtualSwitch/SwitchPolicy.rst>`_, optional):

       Usage policy of the switch.
    description (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Description string for the switch.
    configVersion (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Version string of the configuration.
    contact (`vim.DistributedVirtualSwitch.ContactInfo <vim/DistributedVirtualSwitch/ContactInfo.rst>`_):

       Human operator contact information.
    switchIpAddress (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       IP address for the switch, specified using IPv4 dot notation. The utility of this address is defined by other switch features.
    createTime (`datetime <https://docs.python.org/2/library/stdtypes.html>`_):

       Create time of the switch.
    networkResourceManagementEnabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Boolean to indicate if network I/O control is enabled on the switch.
    defaultProxySwitchMaxNumPorts (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Default host proxy switch maximum port number
    healthCheckConfig ([`vim.DistributedVirtualSwitch.HealthCheckConfig <vim/DistributedVirtualSwitch/HealthCheckConfig.rst>`_], optional):

       VDS health check configuration.
