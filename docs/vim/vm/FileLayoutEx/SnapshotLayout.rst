
vim.vm.FileLayoutEx.SnapshotLayout
==================================
  Layout of a snapshot.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    key (`vim.vm.Snapshot <vim/vm/Snapshot.rst>`_):

       Reference to the snapshot.
    dataKey (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Key to the snapshot data file in `file <vim/vm/FileLayoutEx.rst#file>`_ .
    disk ([`vim.vm.FileLayoutEx.DiskLayout <vim/vm/FileLayoutEx/DiskLayout.rst>`_], optional):

       Layout of each virtual disk of the virtual machine when the snapshot was taken.
