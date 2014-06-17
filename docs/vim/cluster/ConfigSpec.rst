.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.cluster.RuleSpec: ../../vim/cluster/RuleSpec.rst

.. _vim.cluster.DrsConfigInfo: ../../vim/cluster/DrsConfigInfo.rst

.. _vim.cluster.DasConfigInfo: ../../vim/cluster/DasConfigInfo.rst

.. _vim.cluster.DrsVmConfigSpec: ../../vim/cluster/DrsVmConfigSpec.rst

.. _vim.cluster.DasVmConfigSpec: ../../vim/cluster/DasVmConfigSpec.rst


vim.cluster.ConfigSpec
======================
  A complete cluster configuration. All fields are defined as optional. In case of a reconfiguration, unset fields are unchanged.
:extends: vmodl.DynamicData_
**deprecated**


Attributes:
    dasConfig (`vim.cluster.DasConfigInfo`_, optional):

       Changes to the configuration of vSphere HA.
    dasVmConfigSpec (`vim.cluster.DasVmConfigSpec`_, optional):

       Changes to the per-virtual-machine vSphere HA settings.
    drsConfig (`vim.cluster.DrsConfigInfo`_, optional):

       Changes to the configuration of the VMware DRS service.
    drsVmConfigSpec (`vim.cluster.DrsVmConfigSpec`_, optional):

       Changes to the per-virtual-machine DRS settings.
    rulesSpec (`vim.cluster.RuleSpec`_, optional):

       Changes to the set of rules.
