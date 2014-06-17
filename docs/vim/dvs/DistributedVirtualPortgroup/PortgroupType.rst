.. _type: ../../../vim/dvs/DistributedVirtualPortgroup/ConfigInfo.rst#type

.. _config: ../../../vim/dvs/DistributedVirtualPortgroup.rst#config

.. _VirtualMachine: ../../../vim/VirtualMachine.rst

.. _DistributedVirtualPort: ../../../vim/dvs/DistributedVirtualPort.rst

.. _DistributedVirtualPortgroup: ../../../vim/dvs/DistributedVirtualPortgroup.rst

.. _vim.dvs.DistributedVirtualPortgroup: ../../../vim/dvs/DistributedVirtualPortgroup.rst

.. _DistributedVirtualPortgroupPortgroupType: ../../../vim/dvs/DistributedVirtualPortgroup/PortgroupType.rst

.. _vim.dvs.DistributedVirtualPortgroup.PortgroupType: ../../../vim/dvs/DistributedVirtualPortgroup/PortgroupType.rst

vim.dvs.DistributedVirtualPortgroup.PortgroupType
=================================================
  The `DistributedVirtualPortgroupPortgroupType`_ enum defines the distributed virtual portgroup types ( `DistributedVirtualPortgroup`_ . `config`_ . `type`_ ). Early binding specifies a static set of ports that are created when you create the distributed virtual portgroup. An ephemeral portgroup uses dynamic ports that are created when you power on a virtual machine.
  :contained by: `vim.dvs.DistributedVirtualPortgroup`_

  :type: `vim.dvs.DistributedVirtualPortgroup.PortgroupType`_

  :name: ephemeral

values:
--------

lateBinding
   Deprecatedas of vSphere API 5.0. A free distributed virtual port will be selected and assigned to a virtual machine when the virtual machine is powered on.

ephemeral
   A `DistributedVirtualPort`_ will be created and assigned to a `VirtualMachine`_ when the virtual machine is powered on, and will be deleted when the virtual machine is powered off. An ephemeral portgroup has no limit on the number of ports that can be a part of this portgroup. In cases where the vCenter Server is unavailable the host can create conflict ports in this portgroup to be used by a virtual machine at power on.

earlyBinding
   A free `DistributedVirtualPort`_ will be selected and assigned to a `VirtualMachine`_ when the virtual machine is reconfigured to connect to the portgroup.
