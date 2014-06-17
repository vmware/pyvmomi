.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.vm.Snapshot: ../../../vim/vm/Snapshot.rst

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.vm.FileLayout.SnapshotLayout
================================
  Enumerates the set of files that make up a snapshot or redo-point
:extends: vmodl.DynamicData_

Attributes:
    key (`vim.vm.Snapshot`_):

       Identification of the snapshot
    snapshotFile (`str`_):

       A list of files that make up the snapshot state. These are relative paths from the snapshotDirectory. A slash is always used as a separator.
