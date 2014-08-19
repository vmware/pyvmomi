
vim.dvs.TrafficRule.IpQualifier
===============================
  This class defines the IP Rule Qualifier. Here IP addresses of source and destination will be used for classifying packets.
:extends: vim.dvs.TrafficRule.Qualifier_
:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_

Attributes:
    sourceAddress (`vim.IpAddress <vim/IpAddress.rst>`_, optional):

       IP qualifier for source. If this property is NULL, it will match "any IPv4 or any IPv6 address".
    destinationAddress (`vim.IpAddress <vim/IpAddress.rst>`_, optional):

       IP qualifier for destination. If this property is NULL, it will match "any IPv4 or any IPv6 address".
    protocol (`vim.IntExpression <vim/IntExpression.rst>`_, optional):

       Protocols like TCP, UDP, ICMP etc. The valid value for a protocol is got from IANA assigned value for the protocol. This can be got from RFC 5237 and IANA website section related to protocol numbers.
    sourceIpPort (`vim.dvs.TrafficRule.IpPort <vim/dvs/TrafficRule/IpPort.rst>`_, optional):

       Source IP Port.
    destinationIpPort (`vim.dvs.TrafficRule.IpPort <vim/dvs/TrafficRule/IpPort.rst>`_, optional):

       Destination IP Port.
    tcpFlags (`vim.IntExpression <vim/IntExpression.rst>`_, optional):

       TCP flags. The valid values can be found at RFC 3168.
