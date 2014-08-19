
vim.host.InternetScsiHba.DiscoveryCapabilities
==============================================
  The discovery capabilities for this host bus adapter. At least one discovery mode must always be active. Multiple modes may be active at the same time.
:extends: vmodl.DynamicData_

Attributes:
    iSnsDiscoverySettable (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       True if this host bus adapter supports iSNS
    slpDiscoverySettable (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       True if this host bus adapter supports SLP
    staticTargetDiscoverySettable (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       True if this host bus adapter supports static discovery
    sendTargetsDiscoverySettable (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       True if this host bus adapter supports changing the configuration state of send targets discovery. Send targets is mandatory, however some adapters may not allow disabling this discovery method.
