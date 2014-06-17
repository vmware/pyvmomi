.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _port: ../../vim/vm/device/VirtualEthernetCard/DistributedVirtualPortBackingInfo.rst#port

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _type: ../../vim/dvs/DistributedVirtualPortgroup/ConfigInfo.rst#type

.. _state: ../../vim/dvs/DistributedVirtualPort.rst#state

.. _config: ../../vim/dvs/DistributedVirtualPortgroup.rst#config

.. _backing: ../../vim/vm/device/VirtualDevice.rst#backing

.. _portKey: ../../vim/dvs/PortConnection.rst#portKey

.. _datetime: https://docs.python.org/2/library/stdtypes.html

.. _conflict: ../../vim/dvs/DistributedVirtualPort.rst#conflict

.. _HostSystem: ../../vim/HostSystem.rst

.. _runtimeInfo: ../../vim/dvs/DistributedVirtualPort/State.rst#runtimeInfo

.. _vim.HostSystem: ../../vim/HostSystem.rst

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _connectionCookie: ../../vim/dvs/PortConnection.rst#connectionCookie

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _HostVirtualNicSpec: ../../vim/host/VirtualNic/Specification.rst

.. _VirtualEthernetCard: ../../vim/vm/device/VirtualEthernetCard.rst

.. _vim.dvs.PortConnectee: ../../vim/dvs/PortConnectee.rst

.. _DistributedVirtualPort: ../../vim/dvs/DistributedVirtualPort.rst

.. _distributedVirtualPort: ../../vim/host/VirtualNic/Specification.rst#distributedVirtualPort

.. _DistributedVirtualSwitch: ../../vim/DistributedVirtualSwitch.rst

.. _DistributedVirtualPortgroup: ../../vim/dvs/DistributedVirtualPortgroup.rst

.. _vim.dvs.DistributedVirtualPort.State: ../../vim/dvs/DistributedVirtualPort/State.rst

.. _DistributedVirtualSwitchPortConnection: ../../vim/dvs/PortConnection.rst

.. _DistributedVirtualPortgroupPortgroupType: ../../vim/dvs/DistributedVirtualPortgroup/PortgroupType.rst

.. _vim.dvs.DistributedVirtualPort.ConfigInfo: ../../vim/dvs/DistributedVirtualPort/ConfigInfo.rst


vim.dvs.DistributedVirtualPort
==============================
  The `DistributedVirtualPort`_ data object represents a port in a `DistributedVirtualSwitch`_ . Virtual ports are part of a distributed virtual portgroup. Servers create virtual ports according to the portgroup type ( `DistributedVirtualPortgroup`_ . `config`_ . `type`_ ). See `DistributedVirtualPortgroupPortgroupType`_ .
   * To configure host network access by port, set the distributed virtual port in the host virtual NIC specification (
   * `HostVirtualNicSpec`_
   * .
   * `distributedVirtualPort`_
   * .
   * `portKey`_
   * ).
   * To configure virtual machine network access by port, set the port in the virtual Ethernet card backing (
   * `VirtualEthernetCard`_
   * .
   * `backing`_
   * .
   * `port`_
   * .
   * `portKey`_
   * ).
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    key (`str`_):

       Port key.
    config (`vim.dvs.DistributedVirtualPort.ConfigInfo`_):

       Port configuration, including identifying information, network settings, and the set of entities that can connect to the port.
    dvsUuid (`str`_):

       UUID of the `DistributedVirtualSwitch`_ to which the port belongs.
    portgroupKey (`str`_, optional):

       Key of the portgroup `DistributedVirtualPortgroup`_ to which the port belongs, if any.
    proxyHost (`vim.HostSystem`_, optional):

        `HostSystem`_ that services this port.
    connectee (`vim.dvs.PortConnectee`_, optional):

       Entity that connects to the port.
    conflict (`bool`_):

       Specifies whether the port is a conflict port. A port could be marked as conflict if an entity is discovered connecting to a port that is already occupied, or if the host creates a port without conferring with vCenter Server.The distributed virtual switch does not persist the runtime state of a conflict port. Also, the port cannot move away from the host. vCenter Server will not move a virtual machine (VMotion) that is using a conflict port.
    conflictPortKey (`str`_, optional):

       If the port is marked conflict in the case of two entities connecting to the same port (see `conflict`_ ), this is the key of the port which the connected entity is contending for.
    state (`vim.dvs.DistributedVirtualPort.State`_, optional):

       Runtime state of the port.
    connectionCookie (`int`_, optional):

       Cookie representing the current instance of association between a port and a virtual or physical NIC. See `DistributedVirtualSwitchPortConnection`_ . The same cookie is present in the physical or virtual NIC configuration ( `DistributedVirtualSwitchPortConnection`_ . `connectionCookie`_ ) so that the Server can verify that the entity is the rightful connectee of the port.
    lastStatusChange (`datetime`_):

       The last time the `state`_ . `runtimeInfo`_ value was changed.
    hostLocalPort (`bool`_, optional):

       Specifies whether the port is a host local port. A host local port is created to resurrect the management network connection on a VMkernel virtual NIC. You cannot use vCenter Server to reconfigure this port and you cannot reassign the port.
