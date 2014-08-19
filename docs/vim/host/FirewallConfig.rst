
vim.host.FirewallConfig
=======================
  DataObject used for firewall configuration
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    rule ([`vim.host.FirewallConfig.RuleSetConfig <vim/host/FirewallConfig/RuleSetConfig.rst>`_], optional):

       Rules determining firewall settings.
    defaultBlockingPolicy (`vim.host.FirewallInfo.DefaultPolicy <vim/host/FirewallInfo/DefaultPolicy.rst>`_):

       Default settings for the firewall, used for ports that are not explicitly opened.
