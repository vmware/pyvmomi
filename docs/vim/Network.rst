
vim.Network
===========
  Represents a network accessible by either hosts or virtual machines. This can be a physical network or a logical network, such as a VLAN.Networks are created:
   * explicitly when configuring a host.
   * automatically when adding a host to VirtualCenter.
   * automatically when adding a new virtual machine to a host or to VirtualCenter.
   * 
   * To configure network access for hosts and virtual machines, use
   * `DistributedVirtualSwitch <vim/DistributedVirtualSwitch.rst>`_
   * and
   * `DistributedVirtualPortgroup <vim/dvs/DistributedVirtualPortgroup.rst>`_
   * managed objects.


:extends: vim.ManagedEntity_


Attributes
----------
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       Name of this network.
    summary (`vim.Network.Summary <vim/Network/Summary.rst>`_):
       Properties of a network.
    host ([`vim.HostSystem <vim/HostSystem.rst>`_]):
       Hosts attached to this network.
    vm ([`vim.VirtualMachine <vim/VirtualMachine.rst>`_]):
       Virtual machines using this network.


Methods
-------


DestroyNetwork():
   Removes a network. A network can be removed only if it is not used by any host or virtual machine.


  Privilege:
               Network.Delete



  Args:


  Returns:
    None
         

  Raises:

    `vim.fault.ResourceInUse <vim/fault/ResourceInUse.rst>`_: 
       if one or more hosts or virtual machines are configured to use the network.


