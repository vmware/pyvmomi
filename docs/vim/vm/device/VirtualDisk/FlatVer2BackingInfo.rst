
vim.vm.device.VirtualDisk.FlatVer2BackingInfo
=============================================
  This data object type contains information about backing a virtual disk using a virtual disk file on the host, in the flat file format used by VMware Server, ESX Server 2.x, and ESX Server 3.x. Flat disks are allocated when created, unlike sparse disks, which grow as needed.
:extends: vim.vm.device.VirtualDevice.FileBackingInfo_

Attributes:
    diskMode (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The disk persistence mode. Valid modes are:
        * `persistent <vim/vm/device/VirtualDiskOption/DiskMode.rst#persistent>`_
        * 
        * `independent_persistent <vim/vm/device/VirtualDiskOption/DiskMode.rst#independent_persistent>`_
        * 
        * `independent_nonpersistent <vim/vm/device/VirtualDiskOption/DiskMode.rst#independent_nonpersistent>`_
        * 
        * `nonpersistent <vim/vm/device/VirtualDiskOption/DiskMode.rst#nonpersistent>`_
        * 
        * `undoable <vim/vm/device/VirtualDiskOption/DiskMode.rst#undoable>`_
        * 
        * `append <vim/vm/device/VirtualDiskOption/DiskMode.rst#append>`_
        * 
        * See
        * `VirtualDiskMode <vim/vm/device/VirtualDiskOption/DiskMode.rst>`_
        * 
    split (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Flag to indicate the type of virtual disk file: split or monolithic. If true, the virtual disk is stored in multiple files, each 2GB. On ESX this property is ignored when creating new disks or editing existing disks. This property is always false for disks created on ESX. When an existing split disk such as those created by VMware Server is added to a virtual machine on ESX, the property will be set to true when retrieved from `VirtualMachineConfigInfo <vim/vm/ConfigInfo.rst>`_ .
    writeThrough (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Flag to indicate whether writes should go directly to the file system or should be buffered.
    thinProvisioned (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Flag to indicate to the underlying filesystem, whether the virtual disk backing file should be allocated lazily (using thin provisioning). This flag is only used for file systems that support configuring the provisioning policy on a per file basis, such as VMFS3.See `perFileThinProvisioningSupported <vim/Datastore/Capability.rst#perFileThinProvisioningSupported>`_ 
    eagerlyScrub (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Flag to indicate to the underlying filesystem whether the virtual disk backing file should be scrubbed completely at this time.Virtual disks on some filesystems like VMFS3 are zeroed-out lazily so that disk creation time doesn't take too long. However, clustering applications and features like Fault Tolerance require that the virtual disk be completely scrubbed. This setting allows controlling the scrubbing policy on a per-disk basis.If this flag is unset or set to false when creating a new disk, the disk scrubbing policy will be decided by the filesystem. If this flag is unset or set to false when editing an existing disk, it is ignored. When returned as part of a `VirtualMachineConfigInfo <vim/vm/ConfigInfo.rst>`_ , this property may be unset if its value is unknown.
    uuid (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Disk UUID for the virtual disk, if available.
    contentId (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Content ID of the virtual disk file, if available.A content ID indicates the logical contents of the disk backing and its parents.This property is only guaranteed to be up to date if this disk backing is not currently being written to by any virtual machine.The only supported operation is comparing if two content IDs are equal or not. The guarantee provided by the content ID is that if two disk backings have the same content ID and are not currently being written to, then reads issued from the guest operating system to those disk backings will return the same data.
    changeId (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The change ID of the virtual disk for the corresponding snapshot or virtual machine. This can be used to track incremental changes to a virtual disk. See `QueryChangedDiskAreas <vim/VirtualMachine.rst#queryChangedDiskAreas>`_ .
    parent (`vim.vm.device.VirtualDisk.FlatVer2BackingInfo <vim/vm/device/VirtualDisk/FlatVer2BackingInfo.rst>`_, optional):

       The parent of this virtual disk file, if this is a delta disk backing. This will be unset if this is not a delta disk backing.A delta disk backing is a way to preserve a virtual disk backing at some point in time. A delta disk backing is a file backing which in turn points to the original virtual disk backing (the parent). After a delta disk backing is added, all writes go to the delta disk backing. All reads first try the delta disk backing and then try the parent backing if needed.A delta disk backing can be added to a disk either implicitly during snapshot operations, or explicitly during create or reconfigure of the virtual machine.Note that the type of the backing is consistent throughout the chain; any new delta disk backing which is added is of the same type as the original disk . Also note that since the parent backing is not being written to, it is possible that the parent backing may be shared among multiple disks belonging to multiple virtual machines.During virtual machine `creation <vim/Folder.rst#createVm>`_ and `reconfiguration <vim/VirtualMachine.rst#reconfigure>`_ this property is only checked if the `VirtualDeviceConfigSpec <vim/vm/device/VirtualDeviceSpec.rst>`_ specifies an `add operation <vim/vm/device/VirtualDeviceSpec/Operation.rst#add>`_ with a `create file operation <vim/vm/device/VirtualDeviceSpec/FileOperation.rst#create>`_ . In this case, a new delta disk backing is created which points to the parent disk backing. Only the `fileName <vim/vm/device/VirtualDevice/FileBackingInfo.rst#fileName>`_ property is important; all other properties will be ignored. The parent backing is assumed to exist and will not be recursively created.This property may only be set if `deltaDiskBackingsSupported <vim/host/Capability.rst#deltaDiskBackingsSupported>`_ is true.
    deltaDiskFormat (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The format of the delta disk.This field is valid only for a delta disk.See `DeltaDiskFormat <vim/vm/device/VirtualDisk/DeltaDiskFormat.rst>`_ for the supported formats. If not specified, the default value used is `redoLogFormat <vim/vm/device/VirtualDisk/DeltaDiskFormat.rst#redoLogFormat>`_ .If `nativeFormat <vim/vm/device/VirtualDisk/DeltaDiskFormat.rst#nativeFormat>`_ is specified and the datastore does not support this format or the parent is on a different datastore, `DeltaDiskFormatNotSupported <vim/fault/DeltaDiskFormatNotSupported.rst>`_ is thrown.vSphere server does not support relocation of virtual machines with `nativeFormat <vim/vm/device/VirtualDisk/DeltaDiskFormat.rst#nativeFormat>`_ . An exception is thrown for such requests.
    digestEnabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Indicates whether the disk backing has digest file enabled.
    deltaGrainSize (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Grain size in kB for a delta disk of format type seSparseFormat. The default size is 1024 kB. This setting is used to specify the grain size of `Flex-SE <vim/vm/device/VirtualDisk/SeSparseBackingInfo.rst>`_ delta disks when the base disk is of type FlatVer2BackingInfo. The `DeltaDiskFormat <vim/vm/device/VirtualDisk/DeltaDiskFormat.rst>`_ must also be set to seSparseFormat.
