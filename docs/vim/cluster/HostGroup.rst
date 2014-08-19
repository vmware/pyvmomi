
vim.cluster.HostGroup
=====================
  The `ClusterHostGroup <vim/cluster/HostGroup.rst>`_ data object identifies hosts for VM-Host rules. VM-Host rules determine placement of virtual machines on hosts in a cluster. The logic specified in a `ClusterVmHostRuleInfo <vim/cluster/VmHostRuleInfo.rst>`_ object determines where virtual machines can be powered-on.
:extends: vim.cluster.GroupInfo_
:since: `vSphere API 4.1 <vim/version.rst#vimversionversion6>`_

Attributes:
    host ([`vim.HostSystem <vim/HostSystem.rst>`_], optional):

       List of hosts that are part of this group. A host group can contain zero or more hosts.
