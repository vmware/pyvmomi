.. _int: https://docs.python.org/2/library/stdtypes.html

.. _file: ../../../vim/vm/FileLayoutEx.rst#file

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vim.vm.Snapshot: ../../../vim/vm/Snapshot.rst

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.vm.FileLayoutEx.DiskLayout: ../../../vim/vm/FileLayoutEx/DiskLayout.rst


vim.vm.FileLayoutEx.SnapshotLayout
==================================
  Layout of a snapshot.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    key (`vim.vm.Snapshot`_):

       Reference to the snapshot.
    dataKey (`int`_):

       Key to the snapshot data file in `file`_ .
    disk (`vim.vm.FileLayoutEx.DiskLayout`_, optional):

       Layout of each virtual disk of the virtual machine when the snapshot was taken.
