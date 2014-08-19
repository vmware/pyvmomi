
vim.cluster.VmGroup
===================
  The `ClusterVmGroup <vim/cluster/VmGroup.rst>`_ data object identifies virtual machines for VM-Host rules. VM-Host rules determine placement of virtual machines on hosts in a cluster. The logic specified in a `ClusterVmHostRuleInfo <vim/cluster/VmHostRuleInfo.rst>`_ object determines where virtual machines can be powered-on.If a virtual machine is removed from the cluster, it loses its DRS group affiliation. The Server does not restore any group affiliations if the virtual machine is returned to the cluster.
:extends: vim.cluster.GroupInfo_
:since: `vSphere API 4.1 <vim/version.rst#vimversionversion6>`_

Attributes:
    vm ([`vim.VirtualMachine <vim/VirtualMachine.rst>`_], optional):

       List of virtual machines that are part of this group. A virtual machine group can contain zero or more virtual machines.
