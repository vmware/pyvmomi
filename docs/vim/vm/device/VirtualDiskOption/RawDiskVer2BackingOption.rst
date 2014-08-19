
vim.vm.device.VirtualDiskOption.RawDiskVer2BackingOption
========================================================
  The VirtualDiskOption.RawDiskVer2BackingOption object type contains the available options when backing a virtual disk using a host device on VMware Server.
:extends: vim.vm.device.VirtualDeviceOption.DeviceBackingOption_

Attributes:
    descriptorFileNameExtensions (`vim.option.ChoiceOption <vim/option/ChoiceOption.rst>`_):

       Valid extensions for the filename of the raw disk descriptor file.
    uuid (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Flag to indicate whether this backing supports disk UUID property.
