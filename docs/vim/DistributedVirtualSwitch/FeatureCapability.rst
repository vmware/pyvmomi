.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _high: ../../vim/SharesInfo/Level.rst#high

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _shares: ../../vim/dvs/NetworkResourcePool/AllocationInfo.rst#shares

.. _normal: ../../vim/SharesInfo/Level.rst#normal

.. _PhysicalNic: ../../vim/host/PhysicalNic.rst

.. _HostCapability: ../../vim/host/Capability.rst

.. _vSphere API 4.1: ../../vim/version.rst#vimversionversion6

.. _DVSRollback_Task: ../../vim/DistributedVirtualSwitch.rst#rollback

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _rollbackSupported: ../../vim/DistributedVirtualSwitch/RollbackCapability.rst#rollbackSupported

.. _UpdateDvsCapability: ../../vim/DistributedVirtualSwitch.rst#updateCapability

.. _DVSFeatureCapability: ../../vim/DistributedVirtualSwitch/FeatureCapability.rst

.. _DVPortgroupRollback_Task: ../../vim/dvs/DistributedVirtualPortgroup.rst#rollback

.. _DistributedVirtualSwitch: ../../vim/DistributedVirtualSwitch.rst

.. _vmDirectPathGen2Supported: ../../vim/host/PhysicalNic.rst#vmDirectPathGen2Supported

.. _DistributedVirtualPortgroup: ../../vim/dvs/DistributedVirtualPortgroup.rst

.. _DVSManagerImportEntity_Task: ../../vim/dvs/DistributedVirtualSwitchManager.rst#importEntity

.. _DVSManagerExportEntity_Task: ../../vim/dvs/DistributedVirtualSwitchManager.rst#exportEntity

.. _VmwareDistributedVirtualSwitch: ../../vim/dvs/VmwareDistributedVirtualSwitch.rst

.. _DistributedVirtualSwitchManager: ../../vim/dvs/DistributedVirtualSwitchManager.rst

.. _DistributedVirtualSwitchNicTeamingPolicyMode: ../../vim/DistributedVirtualSwitch/NicTeamingPolicyMode.rst

.. _vim.DistributedVirtualSwitch.RollbackCapability: ../../vim/DistributedVirtualSwitch/RollbackCapability.rst

.. _vim.DistributedVirtualSwitch.BackupRestoreCapability: ../../vim/DistributedVirtualSwitch/BackupRestoreCapability.rst

.. _vim.DistributedVirtualSwitch.HealthCheckFeatureCapability: ../../vim/DistributedVirtualSwitch/HealthCheckFeatureCapability.rst

.. _vim.DistributedVirtualSwitch.NetworkResourceManagementCapability: ../../vim/DistributedVirtualSwitch/NetworkResourceManagementCapability.rst


vim.DistributedVirtualSwitch.FeatureCapability
==============================================
  The `DVSFeatureCapability`_ data object represents the capabilities supported by a `DistributedVirtualSwitch`_ . These properties are read-only with the exception of `vmDirectPathGen2Supported`_ .
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1`_

Attributes:
    networkResourceManagementSupported (`bool`_):

       Indicates whether network I/O control is supported on the vSphere Distributed Switch.
    vmDirectPathGen2Supported (`bool`_):

       Indicates whether VMDirectPath Gen 2 is supported on the distributed virtual switch. See `HostCapability`_ . `vmDirectPathGen2Supported`_ and `PhysicalNic`_ . `vmDirectPathGen2Supported`_ .For a third-party distributed switch implementation, you can specify this property during switch creation or when you call the `UpdateDvsCapability`_ method.VMDirectPath Gen 2 is supported in vSphere Distributed Switch Version 4.1 or later.
    nicTeamingPolicy (`str`_, optional):

       The available teaming modes for the vSphere Distributed Switch. The value can be one or more of `DistributedVirtualSwitchNicTeamingPolicyMode`_ .
    networkResourcePoolHighShareValue (`int`_, optional):

       This is the value for `high`_ in `shares`_ . This implicitly defines the legal range of share values to be between 1 and this. This also defines values for other level types, such as `normal`_ being one half of this value and `low`_ being one fourth of this value.
    networkResourceManagementCapability (`vim.DistributedVirtualSwitch.NetworkResourceManagementCapability`_, optional):

       Network resource management capabilities supported by a distributed virtual switch.
    healthCheckCapability (`vim.DistributedVirtualSwitch.HealthCheckFeatureCapability`_, optional):

       Health check capabilities supported by a `VmwareDistributedVirtualSwitch`_ .
    rollbackCapability (`vim.DistributedVirtualSwitch.RollbackCapability`_, optional):

       Host rollback capability. IfrollbackCapability. `rollbackSupported`_ is true, network operations that disconnect the the host are rolled back.
    backupRestoreCapability (`vim.DistributedVirtualSwitch.BackupRestoreCapability`_, optional):

       Backup, restore, and rollback capabilities. Backup and restore are supported only for `VmwareDistributedVirtualSwitch`_ . Rollback is supported for `VmwareDistributedVirtualSwitch`_ and `DistributedVirtualPortgroup`_ . For information about backup and restore, see the `DistributedVirtualSwitchManager`_ methods `DVSManagerExportEntity_Task`_ and `DVSManagerImportEntity_Task`_ . For information about rollback, see the `DistributedVirtualSwitch`_ . `DVSRollback_Task`_ and `DistributedVirtualPortgroup`_ . `DVPortgroupRollback_Task`_ methods.
    networkFilterSupported (`bool`_, optional):

       Indicates whether Network Filter feature is supported in vSphere Distributed Switch.
