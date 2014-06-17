.. _IpRange: ../../../vim/IpRange.rst

.. _SingleIp: ../../../vim/SingleIp.rst

.. _MacRange: ../../../vim/MacRange.rst

.. _SingleMac: ../../../vim/SingleMac.rst

.. _DvsSingleIpPort: ../../../vim/dvs/TrafficRule/SingleIpPort.rst

.. _vSphere API 5.5: ../../../vim/version.rst#vimversionversion9

.. _vim.dvs.TrafficRuleset: ../../../vim/dvs/TrafficRuleset.rst

.. _DvsLogNetworkRuleAction: ../../../vim/dvs/TrafficRule/LogAction.rst

.. _DvsCopyNetworkRuleAction: ../../../vim/dvs/TrafficRule/CopyAction.rst

.. _DvsDropNetworkRuleAction: ../../../vim/dvs/TrafficRule/DropAction.rst

.. _DvsPuntNetworkRuleAction: ../../../vim/dvs/TrafficRule/PuntAction.rst

.. _DvsAcceptNetworkRuleAction: ../../../vim/dvs/TrafficRule/AcceptAction.rst

.. _DvsGreEncapNetworkRuleAction: ../../../vim/dvs/TrafficRule/GreAction.rst

.. _DvsRateLimitNetworkRuleAction: ../../../vim/dvs/TrafficRule/RateLimitAction.rst

.. _DvsUpdateTagNetworkRuleAction: ../../../vim/dvs/TrafficRule/UpdateTagAction.rst

.. _DvsMacRewriteNetworkRuleAction: ../../../vim/dvs/TrafficRule/MacRewriteAction.rst

.. _DvsSystemTrafficNetworkRuleQualifier: ../../../vim/dvs/TrafficRule/SystemTrafficQualifier.rst

.. _vim.dvs.DistributedVirtualPort.FilterConfig: ../../../vim/dvs/DistributedVirtualPort/FilterConfig.rst


vim.dvs.DistributedVirtualPort.TrafficFilterConfig
==================================================
  This class defines Traffic Filter configuration.Supported Qualifier and ActionsTraffic Filter ConfigSupported classesQualifiers supported `SingleIp`_ , `IpRange`_ , `SingleMac`_ , `MacRange`_ , `DvsSingleIpPort`_ , `DvsSystemTrafficNetworkRuleQualifier`_ Actions Supported `DvsDropNetworkRuleAction`_ , `DvsAcceptNetworkRuleAction`_ , `DvsPuntNetworkRuleAction`_ , `DvsCopyNetworkRuleAction`_ , `DvsMacRewriteNetworkRuleAction`_ , `DvsGreEncapNetworkRuleAction`_ , `DvsLogNetworkRuleAction`_ , `DvsUpdateTagNetworkRuleAction`_ , `DvsRateLimitNetworkRuleAction`_ 
:extends: vim.dvs.DistributedVirtualPort.FilterConfig_
:since: `vSphere API 5.5`_

Attributes:
    trafficRuleset (`vim.dvs.TrafficRuleset`_, optional):

       Network Traffic Ruleset
