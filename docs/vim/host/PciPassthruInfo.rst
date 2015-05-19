.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.host.PciPassthruInfo
========================
  This data object provides information about the state of PciPassthru for all pci devices.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    id (`str`_):

       The name ID of this PCI, composed of "bus:slot.function".
    dependentDevice (`str`_):

       Device which needs to be unclaimed by vmkernel (may be bridge)
    passthruEnabled (`bool`_):

       Whether passThru has been configured by the user
    passthruCapable (`bool`_):

       Whether passThru is even possible for this device (decided by vmkctl)
    passthruActive (`bool`_):

       Whether passThru is active for this device (meaning enabled + rebooted)
