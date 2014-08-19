
vim.host.PciPassthruInfo
========================
  This data object provides information about the state of PciPassthru for all pci devices.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    id (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The name ID of this PCI, composed of "bus:slot.function".
    dependentDevice (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Device which needs to be unclaimed by vmkernel (may be bridge)
    passthruEnabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Whether passThru has been configured by the user
    passthruCapable (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Whether passThru is even possible for this device (decided by vmkctl)
    passthruActive (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Whether passThru is active for this device (meaning enabled + rebooted)
