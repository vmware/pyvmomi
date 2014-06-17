.. _vim.fault.MigrationFault: ../../vim/fault/MigrationFault.rst


vim.fault.UncommittedUndoableDisk
=================================
    :extends:

        `vim.fault.MigrationFault`_

  Fault thrown when an attempt is made to move or clone an undoable disk with an uncommitted REDO log. This is an error. Undoable disks may be moved but they must be committed.

Attributes:




