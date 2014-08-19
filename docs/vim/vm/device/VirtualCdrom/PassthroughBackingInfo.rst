
vim.vm.device.VirtualCdrom.PassthroughBackingInfo
=================================================
  The VirtualCdrom.PassthroughBackingInfo data class represents a device pass-through backing for a virtual CD-ROM.
:extends: vim.vm.device.VirtualDevice.DeviceBackingInfo_

Attributes:
    exclusive (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Flag to indicate whether or not the virtual machine has exclusive CD-ROM device access.
