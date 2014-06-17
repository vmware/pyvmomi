.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vim.Task: ../../vim/Task.rst

.. _devicePath: ../../vim/host/ScsiDisk.rst#devicePath

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _vim.Datastore: ../../vim/Datastore.rst

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.host.ScsiDisk: ../../vim/host/ScsiDisk.rst

.. _localSwapDatastore: ../../vim/host/ConfigInfo.rst#localSwapDatastore

.. _vim.fault.NotFound: ../../vim/fault/NotFound.rst

.. _vim.fault.NoGateway: ../../vim/fault/NoGateway.rst

.. _vim.fault.InvalidName: ../../vim/fault/InvalidName.rst

.. _vim.fault.NoVirtualNic: ../../vim/fault/NoVirtualNic.rst

.. _vim.fault.InvalidState: ../../vim/fault/InvalidState.rst

.. _vim.fault.FileNotFound: ../../vim/fault/FileNotFound.rst

.. _vim.fault.ResourceInUse: ../../vim/fault/ResourceInUse.rst

.. _vim.fault.AlreadyExists: ../../vim/fault/AlreadyExists.rst

.. _vim.fault.DuplicateName: ../../vim/fault/DuplicateName.rst

.. _vmodl.fault.NotSupported: ../../vmodl/fault/NotSupported.rst

.. _vim.fault.HostConfigFault: ../../vim/fault/HostConfigFault.rst

.. _vmodl.fault.InvalidArgument: ../../vmodl/fault/InvalidArgument.rst

.. _vim.fault.VmfsAmbiguousMount: ../../vim/fault/VmfsAmbiguousMount.rst

.. _vim.host.VmfsDatastoreOption: ../../vim/host/VmfsDatastoreOption.rst

.. _vim.host.UnresolvedVmfsVolume: ../../vim/host/UnresolvedVmfsVolume.rst

.. _vim.fault.InaccessibleDatastore: ../../vim/fault/InaccessibleDatastore.rst

.. _vim.host.VmfsDatastoreCreateSpec: ../../vim/host/VmfsDatastoreCreateSpec.rst

.. _vim.host.ResignatureRescanResult: ../../vim/host/ResignatureRescanResult.rst

.. _vim.host.VmfsDatastoreExpandSpec: ../../vim/host/VmfsDatastoreExpandSpec.rst

.. _vim.host.VmfsDatastoreExtendSpec: ../../vim/host/VmfsDatastoreExtendSpec.rst

.. _vim.host.NasVolume.Specification: ../../vim/host/NasVolume/Specification.rst

.. _vim.fault.DatastoreNotWritableOnHost: ../../vim/fault/DatastoreNotWritableOnHost.rst

.. _vim.host.DatastoreSystem.Capabilities: ../../vim/host/DatastoreSystem/Capabilities.rst

.. _vim.host.UnresolvedVmfsResignatureSpec: ../../vim/host/UnresolvedVmfsResignatureSpec.rst


vim.host.DatastoreSystem
========================
  This managed object creates and removes datastores from the host.To a host, a datastore is a storage abstraction that is backed by one of several types of storage volumes:Local file systemA datastore that is backed by a local file system volume uses a host native local file system such as NTFS or ext3. The datastore is created by identifying a file path for a directory in which virtual machine data will be stored. When the datastore is deleted, the mapping from the datastore to the file is deleted. The contents of the directory are not deleted.NAS VolumeA datastore that is backed by a network-attached storage device is created by specifying the required data needed to attach the volume to the host. Destroying the datastore detaches the volume from the host.VMFSA datastore that is backed by a VMware File System (VMFS) is created by specifying a disk with unpartitioned space, the desired disk partition format on the disk, and some VMFS attributes.An ESX Server system automatically discovers the VMFS volume on attached Logical Unit Numbers (LUNs) on startup and after re-scanning the host bus adapter. Datastores are automatically created. The datastore label is based on the VMFS volume label. If there is a conflict with an existing datastore, it is made unique by appending a suffix. The VMFS volume label will be unchanged.Destroying the datastore removes the partitions that compose the VMFS volume.Datastores are never automatically removed because transient storage connection outages may occur. They must be removed from the host using this interface.See `Datastore`_ 




Attributes
----------
    datastore (`vim.Datastore`_):
      privilege: System.View
       List of datastores on this host.
    capabilities (`vim.host.DatastoreSystem.Capabilities`_):
       Capability vector indicating the available product features.


Methods
-------


UpdateLocalSwapDatastore(datastore):
   Choose the `localSwapDatastore`_ for this host. Any change to this setting will affect virtual machines that subsequently power on or resume from a suspended state at this host, or that migrate to this host while powered on; virtual machines that are currently powered on at this host will not yet be affected.
  since: `VI API 2.5`_


  Privilege:
               Host.Config.Storage



  Args:
    datastore (`vim.Datastore`_, optional):
       The selected datastore. If this argument is unset, then the `localSwapDatastore`_ property becomes unset. Otherwise, the host must have read/write access to the indicated datastore.




  Returns:
    None
         

  Raises:

    `vim.fault.InaccessibleDatastore`_: 
       if the datastore argument is set and the host cannot access the indicated datastore.

    `vim.fault.DatastoreNotWritableOnHost`_: 
       if the datastore argument is set and the host cannot write to the indicated datastore.

    `vmodl.fault.NotSupported`_: 
       if the datastore argument is set and the `localSwapDatastoreSupported`_ capability is not true for the host.


QueryAvailableDisksForVmfs(datastore):
   Query to list disks that can be used to contain VMFS datastore extents. If the optional parameter name is supplied, queries for disks that can be used to contain extents for a VMFS datastore identified by the supplied name. Otherwise, the method retrieves disks that can be used to contain new VMFS datastores.This operation will filter out disks that are currently in use by an existing VMFS unless the VMFS using the disk is one being extended. It will also filter out management LUNs and disks that are referenced by RDMs. These disk LUNs are also unsuited for use by a VMFS.Disk LUNs referenced by RDMs are found by examining all virtual machines known to the system and visiting their virtual disk backends. If a virtual disk backend uses an RDM that is referencing a disk LUN, the disk LUN becomes ineligible for use by a VMFS datastore.


  Privilege:
               Host.Config.Storage



  Args:
    datastore (`vim.Datastore`_, optional):
       The managed object reference of the VMFS datastore you want extents for.




  Returns:
    `vim.host.ScsiDisk`_:
         An array of data objects describing SCSI disks.

  Raises:

    `vim.fault.NotFound`_: 
       if the named VMFS datastore is not found.

    `vim.fault.HostConfigFault`_: 
       if unable to query disk information.

    `vmodl.fault.NotSupported`_: 
       if the host is not an ESX Server.

    `vmodl.fault.InvalidArgument`_: 
       if named VMFS datastore is not a VMFS datastore.


QueryVmfsDatastoreCreateOptions(devicePath, vmfsMajorVersion):
   Queries options for creating a new VMFS datastore for a disk.See `devicePath`_ 


  Privilege:
               Host.Config.Storage



  Args:
    devicePath (`str`_):
       The devicePath of the disk on which datastore creation options are generated.See `devicePath`_ 


    vmfsMajorVersion (`int`_, optional, since `vSphere API 5.0`_ ):
       major version of VMFS to be used for formatting the datastore. If this parameter is not specified, then the highest `supported VMFS major version`_ for the host is used.See `devicePath`_ 




  Returns:
    `vim.host.VmfsDatastoreOption`_:
         An array of VMFS datastore provisioning options that can be applied on a disk.

  Raises:

    `vim.fault.NotFound`_: 
       if the device is not found.See `devicePath`_ 

    `vim.fault.HostConfigFault`_: 
       if unable to get the current partition information for the device.See `devicePath`_ 

    `vmodl.fault.NotSupported`_: 
       if the host is not an ESX Server.See `devicePath`_ 


CreateVmfsDatastore(spec):
   Creates a new VMFS datastore.


  Privilege:
               Host.Config.Storage



  Args:
    spec (`vim.host.VmfsDatastoreCreateSpec`_):
       The specification for creating a datastore backed by a VMFS.




  Returns:
    `vim.Datastore`_:
         The newly created datastore.

  Raises:

    `vim.fault.DuplicateName`_: 
       if a datastore with the same name already exists.

    `vim.fault.HostConfigFault`_: 
       if unable to format the VMFS volume or gather information about the created volume.

    `vmodl.fault.InvalidArgument`_: 
       if the datastore name is invalid, or the spec is invalid.

    `vmodl.fault.NotSupported`_: 
       if the host is not an ESX Server system.


QueryVmfsDatastoreExtendOptions(datastore, devicePath, suppressExpandCandidates):
   Queries for options for increasing the capacity of an existing VMFS datastore by adding new extents using space from the specified disk.See `devicePath`_ 


  Privilege:
               Host.Config.Storage



  Args:
    datastore (`vim.Datastore`_):
       The datastore to be extended.See `devicePath`_ 


    devicePath (`str`_):
       The devicePath of the disk on which datastore extension options are generated.See `devicePath`_ 


    suppressExpandCandidates (`bool`_, optional, since `vSphere API 4.0`_ ):
       Indicates whether to exclude options that can be used for extent expansion also. Free space can be used for adding an extent or expanding an existing extent. If this parameter is set to true, the list of options returned will not include free space that can be used for expansion.See `devicePath`_ 




  Returns:
    `vim.host.VmfsDatastoreOption`_:
         An array of VMFS datastore provisioning options that can be applied on a disk.

  Raises:

    `vim.fault.NotFound`_: 
       if a datastore or device with the given name could not be found or if the datastore is unmounted.See `devicePath`_ 

    `vim.fault.HostConfigFault`_: 
       if unable to get the current partition information for the device.See `devicePath`_ 

    `vmodl.fault.NotSupported`_: 
       if the host is not an ESX Server.See `devicePath`_ 


QueryVmfsDatastoreExpandOptions(datastore):
   Queries for options for increasing the capacity of an existing VMFS datastore by expanding (increasing the size of) an existing extent of the datastore.
  since: `vSphere API 4.0`_


  Privilege:
               Host.Config.Storage



  Args:
    datastore (`vim.Datastore`_):
       The datastore to be expanded.




  Returns:
    `vim.host.VmfsDatastoreOption`_:
         An array of VMFS datastore expansion options that can be applied.

  Raises:

    `vim.fault.NotFound`_: 
       if the specified datastore could not be found or is unmounted.

    `vim.fault.HostConfigFault`_: 
       if unable to get partition information for the devices on which the extents reside

    `vmodl.fault.NotSupported`_: 
       if the host is not an ESX Server.


ExtendVmfsDatastore(datastore, spec):
   Increases the capacity of an existing VMFS datastore by adding new extents to the datastore.


  Privilege:
               Host.Config.Storage



  Args:
    datastore (`vim.Datastore`_):
       The datastore whose capacity should be increased.


    spec (`vim.host.VmfsDatastoreExtendSpec`_):
       The specification describing what extents to add to a VMFS datastore.




  Returns:
    `vim.Datastore`_:
         The extended datastore.

  Raises:

    `vim.fault.NotFound`_: 
       if a datastore with the name could not be found.

    `vim.fault.HostConfigFault`_: 
       if unable to extend the VMFS volume.

    `vmodl.fault.NotSupported`_: 
       if the host is not an ESX Server.


ExpandVmfsDatastore(datastore, spec):
   Increases the capacity of an existing VMFS datastore by expanding (increasing the size of) an existing extent of the datastore.
  since: `vSphere API 4.0`_


  Privilege:
               Host.Config.Storage



  Args:
    datastore (`vim.Datastore`_):
       The datastore whose capacity should be increased.


    spec (`vim.host.VmfsDatastoreExpandSpec`_):
       The specification describing which extent of the VMFS datastore to expand.




  Returns:
    `vim.Datastore`_:
         The expanded datastore.

  Raises:

    `vim.fault.NotFound`_: 
       if a datastore with the name could not be found.

    `vim.fault.HostConfigFault`_: 
       if unable to expand the VMFS volume.

    `vmodl.fault.NotSupported`_: 
       if the host is not an ESX Server.


CreateNasDatastore(spec):
   Creates a new network-attached storage datastore.


  Privilege:
               Host.Config.Storage



  Args:
    spec (`vim.host.NasVolume.Specification`_):
       The specification for creating a network-attached storage volume.




  Returns:
    `vim.Datastore`_:
         The newly created datastore.

  Raises:

    `vim.fault.DuplicateName`_: 
       if a datastore with the same name already exists.

    `vim.fault.AlreadyExists`_: 
       if the local path already exists on the host, or the remote path is already mounted on the host.

    `vim.fault.HostConfigFault`_: 
       if unable to mount the NAS volume.

    `vmodl.fault.InvalidArgument`_: 
       if the datastore name is invalid, or the spec is invalid.

    `vim.fault.NoVirtualNic`_: 
       if VMkernel TCPIP stack is not configured.

    `vim.fault.NoGateway`_: 
       if VMkernel gateway is not configured.


CreateLocalDatastore(name, path):
   Creates a new local datastore.


  Privilege:
               Host.Config.Storage



  Args:
    name (`str`_):
       The name of a datastore to create on the local host.


    path (`str`_):
       The file path for a directory in which the virtual machine data will be stored.




  Returns:
    `vim.Datastore`_:
         

  Raises:

    `vim.fault.DuplicateName`_: 
       if a datastore with the same name already exists.

    `vim.fault.HostConfigFault`_: 
       if unable to create the datastore on host.

    `vim.fault.FileNotFound`_: 
       if path doesn't exist

    `vim.fault.InvalidName`_: 
       if name is not valid datastore name


RemoveDatastore(datastore):
   Removes a datastore from a host.


  Privilege:
               Host.Config.Storage



  Args:
    datastore (`vim.Datastore`_):
       The datastore to be removed.




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound`_: 
       if the datastore could not be found.

    `vim.fault.HostConfigFault`_: 
       if unable to umount the NAS volume for NAS datastore, or gather the existing volume information.

    `vim.fault.ResourceInUse`_: 
       for a VMFS volume if there is any VM registered on any host attached to this datastore.


ConfigureDatastorePrincipal(userName, password):
   Configures datastore principal user for the host.All virtual machine-related file I/O is performed under this user. Configuring datastore principal user will result in all virtual machine files (configuration, disk, and so on) being checked for proper access. If necessary, ownership and permissions are modified. Note that in some environments, file ownership and permissions modification may not be possible. For example, virtual machine files stored on NFS cannot be modified for ownership and permissions if root squashing is enabled. Ownership and permissions for these files must be manually changed by a system administrator. In general, if server process does not have rights to change ownership and file permissions of virtual machine files, they must be modified manually. If a virtual machine files are not read/writeable by this user, virtual machine related operations such as power on/off, configuration, and so on will fail. This operation must be performed while in maintenance mode and requires host reboot.


  Privilege:
               Host.Config.Maintenance



  Args:
    userName (`str`_):
       Datastore principal user name.


    password (`str`_, optional):
       Optional password for systems that require password for user impersonation.




  Returns:
    None
         

  Raises:

    `vim.fault.InvalidState`_: 
       if the host is not in maintenance mode.

    `vim.fault.HostConfigFault`_: 
       if unable to configure the datastore principal.

    `vmodl.fault.InvalidArgument`_: 
       if userName or password is not valid.

    `vmodl.fault.NotSupported`_: 
       if this feature is not supported on the host.


QueryUnresolvedVmfsVolumes():
   Get the list of unbound VMFS volumes. For sharing a volume across hosts, a VMFS volume is bound to its underlying block device storage. When a low level block copy is performed to copy or move the VMFS volume, the copied volume will be unbound.
  since: `vSphere API 4.0`_


  Privilege:
               System.Read



  Args:


  Returns:
    `vim.host.UnresolvedVmfsVolume`_:
         An array of unbound VMFS datastore


ResignatureUnresolvedVmfsVolume(resolutionSpec):
   Resignature an unbound VMFS volume. To safely enable sharing of the volume across hosts, a VMFS volume is bound to its underlying block device storage. When a low level block copy is performed to copy or move the VMFS volume, the copied volume will be unbound. In order for the VMFS volume to be usable, a resolution operation is needed to determine whether the VMFS volume should be treated as a new volume or not and what extents compose that volume in the event there is more than one unbound volume.With 'Resignature' operation, a new Vmfs Uuid is assigned to the volume but its contents are kept intact. Resignature results in a new Vmfs volume on the host. Users can specify a list of hosts on which the volume will be auto-mounted.
  since: `vSphere API 4.0`_


  Privilege:
               Host.Config.Storage



  Args:
    resolutionSpec (`vim.host.UnresolvedVmfsResignatureSpec`_):
       A data object that describes what the disk extents to be used for creating the new VMFS volume.




  Returns:
     `vim.Task`_:
         

  Raises:

    `vim.fault.VmfsAmbiguousMount`_: 
       when ESX is unable to resolve the extents of a VMFS volume unambiguously. This is thrown only when a VMFS volume has multiple extents and multiple copies of non-head extents are detected, and the user has not specified one copy of every extent. Please note that some versions of ESX may not support resolving the situation where multiple copies of non-head extents are detected, even if one copy of every extent is specified in the method parameter. To resolve such a situation, the user is expected to change the configuration (for example, using array management tools) so that only one copy of each non-head extent is presented to ESX.

    `vim.fault.HostConfigFault`_: 
       for all other configuration failures.


