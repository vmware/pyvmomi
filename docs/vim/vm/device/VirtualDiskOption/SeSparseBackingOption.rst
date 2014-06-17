.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _persistent: ../../../../vim/vm/device/VirtualDiskOption/DiskMode.rst#persistent

.. _capacityInKB: ../../../../vim/vm/device/VirtualDisk.rst#capacityInKB

.. _vSphere API 5.1: ../../../../vim/version.rst#vimversionversion8

.. _VirtualDiskMode: ../../../../vim/vm/device/VirtualDiskOption/DiskMode.rst

.. _vim.option.BoolOption: ../../../../vim/option/BoolOption.rst

.. _independent_persistent: ../../../../vim/vm/device/VirtualDiskOption/DiskMode.rst#independent_persistent

.. _vim.option.ChoiceOption: ../../../../vim/option/ChoiceOption.rst

.. _independent_nonpersistent: ../../../../vim/vm/device/VirtualDiskOption/DiskMode.rst#independent_nonpersistent

.. _vim.vm.device.VirtualDeviceOption.FileBackingOption: ../../../../vim/vm/device/VirtualDeviceOption/FileBackingOption.rst

.. _vim.vm.device.VirtualDiskOption.DeltaDiskFormatsSupported: ../../../../vim/vm/device/VirtualDiskOption/DeltaDiskFormatsSupported.rst


vim.vm.device.VirtualDiskOption.SeSparseBackingOption
=====================================================
  Backing options for virtual disks that use the space efficient sparse format.Space for Flex-SE disks is allocated on demand and optimizations are applied to achieve additional space savings.
:extends: vim.vm.device.VirtualDeviceOption.FileBackingOption_
:since: `vSphere API 5.1`_

Attributes:
    diskMode (`vim.option.ChoiceOption`_):

       The disk mode. Valid disk modes are:
        * `persistent`_
        * 
        * `independent_persistent`_
        * 
        * `independent_nonpersistent`_
        * 
        * See
        * `VirtualDiskMode`_
        * 
    writeThrough (`vim.option.BoolOption`_):

       Flag to indicate whether or not the host supports allowing the client to select "writethrough" as a mode for virtual disks. Typically, this is available only for VMware Server Linux hosts.
    growable (`bool`_):

       Indicates whether or not this disk backing can be extended to larger sizes through a reconfigure operation.If set to true, reconfiguring this virtual disk with a `capacityInKB`_ value greater than its current value will grow the disk to the newly specified size.
    hotGrowable (`bool`_):

       Indicates whether or not this disk backing can be extended to larger sizes through a reconfigure operation while the virtual machine is powered on.If set to true, reconfiguring this virtual disk with a `capacityInKB`_ value greater than its current value will grow the disk to the newly specified size while the virtual machine is powered on.
    uuid (`bool`_):

       Flag to indicate whether this backing supports disk UUID property.
    deltaDiskFormatsSupported (`vim.vm.device.VirtualDiskOption.DeltaDiskFormatsSupported`_):

       Delta disk formats supported for each datastore type.
