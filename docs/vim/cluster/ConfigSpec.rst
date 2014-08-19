
vim.cluster.ConfigSpec
======================
  A complete cluster configuration. All fields are defined as optional. In case of a reconfiguration, unset fields are unchanged.
:extends: vmodl.DynamicData_
**deprecated**


Attributes:
    dasConfig (`vim.cluster.DasConfigInfo <vim/cluster/DasConfigInfo.rst>`_, optional):

       Changes to the configuration of vSphere HA.
    dasVmConfigSpec ([`vim.cluster.DasVmConfigSpec <vim/cluster/DasVmConfigSpec.rst>`_], optional):

       Changes to the per-virtual-machine vSphere HA settings.
    drsConfig (`vim.cluster.DrsConfigInfo <vim/cluster/DrsConfigInfo.rst>`_, optional):

       Changes to the configuration of the VMware DRS service.
    drsVmConfigSpec ([`vim.cluster.DrsVmConfigSpec <vim/cluster/DrsVmConfigSpec.rst>`_], optional):

       Changes to the per-virtual-machine DRS settings.
    rulesSpec ([`vim.cluster.RuleSpec <vim/cluster/RuleSpec.rst>`_], optional):

       Changes to the set of rules.
