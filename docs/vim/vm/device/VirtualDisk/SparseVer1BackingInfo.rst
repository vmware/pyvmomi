
vim.vm.device.VirtualDisk.SparseVer1BackingInfo
===============================================
  This data object type contains information about backing a virtual disk by using a virtual disk file on the host, in the sparse disk format used by GSX Server 2.x.
:extends: vim.vm.device.VirtualDevice.FileBackingInfo_

Attributes:
    diskMode (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The disk persistence mode. Valid values are:
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
    split (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Flag to indicate the type of virtual disk file: split or monolithic. If true, the virtual disk is stored in multiple files, each 2GB.
    writeThrough (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Flag to indicate whether writes should go directly to the file system or should be buffered.
    spaceUsedInKB (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The space in use for this sparse disk. This information is provided when retrieving configuration information for an existing virtual machine. The client cannot modify this information using reconfigure on a virtual machine.
    contentId (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Content ID of the virtual disk file, if available.A content ID indicates the logical contents of the disk backing and its parents.This property is only guaranteed to be up to date if this disk backing is not currently being written to by any virtual machine.The only supported operation is comparing if two content IDs are equal or not. The guarantee provided by the content ID is that if two disk backings have the same content ID and are not currently being written to, then reads issued from the guest operating system to those disk backings will return the same data.
    parent (`vim.vm.device.VirtualDisk.SparseVer1BackingInfo <vim/vm/device/VirtualDisk/SparseVer1BackingInfo.rst>`_, optional):

       The parent of this virtual disk file, if this is a delta disk backing. This will be unset if this is not a delta disk backing.A delta disk backing is a way to preserve a virtual disk backing at some point in time. A delta disk backing is a file backing which in turn points to the original virtual disk backing (the parent). After a delta disk backing is added, all writes go to the delta disk backing. All reads first try the delta disk backing and then try the parent backing if needed.A delta disk backing can be added to a disk either implicitly during snapshot operations, or explicitly during create or reconfigure of the virtual machine.Note that the type of the backing is consistent throughout the chain; any new delta disk backing which is added is of the same type as the original disk . Also note that since the parent backing is not being written to, it is possible that the parent backing may be shared among multiple disks belonging to multiple virtual machines.During virtual machine `creation <vim/Folder.rst#createVm>`_ and `reconfiguration <vim/VirtualMachine.rst#reconfigure>`_ this property is only checked if the `VirtualDeviceConfigSpec <vim/vm/device/VirtualDeviceSpec.rst>`_ specifies an `add operation <vim/vm/device/VirtualDeviceSpec/Operation.rst#add>`_ with a `create file operation <vim/vm/device/VirtualDeviceSpec/FileOperation.rst#create>`_ . In this case, a new delta disk backing is created which points to the parent disk backing. Only the `fileName <vim/vm/device/VirtualDevice/FileBackingInfo.rst#fileName>`_ property is important; all other properties will be ignored. The parent backing is assumed to exist and will not be recursively created.This property may only be set if `deltaDiskBackingsSupported <vim/host/Capability.rst#deltaDiskBackingsSupported>`_ is true.
