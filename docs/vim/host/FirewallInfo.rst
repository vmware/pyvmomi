.. _vim.host.Ruleset: ../../vim/host/Ruleset.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.host.FirewallInfo.DefaultPolicy: ../../vim/host/FirewallInfo/DefaultPolicy.rst


vim.host.FirewallInfo
=====================
  Data object describing the firewall configuration.
:extends: vmodl.DynamicData_

Attributes:
    defaultPolicy (`vim.host.FirewallInfo.DefaultPolicy`_):

       Default firewall policy.
    ruleset (`vim.host.Ruleset`_, optional):

       List of configured rulesets.
