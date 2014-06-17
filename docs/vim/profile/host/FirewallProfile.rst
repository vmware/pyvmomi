.. _policy: ../../../vim/profile/ApplyProfile.rst#policy

.. _property: ../../../vim/profile/ApplyProfile.rst#property

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _FirewallProfile: ../../../vim/profile/host/FirewallProfile.rst

.. _vim.profile.ApplyProfile: ../../../vim/profile/ApplyProfile.rst

.. _vim.profile.host.FirewallProfile.RulesetProfile: ../../../vim/profile/host/FirewallProfile/RulesetProfile.rst


vim.profile.host.FirewallProfile
================================
  The `FirewallProfile`_ data object represents a host firewall configuration. If a profile plug-in defines policies or subprofiles, use the `policy`_ or `property`_ list to access the additional configuration data.
:extends: vim.profile.ApplyProfile_
:since: `vSphere API 4.0`_

Attributes:
    ruleset (`vim.profile.host.FirewallProfile.RulesetProfile`_, optional):

       List of Rulesets that will be configured for the firewall subprofile.
