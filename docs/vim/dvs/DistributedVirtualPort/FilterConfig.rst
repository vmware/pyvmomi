
vim.dvs.DistributedVirtualPort.FilterConfig
===========================================
  This class defines Network Filter configuration.Supported Qualifier and ActionsNetwork Filter ConfigSupported classesQualifiers supported `SingleIp <vim/SingleIp.rst>`_ , `IpRange <vim/IpRange.rst>`_ , `SingleMac <vim/SingleMac.rst>`_ , `MacRange <vim/MacRange.rst>`_ , `DvsSingleIpPort <vim/dvs/TrafficRule/SingleIpPort.rst>`_ , `DvsSystemTrafficNetworkRuleQualifier <vim/dvs/TrafficRule/SystemTrafficQualifier.rst>`_ Actions Supported `DvsDropNetworkRuleAction <vim/dvs/TrafficRule/DropAction.rst>`_ , `DvsAcceptNetworkRuleAction <vim/dvs/TrafficRule/AcceptAction.rst>`_ , `DvsPuntNetworkRuleAction <vim/dvs/TrafficRule/PuntAction.rst>`_ , `DvsCopyNetworkRuleAction <vim/dvs/TrafficRule/CopyAction.rst>`_ , `DvsMacRewriteNetworkRuleAction <vim/dvs/TrafficRule/MacRewriteAction.rst>`_ , `DvsGreEncapNetworkRuleAction <vim/dvs/TrafficRule/GreAction.rst>`_ , `DvsLogNetworkRuleAction <vim/dvs/TrafficRule/LogAction.rst>`_ , `DvsUpdateTagNetworkRuleAction <vim/dvs/TrafficRule/UpdateTagAction.rst>`_ , `DvsRateLimitNetworkRuleAction <vim/dvs/TrafficRule/RateLimitAction.rst>`_ 
:extends: vim.InheritablePolicy_
:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_

Attributes:
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The key of Network Filter Config.
    agentName (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The name of the network traffic filter agent.
    slotNumber (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The slot number of the network filter agent.
    parameters (`vim.dvs.DistributedVirtualPort.FilterParameter <vim/dvs/DistributedVirtualPort/FilterParameter.rst>`_, optional):

       Network Filter Parameter
    onFailure (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       This property specifies whether to allow all traffic or to deny all traffic when a Network Filter fails to configure. Please see `DvsFilterOnFailure <vim/dvs/DistributedVirtualPort/FilterOnFailure.rst>`_ for more details.
