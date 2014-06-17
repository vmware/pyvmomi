.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.cluster.RuleInfo: ../../vim/cluster/RuleInfo.rst

.. _vim.cluster.DrsConfigInfo: ../../vim/cluster/DrsConfigInfo.rst

.. _vim.cluster.DasConfigInfo: ../../vim/cluster/DasConfigInfo.rst

.. _vim.cluster.DrsVmConfigInfo: ../../vim/cluster/DrsVmConfigInfo.rst

.. _vim.cluster.DasVmConfigInfo: ../../vim/cluster/DasVmConfigInfo.rst


vim.cluster.ConfigInfo
======================
  A complete cluster configuration.
:extends: vmodl.DynamicData_
**deprecated**


Attributes:
    dasConfig (`vim.cluster.DasConfigInfo`_):

       Cluster-wide configuration of the vSphere HA service.
    dasVmConfig (`vim.cluster.DasVmConfigInfo`_, optional):

       List of virtual machine configurations for the vSphere HA service. Each entry applies to one virtual machine.If a virtual machine is not specified in this array, the service uses the default settings for that virtual machine.
    drsConfig (`vim.cluster.DrsConfigInfo`_):

       Cluster-wide configuration of the VMware DRS service.
    drsVmConfig (`vim.cluster.DrsVmConfigInfo`_, optional):

       List of virtual machine configurations for the VMware DRS service. Each entry applies to one virtual machine.If a virtual machine is not specified in this array, the service uses the default settings for that virtual machine.
    rule (`vim.cluster.RuleInfo`_, optional):

       Cluster-wide rules.
