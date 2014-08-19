
vim.host.StorageSystem
======================
  This managed object gets and sets configuration information about the host's storage subsystem. The properties and operations are used to configure the host to make storage available for virtual machines. This object contains properties that are specific to ESX Server and general to both the ESX Server system and the hosted architecture.


:extends: vim.ExtensibleManagedObject_


Attributes
----------
    storageDeviceInfo (`vim.host.StorageDeviceInfo <vim/host/StorageDeviceInfo.rst>`_):
       Host storage information up to the device level.
    fileSystemVolumeInfo (`vim.host.FileSystemVolumeInfo <vim/host/FileSystemVolumeInfo.rst>`_):
       File system volume information for the host. See the `FileSystemVolumeInfo <vim/host/FileSystemVolumeInfo.rst>`_ data object type for more information.
    systemFile ([`str <https://docs.python.org/2/library/stdtypes.html>`_]):
       Datastore paths of files used by the host system on mounted volumes, for instance, the COS vmdk file of the host. For information on datastore paths, see `Datastore <vim/Datastore.rst>`_ .
    multipathStateInfo (`vim.host.MultipathStateInfo <vim/host/MultipathStateInfo.rst>`_):
       Runtime information about the state of a multipath path. A null value will be returned if path state information is not available for this system.In systems prior to the plug-store architecture, the state of a path may be accessible on the `HostMultipathInfo <vim/host/MultipathInfo.rst>`_ data object of the `storageDeviceInfo <vim/host/StorageSystem.rst#storageDeviceInfo>`_ property.


Methods
-------


RetrieveDiskPartitionInfo(devicePath):
   Gets the partition information for the disks named by the device names.


  Privilege:
               System.Read



  Args:
    devicePath (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       An array of device path names that identify disks. See `ScsiDisk <vim/host/ScsiDisk.rst>`_ .




  Returns:
    [`vim.host.DiskPartitionInfo <vim/host/DiskPartitionInfo.rst>`_]:
         An array of information about the partitions.


ComputeDiskPartitionInfo(devicePath, layout, partitionFormat):
   Computes the disk partition information given the desired disk layout. The server computes a new partition information object for a specific disk representing the desired layout.See `HostDiskPartitionInfoPartitionFormat <vim/host/DiskPartitionInfo/PartitionFormat.rst>`_ 


  Privilege:
               Host.Config.Storage



  Args:
    devicePath (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The name of the device path for the specific disk.See `HostDiskPartitionInfoPartitionFormat <vim/host/DiskPartitionInfo/PartitionFormat.rst>`_ 


    layout (`vim.host.DiskPartitionInfo.Layout <vim/host/DiskPartitionInfo/Layout.rst>`_):
       A data object that describes the disk partition layout.See `HostDiskPartitionInfoPartitionFormat <vim/host/DiskPartitionInfo/PartitionFormat.rst>`_ 


    partitionFormat (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional, since `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_ ):
       Specifies the desired partition format to be computed from the block range. If partitionFormat is not specified, the existing partitionFormat on disk is used, if the disk is not blank and mbr otherwise.See `HostDiskPartitionInfoPartitionFormat <vim/host/DiskPartitionInfo/PartitionFormat.rst>`_ 




  Returns:
    `vim.host.DiskPartitionInfo <vim/host/DiskPartitionInfo.rst>`_:
         A data object that contains information about the partitions on a disk

  Raises:

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       if the device could not be found.See `HostDiskPartitionInfoPartitionFormat <vim/host/DiskPartitionInfo/PartitionFormat.rst>`_ 

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       if unable to get the current partition information for the device.See `HostDiskPartitionInfoPartitionFormat <vim/host/DiskPartitionInfo/PartitionFormat.rst>`_ 

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if the layout is invalid.See `HostDiskPartitionInfoPartitionFormat <vim/host/DiskPartitionInfo/PartitionFormat.rst>`_ 


ComputeDiskPartitionInfoForResize(partition, blockRange, partitionFormat):
   Computes the disk partition information for the purpose of resizing a given partition.See `HostDiskPartitionInfoPartitionFormat <vim/host/DiskPartitionInfo/PartitionFormat.rst>`_ 
  since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_


  Privilege:
               Host.Config.Storage



  Args:
    partition (`vim.host.ScsiDisk.Partition <vim/host/ScsiDisk/Partition.rst>`_):
       The disk partition to resize.See `HostDiskPartitionInfoPartitionFormat <vim/host/DiskPartitionInfo/PartitionFormat.rst>`_ 


    blockRange (`vim.host.DiskPartitionInfo.BlockRange <vim/host/DiskPartitionInfo/BlockRange.rst>`_):
       Specifies the desired block range for the resized partition. The start of the block range specified should match that of the current partition.See `HostDiskPartitionInfoPartitionFormat <vim/host/DiskPartitionInfo/PartitionFormat.rst>`_ 


    partitionFormat (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional, since `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_ ):
       Specifies the desired partition format to be computed from the block range. If partitionFormat is not specified, the existing partitionFormat on disk is used, if the disk is not blank and mbr otherwise.See `HostDiskPartitionInfoPartitionFormat <vim/host/DiskPartitionInfo/PartitionFormat.rst>`_ 




  Returns:
    `vim.host.DiskPartitionInfo <vim/host/DiskPartitionInfo.rst>`_:
         resized disk partition information

  Raises:

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       if the device could not be found.See `HostDiskPartitionInfoPartitionFormat <vim/host/DiskPartitionInfo/PartitionFormat.rst>`_ 

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       if unable to get the current partition information for the device.See `HostDiskPartitionInfoPartitionFormat <vim/host/DiskPartitionInfo/PartitionFormat.rst>`_ 

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if blockRange or partition is invalid.See `HostDiskPartitionInfoPartitionFormat <vim/host/DiskPartitionInfo/PartitionFormat.rst>`_ 


UpdateDiskPartitions(devicePath, spec):
   Changes the partitions on the disk by supplying a partition specification and the device name.


  Privilege:
               Host.Config.Storage



  Args:
    devicePath (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The name of the device path for the specific disk.


    spec (`vim.host.DiskPartitionInfo.Specification <vim/host/DiskPartitionInfo/Specification.rst>`_):
       A data object that describes the disk partition table specification used to configure the partitions on a disk.




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       if the device could not be found.

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       for all other configuration failures.

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if the spec is invalid.


FormatVmfs(createSpec):
   Formats a new VMFS on a disk partition.


  Privilege:
               Host.Config.Storage



  Args:
    createSpec (`vim.host.VmfsVolume.Specification <vim/host/VmfsVolume/Specification.rst>`_):
       A data object that describes the VMware File System (VMFS) creation specification.




  Returns:
    `vim.host.VmfsVolume <vim/host/VmfsVolume.rst>`_:
         A data object that represents the VMFS file system.

  Raises:

    `vim.fault.AlreadyExists <vim/fault/AlreadyExists.rst>`_: 
       if the volume name is already being used by another volume on the host.

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       for all other configuration failures.

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if VMFS version specified is not 2 or 3, if blocksize, lock mode, or volume label are invalid, the partition does not exist or is of an invalid type.


MountVmfsVolume(vmfsUuid):
   Mount the unmounted Vmfs volume. A newly discovered vmfs volume will be mounted unless, it has been explicitly unmounted. The default mount behavior of Vmfs volumes is auto-mount. See `UnmountVmfsVolume <vim/host/StorageSystem.rst#unmountVmfsVolume>`_ .mountVmfsVolume is part of the Unmount / Detach workflow used when a device will be permanently removed. See also `DetachScsiLun <vim/host/StorageSystem.rst#detachScsiLun>`_ .
  since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_


  Privilege:
               Host.Config.Storage



  Args:
    vmfsUuid (`str <https://docs.python.org/2/library/stdtypes.html>`_):




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       if VMFS Uuid is not found on the host.

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if
        * The volume is already mounted.
        * The volume is inaccessible.

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       for all other configuration failures.

    `vim.fault.ResourceInUse <vim/fault/ResourceInUse.rst>`_: 
       vim.fault.ResourceInUse


UnmountVmfsVolume(vmfsUuid):
   Unmount the Vmfs volume. An unmounted volume cannot be used for any filesystem operation requiring I/O. In contrast to removal, this operation does not destroy or alter partitions on which vmfs volumes reside. The mountState will be persisted across filesystem rescans and host reboots. See `MountVmfsVolume <vim/host/StorageSystem.rst#mountVmfsVolume>`_ .unmountVmfsVolume is part of the Unmount / Detach workflow used when a device will be permanently removed.Mounted Vmfs Volume unmountVmfsVolume | ^ mountVmfsVolume V | Unmounted Vmfs Volume Attached Scsi Device (honors I/O) detachScsiLun | ^ attachScsiLun V | Detached Scsi Device (does not honor I/O)It is safe to unprovision a Lun from the Storage array *only* after a Scsi device is detached.The best practice for decommisioning a Lun would be to find out the set of subsystems that a Lun is being used for. Many of the systems are listed as exceptions in the function documentation.One typical workflow could be:
    * Find out if the device is used as a Vmfs Extent. (See VmfsVolume.Extent API)
    * Unmount the Vmfs Volume.
    * Find out if device is used by the Diagnostic system (See Diagnostic System API).
    * Deactivate the diagnostic system, if it is being used.
    * Find out if this device is used to back a VM's RDM (See VirtualMachine API).
    * Remove this device from the VM.
    * Detach the Scsi device.
    * On success, it is safe to decommision the Lun at this point.See also `DetachScsiLun <vim/host/StorageSystem.rst#detachScsiLun>`_ .
  since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_


  Privilege:
               Host.Config.Storage



  Args:
    vmfsUuid (`str <https://docs.python.org/2/library/stdtypes.html>`_):




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       if VMFS Uuid is not found on the host.

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if
        * The volume is already unmounted.
        * The volume is inaccessible.

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       for all other configuration failures.

    `vim.fault.ResourceInUse <vim/fault/ResourceInUse.rst>`_: 
       if
        * There is any VM registered on this volume.
        * 1 or more programs have I/O outstanding on this volume.


DeleteVmfsVolumeState(vmfsUuid):
   For previously unmounted VMFS volume, remove the state information from host. VMFS volumes mount state is maintained by host.deleteVmfsVolumeState is part of the Unmount/Detach workflow used when the device will be permanently removed. See also `UnmountVmfsVolume <vim/host/StorageSystem.rst#unmountVmfsVolume>`_ . If the VMFS volume is unmounted using unmountVmfsVolume, ESX maintains the state of VMFS volume. This API will remove the state from the host. If the underlying storage device is going to be un-provisioned on the array side, please detach the storage device. See also `DetachScsiLun <vim/host/StorageSystem.rst#detachScsiLun>`_ .
  since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_


  Privilege:
               Host.Config.Storage



  Args:
    vmfsUuid (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The VMFS UUID.




  Returns:
    None
         

  Raises:

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       for any configuration failures.


RescanVmfs():
   Rescans for new Virtual Machine File Systems (VMFS). The `RefreshStorageSystem <vim/host/StorageSystem.rst#refresh>`_ method also performs a VMFS rescan. `RescanVmfs <vim/host/StorageSystem.rst#rescanVmfs>`_ may update the `HostSystem <vim/HostSystem.rst>`_ . `config <vim/HostSystem.rst#config>`_ . `fileSystemVolume <vim/host/ConfigInfo.rst#fileSystemVolume>`_ property. The Server performs asynchronous updates to the inventory. Use the `PropertyCollector <vmodl/query/PropertyCollector.rst>`_ . `WaitForUpdatesEx <vmodl/query/PropertyCollector.rst#waitForUpdatesEx>`_ method to obtain the property changes.


  Privilege:
               Host.Config.Storage



  Args:


  Returns:
    None
         

  Raises:

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       if configuration fails.


AttachVmfsExtent(vmfsPath, extent):
   Extends a VMFS by attaching a disk partition as an extent.


  Privilege:
               Host.Config.Storage



  Args:
    vmfsPath (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The path of the VMFS to extend. See `FileSystemMountInfo <vim/host/FileSystemMountInfo.rst>`_ .


    extent (`vim.host.ScsiDisk.Partition <vim/host/ScsiDisk/Partition.rst>`_):
       A data object that describes the specification of a Disk partition.




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       if the VMFS cannot be found or is unmounted.

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       for all other configuration failures.

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if the new extent is already used by another vmfs volume, does not exist, or is of an invalid partition type.


ExpandVmfsExtent(vmfsPath, extent):
   Expands a VMFS extent as specified by the Disk partition specification.
  since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_


  Privilege:
               Host.Config.Storage



  Args:
    vmfsPath (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The path of the VMFS to expand. See `FileSystemMountInfo <vim/host/FileSystemMountInfo.rst>`_ .


    extent (`vim.host.ScsiDisk.Partition <vim/host/ScsiDisk/Partition.rst>`_):
       The disk partition corresponding to the extent to be expanded.




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       if the VMFS cannot be found or is unmounted.

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       for all other configuration failures.

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if the extent is not part of the VMFS volume.


UpgradeVmfs(vmfsPath):
   Upgrades the VMFS to the `latest supported VMFS version <vim/host/Capability.rst#supportedVmfsMajorVersion>`_ .Prerequisite:All hosts that have mounted the volume must support the VMFS version to which the volume will be upgraded.


  Privilege:
               Host.Config.Storage



  Args:
    vmfsPath (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The path of the VMFS.




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       if the VMFS cannot be found or is unmounted.

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       if the prerequisite is not satisfied or for all other configuration failures.


UpgradeVmLayout():
   Iterates over all registered virtual machines. For each VM which .vmx file is located on the service console and all disks are available on VMFS3 or NAS, it will relocate the disks into directories if stored in the ROOT, and relocate the VMX file into the directory too. Events are logged for each virtual machine that is relocated.On ESXi systems, this operation has no effect.


  Privilege:
               Host.Config.Storage



  Args:


  Returns:
    None
         


QueryUnresolvedVmfsVolume():
   Get the list of unbound VMFS volumes. For sharing a volume across hosts, a VMFS volume is bound to its underlying block device storage. When a low level block copy is performed to copy or move the VMFS volume, the copied volume will be unbound.
  since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_


  Privilege:
               System.Read



  Args:


  Returns:
    [`vim.host.UnresolvedVmfsVolume <vim/host/UnresolvedVmfsVolume.rst>`_]:
         An array of unbound VMFS volumes.


ResolveMultipleUnresolvedVmfsVolumes(resolutionSpec):
   Resignature or 'Force Mount' list of unbound VMFS volumes. To safely enable sharing of the volume across hosts, a VMFS volume is bound to its underlying block device storage. When a low level block copy is performed to copy or move the VMFS volume, the copied volume will be unbound. In order for the VMFS volume to be usable, a resolution operation is needed to determine whether the VMFS volume should be treated as a new volume or not and what extents compose that volume in the event there is more than one unbound volume.Resignature results in a new VMFS volume on the host. Operations performed at the StorageSystem interface apply only to a specific host. Hence, callers of this method are responsible for issuing rescan operations to detect the new VMFS volume on other hosts. Alternatively, callers that want VirtualCenter to handle rescanning the necessary hosts should use the DatastoreSystem interface.When user wants to keep the original Vmfs Uuid and mount it on the host, set the 'resolutionSpec.uuidResolution' to 'forceMounted' This is per-host operation. It will return an array of ResolutionResult describing success or failure associated with each specification.
  since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_


  Privilege:
               Host.Config.Storage



  Args:
    resolutionSpec (`vim.host.UnresolvedVmfsResolutionSpec <vim/host/UnresolvedVmfsResolutionSpec.rst>`_):
       List of data object that describes what the disk extents to be used for creating the new VMFS volume.




  Returns:
    [`vim.host.UnresolvedVmfsResolutionResult <vim/host/UnresolvedVmfsResolutionResult.rst>`_]:
         A data object that represents the VMFS file system and return status value.

  Raises:

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       if batch operation fails on the host. Because the returned array of ResolutionResult contains the new VMFS volume or fault for each operation, as of vSphere API 5.x, we won't throw fault when batch operation fails.


ResolveMultipleUnresolvedVmfsVolumesEx(resolutionSpec):
   Resignature or 'Force Mount' list of unbound VMFS volumes.To safely enable sharing of the volume across hosts, a VMFS volume is bound to its underlying block device storage. When a low level block copy is performed to copy or move the VMFS volume, the copied volume will be unbound. In order for the VMFS volume to be usable, a resolution operation is needed to determine whether the VMFS volume should be treated as a new volume or not and what extents compose that volume in the event there is more than one unbound volume.Resignature results in a new VMFS volume on the host. Operations performed at the `HostStorageSystem <vim/host/StorageSystem.rst>`_ interface apply only to a specific host. Hence, callers of this method are responsible for issuing rescan operations to detect the new VMFS volume on other hosts. Alternatively, callers that want VirtualCenter to handle rescanning the necessary hosts should use the `HostDatastoreSystem <vim/host/DatastoreSystem.rst>`_ interface.When user wants to keep the original VMFS UUID and mount it on the host, set the resolutionSpec.uuidResolution ( `uuidResolution <vim/host/UnresolvedVmfsResolutionSpec.rst#uuidResolution>`_ ) to `forceMount <vim/host/UnresolvedVmfsResolutionSpec/VmfsUuidResolution.rst#forceMount>`_ . This is per-host operation.It will return an array of `HostUnresolvedVmfsResolutionResult <vim/host/UnresolvedVmfsResolutionResult.rst>`_ describing success or failure associated with each specification.This method behaves the same as `ResolveMultipleUnresolvedVmfsVolumes <vim/host/StorageSystem.rst#resolveMultipleUnresolvedVmfsVolumes>`_ except that it returns a task to support monitoring the operation. This is important for operations with large number of unresolved volumes which may take potentially dozens of minutes to complete.
  since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_


  Privilege:
               Host.Config.Storage



  Args:
    resolutionSpec (`vim.host.UnresolvedVmfsResolutionSpec <vim/host/UnresolvedVmfsResolutionSpec.rst>`_):
       List of data object that describes what the disk extents to be used for creating the new VMFS volume.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       if batch operation fails on the host. Because the returned array of ResolutionResult contains the new VMFS volume or fault for each operation, as of vSphere API 5.x, we won't throw fault when batch operation fails.


UnmountForceMountedVmfsVolume(vmfsUuid):
   Unmount the 'forceMounted' Vmfs volume. When a low level block copy is performed to copy or move the VMFS volume, the copied volume is unresolved. For the VMFS volume to be usable, a resolution operation is applied. As part of resolution operation, user may decide to keep the original VMFS Uuid. Once the resolution is applied, the VMFS volume is mounted on the host for its use. User can unmount the VMFS volume if it is not being used by any registered VMs.
  since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_


  Privilege:
               Host.Config.Storage



  Args:
    vmfsUuid (`str <https://docs.python.org/2/library/stdtypes.html>`_):




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       if VMFS Uuid is not found on the host.

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       for all other configuration failures.


RescanHba(hbaDevice):
   Issues a request to rescan a specific host bus adapter for new storage devices.


  Privilege:
               Host.Config.Storage



  Args:
    hbaDevice (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The device of the host bus adapter.




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       if the host bus adapter cannot be found.

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       for all other configuration failures.


RescanAllHba():
   Scans all host bus adapters to obtain the current list of devices and device topology. The `RescanAllHba <vim/host/StorageSystem.rst#rescanAllHba>`_ method looks for new devices, removed devices, and path changes.This method may update the following inventory elements:
    * Devices and storage topology (
    * `HostSystem <vim/HostSystem.rst>`_
    * .
    * `config <vim/HostSystem.rst#config>`_
    * .
    * `storageDevice <vim/host/ConfigInfo.rst#storageDevice>`_
    * ).
    * VMFS and NFS datastores (
    * `HostSystem <vim/HostSystem.rst>`_
    * .
    * `datastore <vim/HostSystem.rst#datastore>`_
    * ).
    * File system volumes (
    * `HostSystem <vim/HostSystem.rst>`_
    * .
    * `config <vim/HostSystem.rst#config>`_
    * .
    * `fileSystemVolume <vim/host/ConfigInfo.rst#fileSystemVolume>`_
    * ).The Server performs asynchronous updates to the inventory. Use the `PropertyCollector <vmodl/query/PropertyCollector.rst>`_ . `WaitForUpdatesEx <vmodl/query/PropertyCollector.rst#waitForUpdatesEx>`_ method to obtain the property changes.


  Privilege:
               Host.Config.Storage



  Args:


  Returns:
    None
         

  Raises:

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       if rescan failed.


UpdateSoftwareInternetScsiEnabled(enabled):
   Enables or disables Software iSCSI.


  Privilege:
               Host.Config.Storage



  Args:
    enabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_):
       True to enable the iSCSI; false to disable it




  Returns:
    None
         

  Raises:

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       for any configuration failure.


UpdateInternetScsiDiscoveryProperties(iScsiHbaDevice, discoveryProperties):
   Updates the Discovery properties for an iSCSI host bus adapter.


  Privilege:
               Host.Config.Storage



  Args:
    iScsiHbaDevice (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The device of the Internet SCSI HBA adapter.


    discoveryProperties (`vim.host.InternetScsiHba.DiscoveryProperties <vim/host/InternetScsiHba/DiscoveryProperties.rst>`_):
       The discovery settings for this host bus adapter.




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       if the host bus adapter could not be found.

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       for all other configuration failures.


UpdateInternetScsiAuthenticationProperties(iScsiHbaDevice, authenticationProperties, targetSet):
   Updates the authentication properties for one or more targets or discovery addresses associated with an iSCSI host bus adapter.


  Privilege:
               Host.Config.Storage



  Args:
    iScsiHbaDevice (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The device of the Internet SCSI HBA adapter. associated with the target.


    authenticationProperties (`vim.host.InternetScsiHba.AuthenticationProperties <vim/host/InternetScsiHba/AuthenticationProperties.rst>`_):
       The data object that represents the authentication settings to set.


    targetSet (`vim.host.InternetScsiHba.TargetSet <vim/host/InternetScsiHba/TargetSet.rst>`_, optional, since `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_ ):
       The set the targets to configure. Optional, when obmitted will configura the authentication properties for the adapter instead.




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       if the host bus adapter could not be found.

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       for all other configuration failures.


UpdateInternetScsiDigestProperties(iScsiHbaDevice, targetSet, digestProperties):
   Updates the digest properties for the iSCSI host bus adapter or the discovery addresses and targets associated with it.
  since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_


  Privilege:
               Host.Config.Storage



  Args:
    iScsiHbaDevice (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The device of the Internet SCSI HBA adapter.


    targetSet (`vim.host.InternetScsiHba.TargetSet <vim/host/InternetScsiHba/TargetSet.rst>`_, optional):
       The set the targets to configure. If not provided, the settings will be applied to the host bus adapter itself.


    digestProperties (`vim.host.InternetScsiHba.DigestProperties <vim/host/InternetScsiHba/DigestProperties.rst>`_):
       The data object that represents the digest settings to set.




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       if the host bus adapter could not be found.

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       for all other configuration failures.


UpdateInternetScsiAdvancedOptions(iScsiHbaDevice, targetSet, options):
   Updates the advanced options the iSCSI host bus adapter or the discovery addresses and targets associated with it.
  since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_


  Privilege:
               Host.Config.Storage



  Args:
    iScsiHbaDevice (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The device of the Internet SCSI HBA adapter.


    targetSet (`vim.host.InternetScsiHba.TargetSet <vim/host/InternetScsiHba/TargetSet.rst>`_, optional):
       The set the targets to configure. If not provided, the settings will be applied to the host bus adapter itself.


    options (`vim.host.InternetScsiHba.ParamValue <vim/host/InternetScsiHba/ParamValue.rst>`_):
       The list of options to set.




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       if the host bus adapter could not be found.

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       for all other configuration failures.


UpdateInternetScsiIPProperties(iScsiHbaDevice, ipProperties):
   Updates the IP properties for an iSCSI host bus adapter.


  Privilege:
               Host.Config.Storage



  Args:
    iScsiHbaDevice (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The device of the Internet SCSI HBA adapter.


    ipProperties (`vim.host.InternetScsiHba.IPProperties <vim/host/InternetScsiHba/IPProperties.rst>`_):
       A data object representing the IP properties for the host bus adapter




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       if the host bus adapter could not be found.

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       for all other configuration failures.


UpdateInternetScsiName(iScsiHbaDevice, iScsiName):
   Updates the name of an iSCSI host bus adapter.


  Privilege:
               Host.Config.Storage



  Args:
    iScsiHbaDevice (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The current name of the Internet SCSI HBA adapter.


    iScsiName (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The new name for the Internet SCSI HBA adapter




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       if the host bus adapter could not be found.

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       for all other configuration failures.


UpdateInternetScsiAlias(iScsiHbaDevice, iScsiAlias):
   Updates the alias of an iSCSI host bus adapter.


  Privilege:
               Host.Config.Storage



  Args:
    iScsiHbaDevice (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The device of the Internet SCSI HBA adapter.


    iScsiAlias (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The new value for the alias of the adapter.




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       if the host bus adapter could not be found.

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       for all other configuration failures.


AddInternetScsiSendTargets(iScsiHbaDevice, targets):
   Adds Send Target entries to the host bus adapter discovery list. The DiscoveryProperties.sendTargetsDiscoveryEnabled flag must be set to true.


  Privilege:
               Host.Config.Storage



  Args:
    iScsiHbaDevice (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The device of the Internet SCSI HBA adapter.


    targets (`vim.host.InternetScsiHba.SendTarget <vim/host/InternetScsiHba/SendTarget.rst>`_):
       An array of iSCSI send targets.




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       if the discovery list could not be found.

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       for all other configuration failures.


RemoveInternetScsiSendTargets(iScsiHbaDevice, targets):
   Removes Send Target entries from the host bus adapter discovery list. The DiscoveryProperty.sendTargetsDiscoveryEnabled must be set to true. If any of the targets provided as parameters are not found in the existing list, the other targets are removed and an exception is thrown.


  Privilege:
               Host.Config.Storage



  Args:
    iScsiHbaDevice (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The device of the Internet SCSI HBA adapter.


    targets (`vim.host.InternetScsiHba.SendTarget <vim/host/InternetScsiHba/SendTarget.rst>`_):
       An array of iSCSI send targets to remove.




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       if at least one target was not found.

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       for all other configuration failures.


AddInternetScsiStaticTargets(iScsiHbaDevice, targets):
   Adds Static Target entries to the host bus adapter discovery list. The DiscoveryProperty.staticTargetDiscoveryEnabled must be set to true.


  Privilege:
               Host.Config.Storage



  Args:
    iScsiHbaDevice (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The device of the Internet SCSI HBA adapter.


    targets (`vim.host.InternetScsiHba.StaticTarget <vim/host/InternetScsiHba/StaticTarget.rst>`_):
       An array of iSCSI static targets to add.




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       if the host bus adaptor discovery list was not found.

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       for all other configuration failures.


RemoveInternetScsiStaticTargets(iScsiHbaDevice, targets):
   Removes static target entries from the host bus adapter discovery list. The DiscoveryProperty.staticTargetDiscoveryEnabled must be set to true. If any of the targets provided as parameters are not found in the existing list, the other targets are removed and an exception is thrown.


  Privilege:
               Host.Config.Storage



  Args:
    iScsiHbaDevice (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The device of the Internet SCSI HBA adapter.


    targets (`vim.host.InternetScsiHba.StaticTarget <vim/host/InternetScsiHba/StaticTarget.rst>`_):
       An array of iSCSI static targets to remove.




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       if at least one target was not found.

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       for all other configuration failures.


EnableMultipathPath(pathName):
   Enables a disabled path for a Logical Unit. Use the path name from `HostMultipathStateInfoPath <vim/host/MultipathStateInfo/Path.rst>`_ or `HostMultipathInfoPath <vim/host/MultipathInfo/Path.rst>`_ .


  Privilege:
               Host.Config.Storage



  Args:
    pathName (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The name of the path to enable.




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       if the LUN could not be found.

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       for all other configuration failures.


DisableMultipathPath(pathName):
   Disables an enabled path for a Logical Unit. Use the path name from `HostMultipathStateInfoPath <vim/host/MultipathStateInfo/Path.rst>`_ or `HostMultipathInfoPath <vim/host/MultipathInfo/Path.rst>`_ .


  Privilege:
               Host.Config.Storage



  Args:
    pathName (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The name of the path to disable.




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       if the LUN could not be found.

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       for all other configuration failures.


SetMultipathLunPolicy(lunId, policy):
   Updates the path selection policy for a Logical Unit. Use the LUN uuid from `HostMultipathInfoLogicalUnit <vim/host/MultipathInfo/LogicalUnit.rst>`_ .


  Privilege:
               Host.Config.Storage



  Args:
    lunId (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The logical unit ID


    policy (`vim.host.MultipathInfo.LogicalUnitPolicy <vim/host/MultipathInfo/LogicalUnitPolicy.rst>`_):
       A data object that describes a path selection policy for the logical unit.




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       if the LUN could not be found.

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       for all other configuration failures.

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if the policy is invalid.


QueryPathSelectionPolicyOptions():
   Queries the set of path selection policy options. The set of policy options indicates what path selection policies can be used by a device managed by native multipathing. Devices managed through native multipathing are described in the `HostMultipathInfo <vim/host/MultipathInfo.rst>`_ data object.Filtering capabilities are not currently present but may be added in the future.
  since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_


  Privilege:
               System.Read



  Args:


  Returns:
    [`vim.host.PathSelectionPolicyOption <vim/host/PathSelectionPolicyOption.rst>`_]:
         The list of path selection policy descriptions that match the search criteria. Details about the policies will also be provided in accordance to the query specification.

  Raises:

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       for system configuration failures.


QueryStorageArrayTypePolicyOptions():
   Queries the set of storage array type policy options. The set of policy options indicates what storage array type policies can be used by a device managed by native multipathing. Devices managed through native multipathing are described in the `HostMultipathInfo <vim/host/MultipathInfo.rst>`_ data object.Filtering capabilities are not currently present but may be added in the future.
  since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_


  Privilege:
               System.Read



  Args:


  Returns:
    [`vim.host.StorageArrayTypePolicyOption <vim/host/StorageArrayTypePolicyOption.rst>`_]:
         The list of storage array type policy descriptions.

  Raises:

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       for system configuration failures.


UpdateScsiLunDisplayName(lunUuid, displayName):
   Update the mutable display name associated with a ScsiLun. The ScsiLun to be updated is identified using the specified uuid.
  since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_


  Privilege:
               Host.Config.Storage



  Args:
    lunUuid (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The uuid of the ScsiLun to update.


    displayName (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The new name to assign to the ScsiLun object.




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       if the device could not be found.

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       for all other configuration failures.

    `vim.fault.InvalidName <vim/fault/InvalidName.rst>`_: 
       if the name does not meet name restrictions such as an 80 character limit.

    `vim.fault.DuplicateName <vim/fault/DuplicateName.rst>`_: 
       if the name does not name uniqueness restrictions. Name uniqueness restrictions will vary based on the context in which this method is invoked.When this method is invoked on a host directly, no uniqueness checks will be performed on the name.When this method is invoked on a VC server, uniqueness checks will be performed on the name. The uniqueness check will ensure that the name is unique with respect to the entire VC instance.


DetachScsiLun(lunUuid):
   Disallow I/O issue to the specified ScsiLun. The ScsiLun is detached, i.e. administratively configured off until a subsequent attachScsiLun is performed, if the operation is successful. See `AttachScsiLun <vim/host/StorageSystem.rst#attachScsiLun>`_ .detachScsiLun is part of the Unmount / Detach workflow used when a device will be permanently removed. See also `UnmountVmfsVolume <vim/host/StorageSystem.rst#unmountVmfsVolume>`_ .
  since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_


  Privilege:
               Host.Config.Storage



  Args:
    lunUuid (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The uuid of the ScsiLun device to detach.




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       if the device could not be found.

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       for all other configuration failures.

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if
        * The device is already detached(turned 'off'). See
        * `operationalState <vim/host/ScsiLun.rst#operationalState>`_
        * .

    `vim.fault.ResourceInUse <vim/fault/ResourceInUse.rst>`_: 
       if
        * This device is backing a Vm with a Raw Device Mapped Virtual Disk.
        * 1 or more programs have I/O outstanding on this device.
        * 1 or more mounted vmfs volumes have extents residing on this device.
        * The device is configured for use by the host e.g. diagnostic partition is configured on this device.


DeleteScsiLunState(lunCanonicalName):
   For previously detached SCSI Lun, remove the state information from host. Detach SCSI Lun marks the device where I/Os are not allowed. Host still maintains the entry of this device and its state. If a LUN is detached using detachScsiLun, ESX will not automatically attach this LUN durng a rescan or after a reboot. See `DetachScsiLun <vim/host/StorageSystem.rst#detachScsiLun>`_ . Please note: The API takes 'canonicalName' of the ScsiLun object instead of the ScsiLun.uuid.See `canonicalName <vim/host/ScsiLun.rst#canonicalName>`_ 
  since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_


  Privilege:
               Host.Config.Storage



  Args:
    lunCanonicalName (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The 'canonicalName' of the ScsiLun whose state needs to be deleted.See `canonicalName <vim/host/ScsiLun.rst#canonicalName>`_ 




  Returns:
    None
         

  Raises:

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       for any configuration failures.See `canonicalName <vim/host/ScsiLun.rst#canonicalName>`_ 


AttachScsiLun(lunUuid):
   Allow I/O issue to the specified detached ScsiLun. The ScsiLun is administratively configured on, if the attach operation is successful. See `DetachScsiLun <vim/host/StorageSystem.rst#detachScsiLun>`_ .attachScsiLun is part of the Unmount, Detach workflow used when a device will be permanently removed. See also `UnmountVmfsVolume <vim/host/StorageSystem.rst#unmountVmfsVolume>`_ .
  since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_


  Privilege:
               Host.Config.Storage



  Args:
    lunUuid (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The uuid of the ScsiLun to update.




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       if the device could not be found.

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       for all other configuration failures.

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if
        * The device is already attached. i.e. Device state is not 'off' in
        * `operationalState <vim/host/ScsiLun.rst#operationalState>`_
        * .
        * The device is unreachable. See
        * `operationalState <vim/host/ScsiLun.rst#operationalState>`_
        * .


RefreshStorageSystem():
   Obtains the latest host storage information related to storage devices, topology, and file systems. The ESX host updates its storage information asynchronously. The `RefreshStorageSystem <vim/host/StorageSystem.rst#refresh>`_ method obtains information from the host platform and it performs a rescan of VMFS volumes. It does not look for new devices.This method may update the following inventory elements:
    * Devices and storage topology (
    * `HostSystem <vim/HostSystem.rst>`_
    * .
    * `config <vim/HostSystem.rst#config>`_
    * .
    * `storageDevice <vim/host/ConfigInfo.rst#storageDevice>`_
    * ).
    * VMFS and NFS datastores (
    * `HostSystem <vim/HostSystem.rst>`_
    * .
    * `datastore <vim/HostSystem.rst#datastore>`_
    * ).
    * File system volumes (
    * `HostSystem <vim/HostSystem.rst>`_
    * .
    * `config <vim/HostSystem.rst#config>`_
    * .
    * `fileSystemVolume <vim/host/ConfigInfo.rst#fileSystemVolume>`_
    * ).The Server performs asynchronous updates to the inventory. Use the `PropertyCollector <vmodl/query/PropertyCollector.rst>`_ . `WaitForUpdatesEx <vmodl/query/PropertyCollector.rst#waitForUpdatesEx>`_ method to obtain the property changes.


  Privilege:
               Host.Config.Storage



  Args:


  Returns:
    None
         


DiscoverFcoeHbas(fcoeSpec):
   Initiates FCoE discovery using the given FcoeSpecification. Upon success, discovered VNPorts will have registered with the system as FCoE HBAs.
  since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_


  Privilege:
               Host.Config.Storage



  Args:
    fcoeSpec (`vim.host.FcoeConfig.FcoeSpecification <vim/host/FcoeConfig/FcoeSpecification.rst>`_):




  Returns:
    None
         

  Raises:

    `vim.fault.FcoeFaultPnicHasNoPortSet <vim/fault/FcoeFaultPnicHasNoPortSet.rst>`_: 
       vim.fault.FcoeFaultPnicHasNoPortSet

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       if the host is unable to issue FCoE discovery.

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       if the given HBA could not be found.

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if any parameter in the given FcoeSpecification is invalid.


MarkForRemoval(hbaName, remove):
   Mark or unmark the given FCoE HBA for removal from the host system. Marking an FCoE HBA for removal will result in the HBA not being discovered upon host reboot. Until reboot, the HBA remains visible in the storage topology.
  since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_


  Privilege:
               Host.Config.Storage



  Args:
    hbaName (`str <https://docs.python.org/2/library/stdtypes.html>`_):


    remove (`bool <https://docs.python.org/2/library/stdtypes.html>`_):




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       if the given HBA could not be found.

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       if the host does not support removing the given HBA.

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if the given HBA is not an FCoE HBA.


FormatVffs(createSpec):
   Format a new VFFS on a SSD disk
  since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_


  Privilege:
               Host.Config.Storage



  Args:
    createSpec (`vim.host.VffsVolume.Specification <vim/host/VffsVolume/Specification.rst>`_):
       A data object that describes the VFFS volume creation specification.




  Returns:
    `vim.host.VffsVolume <vim/host/VffsVolume.rst>`_:
         A data object that represents the VFFS file system.

  Raises:

    `vim.fault.AlreadyExists <vim/fault/AlreadyExists.rst>`_: 
       if the volume name is already being used by another volume on the host.

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       for all other configuration failures.

    `vim.fault.ResourceInUse <vim/fault/ResourceInUse.rst>`_: 
       VFFS volume is being used.

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if VFFS version is invalid, the SSD disk does not exist or is of an invalid type.


ExtendVffs(vffsPath, devicePath, spec):
   Extends a VFFS by attaching a SSD.See `devicePath <vim/host/ScsiDisk.rst#devicePath>`_ 
  since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_


  Privilege:
               Host.Config.Storage



  Args:
    vffsPath (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The path of the VFFS to extend. See `FileSystemMountInfo <vim/host/FileSystemMountInfo.rst>`_ .See `devicePath <vim/host/ScsiDisk.rst#devicePath>`_ 


    devicePath (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       Device path of the SSD disk.See `devicePath <vim/host/ScsiDisk.rst#devicePath>`_ 


    spec (`vim.host.DiskPartitionInfo.Specification <vim/host/DiskPartitionInfo/Specification.rst>`_, optional):
       A data object that describes the SSD disk partition information. If this property is not provided, partition information will be computed and generated.See `devicePath <vim/host/ScsiDisk.rst#devicePath>`_ 




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       if the VFFS cannot be found or is unmounted.See `devicePath <vim/host/ScsiDisk.rst#devicePath>`_ 

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       for all other configuration failures.See `devicePath <vim/host/ScsiDisk.rst#devicePath>`_ 

    `vim.fault.ResourceInUse <vim/fault/ResourceInUse.rst>`_: 
       VFFS volume is being used.See `devicePath <vim/host/ScsiDisk.rst#devicePath>`_ 

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if the new SSD is already used by another VFFS volume, does not exist, or is of an invalid partition type.See `devicePath <vim/host/ScsiDisk.rst#devicePath>`_ 


DestroyVffs(vffsPath):
   Destroy a VFFS volume.
  since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_


  Privilege:
               Host.Config.Storage



  Args:
    vffsPath (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The path of the VFFS to destroy. See `FileSystemMountInfo <vim/host/FileSystemMountInfo.rst>`_ .




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       if the VFFS cannot be found or is unmounted.

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       for all other configuration failures.

    `vim.fault.ResourceInUse <vim/fault/ResourceInUse.rst>`_: 
       VFFS volume is being used.


MountVffsVolume(vffsUuid):
   Mount the unmounted VFFS volume. See `UnmountVffsVolume <vim/host/StorageSystem.rst#unmountVffsVolume>`_ .mountVffsVolume is part of the Unmount / Detach workflow used when a device will be permanently removed. See also `DetachScsiLun <vim/host/StorageSystem.rst#detachScsiLun>`_ .
  since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_


  Privilege:
               Host.Config.Storage



  Args:
    vffsUuid (`str <https://docs.python.org/2/library/stdtypes.html>`_):




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       if VFFS uuid is not found on the host.

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if
        * The volume is already mounted.
        * The volume is inaccessible.

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       for all other configuration failures.

    `vim.fault.ResourceInUse <vim/fault/ResourceInUse.rst>`_: 
       VFFS volume is being used.


UnmountVffsVolume(vffsUuid):
   Unmount the VFFS volume. An unmounted volume cannot be used for any filesystem operation requiring I/O. In contrast to removal, this operation does not destroy or alter partitions on which VFFS volumes reside. The mountState will be persisted across filesystem rescans and host reboots. See `MountVffsVolume <vim/host/StorageSystem.rst#mountVffsVolume>`_ .unmountVffsVolume is part of the Unmount / Detach workflow used when a device will be permanently removed. See also `DetachScsiLun <vim/host/StorageSystem.rst#detachScsiLun>`_ .
  since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_


  Privilege:
               Host.Config.Storage



  Args:
    vffsUuid (`str <https://docs.python.org/2/library/stdtypes.html>`_):




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       if VFFS uuid is not found on the host.

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if
        * The volume is already unmounted.
        * The volume is inaccessible.

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       for all other configuration failures.

    `vim.fault.ResourceInUse <vim/fault/ResourceInUse.rst>`_: 
       if
        * 1 or more programs have I/O outstanding on this volume.


DeleteVffsVolumeState(vffsUuid):
   For previously unmounted VFFS volume, remove the state information from host. VFFS volumes mount state is maintained by host.deleteVffsVolumeState is part of the Unmount/Detach workflow used when the device will be permanently removed. See also `UnmountVffsVolume <vim/host/StorageSystem.rst#unmountVffsVolume>`_ . If the VFFS volume is unmounted using unmountVffsVolume, ESX maintains the state of VFFS volume. This API will remove the state from the host. If the underlying storage device is going to be un-provisioned on the array side, please detach the storage device. See also `DetachScsiLun <vim/host/StorageSystem.rst#detachScsiLun>`_ .
  since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_


  Privilege:
               Host.Config.Storage



  Args:
    vffsUuid (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The VFFS UUID.




  Returns:
    None
         

  Raises:

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       for any configuration failures.


RescanVffs():
   Rescans for new VFFS. The `RefreshStorageSystem <vim/host/StorageSystem.rst#refresh>`_ method also performs a VFFS rescan. `RescanVffs <vim/host/StorageSystem.rst#rescanVffs>`_ may update the `HostSystem <vim/HostSystem.rst>`_ . `config <vim/HostSystem.rst#config>`_ . `fileSystemVolume <vim/host/ConfigInfo.rst#fileSystemVolume>`_ property. The Server performs asynchronous updates to the inventory. Use the `PropertyCollector <vmodl/query/PropertyCollector.rst>`_ . `WaitForUpdatesEx <vmodl/query/PropertyCollector.rst#waitForUpdatesEx>`_ method to obtain the property changes.
  since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_


  Privilege:
               Host.Config.Storage



  Args:


  Returns:
    None
         

  Raises:

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       if configuration fails.


QueryAvailableSsds(vffsPath):
   Query the list SSD disks that can be used to contain a VFFS volume. If the optional parameter name is supplied, queries for the SSD disks that can be used to contain extents of the specified VFFS volume. Otherwise, the method retrieves the SSD disks that can be used to contain the new VFFS volume.This operation will filter out SSD disks that are currently in use by an existing VFFS volume.
  since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_


  Privilege:
               Host.Config.Storage



  Args:
    vffsPath (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       The path of the VFFS to extend. See `FileSystemMountInfo <vim/host/FileSystemMountInfo.rst>`_ .




  Returns:
    [`vim.host.ScsiDisk <vim/host/ScsiDisk.rst>`_]:
         An array of data objects descrbing SSD disks.

  Raises:

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       if the named VFFS volume is not found.

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       if unable to query disk information.

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if named VFFS volume is not a VFFS volume


