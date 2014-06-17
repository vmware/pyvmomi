.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _persistent: ../../../../vim/vm/device/VirtualDiskOption/DiskMode.rst#persistent

.. _VirtualDiskMode: ../../../../vim/vm/device/VirtualDiskOption/DiskMode.rst

.. _independent_persistent: ../../../../vim/vm/device/VirtualDiskOption/DiskMode.rst#independent_persistent

.. _vim.option.ChoiceOption: ../../../../vim/option/ChoiceOption.rst

.. _independent_nonpersistent: ../../../../vim/vm/device/VirtualDiskOption/DiskMode.rst#independent_nonpersistent

.. _VirtualDiskCompatibilityMode: ../../../../vim/vm/device/VirtualDiskOption/CompatibilityMode.rst

.. _vim.vm.device.VirtualDeviceOption.DeviceBackingOption: ../../../../vim/vm/device/VirtualDeviceOption/DeviceBackingOption.rst


vim.vm.device.VirtualDiskOption.RawDiskMappingVer1BackingOption
===============================================================
  The VirtualDiskOption.RawDiskMappingVer1BackingOption object type contains the available options when backing a virtual disk using a raw device mapping on ESX Server 2.5 or 3.x.
:extends: vim.vm.device.VirtualDeviceOption.DeviceBackingOption_

Attributes:
    descriptorFileNameExtensions (`vim.option.ChoiceOption`_, optional):

       Valid extensions for the filename of the optional raw disk mapping descriptor file. This is present only for ESX Server 3.x and greater hosts.
    compatibilityMode (`vim.option.ChoiceOption`_):

       The supported raw disk mapping compatibility modes.See `VirtualDiskCompatibilityMode`_ 
    diskMode (`vim.option.ChoiceOption`_):

       The disk mode. Valid values are:
        * `persistent`_
        * 
        * `independent_persistent`_
        * 
        * `independent_nonpersistent`_
        * 
        * See
        * `VirtualDiskMode`_
        * 
    uuid (`bool`_):

       Flag to indicate whether this backing supports disk UUID property.
