
vim.host.Ruleset
================
  Data object that describes a single network ruleset that can be allowed or blocked by the firewall using the `HostFirewallSystem <vim/host/FirewallSystem.rst>`_ object.
:extends: vmodl.DynamicData_

Attributes:
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Brief identifier for the ruleset.
    label (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Display label for the ruleset.
    required (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Flag indicating whether the ruleset is required and cannot be disabled.
    rule ([`vim.host.Ruleset.Rule <vim/host/Ruleset/Rule.rst>`_]):

       List of rules within the ruleset.
    service (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Managed service (if any) that uses this ruleset. Must be one of the services listed in `service <vim/host/ServiceInfo.rst#service>`_ .
    enabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Flag indicating whether the ruleset is enabled. If the ruleset is enabled, all ports specified in the ruleset are opened by the firewall.
    allowedHosts (`vim.host.Ruleset.IpList <vim/host/Ruleset/IpList.rst>`_, optional):

       List of ipaddress to allow access to the service
