
vim.dvs.TrafficRule
===================
  This class defines a single rule that will be applied to network traffic.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_

Attributes:
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The key of the rule
    description (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Description of the rule
    sequence (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Sequence of this rule. i.e, the order in which this rule appears in the ruleset.
    qualifier ([`vim.dvs.TrafficRule.Qualifier <vim/dvs/TrafficRule/Qualifier.rst>`_], optional):

       List of Network rule qualifiers. 'AND' of this array of network rule qualifiers is applied as one network traffic rule. If the TrafficRule belongs to `DvsFilterPolicy <vim/dvs/DistributedVirtualPort/FilterPolicy.rst>`_ : There can be a maximum of 1 `DvsIpNetworkRuleQualifier <vim/dvs/TrafficRule/IpQualifier.rst>`_ , 1 `DvsMacNetworkRuleQualifier <vim/dvs/TrafficRule/MacQualifier.rst>`_ and 1 `DvsSystemTrafficNetworkRuleQualifier <vim/dvs/TrafficRule/SystemTrafficQualifier.rst>`_ for a total of 3 `qualifier <vim/dvs/TrafficRule.rst#qualifier>`_ If the TrafficRule belongs to `DvsStatefulFirewallPolicy <vim/dvs/StatefulFirewallPolicy.rst>`_ : There can be only 1 `DvsNetworkRuleQualifier <vim/dvs/TrafficRule/Qualifier.rst>`_ in `qualifier <vim/dvs/TrafficRule.rst#qualifier>`_ 
    action (`vim.dvs.TrafficRule.Action <vim/dvs/TrafficRule/Action.rst>`_, optional):

       Action to be applied for this rule.
    direction (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Whether this rule needs to be applied to incoming packets, to outgoing packets or both. See RuleDirectionType for valid values.
