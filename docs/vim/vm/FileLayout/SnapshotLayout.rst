
vim.vm.FileLayout.SnapshotLayout
================================
  Enumerates the set of files that make up a snapshot or redo-point
:extends: vmodl.DynamicData_

Attributes:
    key (`vim.vm.Snapshot <vim/vm/Snapshot.rst>`_):

       Identification of the snapshot
    snapshotFile ([`str <https://docs.python.org/2/library/stdtypes.html>`_]):

       A list of files that make up the snapshot state. These are relative paths from the snapshotDirectory. A slash is always used as a separator.
