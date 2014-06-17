.. _vim.VirtualDiskManager: ../../vim/VirtualDiskManager.rst

.. _vim.VirtualDiskManager.VirtualDiskType: ../../vim/VirtualDiskManager/VirtualDiskType.rst

vim.VirtualDiskManager.VirtualDiskType
======================================
  The types of virtual disks that can be created or cloned.
  :contained by: `vim.VirtualDiskManager`_

  :type: `vim.VirtualDiskManager.VirtualDiskType`_

  :name: thick

values:
--------

eagerZeroedThick
   An eager zeroed thick disk has all space allocated and wiped clean of any previous contents on the physical media at creation time. Such disks may take longer time during creation compared to other disk formats.

rdmp
   Physical compatibility mode (pass-through) raw disk mapping. An rdmp virtual disk passes SCSI commands directly to the hardware, but the virtual disk cannot participate in snapshots.

sparse2Gb
   A sparse disk with 2GB maximum extent size. Disks in this format can be used with other VMware products. The 2GB extent size makes these disks easier to burn to dvd or use on filesystems that don't support large files. This format is only applicable as a destination format in a clone operation, and not usable for disk creation.

raw
   Raw device.

flatMonolithic
   A preallocated monolithic disk. Disks in this format can be used with other VMware products. This format is only applicable as a destination format in a clone operation, and not usable for disk creation.

thick2Gb
   A thick disk with 2GB maximum extent size. Disks in this format can be used with other VMware products. The 2GB extent size makes these disks easier to burn to dvd or use on filesystems that don't support large files. This format is only applicable as a destination format in a clone operation, and not usable for disk creation.

thin
   Space required for thin-provisioned virtual disk is allocated and zeroed on demand as the space is used.

preallocated
   A preallocated disk has all space allocated at creation time and the space is zeroed on demand as the space is used.

delta
   A redo log disk. This format is only applicable as a destination format in a clone operation, and not usable for disk creation.

rdm
   Virtual compatibility mode raw disk mapping. An rdm virtual disk grants access to the entire raw disk and the virtual disk can participate in snapshots.

sparseMonolithic
   A sparse monolithic disk. Disks in this format can be used with other VMware products. This format is only applicable as a destination format in a clone operation, and not usable for disk creation.

thick
   A thick disk has all space allocated at creation time. This space may contain stale data on the physical media. Thick disks are primarily used for virtual machine clustering, but they are generally insecure and should not be used. Due to better performance and security properties, the use of the 'preallocated' format is preferred over this format.

seSparse
   A sparse (allocate on demand) format with additional space optimizations.
