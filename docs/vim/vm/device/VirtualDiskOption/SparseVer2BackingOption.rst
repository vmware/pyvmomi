
vim.vm.device.VirtualDiskOption.SparseVer2BackingOption
=======================================================
  This data object type contains the options available when backing a virtual disk using a host file with the sparse file format from VMware Server.
:extends: vim.vm.device.VirtualDeviceOption.FileBackingOption_

Attributes:
    diskMode (`vim.option.ChoiceOption <vim/option/ChoiceOption.rst>`_):

       The disk mode. Valid disk modes are:
        * `persistent <vim/vm/device/VirtualDiskOption/DiskMode.rst#persistent>`_
        * 
        * `nonpersistent <vim/vm/device/VirtualDiskOption/DiskMode.rst#nonpersistent>`_
        * 
        * `undoable <vim/vm/device/VirtualDiskOption/DiskMode.rst#undoable>`_
        * 
        * `independent_persistent <vim/vm/device/VirtualDiskOption/DiskMode.rst#independent_persistent>`_
        * 
        * `independent_nonpersistent <vim/vm/device/VirtualDiskOption/DiskMode.rst#independent_nonpersistent>`_
        * 
        * `append <vim/vm/device/VirtualDiskOption/DiskMode.rst#append>`_
        * 
        * See
        * `VirtualDiskMode <vim/vm/device/VirtualDiskOption/DiskMode.rst>`_
        * 
    split (`vim.option.BoolOption <vim/option/BoolOption.rst>`_):

       Flag to indicate whether or not the host supports allowing the client to select whether or not a sparse disk should be split.
    writeThrough (`vim.option.BoolOption <vim/option/BoolOption.rst>`_):

       Flag to indicate whether or not the host supports allowing the client to select "writethrough" as a mode for virtual disks. Typically, this is available only for VMware Server Linux hosts.
    growable (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether or not this disk backing can be extended to larger sizes through a reconfigure operation.If set to true, reconfiguring this virtual disk with a `capacityInKB <vim/vm/device/VirtualDisk.rst#capacityInKB>`_ value greater than its current value will grow the disk to the newly specified size.
    hotGrowable (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether or not this disk backing can be extended to larger sizes through a reconfigure operation while the virtual machine is powered on.If set to true, reconfiguring this virtual disk with a `capacityInKB <vim/vm/device/VirtualDisk.rst#capacityInKB>`_ value greater than its current value will grow the disk to the newly specified size while the virtual machine is powered on.
    uuid (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Flag to indicate whether this backing supports disk UUID property.
