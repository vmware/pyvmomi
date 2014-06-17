.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.1: ../../vim/version.rst#vimversionversion8

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _DistributedVirtualSwitch: ../../vim/DistributedVirtualSwitch.rst

.. _DVSBackupRestoreCapability: ../../vim/DistributedVirtualSwitch/BackupRestoreCapability.rst

.. _DistributedVirtualPortgroup: ../../vim/dvs/DistributedVirtualPortgroup.rst


vim.DistributedVirtualSwitch.BackupRestoreCapability
====================================================
  The `DVSBackupRestoreCapability`_ data object describes backup, restore, and rollback capabilities for distributed virtual switches and distributed virtual portgroups. Backup and restore capabilities are indicated for `DistributedVirtualSwitch`_ . Rollback capability is indicated for `DistributedVirtualSwitch`_ and `DistributedVirtualPortgroup`_ .
:extends: vmodl.DynamicData_
:since: `vSphere API 5.1`_

Attributes:
    backupRestoreSupported (`bool`_):

       Indicates whether backup, restore, and rollback are supported.
