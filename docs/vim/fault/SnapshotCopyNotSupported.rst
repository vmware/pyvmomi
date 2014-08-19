
vim.fault.SnapshotCopyNotSupported
==================================
    :extends:

        `vim.fault.MigrationFault <vim/fault/MigrationFault.rst>`_

  An attempt is being made to move or copy a virtual machine's disk that has associated snapshots, and preserving the snapshots is not supported because of some aspect of the virtual machine configuration, virtual machine power state, or the requested disk placement. This is an error for move operations (where the source is deleted after the copy) and a warning for clones (where the source is preserved).

Attributes:




