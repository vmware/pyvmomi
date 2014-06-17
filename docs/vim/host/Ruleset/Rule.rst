.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _HostFirewallRuleProtocol: ../../../vim/host/Ruleset/Rule/Protocol.rst

.. _vim.host.Ruleset.Rule.PortType: ../../../vim/host/Ruleset/Rule/PortType.rst

.. _vim.host.Ruleset.Rule.Direction: ../../../vim/host/Ruleset/Rule/Direction.rst


vim.host.Ruleset.Rule
=====================
  This data object type describes a port (or range of ports), identified by port number(s), direction and protocol. It is used as a convenient way for users to express what ports they want to permit through the firewall.
:extends: vmodl.DynamicData_

Attributes:
    port (`int`_):

       The port number.
    endPort (`int`_, optional):

       For a port range, the ending port number.
    direction (`vim.host.Ruleset.Rule.Direction`_):

       The port direction.
    portType (`vim.host.Ruleset.Rule.PortType`_, optional):

       The port type.
    protocol (`str`_):

       The port protocol. Valid values are defined by the `HostFirewallRuleProtocol`_ enumeration.
