.. _portKey: ../../../../vim/dvs/PortConnection.rst#portKey

.. _portgroupKey: ../../../../vim/dvs/PortConnection.rst#portgroupKey

.. _vSphere API 4.0: ../../../../vim/version.rst#vimversionversion5

.. _DistributedVirtualPort: ../../../../vim/dvs/DistributedVirtualPort.rst

.. _vim.dvs.PortConnection: ../../../../vim/dvs/PortConnection.rst

.. _DistributedVirtualPortgroup: ../../../../vim/dvs/DistributedVirtualPortgroup.rst

.. _DistributedVirtualSwitchPortConnection: ../../../../vim/dvs/PortConnection.rst

.. _vim.vm.device.VirtualDevice.BackingInfo: ../../../../vim/vm/device/VirtualDevice/BackingInfo.rst

.. _VirtualEthernetCardDistributedVirtualPortBackingInfo: ../../../../vim/vm/device/VirtualEthernetCard/DistributedVirtualPortBackingInfo.rst


vim.vm.device.VirtualEthernetCard.DistributedVirtualPortBackingInfo
===================================================================
  The `VirtualEthernetCardDistributedVirtualPortBackingInfo`_ data object defines backing for a virtual Ethernet card that connects to a distributed virtual switch port or portgroup.
:extends: vim.vm.device.VirtualDevice.BackingInfo_
:since: `vSphere API 4.0`_

Attributes:
    port (`vim.dvs.PortConnection`_):

        `DistributedVirtualPort`_ or `DistributedVirtualPortgroup`_ connection. To specify a port connection, set the `portKey`_ property. To specify a portgroup connection, set the `portgroupKey`_ property.This property will be unset during Virtual Machine or template cloning operation unless it's set to a `DistributedVirtualSwitchPortConnection`_ object and the portgroup is a late binding portgroup.
