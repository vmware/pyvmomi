.. _vim.fault.SnapshotFault: ../../vim/fault/SnapshotFault.rst


vim.fault.FilesystemQuiesceFault
================================
    :extends:

        `vim.fault.SnapshotFault`_

  This fault is thrown when creating a quiesced snapshot failed because the create snapshot operation exceeded the time limit for holding off I/O in the frozen VM.This indicates that when we attempted to thaw the VM after creating the snapshot, we got an error back indicating that the VM was not frozen anymore. In this case, we roll back the entire snapshot create operation and throw this exception.

Attributes:




