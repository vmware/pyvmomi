.. _int: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.5: ../../vim/version.rst#vimversionversion9

.. _vim.host.PciPassthruInfo: ../../vim/host/PciPassthruInfo.rst


vim.host.SriovInfo
==================
  This data object provides information about the state of SR-IOV device.
:extends: vim.host.PciPassthruInfo_
:since: `vSphere API 5.5`_

Attributes:
    sriovEnabled (`bool`_):

       Whether SRIOV has been enabled by the user
    sriovCapable (`bool`_):

       Whether SRIOV is possible for this device
    sriovActive (`bool`_):

       Whether SRIOV is active for this device (meaning enabled + rebooted)
    numVirtualFunctionRequested (`int`_):

       Number of SRIOV virtual functions requested for this device
    numVirtualFunction (`int`_):

       Number of SRIOV virtual functions present on this device
    maxVirtualFunctionSupported (`int`_):

       Maximum number of SRIOV virtual functions supported on this device
