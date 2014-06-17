.. _str: https://docs.python.org/2/library/stdtypes.html

.. _IpRange: ../../../vim/IpRange.rst

.. _SingleIp: ../../../vim/SingleIp.rst

.. _MacRange: ../../../vim/MacRange.rst

.. _SingleMac: ../../../vim/SingleMac.rst

.. _DvsSingleIpPort: ../../../vim/dvs/TrafficRule/SingleIpPort.rst

.. _vSphere API 5.5: ../../../vim/version.rst#vimversionversion9

.. _DvsFilterOnFailure: ../../../vim/dvs/DistributedVirtualPort/FilterOnFailure.rst

.. _vim.InheritablePolicy: ../../../vim/InheritablePolicy.rst

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

.. _vim.dvs.DistributedVirtualPort.FilterParameter: ../../../vim/dvs/DistributedVirtualPort/FilterParameter.rst


vim.dvs.DistributedVirtualPort.FilterConfig
===========================================
  This class defines Network Filter configuration.Supported Qualifier and ActionsNetwork Filter ConfigSupported classesQualifiers supported `SingleIp`_ , `IpRange`_ , `SingleMac`_ , `MacRange`_ , `DvsSingleIpPort`_ , `DvsSystemTrafficNetworkRuleQualifier`_ Actions Supported `DvsDropNetworkRuleAction`_ , `DvsAcceptNetworkRuleAction`_ , `DvsPuntNetworkRuleAction`_ , `DvsCopyNetworkRuleAction`_ , `DvsMacRewriteNetworkRuleAction`_ , `DvsGreEncapNetworkRuleAction`_ , `DvsLogNetworkRuleAction`_ , `DvsUpdateTagNetworkRuleAction`_ , `DvsRateLimitNetworkRuleAction`_ 
:extends: vim.InheritablePolicy_
:since: `vSphere API 5.5`_

Attributes:
    key (`str`_, optional):

       The key of Network Filter Config.
    agentName (`str`_, optional):

       The name of the network traffic filter agent.
    slotNumber (`str`_, optional):

       The slot number of the network filter agent.
    parameters (`vim.dvs.DistributedVirtualPort.FilterParameter`_, optional):

       Network Filter Parameter
    onFailure (`str`_, optional):

       This property specifies whether to allow all traffic or to deny all traffic when a Network Filter fails to configure. Please see `DvsFilterOnFailure`_ for more details.
