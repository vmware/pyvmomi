.. _str: https://docs.python.org/2/library/stdtypes.html

.. _append: ../../../../vim/vm/device/VirtualDiskOption/DiskMode.rst#append

.. _creation: ../../../../vim/Folder.rst#createVm

.. _fileName: ../../../../vim/vm/device/VirtualDevice/FileBackingInfo.rst#fileName

.. _undoable: ../../../../vim/vm/device/VirtualDiskOption/DiskMode.rst#undoable

.. _persistent: ../../../../vim/vm/device/VirtualDiskOption/DiskMode.rst#persistent

.. _add operation: ../../../../vim/vm/device/VirtualDeviceSpec/Operation.rst#add

.. _nonpersistent: ../../../../vim/vm/device/VirtualDiskOption/DiskMode.rst#nonpersistent

.. _reconfiguration: ../../../../vim/VirtualMachine.rst#reconfigure

.. _VirtualDiskMode: ../../../../vim/vm/device/VirtualDiskOption/DiskMode.rst

.. _create file operation: ../../../../vim/vm/device/VirtualDeviceSpec/FileOperation.rst#create

.. _QueryChangedDiskAreas: ../../../../vim/VirtualMachine.rst#queryChangedDiskAreas

.. _independent_persistent: ../../../../vim/vm/device/VirtualDiskOption/DiskMode.rst#independent_persistent

.. _VirtualDeviceConfigSpec: ../../../../vim/vm/device/VirtualDeviceSpec.rst

.. _independent_nonpersistent: ../../../../vim/vm/device/VirtualDiskOption/DiskMode.rst#independent_nonpersistent

.. _deltaDiskBackingsSupported: ../../../../vim/host/Capability.rst#deltaDiskBackingsSupported

.. _virtual compatibility mode: ../../../../vim/vm/device/VirtualDiskOption/CompatibilityMode.rst#virtualMode

.. _VirtualDiskCompatibilityMode: ../../../../vim/vm/device/VirtualDiskOption/CompatibilityMode.rst

.. _vim.vm.device.VirtualDevice.FileBackingInfo: ../../../../vim/vm/device/VirtualDevice/FileBackingInfo.rst

.. _vim.vm.device.VirtualDisk.RawDiskMappingVer1BackingInfo: ../../../../vim/vm/device/VirtualDisk/RawDiskMappingVer1BackingInfo.rst


vim.vm.device.VirtualDisk.RawDiskMappingVer1BackingInfo
=======================================================
  This data object type contains information about backing a virtual disk using a raw device mapping. Supported for ESX Server 2.5 and 3.x.
:extends: vim.vm.device.VirtualDevice.FileBackingInfo_

Attributes:
    lunUuid (`str`_, optional):

       Unique identifier of the LUN accessed by the raw disk mapping.
    deviceName (`str`_, optional):

       The host-specific device the LUN is being accessed through. If the target LUN is not available on the host then it is empty. For example, this could happen if it has accidentally been masked out.
    compatibilityMode (`str`_, optional):

       The compatibility mode of the raw disk mapping (RDM). This must be specified when a new virtual disk with an RDM backing is created. On subsequent virtual machine reconfigurations, this property should be handled as follows, depending on the version of the host:On ESX Server 2.5, the compatibility mode of an RDM backing is a characteristic of the virtual machine's configuration. When reconfiguring a virtual machine that currently uses a virtual disk backed by an RDM, the compatibility mode of that backing may be modified. When reconfiguring a virtual machine to add an existing virtual disk backed by an RDM, the compatibility mode of that backing may be specified. If left unspecified it defaults to "physicalMode".On ESX Server 3.x, the compatibility mode of an RDM backing is a characteristic of the RDM itself. Once the RDM is created, its compatibility mode cannot be changed by reconfiguring the virtual machine. When reconfiguring a virtual machine to add an existing virtual disk backed by an RDM, the compatibility mode of that backing must be left unspecified.See `VirtualDiskCompatibilityMode`_ 
    diskMode (`str`_, optional):

       The disk mode. Valid values are:
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
        * 
        * Disk modes are only supported when the raw disk mapping is using virtual compatibility mode.
        * See
        * `VirtualDiskMode`_
        * 
    uuid (`str`_, optional):

       Disk UUID for the virtual disk, if available. Disk UUID is not available if the raw disk mapping is in physical compatibility mode.
    contentId (`str`_, optional):

       Content ID of the virtual disk file, if available.A content ID indicates the logical contents of the disk backing and its parents.This property is only guaranteed to be up to date if this disk backing is not currently being written to by any virtual machine.The only supported operation is comparing if two content IDs are equal or not. The guarantee provided by the content ID is that if two disk backings have the same content ID and are not currently being written to, then reads issued from the guest operating system to those disk backings will return the same data.
    changeId (`str`_, optional):

       The change ID of the virtual disk for the corresponding snapshot or virtual machine. This can be used to track incremental changes to a virtual disk. See `QueryChangedDiskAreas`_ .
    parent (`vim.vm.device.VirtualDisk.RawDiskMappingVer1BackingInfo`_, optional):

       The parent of this virtual disk file, if this is a delta disk backing. This will be unset if this is not a delta disk backing.A delta disk backing is a way to preserve a virtual disk backing at some point in time. A delta disk backing is a file backing which in turn points to the original virtual disk backing (the parent). After a delta disk backing is added, all writes go to the delta disk backing. All reads first try the delta disk backing and then try the parent backing if needed.A delta disk backing can be added to a disk either implicitly during snapshot operations, or explicitly during create or reconfigure of the virtual machine.Note that the type of the backing is consistent throughout the chain; any new delta disk backing which is added is of the same type as the original disk . Also note that since the parent backing is not being written to, it is possible that the parent backing may be shared among multiple disks belonging to multiple virtual machines.During virtual machine `creation`_ and `reconfiguration`_ this property is only checked if the `VirtualDeviceConfigSpec`_ specifies an `add operation`_ with a `create file operation`_ . In this case, a new delta disk backing is created which points to the parent disk backing. Only the `fileName`_ property is important; all other properties will be ignored. The parent backing is assumed to exist and will not be recursively created.Only raw disk mappings in `virtual compatibility mode`_ can have parents.This property may only be set if `deltaDiskBackingsSupported`_ is true.
