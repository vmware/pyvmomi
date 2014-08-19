
vim.vm.device.VirtualEthernetCard.DistributedVirtualPortBackingInfo
===================================================================
  The `VirtualEthernetCardDistributedVirtualPortBackingInfo <vim/vm/device/VirtualEthernetCard/DistributedVirtualPortBackingInfo.rst>`_ data object defines backing for a virtual Ethernet card that connects to a distributed virtual switch port or portgroup.
:extends: vim.vm.device.VirtualDevice.BackingInfo_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    port (`vim.dvs.PortConnection <vim/dvs/PortConnection.rst>`_):

        `DistributedVirtualPort <vim/dvs/DistributedVirtualPort.rst>`_ or `DistributedVirtualPortgroup <vim/dvs/DistributedVirtualPortgroup.rst>`_ connection. To specify a port connection, set the `portKey <vim/dvs/PortConnection.rst#portKey>`_ property. To specify a portgroup connection, set the `portgroupKey <vim/dvs/PortConnection.rst#portgroupKey>`_ property.This property will be unset during Virtual Machine or template cloning operation unless it's set to a `DistributedVirtualSwitchPortConnection <vim/dvs/PortConnection.rst>`_ object and the portgroup is a late binding portgroup.
