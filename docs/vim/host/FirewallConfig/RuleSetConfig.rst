.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.host.Ruleset.IpList: ../../../vim/host/Ruleset/IpList.rst


vim.host.FirewallConfig.RuleSetConfig
=====================================
  
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    rulesetId (`str`_):

       Id of the ruleset.
    enabled (`bool`_):

       Flag indicating if the specified ruleset should be enabled.
    allowedHosts (`vim.host.Ruleset.IpList`_, optional):

       The list of allowed ip addresses
