
vim.fault.SnapshotRevertIssue
=============================
    :extends:

        `vim.fault.MigrationFault <vim/fault/MigrationFault.rst>`_

  If the virtual machine is migrated to the destination host, there may be a problem reverting to one of its snapshots. This is a warning. If the snapshot name is not set and the event array is empty, then it the snapshot might possibly revert correctly. If the name is set and the event array is not empty then there surely will be a problem reverting to the snapshot.

Attributes:

    snapshotName (`str <https://docs.python.org/2/library/stdtypes.html>`_): is optional.

    event (`str <https://docs.python.org/2/library/stdtypes.html>`_): is optional.

    errors (`bool <https://docs.python.org/2/library/stdtypes.html>`_)




