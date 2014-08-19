
vim.dvs.TrafficRule.UpdateTagAction
===================================
  This class defines network rule action to tag packets(qos,dscp) or clear tags(clear qos, dscp tags) on packets. One or both of qos and dscp may be specified.
:extends: vim.dvs.TrafficRule.Action_
:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_

Attributes:
    qosTag (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       QOS tag. IEEE 802.1p supports 3 bit Priority Code Point (PCP). The valid values are between 0-7. Please refer the IEEE 802.1p documentation for more details about what each value represents. If qosTag is set to 0 then the tag on the packets will be cleared.
    dscpTag (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       DSCP tag. The valid values for DSCP tag can be found in 'Differentiated Services Field Codepoints' section of IANA website. The information can also be got from reading all of the below RFC: RFC 2474, RFC 2597, RFC 3246, RFC 5865. If the dscpTag is set to 0 then the dscp tag on packets will be cleared.
