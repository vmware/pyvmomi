.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _service: ../../vim/host/ServiceInfo.rst#service

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _HostFirewallSystem: ../../vim/host/FirewallSystem.rst

.. _vim.host.Ruleset.Rule: ../../vim/host/Ruleset/Rule.rst

.. _vim.host.Ruleset.IpList: ../../vim/host/Ruleset/IpList.rst


vim.host.Ruleset
================
  Data object that describes a single network ruleset that can be allowed or blocked by the firewall using the `HostFirewallSystem`_ object.
:extends: vmodl.DynamicData_

Attributes:
    key (`str`_):

       Brief identifier for the ruleset.
    label (`str`_):

       Display label for the ruleset.
    required (`bool`_):

       Flag indicating whether the ruleset is required and cannot be disabled.
    rule (`vim.host.Ruleset.Rule`_):

       List of rules within the ruleset.
    service (`str`_, optional):

       Managed service (if any) that uses this ruleset. Must be one of the services listed in `service`_ .
    enabled (`bool`_):

       Flag indicating whether the ruleset is enabled. If the ruleset is enabled, all ports specified in the ruleset are opened by the firewall.
    allowedHosts (`vim.host.Ruleset.IpList`_, optional):

       List of ipaddress to allow access to the service
