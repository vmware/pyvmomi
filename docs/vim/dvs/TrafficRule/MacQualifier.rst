.. _vim.MacAddress: ../../../vim/MacAddress.rst

.. _vSphere API 5.5: ../../../vim/version.rst#vimversionversion9

.. _vim.IntExpression: ../../../vim/IntExpression.rst

.. _vim.dvs.TrafficRule.Qualifier: ../../../vim/dvs/TrafficRule/Qualifier.rst


vim.dvs.TrafficRule.MacQualifier
================================
  This class defines the MAC Rule Qualifier. Here MAC addresses of source and destination will be used for classifying packets.
:extends: vim.dvs.TrafficRule.Qualifier_
:since: `vSphere API 5.5`_

Attributes:
    sourceAddress (`vim.MacAddress`_, optional):

       MAC address for source. If this property is NULL, it will match "any MAC address".
    destinationAddress (`vim.MacAddress`_, optional):

       MAC address for destination. If this property is NULL, it will match "any MAC address".
    protocol (`vim.IntExpression`_, optional):

       Protocol used. This corresponds to the EtherType field in Ethernet frame. The valid values can be found from IEEE list at: http://standards.ieee.org/regauth/ as mentioned in RFC 5342.
    vlanId (`vim.IntExpression`_, optional):

       vlan id.
