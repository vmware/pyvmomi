
vim.DistributedVirtualSwitch.BackupRestoreCapability
====================================================
  The `DVSBackupRestoreCapability <vim/DistributedVirtualSwitch/BackupRestoreCapability.rst>`_ data object describes backup, restore, and rollback capabilities for distributed virtual switches and distributed virtual portgroups. Backup and restore capabilities are indicated for `DistributedVirtualSwitch <vim/DistributedVirtualSwitch.rst>`_ . Rollback capability is indicated for `DistributedVirtualSwitch <vim/DistributedVirtualSwitch.rst>`_ and `DistributedVirtualPortgroup <vim/dvs/DistributedVirtualPortgroup.rst>`_ .
:extends: vmodl.DynamicData_
:since: `vSphere API 5.1 <vim/version.rst#vimversionversion8>`_

Attributes:
    backupRestoreSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether backup, restore, and rollback are supported.
