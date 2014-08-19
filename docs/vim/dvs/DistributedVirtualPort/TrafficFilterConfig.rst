
vim.dvs.DistributedVirtualPort.TrafficFilterConfig
==================================================
  This class defines Traffic Filter configuration.Supported Qualifier and ActionsTraffic Filter ConfigSupported classesQualifiers supported `SingleIp <vim/SingleIp.rst>`_ , `IpRange <vim/IpRange.rst>`_ , `SingleMac <vim/SingleMac.rst>`_ , `MacRange <vim/MacRange.rst>`_ , `DvsSingleIpPort <vim/dvs/TrafficRule/SingleIpPort.rst>`_ , `DvsSystemTrafficNetworkRuleQualifier <vim/dvs/TrafficRule/SystemTrafficQualifier.rst>`_ Actions Supported `DvsDropNetworkRuleAction <vim/dvs/TrafficRule/DropAction.rst>`_ , `DvsAcceptNetworkRuleAction <vim/dvs/TrafficRule/AcceptAction.rst>`_ , `DvsPuntNetworkRuleAction <vim/dvs/TrafficRule/PuntAction.rst>`_ , `DvsCopyNetworkRuleAction <vim/dvs/TrafficRule/CopyAction.rst>`_ , `DvsMacRewriteNetworkRuleAction <vim/dvs/TrafficRule/MacRewriteAction.rst>`_ , `DvsGreEncapNetworkRuleAction <vim/dvs/TrafficRule/GreAction.rst>`_ , `DvsLogNetworkRuleAction <vim/dvs/TrafficRule/LogAction.rst>`_ , `DvsUpdateTagNetworkRuleAction <vim/dvs/TrafficRule/UpdateTagAction.rst>`_ , `DvsRateLimitNetworkRuleAction <vim/dvs/TrafficRule/RateLimitAction.rst>`_ 
:extends: vim.dvs.DistributedVirtualPort.FilterConfig_
:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_

Attributes:
    trafficRuleset (`vim.dvs.TrafficRuleset <vim/dvs/TrafficRuleset.rst>`_, optional):

       Network Traffic Ruleset
