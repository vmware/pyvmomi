
vim.host.FirewallConfig.RuleSetConfig
=====================================
  
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    rulesetId (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Id of the ruleset.
    enabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Flag indicating if the specified ruleset should be enabled.
    allowedHosts (`vim.host.Ruleset.IpList <vim/host/Ruleset/IpList.rst>`_, optional):

       The list of allowed ip addresses
