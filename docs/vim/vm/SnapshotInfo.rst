
vim.vm.SnapshotInfo
===================
  The SnapshotInfo data object type provides all the information about the hierarchy of snapshots in a virtual machine.
:extends: vmodl.DynamicData_

Attributes:
    currentSnapshot (`vim.vm.Snapshot <vim/vm/Snapshot.rst>`_, optional):

       Current snapshot of the virtual machineThis property is set by calling `Snapshot.revert <vim/vm/Snapshot.rst#revert>`_ or `VirtualMachine.createSnapshot <vim/VirtualMachine.rst#createSnapshot>`_ . This property will be empty when the working snapshot is at the root of the snapshot tree.
    rootSnapshotList ([`vim.vm.SnapshotTree <vim/vm/SnapshotTree.rst>`_]):

       Data for the entire set of snapshots for one virtual machine.
