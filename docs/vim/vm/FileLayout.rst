
vim.vm.FileLayout
=================
  Describes the set of files that makes up a virtual machine on disk. The file layout is broken into 4 major sections:
   * Configuration: Files stored in the configuration directory
   * Log: Files stored in the log directory
   * Disk: Files stored relative to a disk configuration file
   * Snapshot: Stored in the snapshot directory
   * Often the same directory is used for configuration, log, disk and snapshots.
   * 
:extends: vmodl.DynamicData_
**deprecated**


Attributes:
    configFile ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       A list of files that makes up the configuration of the virtual machine (excluding the .vmx file, since that file is represented in the FileInfo). These are relative paths from the configuration directory. A slash is always used as a separator. This list will typically include the NVRAM file, but could also include other meta-data files.
    logFile ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       A list of files stored in the virtual machine's log directory. These are relative paths from the logDirectory. A slash is always used as a separator.
    disk ([`vim.vm.FileLayout.DiskLayout <vim/vm/FileLayout/DiskLayout.rst>`_], optional):

       Files making up each virtual disk.
    snapshot ([`vim.vm.FileLayout.SnapshotLayout <vim/vm/FileLayout/SnapshotLayout.rst>`_], optional):

       Files of each snapshot.
    swapFile (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The swapfile specific to this virtual machine, if any. This is a complete datastore path, not a relative path.
