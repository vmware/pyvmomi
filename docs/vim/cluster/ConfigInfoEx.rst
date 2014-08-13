.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _ClusterConfigInfoEx: ../../vim/cluster/ConfigInfoEx.rst

.. _ClusterConfigSpecEx: ../../vim/cluster/ConfigSpecEx.rst

.. _vim.cluster.RuleInfo: ../../vim/cluster/RuleInfo.rst

.. _vim.cluster.GroupInfo: ../../vim/cluster/GroupInfo.rst

.. _vim.vsan.host.ConfigInfo: ../../vim/vsan/host/ConfigInfo.rst

.. _vim.cluster.DrsConfigInfo: ../../vim/cluster/DrsConfigInfo.rst

.. _vim.cluster.DpmConfigInfo: ../../vim/cluster/DpmConfigInfo.rst

.. _vim.cluster.DasConfigInfo: ../../vim/cluster/DasConfigInfo.rst

.. _vim.cluster.DrsVmConfigInfo: ../../vim/cluster/DrsVmConfigInfo.rst

.. _vim.cluster.DasVmConfigInfo: ../../vim/cluster/DasVmConfigInfo.rst

.. _vim.vsan.cluster.ConfigInfo: ../../vim/vsan/cluster/ConfigInfo.rst

.. _vim.cluster.DpmHostConfigInfo: ../../vim/cluster/DpmHostConfigInfo.rst

.. _vim.ComputeResource.ConfigInfo: ../../vim/ComputeResource/ConfigInfo.rst


vim.cluster.ConfigInfoEx
========================
  The `ClusterConfigInfoEx`_ data object describes a complete cluster configuration. For information about configuring a cluster, see `ClusterConfigSpecEx`_ .
:extends: vim.ComputeResource.ConfigInfo_
:since: `VI API 2.5`_

Attributes:
    dasConfig (`vim.cluster.DasConfigInfo`_):

       Cluster-wide configuration of the vSphere HA service.
    dasVmConfig ([`vim.cluster.DasVmConfigInfo`_], optional):

       List of virtual machine configurations for the vSphere HA service. Each entry applies to one virtual machine.If a virtual machine is not specified in this array, the service uses the default settings for that virtual machine.
    drsConfig (`vim.cluster.DrsConfigInfo`_):

       Cluster-wide configuration of the VMware DRS service.
    drsVmConfig ([`vim.cluster.DrsVmConfigInfo`_], optional):

       List of virtual machine configurations for the VMware DRS service. Each entry applies to one virtual machine.If a virtual machine is not specified in this array, the service uses the default settings for that virtual machine.
    rule ([`vim.cluster.RuleInfo`_], optional):

       Cluster-wide rules.
    dpmConfigInfo (`vim.cluster.DpmConfigInfo`_, optional):

       Cluster-wide configuration of the VMware DPM service.
    dpmHostConfig ([`vim.cluster.DpmHostConfigInfo`_], optional):

       List of host configurations for the VMware DPM service. Each entry applies to one host.If a host is not specified in this array, the service uses the cluster default settings for that host.
    vsanConfigInfo (`vim.vsan.cluster.ConfigInfo`_, optional):

       Cluster-wide configuration of the VMware VSAN service.
    vsanHostConfig ([`vim.vsan.host.ConfigInfo`_], optional):

       List of host configurations for the VMware VSAN service. Each entry applies to one host.If a host is not specified in this array, the service uses the cluster default settings for that host.
    group ([`vim.cluster.GroupInfo`_], optional):

       Cluster-wide groups.
