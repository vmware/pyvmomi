
vim.DistributedVirtualSwitch.FeatureCapability
==============================================
  The `DVSFeatureCapability <vim/DistributedVirtualSwitch/FeatureCapability.rst>`_ data object represents the capabilities supported by a `DistributedVirtualSwitch <vim/DistributedVirtualSwitch.rst>`_ . These properties are read-only with the exception of `vmDirectPathGen2Supported <vim/DistributedVirtualSwitch/FeatureCapability.rst#vmDirectPathGen2Supported>`_ .
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1 <vim/version.rst#vimversionversion6>`_

Attributes:
    networkResourceManagementSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether network I/O control is supported on the vSphere Distributed Switch.
    vmDirectPathGen2Supported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether VMDirectPath Gen 2 is supported on the distributed virtual switch. See `HostCapability <vim/host/Capability.rst>`_ . `vmDirectPathGen2Supported <vim/host/Capability.rst#vmDirectPathGen2Supported>`_ and `PhysicalNic <vim/host/PhysicalNic.rst>`_ . `vmDirectPathGen2Supported <vim/host/PhysicalNic.rst#vmDirectPathGen2Supported>`_ .For a third-party distributed switch implementation, you can specify this property during switch creation or when you call the `UpdateDvsCapability <vim/DistributedVirtualSwitch.rst#updateCapability>`_ method.VMDirectPath Gen 2 is supported in vSphere Distributed Switch Version 4.1 or later.
    nicTeamingPolicy ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       The available teaming modes for the vSphere Distributed Switch. The value can be one or more of `DistributedVirtualSwitchNicTeamingPolicyMode <vim/DistributedVirtualSwitch/NicTeamingPolicyMode.rst>`_ .
    networkResourcePoolHighShareValue (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       This is the value for `high <vim/SharesInfo/Level.rst#high>`_ in `shares <vim/dvs/NetworkResourcePool/AllocationInfo.rst#shares>`_ . This implicitly defines the legal range of share values to be between 1 and this. This also defines values for other level types, such as `normal <vim/SharesInfo/Level.rst#normal>`_ being one half of this value and `low <vim/SharesInfo/Level.rst#low>`_ being one fourth of this value.
    networkResourceManagementCapability (`vim.DistributedVirtualSwitch.NetworkResourceManagementCapability <vim/DistributedVirtualSwitch/NetworkResourceManagementCapability.rst>`_, optional):

       Network resource management capabilities supported by a distributed virtual switch.
    healthCheckCapability (`vim.DistributedVirtualSwitch.HealthCheckFeatureCapability <vim/DistributedVirtualSwitch/HealthCheckFeatureCapability.rst>`_, optional):

       Health check capabilities supported by a `VmwareDistributedVirtualSwitch <vim/dvs/VmwareDistributedVirtualSwitch.rst>`_ .
    rollbackCapability (`vim.DistributedVirtualSwitch.RollbackCapability <vim/DistributedVirtualSwitch/RollbackCapability.rst>`_, optional):

       Host rollback capability. IfrollbackCapability. `rollbackSupported <vim/DistributedVirtualSwitch/RollbackCapability.rst#rollbackSupported>`_ is true, network operations that disconnect the the host are rolled back.
    backupRestoreCapability (`vim.DistributedVirtualSwitch.BackupRestoreCapability <vim/DistributedVirtualSwitch/BackupRestoreCapability.rst>`_, optional):

       Backup, restore, and rollback capabilities. Backup and restore are supported only for `VmwareDistributedVirtualSwitch <vim/dvs/VmwareDistributedVirtualSwitch.rst>`_ . Rollback is supported for `VmwareDistributedVirtualSwitch <vim/dvs/VmwareDistributedVirtualSwitch.rst>`_ and `DistributedVirtualPortgroup <vim/dvs/DistributedVirtualPortgroup.rst>`_ . For information about backup and restore, see the `DistributedVirtualSwitchManager <vim/dvs/DistributedVirtualSwitchManager.rst>`_ methods `DVSManagerExportEntity_Task <vim/dvs/DistributedVirtualSwitchManager.rst#exportEntity>`_ and `DVSManagerImportEntity_Task <vim/dvs/DistributedVirtualSwitchManager.rst#importEntity>`_ . For information about rollback, see the `DistributedVirtualSwitch <vim/DistributedVirtualSwitch.rst>`_ . `DVSRollback_Task <vim/DistributedVirtualSwitch.rst#rollback>`_ and `DistributedVirtualPortgroup <vim/dvs/DistributedVirtualPortgroup.rst>`_ . `DVPortgroupRollback_Task <vim/dvs/DistributedVirtualPortgroup.rst#rollback>`_ methods.
    networkFilterSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Indicates whether Network Filter feature is supported in vSphere Distributed Switch.
