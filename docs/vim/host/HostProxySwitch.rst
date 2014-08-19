
vim.host.HostProxySwitch
========================
  The HostProxySwitch is a software entity which represents the component of a DistributedVirtualSwitch on a particular host.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    dvsUuid (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The uuid of the DistributedVirtualSwitch that the HostProxySwitch is a part of.
    dvsName (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The name of the DistributedVirtualSwitch that the HostProxySwitch is part of.
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The proxy switch key.
    numPorts (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The number of ports that this switch currently has.
    configNumPorts (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The configured number of ports that this switch has. If configured number of ports is changed, a host reboot is required for the new value to take effect.
    numPortsAvailable (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The number of ports that are available on this virtual switch.
    uplinkPort ([`vim.KeyValue <vim/KeyValue.rst>`_], optional):

       The list of ports that can be potentially used by physical nics. This property contains the keys and names of such ports.
    mtu (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The maximum transmission unit (MTU) associated with this switch in bytes.
    pnic ([`vim.host.PhysicalNic <vim/host/PhysicalNic.rst>`_], optional):

       The set of physical network adapters associated with this switch.
    spec (`vim.host.HostProxySwitch.Specification <vim/host/HostProxySwitch/Specification.rst>`_):

       The specification of the switch.
    hostLag ([`vim.host.HostProxySwitch.HostLagConfig <vim/host/HostProxySwitch/HostLagConfig.rst>`_], optional):

       The Link Aggregation Control Protocol group and Uplink ports in the group.
    networkReservationSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Indicates whether network reservation is supported on this switch
