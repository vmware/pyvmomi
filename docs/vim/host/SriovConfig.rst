.. _int: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.5: ../../vim/version.rst#vimversionversion9

.. _vim.host.PciPassthruConfig: ../../vim/host/PciPassthruConfig.rst


vim.host.SriovConfig
====================
  This data object allows configuration of SR-IOV device.
:extends: vim.host.PciPassthruConfig_
:since: `vSphere API 5.5`_

Attributes:
    sriovEnabled (`bool`_):

       enable SR-IOV for this device
    numVirtualFunction (`int`_):

       Number of SR-IOV virtual functions to enable on this device
