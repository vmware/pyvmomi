
vim.host.VirtualNic
===================
  The `HostVirtualNic <vim/host/VirtualNic.rst>`_ data object describes a virtual network adapter representing an adapter that connects to a virtual switch. A host virtual NIC differs from a physical NIC:
   * A host virtual NIC is a virtual device that is connected to a virtual switch.
   * A physical NIC (
   * `HostNetworkInfo <vim/host/NetworkInfo.rst>`_
   * .
   * `pnic <vim/host/NetworkInfo.rst#pnic>`_
   * ) corresponds to a physical device that is connected to the physical network.
   * 
   * A host virtual NIC provides access to the external network through a virtual switch that is bridged through a Physical NIC to a physical network (
   * `HostNetworkConfig <vim/host/NetworkConfig.rst>`_
   * .
   * `vswitch <vim/host/NetworkConfig.rst#vswitch>`_
   * [].
   * `spec <vim/host/VirtualSwitch/Config.rst#spec>`_
   * .
   * `bridge <vim/host/VirtualSwitch/Specification.rst#bridge>`_
   * )
:extends: vmodl.DynamicData_

Attributes:
    device (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Device name.
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Linkable identifier.
    portgroup (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       If the Virtual NIC is connecting to a vSwitch, this property is the name of portgroup connected. If the Virtual NIC is connecting to a DistributedVirtualSwitch, this property is an empty string.
    spec (`vim.host.VirtualNic.Specification <vim/host/VirtualNic/Specification.rst>`_):

       Configurable properties for the virtual network adapter object.
    port (`vim.host.PortGroup.Port <vim/host/PortGroup/Port.rst>`_, optional):

       Port on the port group that the virtual network adapter is using when it is enabled ( `DistributedVirtualPort <vim/dvs/DistributedVirtualPort.rst>`_ . `key <vim/dvs/DistributedVirtualPort.rst#key>`_ ).
