.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vim.KeyValue: ../../vim/KeyValue.rst

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.host.PhysicalNic: ../../vim/host/PhysicalNic.rst

.. _vim.host.HostProxySwitch.Specification: ../../vim/host/HostProxySwitch/Specification.rst

.. _vim.host.HostProxySwitch.HostLagConfig: ../../vim/host/HostProxySwitch/HostLagConfig.rst


vim.host.HostProxySwitch
========================
  The HostProxySwitch is a software entity which represents the component of a DistributedVirtualSwitch on a particular host.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    dvsUuid (`str`_):

       The uuid of the DistributedVirtualSwitch that the HostProxySwitch is a part of.
    dvsName (`str`_):

       The name of the DistributedVirtualSwitch that the HostProxySwitch is part of.
    key (`str`_):

       The proxy switch key.
    numPorts (`int`_):

       The number of ports that this switch currently has.
    configNumPorts (`int`_, optional):

       The configured number of ports that this switch has. If configured number of ports is changed, a host reboot is required for the new value to take effect.
    numPortsAvailable (`int`_):

       The number of ports that are available on this virtual switch.
    uplinkPort (`vim.KeyValue`_, optional):

       The list of ports that can be potentially used by physical nics. This property contains the keys and names of such ports.
    mtu (`int`_, optional):

       The maximum transmission unit (MTU) associated with this switch in bytes.
    pnic (`vim.host.PhysicalNic`_, optional):

       The set of physical network adapters associated with this switch.
    spec (`vim.host.HostProxySwitch.Specification`_):

       The specification of the switch.
    hostLag (`vim.host.HostProxySwitch.HostLagConfig`_, optional):

       The Link Aggregation Control Protocol group and Uplink ports in the group.
    networkReservationSupported (`bool`_, optional):

       Indicates whether network reservation is supported on this switch
