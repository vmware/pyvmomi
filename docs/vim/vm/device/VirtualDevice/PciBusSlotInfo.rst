.. _int: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.1: ../../../../vim/version.rst#vimversionversion8

.. _VirtualDevicePciBusSlotInfo: ../../../../vim/vm/device/VirtualDevice/PciBusSlotInfo.rst

.. _vim.vm.device.VirtualDevice.BusSlotInfo: ../../../../vim/vm/device/VirtualDevice/BusSlotInfo.rst


vim.vm.device.VirtualDevice.PciBusSlotInfo
==========================================
  The `VirtualDevicePciBusSlotInfo`_ data object type defines information about a pci bus slot of pci device in a virtual machine.
:extends: vim.vm.device.VirtualDevice.BusSlotInfo_
:since: `vSphere API 5.1`_

Attributes:
    pciSlotNumber (`int`_):

       The pci slot number of the virtual device.The pci slot number assignment should generally be left to the system. If assigned a value, and the value is invalid or duplicated, it will automatically be reassigned. This will not cause an error.Generally, the PCI slot numbers should never be specified in an Reconfigure operation, and only in a CreateVM operation if i) they are specified for all devices, and ii) the numbers have been determined by looking at an existing VM configuration of similar hardware version. In other words, when the virtual hardware configuration is duplicated.
