.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _qualifier: ../../vim/dvs/TrafficRule.rst#qualifier

.. _vSphere API 5.5: ../../vim/version.rst#vimversionversion9

.. _DvsFilterPolicy: ../../vim/dvs/DistributedVirtualPort/FilterPolicy.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _DvsNetworkRuleQualifier: ../../vim/dvs/TrafficRule/Qualifier.rst

.. _DvsStatefulFirewallPolicy: ../../vim/dvs/StatefulFirewallPolicy.rst

.. _DvsIpNetworkRuleQualifier: ../../vim/dvs/TrafficRule/IpQualifier.rst

.. _vim.dvs.TrafficRule.Action: ../../vim/dvs/TrafficRule/Action.rst

.. _DvsMacNetworkRuleQualifier: ../../vim/dvs/TrafficRule/MacQualifier.rst

.. _vim.dvs.TrafficRule.Qualifier: ../../vim/dvs/TrafficRule/Qualifier.rst

.. _DvsSystemTrafficNetworkRuleQualifier: ../../vim/dvs/TrafficRule/SystemTrafficQualifier.rst


vim.dvs.TrafficRule
===================
  This class defines a single rule that will be applied to network traffic.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5`_

Attributes:
    key (`str`_, optional):

       The key of the rule
    description (`str`_, optional):

       Description of the rule
    sequence (`int`_, optional):

       Sequence of this rule. i.e, the order in which this rule appears in the ruleset.
    qualifier (`vim.dvs.TrafficRule.Qualifier`_, optional):

       List of Network rule qualifiers. 'AND' of this array of network rule qualifiers is applied as one network traffic rule. If the TrafficRule belongs to `DvsFilterPolicy`_ : There can be a maximum of 1 `DvsIpNetworkRuleQualifier`_ , 1 `DvsMacNetworkRuleQualifier`_ and 1 `DvsSystemTrafficNetworkRuleQualifier`_ for a total of 3 `qualifier`_ If the TrafficRule belongs to `DvsStatefulFirewallPolicy`_ : There can be only 1 `DvsNetworkRuleQualifier`_ in `qualifier`_ 
    action (`vim.dvs.TrafficRule.Action`_, optional):

       Action to be applied for this rule.
    direction (`str`_, optional):

       Whether this rule needs to be applied to incoming packets, to outgoing packets or both. See RuleDirectionType for valid values.
