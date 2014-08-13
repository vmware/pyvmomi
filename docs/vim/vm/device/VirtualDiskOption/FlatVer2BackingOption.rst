.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _persistent: ../../../../vim/vm/device/VirtualDiskOption/DiskMode.rst#persistent

.. _nativeFormat: ../../../../vim/vm/device/VirtualDisk/DeltaDiskFormat.rst#nativeFormat

.. _capacityInKB: ../../../../vim/vm/device/VirtualDisk.rst#capacityInKB

.. _redoLogFormat: ../../../../vim/vm/device/VirtualDisk/DeltaDiskFormat.rst#redoLogFormat

.. _VirtualDiskMode: ../../../../vim/vm/device/VirtualDiskOption/DiskMode.rst

.. _vim.option.BoolOption: ../../../../vim/option/BoolOption.rst

.. _independent_persistent: ../../../../vim/vm/device/VirtualDiskOption/DiskMode.rst#independent_persistent

.. _vim.option.ChoiceOption: ../../../../vim/option/ChoiceOption.rst

.. _independent_nonpersistent: ../../../../vim/vm/device/VirtualDiskOption/DiskMode.rst#independent_nonpersistent

.. _perFileThinProvisioningSupported: ../../../../vim/Datastore/Capability.rst#perFileThinProvisioningSupported

.. _vim.vm.device.VirtualDeviceOption.FileBackingOption: ../../../../vim/vm/device/VirtualDeviceOption/FileBackingOption.rst

.. _vim.vm.device.VirtualDiskOption.DeltaDiskFormatsSupported: ../../../../vim/vm/device/VirtualDiskOption/DeltaDiskFormatsSupported.rst


vim.vm.device.VirtualDiskOption.FlatVer2BackingOption
=====================================================
  This data object type contains the available options when backing a virtual disk using a host file with the flat file format used in VMware Server and in ESX Server 2.x and greater. Flat disks are pre-allocated, whereas sparse disks are grown as needed.
:extends: vim.vm.device.VirtualDeviceOption.FileBackingOption_

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
    split (`vim.option.BoolOption`_):

       Flag to indicate whether or not the host supports allowing the client to select whether or not a disk should be split.
    writeThrough (`vim.option.BoolOption`_):

       Flag to indicate whether or not the host supports allowing the client to select "writethrough" as a mode for virtual disks. Typically, this is available only for VMware Server Linux hosts.
    growable (`bool`_):

       Indicates whether or not this disk backing can be extended to larger sizes through a reconfigure operation.If set to true, reconfiguring this virtual disk with a `capacityInKB`_ value greater than its current value will grow the disk to the newly specified size.
    hotGrowable (`bool`_):

       Indicates whether or not this disk backing can be extended to larger sizes through a reconfigure operation while the virtual machine is powered on.If set to true, reconfiguring this virtual disk with a `capacityInKB`_ value greater than its current value will grow the disk to the newly specified size while the virtual machine is powered on.
    uuid (`bool`_):

       Flag to indicate whether this backing supports disk UUID property.
    thinProvisioned (`vim.option.BoolOption`_):

       Flag to indicate if this backing supports thin-provisioned disks.When creating a thin-provisioned disk (or converting an existing disk to to a thin-provisioned one), both the target datastore and the host accessing it must support thin-provisioning. This flag indicates only the host capability. See `perFileThinProvisioningSupported`_ for datastore capability.
    eagerlyScrub (`vim.option.BoolOption`_):

       Flag to indicate if this backing supports eager scrubbing.
    deltaDiskFormat (`vim.option.ChoiceOption`_):

       Delta disk formats supported. Valid values are:
        * `redoLogFormat`_
        * 
        * `nativeFormat`_
        * 
        * 
        * 
    deltaDiskFormatsSupported ([`vim.vm.device.VirtualDiskOption.DeltaDiskFormatsSupported`_]):

       Delta disk formats supported for each datastore type.
