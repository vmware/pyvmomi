
vim.vm.SnapshotTree
===================
  SnapshotTree encapsulates all the read-only data produced by the snapshot.
:extends: vmodl.DynamicData_

Attributes:
    snapshot (`vim.vm.Snapshot <vim/vm/Snapshot.rst>`_):

       The managed object for this snapshot.
    vm (`vim.VirtualMachine <vim/VirtualMachine.rst>`_):

       The virtual machine for which the snapshot was taken.
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Name of the snapshot.
    description (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Description of the snapshot.
    id (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The unique identifier that distinguishes this snapshot from other snapshots of the virtual machine.
    createTime (`datetime <https://docs.python.org/2/library/stdtypes.html>`_):

       The date and time the snapshot was taken.
    state (`vim.VirtualMachine.PowerState <vim/VirtualMachine/PowerState.rst>`_):

       The power state of the virtual machine when this snapshot was taken.
    quiesced (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Flag to indicate whether or not the snapshot was created with the "quiesce" option, ensuring a consistent state of the file system.
    backupManifest (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The relative path from the snapshotDirectory pointing to the backup manifest. Available for certain quiesced snapshots only.
    childSnapshotList ([`vim.vm.SnapshotTree <vim/vm/SnapshotTree.rst>`_], optional):

       The snapshot data for all snapshots for which this snapshot is the parent.
    replaySupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Flag to indicate whether this snapshot is associated with a recording session on the virtual machine that can be replayed.
