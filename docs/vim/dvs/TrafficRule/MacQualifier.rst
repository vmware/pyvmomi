
vim.dvs.TrafficRule.MacQualifier
================================
  This class defines the MAC Rule Qualifier. Here MAC addresses of source and destination will be used for classifying packets.
:extends: vim.dvs.TrafficRule.Qualifier_
:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_

Attributes:
    sourceAddress (`vim.MacAddress <vim/MacAddress.rst>`_, optional):

       MAC address for source. If this property is NULL, it will match "any MAC address".
    destinationAddress (`vim.MacAddress <vim/MacAddress.rst>`_, optional):

       MAC address for destination. If this property is NULL, it will match "any MAC address".
    protocol (`vim.IntExpression <vim/IntExpression.rst>`_, optional):

       Protocol used. This corresponds to the EtherType field in Ethernet frame. The valid values can be found from IEEE list at: http://standards.ieee.org/regauth/ as mentioned in RFC 5342.
    vlanId (`vim.IntExpression <vim/IntExpression.rst>`_, optional):

       vlan id.
