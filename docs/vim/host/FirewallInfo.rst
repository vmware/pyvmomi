
vim.host.FirewallInfo
=====================
  Data object describing the firewall configuration.
:extends: vmodl.DynamicData_

Attributes:
    defaultPolicy (`vim.host.FirewallInfo.DefaultPolicy <vim/host/FirewallInfo/DefaultPolicy.rst>`_):

       Default firewall policy.
    ruleset ([`vim.host.Ruleset <vim/host/Ruleset.rst>`_], optional):

       List of configured rulesets.
