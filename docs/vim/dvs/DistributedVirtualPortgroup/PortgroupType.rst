vim.dvs.DistributedVirtualPortgroup.PortgroupType
=================================================
  The `DistributedVirtualPortgroupPortgroupType <vim/dvs/DistributedVirtualPortgroup/PortgroupType.rst>`_ enum defines the distributed virtual portgroup types ( `DistributedVirtualPortgroup <vim/dvs/DistributedVirtualPortgroup.rst>`_ . `config <vim/dvs/DistributedVirtualPortgroup.rst#config>`_ . `type <vim/dvs/DistributedVirtualPortgroup/ConfigInfo.rst#type>`_ ). Early binding specifies a static set of ports that are created when you create the distributed virtual portgroup. An ephemeral portgroup uses dynamic ports that are created when you power on a virtual machine.
  :contained by: `vim.dvs.DistributedVirtualPortgroup <vim/dvs/DistributedVirtualPortgroup.rst>`_

  :type: `vim.dvs.DistributedVirtualPortgroup.PortgroupType <vim/dvs/DistributedVirtualPortgroup/PortgroupType.rst>`_

  :name: ephemeral

values:
--------

lateBinding
   Deprecatedas of vSphere API 5.0. A free distributed virtual port will be selected and assigned to a virtual machine when the virtual machine is powered on.

ephemeral
   A `DistributedVirtualPort <vim/dvs/DistributedVirtualPort.rst>`_ will be created and assigned to a `VirtualMachine <vim/VirtualMachine.rst>`_ when the virtual machine is powered on, and will be deleted when the virtual machine is powered off. An ephemeral portgroup has no limit on the number of ports that can be a part of this portgroup. In cases where the vCenter Server is unavailable the host can create conflict ports in this portgroup to be used by a virtual machine at power on.

earlyBinding
   A free `DistributedVirtualPort <vim/dvs/DistributedVirtualPort.rst>`_ will be selected and assigned to a `VirtualMachine <vim/VirtualMachine.rst>`_ when the virtual machine is reconfigured to connect to the portgroup.
