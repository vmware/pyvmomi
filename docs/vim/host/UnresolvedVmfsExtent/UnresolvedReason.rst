vim.host.UnresolvedVmfsExtent.UnresolvedReason
==============================================
  Reasons for identifying the disk extent as copy of VMFS volume extent.
  :contained by: `vim.host.UnresolvedVmfsExtent <vim/host/UnresolvedVmfsExtent.rst>`_

  :type: `vim.host.UnresolvedVmfsExtent.UnresolvedReason <vim/host/UnresolvedVmfsExtent/UnresolvedReason.rst>`_

  :name: uuidConflict

values:
--------

diskIdMismatch
   The VMFS detected 'diskid' does not match with LVM detected 'diskId'

uuidConflict
   VMFS 'uuid' does not match
