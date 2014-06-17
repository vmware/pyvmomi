.. _str: https://docs.python.org/2/library/stdtypes.html

.. _spec: ../../vim/host/VirtualSwitch/Config.rst#spec

.. _pnic: ../../vim/host/NetworkInfo.rst#pnic

.. _bridge: ../../vim/host/VirtualSwitch/Specification.rst#bridge

.. _vswitch: ../../vim/host/NetworkConfig.rst#vswitch

.. _HostVirtualNic: ../../vim/host/VirtualNic.rst

.. _HostNetworkInfo: ../../vim/host/NetworkInfo.rst

.. _HostNetworkConfig: ../../vim/host/NetworkConfig.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _DistributedVirtualPort: ../../vim/dvs/DistributedVirtualPort.rst

.. _vim.host.PortGroup.Port: ../../vim/host/PortGroup/Port.rst

.. _vim.host.VirtualNic.Specification: ../../vim/host/VirtualNic/Specification.rst


vim.host.VirtualNic
===================
  The `HostVirtualNic`_ data object describes a virtual network adapter representing an adapter that connects to a virtual switch. A host virtual NIC differs from a physical NIC:
   * A host virtual NIC is a virtual device that is connected to a virtual switch.
   * A physical NIC (
   * `HostNetworkInfo`_
   * .
   * `pnic`_
   * ) corresponds to a physical device that is connected to the physical network.
   * 
   * A host virtual NIC provides access to the external network through a virtual switch that is bridged through a Physical NIC to a physical network (
   * `HostNetworkConfig`_
   * .
   * `vswitch`_
   * [].
   * `spec`_
   * .
   * `bridge`_
   * )
:extends: vmodl.DynamicData_

Attributes:
    device (`str`_):

       Device name.
    key (`str`_):

       Linkable identifier.
    portgroup (`str`_):

       If the Virtual NIC is connecting to a vSwitch, this property is the name of portgroup connected. If the Virtual NIC is connecting to a DistributedVirtualSwitch, this property is an empty string.
    spec (`vim.host.VirtualNic.Specification`_):

       Configurable properties for the virtual network adapter object.
    port (`vim.host.PortGroup.Port`_, optional):

       Port on the port group that the virtual network adapter is using when it is enabled ( `DistributedVirtualPort`_ . `key`_ ).
