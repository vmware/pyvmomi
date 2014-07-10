.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _SlpDiscoveryMethod: ../../../vim/host/InternetScsiHba/DiscoveryProperties/SlpDiscoveryMethod.rst

.. _InternetScsiSnsDiscoveryMethod: ../../../vim/host/InternetScsiHba/DiscoveryProperties/ISnsDiscoveryMethod.rst


vim.host.InternetScsiHba.DiscoveryProperties
============================================
  The discovery settings for this host bus adapter. At least one discovery mode must always be active. Multiple modes may be active at the same time.
:extends: vmodl.DynamicData_

Attributes:
    iSnsDiscoveryEnabled (`bool`_):

       True if iSNS is currently enabled
    iSnsDiscoveryMethod (`str`_, optional):

       The iSNS discovery method in use when iSNS is enabled. Must be one of the values of `InternetScsiSnsDiscoveryMethod`_ 
    iSnsHost (`str`_, optional):

       For STATIC iSNS, this is the iSNS server address
    slpDiscoveryEnabled (`bool`_):

       True if SLP is enabled
    slpDiscoveryMethod (`str`_, optional):

       The current SLP discovery method when SLP is enabled. Must be one of the values of `SlpDiscoveryMethod`_ 
    slpHost (`str`_, optional):

       When the SLP discovery method is set to MANUAL, this property reflects the hostname, and optionally port number of the SLP DA.
    staticTargetDiscoveryEnabled (`bool`_):

       True if static target discovery is enabled
    sendTargetsDiscoveryEnabled (`bool`_):

       True if send targets discovery is enabled
