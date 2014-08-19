
vim.host.Ruleset.Rule
=====================
  This data object type describes a port (or range of ports), identified by port number(s), direction and protocol. It is used as a convenient way for users to express what ports they want to permit through the firewall.
:extends: vmodl.DynamicData_

Attributes:
    port (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The port number.
    endPort (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       For a port range, the ending port number.
    direction (`vim.host.Ruleset.Rule.Direction <vim/host/Ruleset/Rule/Direction.rst>`_):

       The port direction.
    portType (`vim.host.Ruleset.Rule.PortType <vim/host/Ruleset/Rule/PortType.rst>`_, optional):

       The port type.
    protocol (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The port protocol. Valid values are defined by the `HostFirewallRuleProtocol <vim/host/Ruleset/Rule/Protocol.rst>`_ enumeration.
