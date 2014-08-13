.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _datetime: https://docs.python.org/2/library/stdtypes.html

.. _vim.vm.Snapshot: ../../vim/vm/Snapshot.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.VirtualMachine: ../../vim/VirtualMachine.rst

.. _vim.vm.SnapshotTree: ../../vim/vm/SnapshotTree.rst

.. _vim.VirtualMachine.PowerState: ../../vim/VirtualMachine/PowerState.rst


vim.vm.SnapshotTree
===================
  SnapshotTree encapsulates all the read-only data produced by the snapshot.
:extends: vmodl.DynamicData_

Attributes:
    snapshot (`vim.vm.Snapshot`_):

       The managed object for this snapshot.
    vm (`vim.VirtualMachine`_):

       The virtual machine for which the snapshot was taken.
    name (`str`_):

       Name of the snapshot.
    description (`str`_):

       Description of the snapshot.
    id (`int`_):

       The unique identifier that distinguishes this snapshot from other snapshots of the virtual machine.
    createTime (`datetime`_):

       The date and time the snapshot was taken.
    state (`vim.VirtualMachine.PowerState`_):

       The power state of the virtual machine when this snapshot was taken.
    quiesced (`bool`_):

       Flag to indicate whether or not the snapshot was created with the "quiesce" option, ensuring a consistent state of the file system.
    backupManifest (`str`_, optional):

       The relative path from the snapshotDirectory pointing to the backup manifest. Available for certain quiesced snapshots only.
    childSnapshotList ([`vim.vm.SnapshotTree`_], optional):

       The snapshot data for all snapshots for which this snapshot is the parent.
    replaySupported (`bool`_, optional):

       Flag to indicate whether this snapshot is associated with a recording session on the virtual machine that can be replayed.
