.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.host.PciPassthruConfig
==========================
  This data object provides information about the state of PciPassthru for all pci devices.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    id (`str`_):

       The name ID of this PCI, composed of "bus:slot.function".
    passthruEnabled (`bool`_):

       Whether passThru is has been configured for this device
