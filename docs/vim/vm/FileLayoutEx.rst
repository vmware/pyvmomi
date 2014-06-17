.. _datetime: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.vm.FileLayoutEx.FileInfo: ../../vim/vm/FileLayoutEx/FileInfo.rst

.. _vim.vm.FileLayoutEx.DiskLayout: ../../vim/vm/FileLayoutEx/DiskLayout.rst

.. _vim.vm.FileLayoutEx.SnapshotLayout: ../../vim/vm/FileLayoutEx/SnapshotLayout.rst

.. _VirtualMachineFileLayoutExFileType: ../../vim/vm/FileLayoutEx/FileType.rst


vim.vm.FileLayoutEx
===================
  Detailed description of files that make up a virtual machine on disk. The file layout is broken into 4 major sections:
   * Configuration: Files stored in the configuration directory
   * Log: Files stored in the log directory
   * Disk: Files stored relative to a disk configuration file
   * Snapshot: Stored in the snapshot directory
   * Often the same directory is used for configuration, log, disk and snapshots.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    file (`vim.vm.FileLayoutEx.FileInfo`_, optional):

       Information about all the files that constitute the virtual machine including configuration files, disks, swap file, suspend file, log files, core files, memory file etc. `VirtualMachineFileLayoutExFileType`_ lists the different file-types that make a virtual machine.
    disk (`vim.vm.FileLayoutEx.DiskLayout`_, optional):

       Layout of each virtual disk attached to the virtual machine.For a virtual machine with snaphots, this property gives only those disks that are attached to it at the current point of running.
    snapshot (`vim.vm.FileLayoutEx.SnapshotLayout`_, optional):

       Layout of each snapshot of the virtual machine.
    timestamp (`datetime`_):

       Time when values in this structure were last updated.
