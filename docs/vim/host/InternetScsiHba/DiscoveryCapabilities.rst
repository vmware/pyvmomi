.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.host.InternetScsiHba.DiscoveryCapabilities
==============================================
  The discovery capabilities for this host bus adapter. At least one discovery mode must always be active. Multiple modes may be active at the same time.
:extends: vmodl.DynamicData_

Attributes:
    iSnsDiscoverySettable (`bool`_):

       True if this host bus adapter supports iSNS
    slpDiscoverySettable (`bool`_):

       True if this host bus adapter supports SLP
    staticTargetDiscoverySettable (`bool`_):

       True if this host bus adapter supports static discovery
    sendTargetsDiscoverySettable (`bool`_):

       True if this host bus adapter supports changing the configuration state of send targets discovery. Send targets is mandatory, however some adapters may not allow disabling this discovery method.
