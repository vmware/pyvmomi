
vim.dvs.DistributedVirtualPort
==============================
  The `DistributedVirtualPort <vim/dvs/DistributedVirtualPort.rst>`_ data object represents a port in a `DistributedVirtualSwitch <vim/DistributedVirtualSwitch.rst>`_ . Virtual ports are part of a distributed virtual portgroup. Servers create virtual ports according to the portgroup type ( `DistributedVirtualPortgroup <vim/dvs/DistributedVirtualPortgroup.rst>`_ . `config <vim/dvs/DistributedVirtualPortgroup.rst#config>`_ . `type <vim/dvs/DistributedVirtualPortgroup/ConfigInfo.rst#type>`_ ). See `DistributedVirtualPortgroupPortgroupType <vim/dvs/DistributedVirtualPortgroup/PortgroupType.rst>`_ .
   * To configure host network access by port, set the distributed virtual port in the host virtual NIC specification (
   * `HostVirtualNicSpec <vim/host/VirtualNic/Specification.rst>`_
   * .
   * `distributedVirtualPort <vim/host/VirtualNic/Specification.rst#distributedVirtualPort>`_
   * .
   * `portKey <vim/dvs/PortConnection.rst#portKey>`_
   * ).
   * To configure virtual machine network access by port, set the port in the virtual Ethernet card backing (
   * `VirtualEthernetCard <vim/vm/device/VirtualEthernetCard.rst>`_
   * .
   * `backing <vim/vm/device/VirtualDevice.rst#backing>`_
   * .
   * `port <vim/vm/device/VirtualEthernetCard/DistributedVirtualPortBackingInfo.rst#port>`_
   * .
   * `portKey <vim/dvs/PortConnection.rst#portKey>`_
   * ).
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Port key.
    config (`vim.dvs.DistributedVirtualPort.ConfigInfo <vim/dvs/DistributedVirtualPort/ConfigInfo.rst>`_):

       Port configuration, including identifying information, network settings, and the set of entities that can connect to the port.
    dvsUuid (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       UUID of the `DistributedVirtualSwitch <vim/DistributedVirtualSwitch.rst>`_ to which the port belongs.
    portgroupKey (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Key of the portgroup `DistributedVirtualPortgroup <vim/dvs/DistributedVirtualPortgroup.rst>`_ to which the port belongs, if any.
    proxyHost (`vim.HostSystem <vim/HostSystem.rst>`_, optional):

        `HostSystem <vim/HostSystem.rst>`_ that services this port.
    connectee (`vim.dvs.PortConnectee <vim/dvs/PortConnectee.rst>`_, optional):

       Entity that connects to the port.
    conflict (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Specifies whether the port is a conflict port. A port could be marked as conflict if an entity is discovered connecting to a port that is already occupied, or if the host creates a port without conferring with vCenter Server.The distributed virtual switch does not persist the runtime state of a conflict port. Also, the port cannot move away from the host. vCenter Server will not move a virtual machine (VMotion) that is using a conflict port.
    conflictPortKey (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       If the port is marked conflict in the case of two entities connecting to the same port (see `conflict <vim/dvs/DistributedVirtualPort.rst#conflict>`_ ), this is the key of the port which the connected entity is contending for.
    state (`vim.dvs.DistributedVirtualPort.State <vim/dvs/DistributedVirtualPort/State.rst>`_, optional):

       Runtime state of the port.
    connectionCookie (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Cookie representing the current instance of association between a port and a virtual or physical NIC. See `DistributedVirtualSwitchPortConnection <vim/dvs/PortConnection.rst>`_ . The same cookie is present in the physical or virtual NIC configuration ( `DistributedVirtualSwitchPortConnection <vim/dvs/PortConnection.rst>`_ . `connectionCookie <vim/dvs/PortConnection.rst#connectionCookie>`_ ) so that the Server can verify that the entity is the rightful connectee of the port.
    lastStatusChange (`datetime <https://docs.python.org/2/library/stdtypes.html>`_):

       The last time the `state <vim/dvs/DistributedVirtualPort.rst#state>`_ . `runtimeInfo <vim/dvs/DistributedVirtualPort/State.rst#runtimeInfo>`_ value was changed.
    hostLocalPort (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Specifies whether the port is a host local port. A host local port is created to resurrect the management network connection on a VMkernel virtual NIC. You cannot use vCenter Server to reconfigure this port and you cannot reassign the port.
