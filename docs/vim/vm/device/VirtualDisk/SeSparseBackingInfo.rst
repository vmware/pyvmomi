.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _append: ../../../../vim/vm/device/VirtualDiskOption/DiskMode.rst#append

.. _creation: ../../../../vim/Folder.rst#createVm

.. _fileName: ../../../../vim/vm/device/VirtualDevice/FileBackingInfo.rst#fileName

.. _undoable: ../../../../vim/vm/device/VirtualDiskOption/DiskMode.rst#undoable

.. _persistent: ../../../../vim/vm/device/VirtualDiskOption/DiskMode.rst#persistent

.. _add operation: ../../../../vim/vm/device/VirtualDeviceSpec/Operation.rst#add

.. _nonpersistent: ../../../../vim/vm/device/VirtualDiskOption/DiskMode.rst#nonpersistent

.. _redoLogFormat: ../../../../vim/vm/device/VirtualDisk/DeltaDiskFormat.rst#redoLogFormat

.. _VirtualDiskMode: ../../../../vim/vm/device/VirtualDiskOption/DiskMode.rst

.. _vSphere API 5.1: ../../../../vim/version.rst#vimversionversion8

.. _DeltaDiskFormat: ../../../../vim/vm/device/VirtualDisk/DeltaDiskFormat.rst

.. _reconfiguration: ../../../../vim/VirtualMachine.rst#reconfigure

.. _QueryChangedDiskAreas: ../../../../vim/VirtualMachine.rst#queryChangedDiskAreas

.. _create file operation: ../../../../vim/vm/device/VirtualDeviceSpec/FileOperation.rst#create

.. _independent_persistent: ../../../../vim/vm/device/VirtualDiskOption/DiskMode.rst#independent_persistent

.. _VirtualDeviceConfigSpec: ../../../../vim/vm/device/VirtualDeviceSpec.rst

.. _independent_nonpersistent: ../../../../vim/vm/device/VirtualDiskOption/DiskMode.rst#independent_nonpersistent

.. _deltaDiskBackingsSupported: ../../../../vim/host/Capability.rst#deltaDiskBackingsSupported

.. _VirtualMachineFileLayoutEx: ../../../../vim/vm/FileLayoutEx.rst

.. _vim.vm.device.VirtualDevice.FileBackingInfo: ../../../../vim/vm/device/VirtualDevice/FileBackingInfo.rst

.. _vim.vm.device.VirtualDisk.SeSparseBackingInfo: ../../../../vim/vm/device/VirtualDisk/SeSparseBackingInfo.rst


vim.vm.device.VirtualDisk.SeSparseBackingInfo
=============================================
  Backing type for virtual disks that use the space efficient sparse format.Space for space efficient sparse disks is allocated on demand and optimizations are applied to achieve additional space savings. The effective space usage of such a disk can be obtained from `VirtualMachineFileLayoutEx`_ .
:extends: vim.vm.device.VirtualDevice.FileBackingInfo_
:since: `vSphere API 5.1`_

Attributes:
    diskMode (`str`_):

       The disk persistence mode. Valid modes are:
        * `persistent`_
        * 
        * `independent_persistent`_
        * 
        * `independent_nonpersistent`_
        * 
        * `nonpersistent`_
        * 
        * `undoable`_
        * 
        * `append`_
        * 
        * See
        * `VirtualDiskMode`_
        * 
    writeThrough (`bool`_, optional):

       Flag to indicate whether writes should go directly to the file system or should be buffered.
    uuid (`str`_, optional):

       Disk UUID for the virtual disk, if available.
    contentId (`str`_, optional):

       Content ID of the virtual disk file, if available.A content ID indicates the logical contents of the disk backing and its parents.This property is only guaranteed to be up to date if this disk backing is not currently being written to by any virtual machine.The only supported operation is comparing if two content IDs are equal or not. The guarantee provided by the content ID is that if two disk backings have the same content ID and are not currently being written to, then reads issued from the guest operating system to those disk backings will return the same data.
    changeId (`str`_, optional):

       The change ID of the virtual disk for the corresponding snapshot or virtual machine. This can be used to track incremental changes to a virtual disk. See `QueryChangedDiskAreas`_ .
    parent (`vim.vm.device.VirtualDisk.SeSparseBackingInfo`_, optional):

       The parent of this virtual disk file, if this is a delta disk backing. This will be unset if this is not a delta disk backing.A delta disk backing is a way to preserve a virtual disk backing at some point in time. A delta disk backing is a file backing which in turn points to the original virtual disk backing (the parent). After a delta disk backing is added, all writes go to the delta disk backing. All reads first try the delta disk backing and then try the parent backing if needed.A delta disk backing can be added to a disk either implicitly during snapshot operations, or explicitly during create or reconfigure of the virtual machine.Note that the type of the backing is consistent throughout the chain; any new delta disk backing which is added is of the same type as the original disk . Also note that since the parent backing is not being written to, it is possible that the parent backing may be shared among multiple disks belonging to multiple virtual machines.During virtual machine `creation`_ and `reconfiguration`_ this property is only checked if the `VirtualDeviceConfigSpec`_ specifies an `add operation`_ with a `create file operation`_ . In this case, a new delta disk backing is created which points to the parent disk backing. Only the `fileName`_ property is important; all other properties will be ignored. The parent backing is assumed to exist and will not be recursively created.This property may only be set if `deltaDiskBackingsSupported`_ is true.
    deltaDiskFormat (`str`_, optional):

       The format of the delta disk.This field is valid only for a delta disk.See `DeltaDiskFormat`_ for the supported formats. If not specified, the default value used is `redoLogFormat`_ .
    digestEnabled (`bool`_, optional):

       Indicates whether the disk backing has digest file enabled.
    grainSize (`int`_, optional):

       Specify the grain size in kB. The default size is 1024 kB.
