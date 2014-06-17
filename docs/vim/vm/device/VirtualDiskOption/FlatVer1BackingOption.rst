.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _append: ../../../../vim/vm/device/VirtualDiskOption/DiskMode.rst#append

.. _undoable: ../../../../vim/vm/device/VirtualDiskOption/DiskMode.rst#undoable

.. _persistent: ../../../../vim/vm/device/VirtualDiskOption/DiskMode.rst#persistent

.. _nonpersistent: ../../../../vim/vm/device/VirtualDiskOption/DiskMode.rst#nonpersistent

.. _VirtualDiskMode: ../../../../vim/vm/device/VirtualDiskOption/DiskMode.rst

.. _vim.option.BoolOption: ../../../../vim/option/BoolOption.rst

.. _independent_persistent: ../../../../vim/vm/device/VirtualDiskOption/DiskMode.rst#independent_persistent

.. _vim.option.ChoiceOption: ../../../../vim/option/ChoiceOption.rst

.. _independent_nonpersistent: ../../../../vim/vm/device/VirtualDiskOption/DiskMode.rst#independent_nonpersistent

.. _vim.vm.device.VirtualDeviceOption.FileBackingOption: ../../../../vim/vm/device/VirtualDeviceOption/FileBackingOption.rst


vim.vm.device.VirtualDiskOption.FlatVer1BackingOption
=====================================================
  This data object type contains the available options when backing a virtual disk using a host file with the flat file format from GSX Server 2.x. Flat disks are pre-allocated, whereas sparse disks are grown as needed.
:extends: vim.vm.device.VirtualDeviceOption.FileBackingOption_

Attributes:
    diskMode (`vim.option.ChoiceOption`_):

       The disk mode. Valid disk modes are:
        * `persistent`_
        * 
        * `nonpersistent`_
        * 
        * `undoable`_
        * 
        * `independent_persistent`_
        * 
        * `independent_nonpersistent`_
        * 
        * `append`_
        * 
        * See
        * `VirtualDiskMode`_
        * 
    split (`vim.option.BoolOption`_):

       Flag to indicate whether or not the host supports allowing the client to select whether or not a disk should be split.
    writeThrough (`vim.option.BoolOption`_):

       Flag to indicate whether or not the host supports allowing the client to select "writethrough" as a mode for virtual disks. Typically, this is available only for GSX Server Linux hosts.
    growable (`bool`_):

       Flag to indicate whether this backing can have its size changed.
