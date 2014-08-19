
vim.VirtualMachine
==================
  VirtualMachine is the managed object type for manipulating virtual machines, including templates that can be deployed (repeatedly) as new virtual machines. This type provides methods for configuring and controlling a virtual machine.VirtualMachine extends the ManagedEntity type because virtual machines are part of a virtual infrastructure inventory. The parent of a virtual machine must be a folder, and a virtual machine has no children.Destroying a virtual machine disposes of all associated storage, including the virtual disks. To remove a virtual machine while retaining its virtual disk storage, a client must remove the virtual disks from the virtual machine before destroying it.


:extends: vim.ManagedEntity_


Attributes
----------
    capability (`vim.vm.Capability <vim/vm/Capability.rst>`_):
       Information about the runtime capabilities of this virtual machine.
    config (`vim.vm.ConfigInfo <vim/vm/ConfigInfo.rst>`_):
       Configuration of this virtual machine, including the name and UUID.This property is set when a virtual machine is created or when the `reconfigVM <vim/VirtualMachine.rst#reconfigure>`_ method is called.The virtual machine configuration is not guaranteed to be available. For example, the configuration information would be unavailable if the server is unable to access the virtual machine files on disk, and is often also unavailable during the initial phases of virtual machine creation.
    layout (`vim.vm.FileLayout <vim/vm/FileLayout.rst>`_):
       Detailed information about the files that comprise this virtual machine.
    layoutEx (`vim.vm.FileLayoutEx <vim/vm/FileLayoutEx.rst>`_):
       Detailed information about the files that comprise this virtual machine.Can be explicitly refreshed by the `RefreshStorageInfo <vim/VirtualMachine.rst#refreshStorageInfo>`_ operation. In releases after vSphere API 5.0, vSphere Servers might not generate property collector update notifications for this property. To obtain the latest value of the property, you can use PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx. If you use the PropertyCollector.WaitForUpdatesEx method, specify an empty string for the version parameter. Any other version value will not produce any property values as no updates are generated.
    storage (`vim.vm.StorageInfo <vim/vm/StorageInfo.rst>`_):
       Storage space used by the virtual machine, split by datastore. Can be explicitly refreshed by the `RefreshStorageInfo <vim/VirtualMachine.rst#refreshStorageInfo>`_ operation. In releases after vSphere API 5.0, vSphere Servers might not generate property collector update notifications for this property. To obtain the latest value of the property, you can use PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx. If you use the PropertyCollector.WaitForUpdatesEx method, specify an empty string for the version parameter. Any other version value will not produce any property values as no updates are generated.
    environmentBrowser (`vim.EnvironmentBrowser <vim/EnvironmentBrowser.rst>`_):
       The current virtual machine's environment browser object. This contains information on all the configurations that can be used on the virtual machine. This is identical to the environment browser on the `ComputeResource <vim/ComputeResource.rst>`_ to which this virtual machine belongs.
    resourcePool (`vim.ResourcePool <vim/ResourcePool.rst>`_):
       The current resource pool that specifies resource allocation for this virtual machine.This property is set when a virtual machine is created or associated with a different resource pool.Returns null if the virtual machine is a template or the session has no access to the resource pool.
    parentVApp (`vim.ManagedEntity <vim/ManagedEntity.rst>`_):
       Reference to the parent vApp.
    resourceConfig (`vim.ResourceConfigSpec <vim/ResourceConfigSpec.rst>`_):
       The resource configuration for a virtual machine. The shares in this specification are evaluated relative to the resource pool to which it is assigned. This will return null if the product the virtual machine is registered on does not support resource configuration.To retrieve the configuration, you typically use `childConfiguration <vim/ResourcePool.rst#childConfiguration>`_ .To change the configuration, use `UpdateChildResourceConfiguration <vim/ResourcePool.rst#updateChildResourceConfiguration>`_ .
    runtime (`vim.vm.RuntimeInfo <vim/vm/RuntimeInfo.rst>`_):
       Execution state and history for this virtual machine.The contents of this property change when:
        * the virtual machine's power state changes.
        * an execution message is pending.
        * an event occurs.
    guest (`vim.vm.GuestInfo <vim/vm/GuestInfo.rst>`_):
       Information about VMware Tools and about the virtual machine from the perspective of VMware Tools. Information about the guest operating system is available in VirtualCenter. Guest operating system information reflects the last known state of the virtual machine. For powered on machines, this is current information. For powered off machines, this is the last recorded state before the virtual machine was powered off.
    summary (`vim.vm.Summary <vim/vm/Summary.rst>`_):
       Basic information about this virtual machine. This includes:
        * runtimeInfo
        * guest
        * basic configuration
        * alarms
        * performance information
    datastore ([`vim.Datastore <vim/Datastore.rst>`_]):
      privilege: System.View
       A collection of references to the subset of datastore objects in the datacenter that is used by this virtual machine.
    network ([`vim.Network <vim/Network.rst>`_]):
      privilege: System.View
       A collection of references to the subset of network objects in the datacenter that is used by this virtual machine.
    snapshot (`vim.vm.SnapshotInfo <vim/vm/SnapshotInfo.rst>`_):
       Current snapshot and tree. The property is valid if snapshots have been created for this virtual machine.The contents of this property change in response to the methods:
        * `CreateSnapshot_Task <vim/VirtualMachine.rst#createSnapshot>`_
        * `RevertToCurrentSnapshot_Task <vim/VirtualMachine.rst#revertToCurrentSnapshot>`_
        * `RemoveSnapshot_Task <vim/vm/Snapshot.rst#remove>`_
        * `RevertToSnapshot_Task <vim/vm/Snapshot.rst#revert>`_
        * `RemoveAllSnapshots_Task <vim/VirtualMachine.rst#removeAllSnapshots>`_
    rootSnapshot ([`vim.vm.Snapshot <vim/vm/Snapshot.rst>`_]):
       The roots of all snapshot trees for the virtual machine.
    guestHeartbeatStatus (`vim.ManagedEntity.Status <vim/ManagedEntity/Status.rst>`_):
       The guest heartbeat. The heartbeat status is classified as:
        * gray - VMware Tools are not installed or not running.
        * red - No heartbeat. Guest operating system may have stopped responding.
        * yellow - Intermittent heartbeat. May be due to guest load.
        * green - Guest operating system is responding normally.The guest heartbeat is a statistics metric. Alarms can be configured on this metric to trigger emails or other actions.


Methods
-------


RefreshStorageInfo():
   Explicitly refreshes the storage information of this virtual machine, updating properties `storage <vim/VirtualMachine.rst#storage>`_ , `layoutEx <vim/VirtualMachine.rst#layoutEx>`_ and `storage <vim/vm/Summary.rst#storage>`_ .
  since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_


  Privilege:
               System.Read



  Args:


  Returns:
    None
         


CreateSnapshot(name, description, memory, quiesce):
   Creates a new snapshot of this virtual machine. As a side effect, this updates the current snapshot.Snapshots are not supported for Fault Tolerance primary and secondary virtual machines.Any % (percent) character used in this name parameter must be escaped, unless it is used to start an escape sequence. Clients may also escape any other characters in this name parameter.


  Privilege:
               VirtualMachine.State.CreateSnapshot



  Args:
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The name for this snapshot. The name need not be unique for this virtual machine.


    description (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       A description for this snapshot. If omitted, a default description may be provided.


    memory (`bool <https://docs.python.org/2/library/stdtypes.html>`_):
       If TRUE, a dump of the internal state of the virtual machine (basically a memory dump) is included in the snapshot. Memory snapshots consume time and resources, and thus take longer to create. When set to FALSE, the power state of the snapshot is set to powered off. `capabilities <vim/vm/ConfigOption.rst#capabilities>`_ indicates whether or not this virtual machine supports this operation.


    quiesce (`bool <https://docs.python.org/2/library/stdtypes.html>`_):
       If TRUE and the virtual machine is powered on when the snapshot is taken, VMware Tools is used to quiesce the file system in the virtual machine. This assures that a disk snapshot represents a consistent state of the guest file systems. If the virtual machine is powered off or VMware Tools are not available, the quiesce flag is ignored.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         the newly created Snapshot.

  Raises:

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if the virtual machine is busy.

    `vim.fault.SnapshotFault <vim/fault/SnapshotFault.rst>`_: 
       if an error occurs during the snapshot operation. Typically a more specific fault like MultipleSnapshotsNotSupported is thrown.

    `vim.fault.VmConfigFault <vim/fault/VmConfigFault.rst>`_: 
       if the virtual machine's configuration is invalid. Typically, a more specific fault like InvalidSnapshotState is thrown.

    `vim.fault.FileFault <vim/fault/FileFault.rst>`_: 
       if there is a problem with creating or accessing one or more files needed for this operation.

    `vim.fault.InvalidName <vim/fault/InvalidName.rst>`_: 
       if the specified snapshot name is invalid.

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the operation cannot be performed because of the virtual machine's current state. For example, the virtual machine configuration information is not available.

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       if the host product does not support snapshots or if the host does not support quiesced snapshots and the quiesce parameter is set to true; or if the virtual machine is a Fault Tolerance primary or secondary

    `vim.fault.InvalidPowerState <vim/fault/InvalidPowerState.rst>`_: 
       if the operation cannot be performed in the current power state of the virtual machine.


RevertToCurrentSnapshot(host, suppressPowerOn):
   Reverts the virtual machine to the current snapshot. This is equivalent to doing snapshot.currentSnapshot.revert.If no snapshot exists, then the operation does nothing, and the virtual machine state remains unchanged.


  Privilege:
               VirtualMachine.State.RevertToSnapshot



  Args:
    host (`vim.HostSystem <vim/HostSystem.rst>`_, optional):
       (optional) Choice of host for the virtual machine, in case this operation causes the virtual machine to power on.If a snapshot was taken while a virtual machine was powered on, and this operation is invoked after the virtual machine was powered off, the operation causes the virtual machine to power on to reach the snapshot state. This parameter can be used to specify a choice of host where the virtual machine should power on.If this parameter is not set, and the vBalance feature is configured for automatic load balancing, a host is automatically selected. Otherwise, the virtual machine keeps its existing host affiliation.This is not supported for virtual machines associated with hosts on ESX 2.x servers.


    suppressPowerOn (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional, since `vSphere API 4.0 <vim/version.rst#vimversionversion4>`_ ):
       (optional) If set to true, the virtual machine will not be powered on regardless of the power state when the current snapshot was created. Default to false.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if the virtual machine is busy.

    `vim.fault.SnapshotFault <vim/fault/SnapshotFault.rst>`_: 
       if an error occurs during the snapshot operation. Typically, a more specific fault like InvalidSnapshotFormat is thrown.

    `vim.fault.InsufficientResourcesFault <vim/fault/InsufficientResourcesFault.rst>`_: 
       if this operation would violate a resource usage policy.

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the operation cannot be performed because of the virtual machine's current state. For example, if the virtual machine configuration information is not available or if an OVF consumer is blocking the operation.

    `vim.fault.VmConfigFault <vim/fault/VmConfigFault.rst>`_: 
       if a configuration issue prevents the power-on. Typically, a more specific fault, such as UnsupportedVmxLocation, is thrown.

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       if the virtual machine does not have a current snapshot.

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       if the host product does not support snapshots.

    `vim.fault.InvalidPowerState <vim/fault/InvalidPowerState.rst>`_: 
       if the operation cannot be performed in the current power state of the virtual machine.

    `vim.fault.DisallowedOperationOnFailoverHost <vim/fault/DisallowedOperationOnFailoverHost.rst>`_: 
       if the virtual machine is being reverted to a powered on state and the host specified is a failover host. See `ClusterFailoverHostAdmissionControlPolicy <vim/cluster/FailoverHostAdmissionControlPolicy.rst>`_ .


RemoveAllSnapshots(consolidate):
   Remove all the snapshots associated with this virtual machine. If the virtual machine does not have any snapshots, then this operation simply returns successfully.


  Privilege:
               VirtualMachine.State.RemoveSnapshot



  Args:
    consolidate (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional, since `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_ ):
       (optional) If set to true, the virtual disks of the deleted snapshot will be merged with other disk if possible. Default to true.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if the virtual machine is busy.

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the operation cannot be performed because of the virtual machine's current state. For example, if the virtual machine configuration information is not available.

    `vim.fault.SnapshotFault <vim/fault/SnapshotFault.rst>`_: 
       if an error occurs during the snapshot operation. Typically, a more specific fault like InvalidSnapshotFormat is thrown.

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       if the host product does not support snapshots.

    `vim.fault.InvalidPowerState <vim/fault/InvalidPowerState.rst>`_: 
       if the operation cannot be performed in the current power state of the virtual machine.


ConsolidateVMDisks():
   Consolidate the virtual disk files of the virtual machine by finding hierarchies of redo logs that can be combined without violating data dependency. The redundant redo logs after merging are then deleted. Consolidation improves I/O performance since less number of virtual disk files need to be traversed; it also reduces the storage usage. However additional space is temporarily required to perform the operation. Use `EstimateStorageForConsolidateSnapshots_Task <vim/VirtualMachine.rst#estimateStorageRequirementForConsolidate>`_ to estimate the temporary space required. Consolidation can be I/O intensive, it is advisable to invoke this operation when guest is not under heavy I/O usage.
  since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_


  Privilege:
               VirtualMachine.State.RemoveSnapshot



  Args:


  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if the virtual machine is busy.

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the operation cannot be performed because of the virtual machine's current state. For example, if the virtual machine configuration information is not available.

    `vim.fault.FileFault <vim/fault/FileFault.rst>`_: 
       if if there is a problem creating or accessing the virtual machine's files for this operation. Typically a more specific fault for example `NoDiskSpace <vim/fault/NoDiskSpace.rst>`_ is thrown.

    `vim.fault.VmConfigFault <vim/fault/VmConfigFault.rst>`_: 
       if a virtual machine configuration issue prevents consolidation. Typically, a more specific fault is thrown such as `InvalidDiskFormat <vim/fault/InvalidDiskFormat.rst>`_ if a disk cannot be read, or `InvalidSnapshotFormat <vim/fault/InvalidSnapshotFormat.rst>`_ if the snapshot configuration is invalid.


EstimateStorageForConsolidateSnapshots():
   Estimate the temporary space required to consolidation disk files. The estimation is a lower bound if the childmost writable disk file will be consolidated for an online virtual machine, it is accurate for all other situations. This is because the space requirement depending on the size of the childmost disk file and how write intensive the guest is.This method can be used prior to invoke consolidation via `ConsolidateVMDisks_Task <vim/VirtualMachine.rst#consolidateDisks>`_ .
  since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_


  Privilege:
               VirtualMachine.State.RemoveSnapshot



  Args:


  Returns:
     `vim.Task <vim/Task.rst>`_:
         Space requirement for each datastore involved.

  Raises:

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if the virtual machine is busy.

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the operation cannot be performed because of the virtual machine's current state. For example, if the virtual machine configuration information is not available.

    `vim.fault.FileFault <vim/fault/FileFault.rst>`_: 
       if if there is a problem accessing the virtual machine's files for this operation. Typically a more specific fault `FileLocked <vim/fault/FileLocked.rst>`_ is thrown.

    `vim.fault.VmConfigFault <vim/fault/VmConfigFault.rst>`_: 
       if a virtual machine configuration issue prevents the estimation. Typically, a more specific fault is thrown.


ReconfigVM(spec):
   Reconfigures this virtual machine. All the changes in the given configuration are applied to the virtual machine as an atomic operation.Reconfiguring the virtual machine may require any of the following privileges depending on what is being changed:
    * VirtualMachine.Interact.DeviceConnection if changing the runtime connection state of a device as embodied by the Connectable property.
    * VirtualMachine.Interact.SetCDMedia if changing the backing of a CD-ROM device
    * VirtualMachine.Interact.SetFloppyMedia if changing the backing of a floppy device
    * VirtualMachine.Config.Rename if renaming the virtual machine
    * VirtualMachine.Config.Annotation if setting annotation a value
    * VirtualMachine.Config.AddExistingDisk if adding a virtual disk device that is backed by an existing virtual disk file
    * VirtualMachine.Config.AddNewDisk if adding a virtual disk device for which the backing virtual disk file is to be created
    * VirtualMachine.Config.RemoveDisk if removing a virtual disk device that refers to a virtual disk file
    * VirtualMachine.Config.CPUCount if changing the number of CPUs
    * VirtualMachine.Config.Memory if changing the amount of memory
    * VirtualMachine.Config.RawDevice if adding, removing or editing a raw device mapping (RDM) or SCSI passthrough device
    * VirtualMachine.Config.AddRemoveDevice if adding or removing any device other than disk, raw, or USB device
    * VirtualMachine.Config.EditDevice if changing the settings of any device
    * VirtualMachine.Config.Settings if changing any basic settings such as those in ToolsConfigInfo, FlagInfo, or DefaultPowerOpInfo
    * VirtualMachine.Config.Resource if changing resource allocations, affinities, or setting network traffic shaping or virtual disk shares
    * VirtualMachine.Config.AdvancedConfig if changing values in extraConfig
    * VirtualMachine.Config.SwapPlacement if changing swapPlacement
    * VirtualMachine.Config.HostUSBDevice if adding, removing or editing a VirtualUSB device backed by the host USB device.
    * VirtualMachine.Config.DiskExtend if extending an existing VirtualDisk device.
    * VirtualMachine.Config.ChangeTracking if enabling/disabling changed block tracking for the virtual machine's disks.
    * VirtualMachine.Config.MksControl if toggling display connection limits or the guest auto-lock feature.
    * DVSwitch.CanUse if connecting a VirtualEthernetAdapter to a port in a DistributedVirtualSwitch.
    * DVPortgroup.CanUse if connecting a VirtualEthernetAdapter to a DistributedVirtualPortgroup.Creating a virtual machine may require the following privileges:
    * VirtualMachine.Config.RawDevice if adding a raw device
    * VirtualMachine.Config.AddExistingDisk if adding a VirtualDisk and the fileOperation is unset
    * VirtualMachine.Config.AddNewDisk if adding a VirtualDisk and the fileOperation is set
    * VirtualMachine.Config.HostUSBDevice if adding a VirtualUSB device backed by the host USB device.In addition, this operation may require the following privileges:
    * Datastore.AllocateSpace on any datastore where virtual disks will be created or extended.
    * Network.Assign on any network the virtual machine will be connected to.


  Privilege:
               dynamic



  Args:
    spec (`vim.vm.ConfigSpec <vim/vm/ConfigSpec.rst>`_):
       The new configuration values.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if the virtual machine is busy.

    `vim.fault.VmConfigFault <vim/fault/VmConfigFault.rst>`_: 
       if the spec is invalid. Typically, a more specific subclass is thrown.

    `vim.fault.ConcurrentAccess <vim/fault/ConcurrentAccess.rst>`_: 
       if the changeVersion does not match the server's changeVersion for the configuration.

    `vim.fault.FileFault <vim/fault/FileFault.rst>`_: 
       if there is a problem creating or accessing the virtual machine's files for this operation. Typically a more specific fault like NoDiskSpace or FileAlreadyExists is thrown.

    `vim.fault.InvalidName <vim/fault/InvalidName.rst>`_: 
       if the specified name is invalid.

    `vim.fault.DuplicateName <vim/fault/DuplicateName.rst>`_: 
       if the specified name already exists in the parent folder.

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the operation cannot be performed in the current state of the virtual machine. For example, because the virtual machine's configuration is not available.

    `vim.fault.InsufficientResourcesFault <vim/fault/InsufficientResourcesFault.rst>`_: 
       if this operation would violate a resource usage policy.

    `vim.fault.InvalidDatastore <vim/fault/InvalidDatastore.rst>`_: 
       vim.fault.InvalidDatastore

    `vim.fault.InvalidPowerState <vim/fault/InvalidPowerState.rst>`_: 
       if the power state is poweredOn and the virtual hardware cannot support the configuration changes.

    `vim.fault.TooManyDevices <vim/fault/TooManyDevices.rst>`_: 
       if the device specifications exceed the allowed limits.

    `vim.fault.CpuHotPlugNotSupported <vim/fault/CpuHotPlugNotSupported.rst>`_: 
       if the current configuration of the VM does not support hot-plugging of CPUs.

    `vim.fault.MemoryHotPlugNotSupported <vim/fault/MemoryHotPlugNotSupported.rst>`_: 
       if the current configuration of the VM does not support hot-plugging of memory.

    `vim.fault.VmWwnConflict <vim/fault/VmWwnConflict.rst>`_: 
       if the WWN of the virtual machine has been used by other virtual machines.


UpgradeVM(version):
   Upgrades this virtual machine's virtual hardware to the latest revision that is supported by the virtual machine's current host.


  Privilege:
               VirtualMachine.Config.UpgradeVirtualHardware



  Args:
    version (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       If specified, upgrade to that specified version. If not specified, upgrade to the most current virtual hardware supported on the host.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the host is in maintenance mode, if an invalid version string is specified, or if the virtual machine is in a state in which the operation cannot be performed. For example, if the configuration information is not available.

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if the virtual machine is busy.

    `vim.fault.AlreadyUpgraded <vim/fault/AlreadyUpgraded.rst>`_: 
       if the virtual machine's hardware is already up-to-date.

    `vim.fault.NoDiskFound <vim/fault/NoDiskFound.rst>`_: 
       if no virtual disks are attached to this virtual machine.

    `vim.fault.InvalidPowerState <vim/fault/InvalidPowerState.rst>`_: 
       if the power state is not poweredOff.


ExtractOvfEnvironment():
   Returns the OVF environment for a virtual machine. If the virtual machine has no vApp configuration, an empty string is returned. Also, sensitive information is omitted, so this method is not guaranteed to return the complete OVF environment.
  since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_


  Privilege:
               VApp.ExtractOvfEnvironment



  Args:


  Returns:
    `str <https://docs.python.org/2/library/stdtypes.html>`_:
         

  Raises:

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the virtual machine is not running


PowerOnVM(host):
   Powers on this virtual machine. If the virtual machine is suspended, this method resumes execution from the suspend point.When powering on a virtual machine in a cluster, the system might implicitly or due to the host argument, do an implicit relocation of the virtual machine to another host. Hence, errors related to this relocation can be thrown. If the cluster is a DRS cluster, DRS will be invoked if the virtual machine can be automatically placed by DRS (see `DrsBehavior <vim/cluster/DrsConfigInfo/DrsBehavior.rst>`_ ). Because this method does not return a DRS `ClusterRecommendation <vim/cluster/Recommendation.rst>`_ , no vmotion nor host power operations will be done as part of a DRS-facilitated power on. To have DRS consider such operations use `PowerOnMultiVM_Task <vim/Datacenter.rst#powerOnVm>`_ . As of vSphere API 5.1, use of this method with vCenter Server is deprecated; use `PowerOnMultiVM_Task <vim/Datacenter.rst#powerOnVm>`_ instead.If this virtual machine is a fault tolerant primary virtual machine, its secondary virtual machines will be started on system-selected hosts. If the virtual machines are in a VMware DRS enabled cluster, then DRS will be invoked to obtain placements for the secondaries but no vmotion nor host power operations will be considered for these power ons.


  Privilege:
               VirtualMachine.Interact.PowerOn



  Args:
    host (`vim.HostSystem <vim/HostSystem.rst>`_, optional):
       (optional) The host where the virtual machine is to be powered on. If no host is specified, the current associated host is used. This field must specify a host that is part of the same compute resource that the virtual machine is currently associated with. If this host is not compatible, the current host association is used.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if the virtual machine is busy.

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the host is in maintenance mode or if the virtual machine's configuration information is not available.

    `vim.fault.InsufficientResourcesFault <vim/fault/InsufficientResourcesFault.rst>`_: 
       if this operation would violate a resource usage policy.

    `vim.fault.VmConfigFault <vim/fault/VmConfigFault.rst>`_: 
       if a configuration issue prevents the power-on. Typically, a more specific fault, such as UnsupportedVmxLocation, is thrown.

    `vim.fault.FileFault <vim/fault/FileFault.rst>`_: 
       if there is a problem accessing the virtual machine on the filesystem.

    `vim.fault.InvalidPowerState <vim/fault/InvalidPowerState.rst>`_: 
       if the power state is poweredOn.

    `vmodl.fault.NotEnoughLicenses <vmodl/fault/NotEnoughLicenses.rst>`_: 
       if there are not enough licenses to power on this virtual machine.

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       if the virtual machine is marked as a template.

    `vim.fault.DisallowedOperationOnFailoverHost <vim/fault/DisallowedOperationOnFailoverHost.rst>`_: 
       if the host specified is a failover host. See `ClusterFailoverHostAdmissionControlPolicy <vim/cluster/FailoverHostAdmissionControlPolicy.rst>`_ .


PowerOffVM():
   Powers off this virtual machine. If this virtual machine is a fault tolerant primary virtual machine, this will result in the secondary virtual machine(s) getting powered off as well.


  Privilege:
               VirtualMachine.Interact.PowerOff



  Args:


  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if the virtual machine is busy.

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the operation cannot be performed because of the virtual machine's current state. For example, if the virtual machine configuration information is not available.

    `vim.fault.InvalidPowerState <vim/fault/InvalidPowerState.rst>`_: 
       if the power state is not poweredOn.

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       if the virtual machine is marked as a template.


SuspendVM():
   Suspends execution in this virtual machine.


  Privilege:
               VirtualMachine.Interact.Suspend



  Args:


  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if the virtual machine is busy.

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the operation cannot be performed because of the virtual machine's current state. For example, if the virtual machine configuration information is not available.

    `vim.fault.InvalidPowerState <vim/fault/InvalidPowerState.rst>`_: 
       if the power state is not poweredOn.

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       if the virtual machine is marked as a template.


ResetVM():
   Resets power on this virtual machine. If the current state is poweredOn, then this method first performs powerOff(hard). Once the power state is poweredOff, then this method performs powerOn(option).Although this method functions as a powerOff followed by a powerOn, the two operations are atomic with respect to other clients, meaning that other power operations cannot be performed until the reset method completes.


  Privilege:
               VirtualMachine.Interact.Reset



  Args:


  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if the virtual machine is busy.

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the host is in maintenance mode.

    `vim.fault.InvalidPowerState <vim/fault/InvalidPowerState.rst>`_: 
       if the power state is suspended.

    `vmodl.fault.NotEnoughLicenses <vmodl/fault/NotEnoughLicenses.rst>`_: 
       if there are not enough licenses to reset this virtual machine.

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       if the virtual machine is marked as a template.


ShutdownGuest():
   Issues a command to the guest operating system asking it to perform a clean shutdown of all services. Returns immediately and does not wait for the guest operating system to complete the operation.


  Privilege:
               VirtualMachine.Interact.PowerOff



  Args:


  Returns:
    None
         

  Raises:

    `vim.fault.ToolsUnavailable <vim/fault/ToolsUnavailable.rst>`_: 
       if VMware Tools is not running.

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if the virtual machine is busy.

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the operation cannot be performed because of the virtual machine's current state. For example, if the virtual machine configuration information is not available.

    `vim.fault.InvalidPowerState <vim/fault/InvalidPowerState.rst>`_: 
       if the power state is not powered on.


RebootGuest():
   Issues a command to the guest operating system asking it to perform a reboot. Returns immediately and does not wait for the guest operating system to complete the operation.


  Privilege:
               VirtualMachine.Interact.Reset



  Args:


  Returns:
    None
         

  Raises:

    `vim.fault.ToolsUnavailable <vim/fault/ToolsUnavailable.rst>`_: 
       if VMware Tools is not running.

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if the virtual machine is busy.

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the operation cannot be performed because of the virtual machine's current state. For example, if the virtual machine configuration information is not available.

    `vim.fault.InvalidPowerState <vim/fault/InvalidPowerState.rst>`_: 
       if the power state is not powered on.


StandbyGuest():
   Issues a command to the guest operating system asking it to prepare for a suspend operation. Returns immediately and does not wait for the guest operating system to complete the operation.


  Privilege:
               VirtualMachine.Interact.Suspend



  Args:


  Returns:
    None
         

  Raises:

    `vim.fault.ToolsUnavailable <vim/fault/ToolsUnavailable.rst>`_: 
       if VMware Tools is not running.

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if the virtual machine is busy.

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the operation cannot be performed because of the virtual machine's current state. For example, if the virtual machine configuration information is not available.

    `vim.fault.InvalidPowerState <vim/fault/InvalidPowerState.rst>`_: 
       if the power state is not powered on.


AnswerVM(questionId, answerChoice):
   Responds to a question that is blocking this virtual machine.


  Privilege:
               VirtualMachine.Interact.AnswerQuestion



  Args:
    questionId (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The value from QuestionInfo.id that identifies the question to answer.


    answerChoice (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The contents of the QuestionInfo.choice.value array element that identifies the desired answer.




  Returns:
    None
         

  Raises:

    `vim.fault.ConcurrentAccess <vim/fault/ConcurrentAccess.rst>`_: 
       if the question has been or is being answered by another thread or user.

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if the questionId does not apply to this virtual machine. For example, this can happen if another client already answered the message.


CustomizeVM(spec):
   Customizes a virtual machine's guest operating system.


  Privilege:
               VirtualMachine.Provisioning.Customize



  Args:
    spec (`vim.vm.customization.Specification <vim/vm/customization/Specification.rst>`_):
       The customization specification object.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.CustomizationFault <vim/fault/CustomizationFault.rst>`_: 
       A subclass of CustomizationFault is thrown.


CheckCustomizationSpec(spec):
   Checks the customization specification against the virtual machine configuration. For example, this is used on a source virtual machine before a clone operation to catch customization failure before the disk copy. This checks the specification's internal consistency as well as for compatibility with this virtual machine's configuration.


  Privilege:
               VirtualMachine.Provisioning.Customize



  Args:
    spec (`vim.vm.customization.Specification <vim/vm/customization/Specification.rst>`_):
       The customization specification to check.




  Returns:
    None
         

  Raises:

    `vim.fault.CustomizationFault <vim/fault/CustomizationFault.rst>`_: 
       A subclass of CustomizationFault is thrown.


MigrateVM(pool, host, priority, state):
   Migrates a virtual machine's execution to a specific resource pool or host.Requires Resource.HotMigrate privilege if the virtual machine is powered on or Resource.ColdMigrate privilege if the virtual machine is powered off or suspended.


  Privilege:
               dynamic



  Args:
    pool (`vim.ResourcePool <vim/ResourcePool.rst>`_, optional):
       The target resource pool for the virtual machine. If the pool parameter is left unset, the virtual machine's current pool is used as the target pool.


    host (`vim.HostSystem <vim/HostSystem.rst>`_, optional):
       The target host to which the virtual machine is intended to migrate. The host parameter may be left unset if the compute resource associated with the target pool represents a stand-alone host or a DRS-enabled cluster. In the former case the stand-alone host is used as the target host. In the latter case, the DRS system selects an appropriate target host from the cluster.


    priority (`vim.VirtualMachine.MovePriority <vim/VirtualMachine/MovePriority.rst>`_):
       The task priority (@see vim.VirtualMachine.MovePriority).


    state (`vim.VirtualMachine.PowerState <vim/VirtualMachine/PowerState.rst>`_, optional):
       If specified, the virtual machine migrates only if its state matches the specified state.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.MigrationFault <vim/fault/MigrationFault.rst>`_: 
       if it is not possible to migrate the virtual machine to the destination host. This is typically due to hosts being incompatible, such as mismatch in network polices or access to networks and datastores. Typically, a more specific subclass is thrown.

    `vim.fault.FileFault <vim/fault/FileFault.rst>`_: 
       if, in a case where the virtual machine configuration file must be copied, the destination location for that file does not have the necessary file access permissions.

    `vim.fault.Timedout <vim/fault/Timedout.rst>`_: 
       if one of the phases of the migration process times out.

    `vim.fault.InsufficientResourcesFault <vim/fault/InsufficientResourcesFault.rst>`_: 
       if this operation would violate a resource usage policy.

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the operation cannot be performed because of the virtual machine's current state or the target host's current state. For example, if the virtual machine configuration information is not available or if the target host is disconnected or in maintenance mode.

    `vim.fault.VmConfigFault <vim/fault/VmConfigFault.rst>`_: 
       if the virtual machine is not compatible with the destination host. Typically, a specific subclass of this exception is thrown, such as IDEDiskNotSupported.

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       if the virtual machine is marked as a template.

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if the target host and target pool are not associated with the same compute resource or if the host parameter is left unset when the target pool is associated with a non-DRS cluster.

    `vim.fault.InvalidPowerState <vim/fault/InvalidPowerState.rst>`_: 
       if the state argument is set and the virtual machine does not have that power state.

    `vim.fault.NoActiveHostInCluster <vim/fault/NoActiveHostInCluster.rst>`_: 
       if a target host is not specified and the cluster associated with the target pool does not contain at least one potential target host. A host must be connected and not in maintenance mode in order to be considered as a potential target host.


RelocateVM(spec, priority):
   Relocates a virtual machine's virtual disks to a specific location; optionally moves the virtual machine to a different host as well. Starting from VCenter 5.1, this API also supports relocating a template to a new host should the current host becomes inactive. If spec.host is specified, this API attempts to relocate the template to the specified host; otherwise, this API will select a suitable host.Additionally requires the Resource.HotMigrate privilege if the virtual machine is powered on (for Storage VMotion), and Datastore.AllocateSpace on any datastore the virtual machine or its disks are relocated to.If the "pool" field of the RelocateSpec is set, additionally requires the Resource.AssignVMToPool privilege held on the specified pool.


  Privilege:
               Resource.ColdMigrate



  Args:
    spec (`vim.vm.RelocateSpec <vim/vm/RelocateSpec.rst>`_):
       The specification of where to relocate the virtual machine.


    priority (`vim.VirtualMachine.MovePriority <vim/VirtualMachine/MovePriority.rst>`_, optional, since `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_ ):
       The task priority (@see vim.VirtualMachine.MovePriority).




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the operation cannot be performed because of the host or virtual machine's current state. For example, if the host is in maintenance mode, or if the virtual machine's configuration information is not available.

    `vim.fault.InvalidDatastore <vim/fault/InvalidDatastore.rst>`_: 
       if the operation cannot be performed on the target datastores.

    `vim.fault.MigrationFault <vim/fault/MigrationFault.rst>`_: 
       if it is not possible to migrate the virtual machine to the destination host. This is typically due to hosts being incompatible, such as mismatch in network polices or access to networks and datastores. Typically, a more specific subclass is thrown.

    `vim.fault.VmConfigFault <vim/fault/VmConfigFault.rst>`_: 
       if the virtual machine is not compatible with the destination host. Typically, a specific subclass of this exception is thrown, such as IDEDiskNotSupported.

    `vim.fault.FileFault <vim/fault/FileFault.rst>`_: 
       if there is an error accessing the virtual machine files.

    `vim.fault.Timedout <vim/fault/Timedout.rst>`_: 
       if one of the phases of the relocate process times out.

    `vim.fault.InsufficientResourcesFault <vim/fault/InsufficientResourcesFault.rst>`_: 
       if this operation would violate a resource usage policy.

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       if the virtual machine is marked as a template.

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       in the following cases:
        * the target host and target pool are not associated with the same compute resource
        * the target pool represents a cluster without DRS enabled, and the host is not specified
        * Datastore in a diskLocator entry is not specified
        * the specified device ID cannot be found in the virtual machine's current configuration
        * the object specified in relocate cannot be found

    `vim.fault.DisallowedOperationOnFailoverHost <vim/fault/DisallowedOperationOnFailoverHost.rst>`_: 
       if the virtual machine is powered on and is being migrated to a failover host. See `ClusterFailoverHostAdmissionControlPolicy <vim/cluster/FailoverHostAdmissionControlPolicy.rst>`_ .


CloneVM(folder, name, spec):
   Creates a clone of this virtual machine. If the virtual machine is used as a template, this method corresponds to the deploy command.Any % (percent) character used in this name parameter must be escaped, unless it is used to start an escape sequence. Clients may also escape any other characters in this name parameter.The privilege required on the source virtual machine depends on the source and destination types:
    * source is virtual machine, destination is virtual machine - VirtualMachine.Provisioning.Clone
    * source is virtual machine, destination is template - VirtualMachine.Provisioning.CreateTemplateFromVM
    * source is template, destination is virtual machine - VirtualMachine.Provisioning.DeployTemplate
    * source is template, destination is template - VirtualMachine.Provisioning.CloneTemplateIf customization is requested in the CloneSpec, then the VirtualMachine.Provisioning.Customize privilege must also be held on the source virtual machine.The Resource.AssignVMToPool privilege is also required for the resource pool specified in the CloneSpec, if the destination is not a template. The Datastore.AllocateSpace privilege is required on all datastores where the clone is created.


  Privilege:



  Args:
    folder (`vim.Folder <vim/Folder.rst>`_):
       The location of the new virtual machine.


    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The name of the new virtual machine.


    spec (`vim.vm.CloneSpec <vim/vm/CloneSpec.rst>`_):
       Specifies how to clone the virtual machine.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         the newly created VirtualMachine.

  Raises:

    `vim.fault.CustomizationFault <vim/fault/CustomizationFault.rst>`_: 
       if a customization error happens. Typically, a specific subclass of this exception is thrown.

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the operation cannot be performed because of the virtual machine's current state. For example, if the virtual machine configuration information is not available.

    `vim.fault.InvalidDatastore <vim/fault/InvalidDatastore.rst>`_: 
       if the operation cannot be performed on the target datastores.

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if the virtual machine is busy.

    `vim.fault.VmConfigFault <vim/fault/VmConfigFault.rst>`_: 
       if the virtual machine is not compatible with the destination host. Typically, a specific subclass of this exception is thrown, such as IDEDiskNotSupported.

    `vim.fault.FileFault <vim/fault/FileFault.rst>`_: 
       if there is an error accessing the virtual machine files.

    `vim.fault.MigrationFault <vim/fault/MigrationFault.rst>`_: 
       if it is not possible to migrate the virtual machine to the destination host. This is typically due to hosts being incompatible, such as mismatch in network polices or access to networks and datastores. Typically, a more specific subclass is thrown.

    `vim.fault.InsufficientResourcesFault <vim/fault/InsufficientResourcesFault.rst>`_: 
       if this operation would violate a resource usage policy.

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if the host cannot run this virtual machine.

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       if the operation is not supported by the current agent.


ExportVm():
   Obtains an export lease on this virtual machine. The export lease contains a list of URLs for the virtual disks for this virtual machine, as well as a ticket giving access to the URLs.See `HttpNfcLease <vim/HttpNfcLease.rst>`_ for information on how to use the lease.
  since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_


  Privilege:
               VApp.Export



  Args:


  Returns:
    `vim.HttpNfcLease <vim/HttpNfcLease.rst>`_:
         The export lease on this `VirtualMachine <vim/VirtualMachine.rst>`_ . The export task continues running until the lease is completed by the caller.

  Raises:

    `vim.fault.InvalidPowerState <vim/fault/InvalidPowerState.rst>`_: 
       if the virtual machine is powered on.

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if the virtual machine is busy.

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the operation cannot be performed because of the virtual machine's current state. For example, if the virtual machine configuration information is not available.

    `vim.fault.FileFault <vim/fault/FileFault.rst>`_: 
       if there is an error accessing the virtual machine files.


MarkAsTemplate():
   Marks a VirtualMachine object as being used as a template. Note: A VirtualMachine marked as a template cannot be powered on.


  Privilege:
               VirtualMachine.Provisioning.MarkAsTemplate



  Args:


  Returns:
    None
         

  Raises:

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the operation cannot be performed because of the virtual machine's current state. For example, if the virtual machine configuration information is not available.

    `vim.fault.VmConfigFault <vim/fault/VmConfigFault.rst>`_: 
       if the template is incompatible with the host, such as the files are not accessible.

    `vim.fault.FileFault <vim/fault/FileFault.rst>`_: 
       if there is an error accessing the virtual machine files.

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       if marking a virtual machine as a template is not supported.

    `vim.fault.InvalidPowerState <vim/fault/InvalidPowerState.rst>`_: 
       if the virtual machine is not powered off.


MarkAsVirtualMachine(pool, host):
   Clears the 'isTemplate' flag and reassociates the virtual machine with a resource pool and host.


  Privilege:
               VirtualMachine.Provisioning.MarkAsVM



  Args:
    pool (`vim.ResourcePool <vim/ResourcePool.rst>`_):
       Resource pool to associate with the virtual machine.


    host (`vim.HostSystem <vim/HostSystem.rst>`_, optional):
       The target host on which the virtual machine is intended to run. The host parameter must specify a host that is a member of the ComputeResource indirectly specified by the pool. For a stand-alone host or a cluster with DRS, it can be omitted and the system selects a default.




  Returns:
    None
         

  Raises:

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the virtual machine is not marked as a template.

    `vim.fault.InvalidDatastore <vim/fault/InvalidDatastore.rst>`_: 
       if the operation cannot be performed on the target datastores.

    `vim.fault.VmConfigFault <vim/fault/VmConfigFault.rst>`_: 
       if the virtual machine is not compatible with the host. For example, a DisksNotSupported fault if the destination host does not support the disk backings of the template.

    `vim.fault.FileFault <vim/fault/FileFault.rst>`_: 
       if there is an error accessing the virtual machine files.

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       if marking a template as a virtual machine is not supported.


UnregisterVM():
   Removes this virtual machine from the inventory without removing any of the virtual machine's files on disk. All high-level information stored with the management server (ESX Server or VirtualCenter) is removed, including information such as statistics, resource pool association, permissions, and alarms.Use the Folder.RegisterVM method to recreate a VirtualMachine object from the set of virtual machine files by passing in the path to the configuration file. However, the VirtualMachine managed object that results typically has different objects ID and may inherit a different set of permissions.


  Privilege:
               VirtualMachine.Inventory.Unregister



  Args:


  Returns:
    None
         

  Raises:

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if the virtual machine is busy.

    `vim.fault.InvalidPowerState <vim/fault/InvalidPowerState.rst>`_: 
       if the virtual machine is powered on.


ResetGuestInformation():
   Clears cached guest information. Guest information can be cleared only if the virtual machine is powered off.This method can be useful if stale information is cached, preventing an IP address or MAC address from being reused.


  Privilege:
               VirtualMachine.Config.ResetGuestInfo



  Args:


  Returns:
    None
         

  Raises:

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the virtual machine is not powered off.

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       if the virtual machine is marked as a template.


MountToolsInstaller():
   Mounts the VMware Tools CD installer as a CD-ROM for the guest operating system. To monitor the status of the tools install, clients should check the tools status, `toolsVersionStatus <vim/vm/GuestInfo.rst#toolsVersionStatus>`_ and `toolsRunningStatus <vim/vm/GuestInfo.rst#toolsRunningStatus>`_ 


  Privilege:
               VirtualMachine.Interact.ToolsInstall



  Args:


  Returns:
    None
         

  Raises:

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the virtual machine is not running, or the VMware Tools CD is already mounted.

    `vim.fault.VmConfigFault <vim/fault/VmConfigFault.rst>`_: 
       vim.fault.VmConfigFault

    `vim.fault.VmToolsUpgradeFault <vim/fault/VmToolsUpgradeFault.rst>`_: 
       if the VMware Tools CD failed to mount.


UnmountToolsInstaller():
   Unmounts VMware Tools installer CD.


  Privilege:
               VirtualMachine.Interact.ToolsInstall



  Args:


  Returns:
    None
         

  Raises:

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the virtual machine is not running, VMware Tools is not running or the VMware Tools CD is already mounted.

    `vim.fault.VmConfigFault <vim/fault/VmConfigFault.rst>`_: 
       vim.fault.VmConfigFault


UpgradeTools(installerOptions):
   Begins the tools upgrade process. To monitor the status of the tools install, clients should check the tools status, `toolsVersionStatus <vim/vm/GuestInfo.rst#toolsVersionStatus>`_ and `toolsRunningStatus <vim/vm/GuestInfo.rst#toolsRunningStatus>`_ .


  Privilege:
               VirtualMachine.Interact.ToolsInstall



  Args:
    installerOptions (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       Command line options passed to the installer to modify the installation procedure for tools.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the virtual machine is not running or is suspended.

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if an upgrade is already taking place.

    `vim.fault.VmToolsUpgradeFault <vim/fault/VmToolsUpgradeFault.rst>`_: 
       if the upgrade failed.

    `vim.fault.ToolsUnavailable <vim/fault/ToolsUnavailable.rst>`_: 
       if VMware Tools is not running.

    `vim.fault.VmConfigFault <vim/fault/VmConfigFault.rst>`_: 
       vim.fault.VmConfigFault

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       if upgrading tools is not supported.


AcquireMksTicket():
   Creates and returns a one-time credential used in establishing a remote mouse-keyboard-screen connection to this virtual machine. The correct function of this method depends on being able to retrieve TCP binding information about the server end of the client connection that is requesting the ticket. If such information is not available, the NotSupported fault is thrown. This method is appropriate for SOAP and authenticated connections, which are both TCP-based connections.


  Privilege:
               VirtualMachine.Interact.ConsoleInteract



  Args:


  Returns:
    `vim.VirtualMachine.MksTicket <vim/VirtualMachine/MksTicket.rst>`_:
         A one-time credential used in establishing a remote mouse-keyboard-screen connection.

  Raises:

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       if it cannot retrieve TCP binding information about the client connection. For example, TCP binding information is not available for a client connection that is not TCP-based.


AcquireTicket(ticketType):
   Creates and returns a one-time credential used in establishing a specific connection to this virtual machine, for example, a ticket type of mks can be used to establish a remote mouse-keyboard-screen connection.A client using this ticketing mechanism must have network connectivity to the ESX server where the virtual machine is running, and the ESX server must be reachable to the management client from the address made available to the client via the ticket.Acquiring a virtual machine ticket requires different privileges depending on the types of ticket:
    * VirtualMachine.Interact.DeviceConnection if requesting a device ticket.
    * VirtualMachine.Interact.GuestControl if requesting a guestControl ticket.
    * VirtualMachine.Interact.ConsoleInteract if requesting an mks ticket.
  since: `vSphere API 4.1 <vim/version.rst#vimversionversion6>`_


  Privilege:
               dynamic



  Args:
    ticketType (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The type of service to acquire, the set of possible values is described in `VirtualMachineTicketType <vim/VirtualMachine/TicketType.rst>`_ .




  Returns:
    `vim.VirtualMachine.Ticket <vim/VirtualMachine/Ticket.rst>`_:
         A one-time credential used in establishing a remote connection to this virtual machine.

  Raises:

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the virtual machine is not connected.


SetScreenResolution(width, height):
   Sets the console window's resolution as specified.


  Privilege:
               VirtualMachine.Interact.ConsoleInteract



  Args:
    width (`int <https://docs.python.org/2/library/stdtypes.html>`_):
       The screen width that should be set.


    height (`int <https://docs.python.org/2/library/stdtypes.html>`_):
       The screen height that should be set.




  Returns:
    None
         

  Raises:

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the virtual machine is not connected.

    `vim.fault.ToolsUnavailable <vim/fault/ToolsUnavailable.rst>`_: 
       if VMware Tools is not running.

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       if the Guest Operating system does not support setting the screen resolution.

    `vim.fault.InvalidPowerState <vim/fault/InvalidPowerState.rst>`_: 
       if the power state is not poweredOn.


DefragmentAllDisks():
   Defragment all virtual disks attached to this virtual machine.
  since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_


  Privilege:
               VirtualMachine.Interact.DefragmentAllDisks



  Args:


  Returns:
    None
         

  Raises:

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the virtual machine is not connected.

    `vim.fault.InvalidPowerState <vim/fault/InvalidPowerState.rst>`_: 
       if the virtual machine is poweredOn.

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if the virtual machine is busy.

    `vim.fault.FileFault <vim/fault/FileFault.rst>`_: 
       if there is an error accessing the disk files.


CreateSecondaryVM(host):
   Creates a secondary virtual machine to be part of this fault tolerant group.If a host is specified, the secondary virtual machine will be created on it. Otherwise, a host will be selected by the system.If a FaultToleranceConfigSpec is specified, the virtual machine's configuration files and disks will be created in the specified datastores.If the primary virtual machine (i.e., this virtual machine) is powered on when the secondary is created, an attempt will be made to power on the secondary on a system selected host. If the cluster is a DRS cluster, DRS will be invoked to obtain a placement for the new secondary virtual machine. If the DRS recommendation (see `ClusterRecommendation <vim/cluster/Recommendation.rst>`_ ) is automatic, it will be automatically executed. Otherwise, the recommendation will be returned to the caller of this method and the secondary will remain powered off until the recommendation is approved using `ApplyRecommendation <vim/ClusterComputeResource.rst#applyRecommendation>`_ . Failure to power on the secondary virtual machine will not fail the creation of the secondary.
  since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_


  Privilege:
               VirtualMachine.Interact.CreateSecondary



  Args:
    host (`vim.HostSystem <vim/HostSystem.rst>`_, optional):
       The host where the secondary virtual machine is to be created and powered on. If no host is specified, a compatible host will be selected by the system. If a host cannot be found for the secondary or the specified host is not suitable, the secondary will not be created and a fault will be returned.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if the virtual machine is busy.

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the virtual machine's configuration information is not available.

    `vim.fault.InsufficientResourcesFault <vim/fault/InsufficientResourcesFault.rst>`_: 
       if this operation would violate a resource usage policy.

    `vim.fault.VmFaultToleranceIssue <vim/fault/VmFaultToleranceIssue.rst>`_: 
       if any error is encountered with the fault tolerance configuration of the virtual machine. Typically, a more specific fault like FaultToleranceNotLicensed is thrown.

    `vim.fault.FileFault <vim/fault/FileFault.rst>`_: 
       if there is a problem accessing the virtual machine on the filesystem.

    `vim.fault.VmConfigFault <vim/fault/VmConfigFault.rst>`_: 
       if a configuration issue prevents creating the secondary. Typically, a more specific fault such as VmConfigIncompatibleForFaultTolerance is thrown.

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       if the virtual machine is marked as a template, or it is not in a vSphere HA enabled cluster.

    `vmodl.fault.ManagedObjectNotFound <vmodl/fault/ManagedObjectNotFound.rst>`_: 
       if a host is specified and it does not exist.


TurnOffFaultToleranceForVM():
   Removes all secondary virtual machines associated with the fault tolerant group and turns off protection for this virtual machine. This operation can only be invoked from the primary virtual machine in the group.
  since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_


  Privilege:
               VirtualMachine.Interact.TurnOffFaultTolerance



  Args:


  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if the virtual machine is busy.

    `vim.fault.VmFaultToleranceIssue <vim/fault/VmFaultToleranceIssue.rst>`_: 
       if any error is encountered with the fault tolerance configuration of the virtual machine. Typically, a more specific fault like InvalidOperationOnSecondaryVm is thrown.

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the host is in maintenance mode or if the virtual machine's configuration information is not available.


MakePrimaryVM(vm):
   Makes the specified secondary virtual machine from this fault tolerant group as the primary virtual machine.
  since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_


  Privilege:
               VirtualMachine.Interact.MakePrimary



  Args:
    vm (`vim.VirtualMachine <vim/VirtualMachine.rst>`_):
       The secondary virtual machine specified will be made the primary virtual machine. This field must specify a secondary virtual machine that is part of the fault tolerant group that this virtual machine is currently associated with. It can only be invoked from the primary virtual machine in the group.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if the virtual machine is busy.

    `vim.fault.VmFaultToleranceIssue <vim/fault/VmFaultToleranceIssue.rst>`_: 
       if any error is encountered with the fault tolerance configuration of the virtual machine. Typically, a more specific fault like InvalidOperationOnSecondaryVm is thrown.

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the host is in maintenance mode or if the virtual machine's configuration information is not available.


TerminateFaultTolerantVM(vm):
   Terminates the specified secondary virtual machine in a fault tolerant group. This can be used to test fault tolerance on a given virtual machine, and should be used with care.
  since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_


  Privilege:
               VirtualMachine.Interact.TerminateFaultTolerantVM



  Args:
    vm (`vim.VirtualMachine <vim/VirtualMachine.rst>`_, optional):
       The secondary virtual machine specified will be terminated, allowing fault tolerance to activate. If no virtual machine is specified, all secondary virtual machines will be terminated. If vm is a primary, InvalidArgument exception is thrown. This field must specify a virtual machine that is part of the fault tolerant group that this virtual machine is currently associated with. It can only be invoked from the primary virtual machine in the group. If the primary virtual machine is terminated, an available secondary virtual machine will be promoted to primary. If no secondary exists, an exception will be thrown and the primary virtual machine will not be terminated. If a secondary virtual machine is terminated, it may be respawned on a potentially different host.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if the virtual machine is busy.

    `vim.fault.VmFaultToleranceIssue <vim/fault/VmFaultToleranceIssue.rst>`_: 
       if any error is encountered with the fault tolerance configuration of the virtual machine. Typically, a more specific fault like InvalidOperationOnSecondaryVm is thrown.

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the host is in maintenance mode or if the virtual machine's configuration information is not available.


DisableSecondaryVM(vm):
   Disables the specified secondary virtual machine in this fault tolerant group. The specified secondary will not be automatically started on a subsequent power-on of the primary virtual machine. This operation could leave the primary virtual machine in a non-fault tolerant state.
  since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_


  Privilege:
               VirtualMachine.Interact.DisableSecondary



  Args:
    vm (`vim.VirtualMachine <vim/VirtualMachine.rst>`_):
       The secondary virtual machine specified will be disabed. This field must specify a secondary virtual machine that is part of the fault tolerant group that this virtual machine is currently associated with. It can only be invoked from the primary virtual machine in the group.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if the virtual machine is busy.

    `vim.fault.VmFaultToleranceIssue <vim/fault/VmFaultToleranceIssue.rst>`_: 
       if any error is encountered with the fault tolerance configuration of the virtual machine. Typically, a more specific fault like InvalidOperationOnSecondaryVm is thrown.

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the host is in maintenance mode or if the virtual machine's configuration information is not available.


EnableSecondaryVM(vm, host):
   Enables the specified secondary virtual machine in this fault tolerant group.This operation is used to enable a secondary virtual machine that was previously disabled by the `DisableSecondaryVM_Task <vim/VirtualMachine.rst#disableSecondary>`_ call. The specified secondary will be automatically started whenever the primary is powered on.If the primary virtual machine (i.e., this virtual machine) is powered on when the secondary is enabled, an attempt will be made to power on the secondary. If a host was specified in the method call, this host will be used. If a host is not specified, one will be selected by the system. In the latter case, if the cluster is a DRS cluster, DRS will be invoked to obtain a placement for the new secondary virtual machine. If the DRS recommendation (see `ClusterRecommendation <vim/cluster/Recommendation.rst>`_ ) is automatic, it will be executed. Otherwise, the recommendation will be returned to the caller of this method and the secondary will remain powered off until the recommendation is approved using `ApplyRecommendation <vim/ClusterComputeResource.rst#applyRecommendation>`_ .
  since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_


  Privilege:
               VirtualMachine.Interact.EnableSecondary



  Args:
    vm (`vim.VirtualMachine <vim/VirtualMachine.rst>`_):
       The secondary virtual machine specified will be enabled. This field must specify a secondary virtual machine that is part of the fault tolerant group that this virtual machine is currently associated with. It can only be invoked from the primary virtual machine in the group.


    host (`vim.HostSystem <vim/HostSystem.rst>`_, optional):
       The host on which the secondary virtual machine is to be enabled and possibly powered on. If no host is specified, a compatible host will be selected by the system. If the secondary virtual machine is not compatible with the specified host, the secondary will not be re-enabled and a fault will be returned.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if the virtual machine is busy.

    `vim.fault.VmFaultToleranceIssue <vim/fault/VmFaultToleranceIssue.rst>`_: 
       if any error is encountered with the fault tolerance configuration of the virtual machine. Typically, a more specific fault like InvalidOperationOnSecondaryVm is thrown.

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the virtual machine's configuration information is not available, if the secondary virtual machine is not disabled, or if a power-on is attempted and one is already in progress.

    `vim.fault.VmConfigFault <vim/fault/VmConfigFault.rst>`_: 
       if a configuration issue prevents enabling the secondary. Typically, a more specific fault such as VmConfigIncompatibleForFaultTolerance is thrown.

    `vmodl.fault.ManagedObjectNotFound <vmodl/fault/ManagedObjectNotFound.rst>`_: 
       if a host is specified and it does not exist.


SetDisplayTopology(displays):
   Sets the console window's display topology as specified.
  since: `vSphere API 4.0 <vim/version.rst#vimversionversion4>`_


  Privilege:
               VirtualMachine.Interact.ConsoleInteract



  Args:
    displays (`vim.VirtualMachine.DisplayTopology <vim/VirtualMachine/DisplayTopology.rst>`_):
       The topology for each monitor that the virtual machine's display must span.




  Returns:
    None
         

  Raises:

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the virtual machine is not connected.

    `vim.fault.ToolsUnavailable <vim/fault/ToolsUnavailable.rst>`_: 
       if VMware Tools is not running.

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       if the Guest Operating system does not support setting the display topology

    `vim.fault.InvalidPowerState <vim/fault/InvalidPowerState.rst>`_: 
       if the power state is not poweredOn.


StartRecording(name, description):
   Initiates a recording session on this virtual machine. As a side effect, this operation creates a snapshot on the virtual machine, which in turn becomes the current snapshot.This is an experimental interface that is not intended for use in production code.
  since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_


  Privilege:
               VirtualMachine.Interact.Record



  Args:
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The name for the snapshot associated with this recording. The name need not be unique for this virtual machine.


    description (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       A description for the snapshot associated with this recording. If omitted, a default description may be provided.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         the newly created Snapshot associated with this recording.

  Raises:

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the operation cannot be performed because of the virtual machine's current state. For example, the virtual machine configuration information is not available.

    `vim.fault.InvalidPowerState <vim/fault/InvalidPowerState.rst>`_: 
       if the operation cannot be performed in the current power state of the virtual machine.

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if the virtual machine is busy.

    `vim.fault.FileFault <vim/fault/FileFault.rst>`_: 
       if there is a problem with creating or accessing one or more files needed for this operation.

    `vim.fault.SnapshotFault <vim/fault/SnapshotFault.rst>`_: 
       if an error occurs during the snapshot operation. Typically, a more specific fault like MultipleSnapshotsNotSupported is thrown.

    `vim.fault.VmConfigFault <vim/fault/VmConfigFault.rst>`_: 
       vim.fault.VmConfigFault

    `vim.fault.RecordReplayDisabled <vim/fault/RecordReplayDisabled.rst>`_: 
       if the record/replay config flag has not been enabled for this virtual machine.

    `vim.fault.HostIncompatibleForRecordReplay <vim/fault/HostIncompatibleForRecordReplay.rst>`_: 
       if the virtual machine is located on a host that does not support record/replay.

    `vim.fault.InvalidName <vim/fault/InvalidName.rst>`_: 
       if the specified snapshot name is invalid.

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       if the host product does not support record functionality or if the virtual machine does not support this

    `vim.fault.VmConfigIncompatibleForRecordReplay <vim/fault/VmConfigIncompatibleForRecordReplay.rst>`_: 
       if the virtual machine configuration is incompatible for recording.


StopRecording():
   Stops a currently active recording session on this virtual machine.This is an experimental interface that is not intended for use in production code.
  since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_


  Privilege:
               VirtualMachine.Interact.Record



  Args:


  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the operation cannot be performed because of the virtual machine's current state. For example, the virtual machine does not have an active recording session.

    `vim.fault.InvalidPowerState <vim/fault/InvalidPowerState.rst>`_: 
       if the operation cannot be performed in the current power state of the virtual machine.

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if the virtual machine is busy.

    `vim.fault.FileFault <vim/fault/FileFault.rst>`_: 
       if there is a problem with creating or accessing one or more files needed for this operation.

    `vim.fault.SnapshotFault <vim/fault/SnapshotFault.rst>`_: 
       if an error occurs during the snapshot operation. Typically, a more specific fault like InvalidSnapshotFormat is thrown.

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       if the host product does not support record/replay functionality or if the virtual machine does not support this capability.


StartReplaying(replaySnapshot):
   Starts a replay session on this virtual machine. As a side effect, this operation updates the current snapshot of the virtual machine.This is an experimental interface that is not intended for use in production code.
  since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_


  Privilege:
               VirtualMachine.Interact.Replay



  Args:
    replaySnapshot (`vim.vm.Snapshot <vim/vm/Snapshot.rst>`_):
       The snapshot from which to start the replay. This snapshot must have been created by a record operation on the virtual machine.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the operation cannot be performed because of the virtual machine's current state. For example, the virtual machine configuration information is not available.

    `vim.fault.InvalidPowerState <vim/fault/InvalidPowerState.rst>`_: 
       if the operation cannot be performed in the current power state of the virtual machine.

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if the virtual machine is busy.

    `vim.fault.FileFault <vim/fault/FileFault.rst>`_: 
       if there is a problem with creating or accessing one or more files needed for this operation.

    `vim.fault.SnapshotFault <vim/fault/SnapshotFault.rst>`_: 
       if an error occurs during the snapshot operation. Typically, a more specific fault like InvalidSnapshotFormat is thrown.

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       if replaySnapshot is no longer present.

    `vim.fault.VmConfigFault <vim/fault/VmConfigFault.rst>`_: 
       vim.fault.VmConfigFault

    `vim.fault.RecordReplayDisabled <vim/fault/RecordReplayDisabled.rst>`_: 
       if the record/replay config flag has not been enabled for this virtual machine.

    `vim.fault.HostIncompatibleForRecordReplay <vim/fault/HostIncompatibleForRecordReplay.rst>`_: 
       if the virtual machine is located on a host that does not support record/replay.

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       if the host product does not support record/replay functionality or if the virtual machine does not support this capability.

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if replaySnapshot is not a valid snapshot associated with a recorded session on this virtual machine.

    `vim.fault.VmConfigIncompatibleForRecordReplay <vim/fault/VmConfigIncompatibleForRecordReplay.rst>`_: 
       if the virtual machine configuration is incompatible for replaying.


StopReplaying():
   Stops a replay session on this virtual machine.This is an experimental interface that is not intended for use in production code.
  since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_


  Privilege:
               VirtualMachine.Interact.Replay



  Args:


  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the operation cannot be performed because of the virtual machine's current state. For example, the virtual machine does not have an active recording session.

    `vim.fault.InvalidPowerState <vim/fault/InvalidPowerState.rst>`_: 
       if the operation cannot be performed in the current power state of the virtual machine.

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if the virtual machine is busy.

    `vim.fault.FileFault <vim/fault/FileFault.rst>`_: 
       if there is a problem with creating or accessing one or more files needed for this operation.

    `vim.fault.SnapshotFault <vim/fault/SnapshotFault.rst>`_: 
       if an error occurs during the snapshot operation. Typically, a more specific fault like InvalidSnapshotFormat is thrown.

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       if the host product does not support record/replay functionality or if the virtual machine does not support this capability.


PromoteDisks(unlink, disks):
   Promotes disks on this virtual machine that have delta disk backings.A delta disk backing is a way to preserve a virtual disk backing at some point in time. A delta disk backing is a file backing which in turn points to the original virtual disk backing (the parent). After a delta disk backing is added, all writes go to the delta disk backing. All reads first try the delta disk backing and then try the parent backing if needed.Promoting does two things
    * If the unlink parameter is true, any disk backing which is shared shared by multiple virtual machines is copied so that this virtual machine has its own unshared version. Copied files always end up in the virtual machine's home directory.
    * Any disk backing which is not shared between multiple virtual machines and is not associated with a snapshot is consolidated with its child backing.If the unlink parameter is true, the net effect of this operation is improved read performance, at the cost of disk space. If the unlink parameter is false the net effect is improved read performance at the cost of inhibiting future sharing.This operation is only supported if `deltaDiskBackingsSupported <vim/host/Capability.rst#deltaDiskBackingsSupported>`_ is true.This operation is only supported on VirtualCenter.
  since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_


  Privilege:
               VirtualMachine.Provisioning.PromoteDisks



  Args:
    unlink (`bool <https://docs.python.org/2/library/stdtypes.html>`_):
       If true, then these disks will be unlinked before consolidation.


    disks (`vim.vm.device.VirtualDisk <vim/vm/device/VirtualDisk.rst>`_, optional):
       The set of disks that are to be promoted. If this value is unset or the array is empty, all disks which have delta disk backings are promoted.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the virtual machine is not ready to respond to such requests.

    `vim.fault.InvalidPowerState <vim/fault/InvalidPowerState.rst>`_: 
       if the virtual machine is not powered off or suspended

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if the virtual machine is busy.

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       if the host doesnt support disk promotion APIs.


CreateScreenshot():
   Create a screen shot of a virtual machine.
  since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_


  Privilege:
               VirtualMachine.Interact.CreateScreenshot



  Args:


  Returns:
     `vim.Task <vim/Task.rst>`_:
         Returns the datastore path of the created screen shot.

  Raises:

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if the virtual machine is busy.

    `vim.fault.FileFault <vim/fault/FileFault.rst>`_: 
       if there is a problem with creating or accessing one or more files needed for this operation.

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the virtual machine is not ready to respond to such requests.

    `vim.fault.InvalidPowerState <vim/fault/InvalidPowerState.rst>`_: 
       if the virtual machine is not powered on.


QueryChangedDiskAreas(snapshot, deviceKey, startOffset, changeId):
   Get a list of areas of a virtual disk belonging to this VM that have been modified since a well-defined point in the past. The beginning of the change interval is identified by "changeId", while the end of the change interval is implied by the snapshot ID passed in.Note that the result of this function may contain "false positives" (i.e: flag areas of the disk as modified that are not). However, it is guaranteed that no changes will be missed.
  since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_


  Privilege:
               VirtualMachine.Provisioning.DiskRandomRead



  Args:
    snapshot (`vim.vm.Snapshot <vim/vm/Snapshot.rst>`_, optional):
       Snapshot for which changes that have been made sine "changeId" should be computed. If not set, changes are computed against the "current" snapshot of the virtual machine. However, using the "current" snapshot will only work for virtual machines that are powered off.


    deviceKey (`int <https://docs.python.org/2/library/stdtypes.html>`_):
       Identifies the virtual disk for which to compute changes.


    startOffset (`long <https://docs.python.org/2/library/stdtypes.html>`_):
       Start Offset in bytes at which to start computing changes. Typically, callers will make multiple calls to this function, starting with startOffset 0 and then examine the "length" property in the returned DiskChangeInfo structure, repeatedly calling queryChangedDiskAreas until a map forthe entire virtual disk has been obtained.


    changeId (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       Identifyer referring to a point in the past that should be used as the point in time at which to begin including changes to the disk in the result. A typical use case would be a backup application obtaining a changeId from a virtual disk's backing info when performing a backup. When a subsequent incremental backup is to be performed, this change Id can be used to obtain a list of changed areas on disk.




  Returns:
    `vim.VirtualMachine.DiskChangeInfo <vim/VirtualMachine/DiskChangeInfo.rst>`_:
         Returns a data structure specifying extents of the virtual disk that have changed since the thime the changeId string was obtained.

  Raises:

    `vim.fault.FileFault <vim/fault/FileFault.rst>`_: 
       if the virtual disk files cannot be accessed/queried.

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       if the snapshot specified does not exist.

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if deviceKey does not specify a virtual disk, startOffset is beyond the end of the virtual disk or changeId is invalid or change tracking is not supported for this particular disk.


QueryUnownedFiles():
   For all files that belong to the vm, check that the file owner is set to the current datastore principal user, as set by `HostDatastoreSystem.ConfigureDatastorePrincipal <vim/host/DatastoreSystem.rst#configureDatastorePrincipal>`_ 
  since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_


  Privilege:
               VirtualMachine.Config.QueryUnownedFiles



  Args:


  Returns:
    [`str <https://docs.python.org/2/library/stdtypes.html>`_]:
         The list of file paths for vm files whose ownership is not correct. Use `FileManager.ChangeOwner <vim/FileManager.rst#changeOwner>`_ to set the file ownership.


reloadVirtualMachineFromPath(configurationPath):
   Reloads the configuration for this virtual machine from a given datastore path. This is equivalent to unregistering and registering the virtual machine from a different path. The virtual machine's hardware configuration, snapshots, guestinfo variables etc. will be replaced based on the new configuration file. Other information associated with the virtual machine object, such as events and permissions, will be preserved.This method is only supported on vCenter Server. It can be invoked on inaccessible or orphaned virtual machines, but it cannot be invoked on powered on, connected virtual machines. Both the source virtual machine object and the destination path should be of the same type i.e. virtual machine or template. Reloading a virtual machine with a template or vice-versa is not supported.Note:Since the API replaces the source configuration with that of the destination, if the destination configuration does not refer to a valid virtual machine, it will create an invalid virtual machine object. This API should not be invoked on fault tolerant virtual machines since doing so will leave the original virtual machine's configuration in an invalid state. It is recommended that you turn off fault tolerance before invoking this API.
  since: `vSphere API 4.1 <vim/version.rst#vimversionversion6>`_


  Privilege:
               VirtualMachine.Config.ReloadFromPath



  Args:
    configurationPath (`str <https://docs.python.org/2/library/stdtypes.html>`_):




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.InvalidPowerState <vim/fault/InvalidPowerState.rst>`_: 
       if the virtual machine is powered on.

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if the virtual machine is busy.

    `vim.fault.FileFault <vim/fault/FileFault.rst>`_: 
       if there is a problem creating or accessing the files needed for this operation.

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the virtual machine is busy or not ready to respond to such requests.

    `vim.fault.VmConfigFault <vim/fault/VmConfigFault.rst>`_: 
       if the format / configuration of the virtual machine is invalid. Typically, a more specific fault is thrown such as InvalidFormat if the configuration file cannot be read, or InvalidDiskFormat if the disks cannot be read.

    `vim.fault.AlreadyExists <vim/fault/AlreadyExists.rst>`_: 
       if the virtual machine is already registered.

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       if invoked on ESX server or if invoked on a virtual machine with the destination path for a template and vice-versa.


QueryFaultToleranceCompatibility():
   This API can be invoked to determine whether a virtual machine is compatible for Fault Tolerance. The API only checks for VM-specific factors that impact compatibility for Fault Tolerance. Other requirements for Fault Tolerance such as host processor compatibility, logging nic configuration and licensing are not covered by this API. The query returns a list of faults, each fault corresponding to a specific incompatibility. If a given virtual machine is compatible for Fault Tolerance, then the fault list returned will be empty.
  since: `vSphere API 4.1 <vim/version.rst#vimversionversion6>`_


  Privilege:
               VirtualMachine.Config.QueryFTCompatibility



  Args:


  Returns:
    [`vmodl.MethodFault <vmodl/MethodFault.rst>`_]:
         

  Raises:

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the operation cannot be performed because of the virtual machine's current state.

    `vim.fault.VmConfigFault <vim/fault/VmConfigFault.rst>`_: 
       if the virtual machine's configuration is invalid.

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       if the virtual machine is a template or this operation is not supported.


TerminateVM():
   Do an immediate power off of a VM.This API issues a SIGKILL to the vmx process of the VM. Pending synchronous I/Os may not be written out before the vmx process dies depending on accessibility of the datastore.
  since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_


  Privilege:
               VirtualMachine.Interact.PowerOff



  Args:


  Returns:
    None
         

  Raises:

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the VM is not powered on or another issue prevents the operation from being performed.

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if the virtual machine is busy.

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       if this operation is not supported.


