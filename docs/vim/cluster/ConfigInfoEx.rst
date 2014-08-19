
vim.cluster.ConfigInfoEx
========================
  The `ClusterConfigInfoEx <vim/cluster/ConfigInfoEx.rst>`_ data object describes a complete cluster configuration. For information about configuring a cluster, see `ClusterConfigSpecEx <vim/cluster/ConfigSpecEx.rst>`_ .
:extends: vim.ComputeResource.ConfigInfo_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_

Attributes:
    dasConfig (`vim.cluster.DasConfigInfo <vim/cluster/DasConfigInfo.rst>`_):

       Cluster-wide configuration of the vSphere HA service.
    dasVmConfig ([`vim.cluster.DasVmConfigInfo <vim/cluster/DasVmConfigInfo.rst>`_], optional):

       List of virtual machine configurations for the vSphere HA service. Each entry applies to one virtual machine.If a virtual machine is not specified in this array, the service uses the default settings for that virtual machine.
    drsConfig (`vim.cluster.DrsConfigInfo <vim/cluster/DrsConfigInfo.rst>`_):

       Cluster-wide configuration of the VMware DRS service.
    drsVmConfig ([`vim.cluster.DrsVmConfigInfo <vim/cluster/DrsVmConfigInfo.rst>`_], optional):

       List of virtual machine configurations for the VMware DRS service. Each entry applies to one virtual machine.If a virtual machine is not specified in this array, the service uses the default settings for that virtual machine.
    rule ([`vim.cluster.RuleInfo <vim/cluster/RuleInfo.rst>`_], optional):

       Cluster-wide rules.
    dpmConfigInfo (`vim.cluster.DpmConfigInfo <vim/cluster/DpmConfigInfo.rst>`_, optional):

       Cluster-wide configuration of the VMware DPM service.
    dpmHostConfig ([`vim.cluster.DpmHostConfigInfo <vim/cluster/DpmHostConfigInfo.rst>`_], optional):

       List of host configurations for the VMware DPM service. Each entry applies to one host.If a host is not specified in this array, the service uses the cluster default settings for that host.
    vsanConfigInfo (`vim.vsan.cluster.ConfigInfo <vim/vsan/cluster/ConfigInfo.rst>`_, optional):

       Cluster-wide configuration of the VMware VSAN service.
    vsanHostConfig ([`vim.vsan.host.ConfigInfo <vim/vsan/host/ConfigInfo.rst>`_], optional):

       List of host configurations for the VMware VSAN service. Each entry applies to one host.If a host is not specified in this array, the service uses the cluster default settings for that host.
    group ([`vim.cluster.GroupInfo <vim/cluster/GroupInfo.rst>`_], optional):

       Cluster-wide groups.
