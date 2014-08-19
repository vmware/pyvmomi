
vim.cluster.ConfigInfo
======================
  A complete cluster configuration.
:extends: vmodl.DynamicData_
**deprecated**


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
