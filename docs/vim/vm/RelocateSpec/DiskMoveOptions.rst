vim.vm.RelocateSpec.DiskMoveOptions
===================================
  Specifies how a virtual disk is moved or copied to a datastore.In all cases after the move or copy the virtual machine's current running point will be placed on the target datastore. The current running point is defined as the disk backing which the virtual machine is currently writing to. This end state can be achieved in multiple ways, and the supported options are described in this enumeration.These options are only relevant when the backing of the specified disk is a `file backing <vim/vm/device/VirtualDevice/FileBackingInfo.rst>`_ .Since disk backings may become shared as the result of either a `clone operation <vim/VirtualMachine.rst#clone>`_ or a `relocate operation <vim/VirtualMachine.rst#relocate>`_ , `PromoteDisks_Task <vim/VirtualMachine.rst#promoteDisks>`_ has been provided as a way to unshare such disk backings.See `parent <vim/vm/device/VirtualDisk/SparseVer1BackingInfo.rst#parent>`_ See `parent <vim/vm/device/VirtualDisk/SparseVer2BackingInfo.rst#parent>`_ See `parent <vim/vm/device/VirtualDisk/FlatVer1BackingInfo.rst#parent>`_ See `parent <vim/vm/device/VirtualDisk/FlatVer2BackingInfo.rst#parent>`_ See `parent <vim/vm/device/VirtualDisk/RawDiskMappingVer1BackingInfo.rst#parent>`_ See `diskMoveType <vim/vm/RelocateSpec.rst#diskMoveType>`_ See `diskMoveType <vim/vm/RelocateSpec/DiskLocator.rst#diskMoveType>`_ 
  :contained by: `vim.vm.RelocateSpec <vim/vm/RelocateSpec.rst>`_

  :type: `vim.vm.RelocateSpec.DiskMoveOptions <vim/vm/RelocateSpec/DiskMoveOptions.rst>`_

  :name: moveAllDiskBackingsAndConsolidate

values:
--------

moveAllDiskBackingsAndDisallowSharing
   All of the virtual disk's backings should be moved to the new datastore. It is not acceptable to attach to a disk backing with the same content ID on the destination datastore. During a `clone operation <vim/VirtualMachine.rst#clone>`_ any delta disk backings will be consolidated.

moveChildMostDiskBacking
   Move only the child-most disk backing. Any parent disk backings should be left in their current locations.This option only differs from `moveAllDiskBackingsAndAllowSharing <vim/vm/RelocateSpec/DiskMoveOptions.rst#moveAllDiskBackingsAndAllowSharing>`_ and `moveAllDiskBackingsAndDisallowSharing <vim/vm/RelocateSpec/DiskMoveOptions.rst#moveAllDiskBackingsAndDisallowSharing>`_ when the virtual disk has a parent backing.Note that in the case of a `clone operation <vim/VirtualMachine.rst#clone>`_ , this means that the parent disks will now be shared. This is safe as any parent disks are always read-only. Note that in the case of a `RelocateVM_Task <vim/VirtualMachine.rst#relocate>`_ operation, only the virtual disks in the current virtual machine configuration are moved.

createNewChildDiskBacking
   Create a new child disk backing on the destination datastore. None of the virtual disk's existing files should be moved from their current locations.Note that in the case of a `clone operation <vim/VirtualMachine.rst#clone>`_ , this means that the original virtual machine's disks are now all being shared. This is only safe if the clone was taken from a snapshot point, because snapshot points are always read-only. Thus for a clone this option is only valid `when cloning from a snapshot <vim/vm/CloneSpec.rst#snapshot>`_ . Note that in the case of a `RelocateVM_Task <vim/VirtualMachine.rst#relocate>`_ operation, child disks are created for the virtual disks in the current virtual machine configuration only.

moveAllDiskBackingsAndAllowSharing
   All of the virtual disk's backings should be moved to the new datastore.If a disk backing is not the child-most backing of this virtual machine, and there exists a read-only disk backing with the same content ID on the target datastore, then this disk backing may not be copied. Instead it is acceptable to attach to the read-only disk backing at the target datastore. A read-only disk backing is defined as a virtual disk backing which no virtual machine is currently writing to.See `contentId <vim/vm/device/VirtualDisk/SparseVer1BackingInfo.rst#contentId>`_ See `contentId <vim/vm/device/VirtualDisk/SparseVer2BackingInfo.rst#contentId>`_ See `contentId <vim/vm/device/VirtualDisk/FlatVer1BackingInfo.rst#contentId>`_ See `contentId <vim/vm/device/VirtualDisk/FlatVer2BackingInfo.rst#contentId>`_ See `contentId <vim/vm/device/VirtualDisk/RawDiskMappingVer1BackingInfo.rst#contentId>`_ 

moveAllDiskBackingsAndConsolidate
   All of the virtual disk's backings should be moved to the new datastore. During a `clone operation <vim/VirtualMachine.rst#clone>`_ or a `MigrateVM_Task <vim/VirtualMachine.rst#migrate>`_ , any delta disk backings will be consolidated.
