
vim.host.SriovInfo
==================
  This data object provides information about the state of SR-IOV device.
:extends: vim.host.PciPassthruInfo_
:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_

Attributes:
    sriovEnabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Whether SRIOV has been enabled by the user
    sriovCapable (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Whether SRIOV is possible for this device
    sriovActive (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Whether SRIOV is active for this device (meaning enabled + rebooted)
    numVirtualFunctionRequested (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Number of SRIOV virtual functions requested for this device
    numVirtualFunction (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Number of SRIOV virtual functions present on this device
    maxVirtualFunctionSupported (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Maximum number of SRIOV virtual functions supported on this device
