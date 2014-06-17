.. _vim.OvfManager.CreateImportSpecParams: ../../../vim/OvfManager/CreateImportSpecParams.rst

.. _vim.OvfManager.CreateImportSpecParams.DiskProvisioningType: ../../../vim/OvfManager/CreateImportSpecParams/DiskProvisioningType.rst

vim.OvfManager.CreateImportSpecParams.DiskProvisioningType
==========================================================
  Types of disk provisioning that can be set for the disk in the deployed OVF package.
  :contained by: `vim.OvfManager.CreateImportSpecParams`_

  :type: `vim.OvfManager.CreateImportSpecParams.DiskProvisioningType`_

  :name: flat

values:
--------

flat
   Depending on the host type, Flat is mapped to either MonolithicFlat or Thick.

eagerZeroedThick
   An eager zeroed thick disk has all space allocated and wiped clean of any previous contents on the physical media at creation time. Such disks may take longer time during creation compared to other disk formats.

monolithicSparse
   A sparse (allocate on demand) monolithic disk. Disks in this format can be used with other VMware products.

twoGbMaxExtentSparse
   A sparse (allocate on demand) disk with 2GB maximum extent size. Disks in this format can be used with other VMware products. The 2GB extent size makes these disks easier to burn to dvd or use on filesystems that don't support large files.

twoGbMaxExtentFlat
   A preallocated disk with 2GB maximum extent size. Disks in this format can be used with other VMware products. The 2GB extent size makes these disks easier to burn to dvd or use on filesystems that don't support large files.

thin
   Space required for thin-provisioned virtual disk is allocated and zeroed on demand as the space is used.

sparse
   Depending on the host type, Sparse is mapped to either MonolithicSparse or Thin.

thick
   A thick disk has all space allocated at creation time and the space is zeroed on demand as the space is used.

seSparse
   A sparse (allocate on demand) format with additional space optimizations.

monolithicFlat
   A preallocated monolithic disk. Disks in this format can be used with other VMware products.
