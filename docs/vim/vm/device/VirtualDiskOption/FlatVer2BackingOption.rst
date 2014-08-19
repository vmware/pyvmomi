
vim.vm.device.VirtualDiskOption.FlatVer2BackingOption
=====================================================
  This data object type contains the available options when backing a virtual disk using a host file with the flat file format used in VMware Server and in ESX Server 2.x and greater. Flat disks are pre-allocated, whereas sparse disks are grown as needed.
:extends: vim.vm.device.VirtualDeviceOption.FileBackingOption_

Attributes:
    diskMode (`vim.option.ChoiceOption <vim/option/ChoiceOption.rst>`_):

       The disk mode. Valid disk modes are:
        * `persistent <vim/vm/device/VirtualDiskOption/DiskMode.rst#persistent>`_
        * 
        * `independent_persistent <vim/vm/device/VirtualDiskOption/DiskMode.rst#independent_persistent>`_
        * 
        * `independent_nonpersistent <vim/vm/device/VirtualDiskOption/DiskMode.rst#independent_nonpersistent>`_
        * 
        * See
        * `VirtualDiskMode <vim/vm/device/VirtualDiskOption/DiskMode.rst>`_
        * 
    split (`vim.option.BoolOption <vim/option/BoolOption.rst>`_):

       Flag to indicate whether or not the host supports allowing the client to select whether or not a disk should be split.
    writeThrough (`vim.option.BoolOption <vim/option/BoolOption.rst>`_):

       Flag to indicate whether or not the host supports allowing the client to select "writethrough" as a mode for virtual disks. Typically, this is available only for VMware Server Linux hosts.
    growable (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether or not this disk backing can be extended to larger sizes through a reconfigure operation.If set to true, reconfiguring this virtual disk with a `capacityInKB <vim/vm/device/VirtualDisk.rst#capacityInKB>`_ value greater than its current value will grow the disk to the newly specified size.
    hotGrowable (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether or not this disk backing can be extended to larger sizes through a reconfigure operation while the virtual machine is powered on.If set to true, reconfiguring this virtual disk with a `capacityInKB <vim/vm/device/VirtualDisk.rst#capacityInKB>`_ value greater than its current value will grow the disk to the newly specified size while the virtual machine is powered on.
    uuid (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Flag to indicate whether this backing supports disk UUID property.
    thinProvisioned (`vim.option.BoolOption <vim/option/BoolOption.rst>`_):

       Flag to indicate if this backing supports thin-provisioned disks.When creating a thin-provisioned disk (or converting an existing disk to to a thin-provisioned one), both the target datastore and the host accessing it must support thin-provisioning. This flag indicates only the host capability. See `perFileThinProvisioningSupported <vim/Datastore/Capability.rst#perFileThinProvisioningSupported>`_ for datastore capability.
    eagerlyScrub (`vim.option.BoolOption <vim/option/BoolOption.rst>`_):

       Flag to indicate if this backing supports eager scrubbing.
    deltaDiskFormat (`vim.option.ChoiceOption <vim/option/ChoiceOption.rst>`_):

       Delta disk formats supported. Valid values are:
        * `redoLogFormat <vim/vm/device/VirtualDisk/DeltaDiskFormat.rst#redoLogFormat>`_
        * 
        * `nativeFormat <vim/vm/device/VirtualDisk/DeltaDiskFormat.rst#nativeFormat>`_
        * 
        * 
        * 
    deltaDiskFormatsSupported ([`vim.vm.device.VirtualDiskOption.DeltaDiskFormatsSupported <vim/vm/device/VirtualDiskOption/DeltaDiskFormatsSupported.rst>`_]):

       Delta disk formats supported for each datastore type.
