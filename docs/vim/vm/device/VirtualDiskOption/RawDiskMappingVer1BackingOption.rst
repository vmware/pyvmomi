
vim.vm.device.VirtualDiskOption.RawDiskMappingVer1BackingOption
===============================================================
  The VirtualDiskOption.RawDiskMappingVer1BackingOption object type contains the available options when backing a virtual disk using a raw device mapping on ESX Server 2.5 or 3.x.
:extends: vim.vm.device.VirtualDeviceOption.DeviceBackingOption_

Attributes:
    descriptorFileNameExtensions (`vim.option.ChoiceOption <vim/option/ChoiceOption.rst>`_, optional):

       Valid extensions for the filename of the optional raw disk mapping descriptor file. This is present only for ESX Server 3.x and greater hosts.
    compatibilityMode (`vim.option.ChoiceOption <vim/option/ChoiceOption.rst>`_):

       The supported raw disk mapping compatibility modes.See `VirtualDiskCompatibilityMode <vim/vm/device/VirtualDiskOption/CompatibilityMode.rst>`_ 
    diskMode (`vim.option.ChoiceOption <vim/option/ChoiceOption.rst>`_):

       The disk mode. Valid values are:
        * `persistent <vim/vm/device/VirtualDiskOption/DiskMode.rst#persistent>`_
        * 
        * `independent_persistent <vim/vm/device/VirtualDiskOption/DiskMode.rst#independent_persistent>`_
        * 
        * `independent_nonpersistent <vim/vm/device/VirtualDiskOption/DiskMode.rst#independent_nonpersistent>`_
        * 
        * See
        * `VirtualDiskMode <vim/vm/device/VirtualDiskOption/DiskMode.rst>`_
        * 
    uuid (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Flag to indicate whether this backing supports disk UUID property.
