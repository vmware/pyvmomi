.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.host.FirewallInfo.DefaultPolicy: ../../vim/host/FirewallInfo/DefaultPolicy.rst

.. _vim.host.FirewallConfig.RuleSetConfig: ../../vim/host/FirewallConfig/RuleSetConfig.rst


vim.host.FirewallConfig
=======================
  DataObject used for firewall configuration
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    rule ([`vim.host.FirewallConfig.RuleSetConfig`_], optional):

       Rules determining firewall settings.
    defaultBlockingPolicy (`vim.host.FirewallInfo.DefaultPolicy`_):

       Default settings for the firewall, used for ports that are not explicitly opened.
