
vim.host.SriovConfig
====================
  This data object allows configuration of SR-IOV device.
:extends: vim.host.PciPassthruConfig_
:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_

Attributes:
    sriovEnabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       enable SR-IOV for this device
    numVirtualFunction (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Number of SR-IOV virtual functions to enable on this device
