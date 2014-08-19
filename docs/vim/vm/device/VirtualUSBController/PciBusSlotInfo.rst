
vim.vm.device.VirtualUSBController.PciBusSlotInfo
=================================================
  ThePciBusSlotInfodata object type defines information about the pci bus slots of usb controller device in a virtual machine.
:extends: vim.vm.device.VirtualDevice.PciBusSlotInfo_
:since: `vSphere API 5.1 <vim/version.rst#vimversionversion8>`_

Attributes:
    ehciPciSlotNumber (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The pci slot number of eHCI controller.This property should be used only when the ehciEnabled property is set to true.
