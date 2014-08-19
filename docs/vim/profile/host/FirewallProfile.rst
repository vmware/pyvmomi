
vim.profile.host.FirewallProfile
================================
  The `FirewallProfile <vim/profile/host/FirewallProfile.rst>`_ data object represents a host firewall configuration. If a profile plug-in defines policies or subprofiles, use the `policy <vim/profile/ApplyProfile.rst#policy>`_ or `property <vim/profile/ApplyProfile.rst#property>`_ list to access the additional configuration data.
:extends: vim.profile.ApplyProfile_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    ruleset ([`vim.profile.host.FirewallProfile.RulesetProfile <vim/profile/host/FirewallProfile/RulesetProfile.rst>`_], optional):

       List of Rulesets that will be configured for the firewall subprofile.
