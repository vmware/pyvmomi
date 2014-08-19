
vim.host.Capability
===================
  Specifies the capabilities of the particular host. This set of capabilities is referenced in other parts of the API specification to indicate under what circumstances an API will throw a `NotSupported <vmodl/fault/NotSupported.rst>`_ fault.
:extends: vmodl.DynamicData_

Attributes:
    recursiveResourcePoolsSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

    cpuMemoryResourceConfigurationSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Flag indicating whether cpu and memory resource configuration is supported. If this is set to false, `UpdateConfig <vim/ResourcePool.rst#updateConfig>`_ , `UpdateChildResourceConfiguration <vim/ResourcePool.rst#updateChildResourceConfiguration>`_ cannot be used for changing the cpu/memory resource configurations.
    rebootSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Flag indicating whether rebooting the host is supported.
    shutdownSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Flag indicating whether the host can be powered off
    vmotionSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Flag indicating whether you can perform VMotion.
    standbySupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Flag indicating whether you can put the host in a power down state, from which it can be powered up automatically.
    ipmiSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Flag indicating whether the host supports IPMI (Intelligent Platform Management Interface). XXX - Make ipmiSupported optional until there is a compatible hostagent.
    maxSupportedVMs (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The maximum number of virtual machines that can exist on this host. If this capability is not set, the number of virtual machines is unlimited.
    maxRunningVMs (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The maximum number of virtual machines that can be running simultaneously on this host. If this capability is not set, the number of virtual machines running simultaneously is unlimited.
    maxSupportedVcpus (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The maximum number of virtual CPUs supported per virtual machine. If this capability is not set, the number is unlimited.
    maxRegisteredVMs (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The maximum number of registered virtual machines supported by the host. If this limit is exceeded, the management agent will be at risk of running out of system resources. `configIssue <vim/ManagedEntity.rst#configIssue>`_ will be posted on `HostSystem <vim/HostSystem.rst>`_ in this case.If this capability is not set, the number is unknown.
    datastorePrincipalSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Flag indicating whether datastore principal user is supported on the host.
    sanSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Flag indicating whether access to SAN devices is supported.
    nfsSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Is access to NFS devices supported.
    iscsiSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Is access to iSCSI devices supported.
    vlanTaggingSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Is VLAN Tagging supported.
    nicTeamingSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Is NIC teaming supported.
    highGuestMemSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Is high guest memory supported.
    maintenanceModeSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Is maintenance mode supported
    suspendedRelocateSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether this host supports relocation of suspended virtual machines. Must be true on the source and destination hosts for the relocation to work.
    restrictedSnapshotRelocateSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether this host supports relocation of virtual machines with snapshots. Must be true on the source and destination hosts for the relocation to work. Even if this is true, the following conditions must hold: 1) All the the vm's files are in one directory prior to the relocate. 2) All of the vm's files will be in one directory after the relocate. 3) The source and destination hosts are the same product version.
    perVmSwapFiles (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Flag indicating whether virtual machine execution on this host involves a swapfile for each virtual machine. If true, the swapfile placement for a powered-on virtual machine is advertised in its FileLayout by the `swapFile <vim/vm/FileLayout.rst#swapFile>`_ property.
    localSwapDatastoreSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Flag indicating whether the host supports selecting a datastore that that may be used to store virtual machine swapfiles.
    unsharedSwapVMotionSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Flag indicating whether the host supports participating in a VMotion where the virtual machine swapfile is not visible to the destination.
    backgroundSnapshotsSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Flag indicating whether background snapshots are supported on this host.
    preAssignedPCIUnitNumbersSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Flag to indicate whether the server returns unit numbers in a pre-assigned range for devices on the PCI bus. When the server supports this flag, the device unit number namespace is partitioned by device type. Different types of devices will sit in a specific range of unit numbers that may not correspond to physical slots in the pci bus but present a relative ordering of the devices with respect to other devices of the same type. Note that this does not mean that the user can set the relative ordering between device types, but only allows stable orderings between devices of the same type. The unit number will now clearly represent an ordering between devices of the same type. `unitNumber <vim/vm/device/VirtualDevice.rst#unitNumber>`_ This property is only available for devices on the pci controller.
    screenshotSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether the screenshot retrival over https is supported for this host's virtual machines. If true, a screenshot can be retrieved at the HTTPS relative path/screen?id=managed object ID of virtual machine or snapshot. If any of the optional parameters 'top', 'left', 'bottom', and 'right' is specified, the returned image will be cropped from the rectangle with upper left corner (left, top) and bottom right corner (right - 1, bottom - 1). These values default to the top, left, bottom and right edges of the image. The client must use an authenticated session with privilege VirtualMachine.Interact.ConsoleInteract on the requested virtual machine or, in the case of a snapshot, the virtual machine associated with that snapshot.
    scaledScreenshotSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether scaling is supported for screenshots retrieved over https. If true, screenshot retrieval supports the additional optional parameters 'width' and 'height'. After cropping, the returned image will be scaled to these dimensions. If only one of these parameters is specified, default behavior is to return an image roughly proportional to the source image.
    storageVMotionSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether the storage of a powered-on virtual machine may be relocated.
    vmotionWithStorageVMotionSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether the storage of a powered-on virtual machine may be relocated while simultaneously changing the execution host of the virtual machine.
    vmotionAcrossNetworkSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Indicates whether the network of a powered-on virtual machine can be changed while simultaneously changing the execution host of the virtual machine.
    hbrNicSelectionSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether a dedicated nic can be selected for vSphere Replication LWD traffic, i.e., from the primary host to the VR server.
    recordReplaySupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether this host supports record and replay
    ftSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether this host supports Fault Tolerance There can be many reasons why a host does not support Fault Tolerance, which includes CPU compatibility, product compatibility as well as other host configuration settings. For specific reasons, look into `replayCompatibilityIssues <vim/host/Capability.rst#replayCompatibilityIssues>`_ and `ftCompatibilityIssues <vim/host/Capability.rst#ftCompatibilityIssues>`_ In releases after vSphere API 5.0, vSphere Servers might not generate property collector update notifications for this property. To obtain the latest value of the property, you can use PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx. If you use the PropertyCollector.WaitForUpdatesEx method, specify an empty string for the version parameter. Since this property is on a DataObject, an update returned by WaitForUpdatesEx may contain values for this property when some other property on the DataObject changes. If this update is a result of a call to WaitForUpdatesEx with a non-empty version parameter, the value for this property may not be current.
    replayUnsupportedReason (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       For a host whose CPU doesn't support replay, indicates the reason for the incompatibility. `HostReplayUnsupportedReason <vim/host/Capability/ReplayUnsupportedReason.rst>`_ represents the set of possible values.
    replayCompatibilityIssues ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       For a host which doesn't support replay, indicates all the reasons for the incompatibility. `HostReplayUnsupportedReason <vim/host/Capability/ReplayUnsupportedReason.rst>`_ lists the set of possible values.
    ftCompatibilityIssues ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       For a host which doesn't support Fault Tolerance, indicates all the reasons for the incompatibility. `HostCapabilityFtUnsupportedReason <vim/host/Capability/FtUnsupportedReason.rst>`_ lists the set of possible values.
    loginBySSLThumbprintSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Flag indicating whether this host supports SSL thumbprint authentication
    cloneFromSnapshotSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether or not cloning a virtual machine from a snapshot point is allowed.This property must be true on the host where the virtual machine is currently residing. This property need not be true on the destination host for the clone.See `snapshot <vim/vm/CloneSpec.rst#snapshot>`_ 
    deltaDiskBackingsSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Flag indicating whether explicitly creating arbirary configurations of delta disk backings is supported.A delta disk backing is a way to preserve a virtual disk backing at some point in time. A delta disk backing is a file backing which in turn points to the original virtual disk backing (the parent). After a delta disk backing is added, all writes go to the delta disk backing. All reads first try the delta disk backing and then try the parent backing if needed.If this property is false, then delta disk backings can only be implicitly created through using snapshot operations and two virtual machines cannot safely share a parent disk backing.If this property is true, then delta disk backings can be explicitly created and managed, and two virtual machines may safely share a parent disk backing.In the context above, "safely" means that performing operations on one of the virtual machines will not affect the operation of the other virtual machine.See `parent <vim/vm/device/VirtualDisk/SparseVer1BackingInfo.rst#parent>`_ See `parent <vim/vm/device/VirtualDisk/SparseVer2BackingInfo.rst#parent>`_ See `parent <vim/vm/device/VirtualDisk/FlatVer1BackingInfo.rst#parent>`_ See `parent <vim/vm/device/VirtualDisk/FlatVer2BackingInfo.rst#parent>`_ See `parent <vim/vm/device/VirtualDisk/RawDiskMappingVer1BackingInfo.rst#parent>`_ See `PromoteDisks_Task <vim/VirtualMachine.rst#promoteDisks>`_ See `diskMoveType <vim/vm/RelocateSpec.rst#diskMoveType>`_ See `diskMoveType <vim/vm/RelocateSpec/DiskLocator.rst#diskMoveType>`_ 
    perVMNetworkTrafficShapingSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether network traffic shaping on a per virtual machine basis is supported.
    tpmSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Flag indicating whether this host supports the integrity measurement using a TPM device.
    supportedCpuFeature ([`vim.host.CpuIdInfo <vim/host/CpuIdInfo.rst>`_], optional):

       CPU feature set that is supported by the virtualization platform. This feature set may reflect characteristics of the product capabilities and licensing. For any feature marked '-', reference the `cpuFeature <vim/host/HardwareInfo.rst#cpuFeature>`_ array of the host's HardwareInfo to determine the correct value.
    virtualExecUsageSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether the host supports configuring hardware virtualization (HV) support for virtual machines.
    storageIORMSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether the host supports storage I/O resource management.
    vmDirectPathGen2Supported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether the host supports network passthrough using VMDirectPath Gen 2. Note that this is a general capability for the host and is independent of support by a given physical NIC. If false, the reason(s) for lack of support will be provided in `vmDirectPathGen2UnsupportedReason <vim/host/Capability.rst#vmDirectPathGen2UnsupportedReason>`_ and/or in `vmDirectPathGen2UnsupportedReasonExtended <vim/host/Capability.rst#vmDirectPathGen2UnsupportedReasonExtended>`_ .See `vmDirectPathGen2Supported <vim/host/PhysicalNic.rst#vmDirectPathGen2Supported>`_ 
    vmDirectPathGen2UnsupportedReason ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       If `vmDirectPathGen2Supported <vim/host/Capability.rst#vmDirectPathGen2Supported>`_ is false, this array will be populated with reasons for the lack of support (chosen from VmDirectPathGen2UnsupportedReason). If there is a reason for the lack of support that cannot be described by the available constants, `vmDirectPathGen2UnsupportedReasonExtended <vim/host/Capability.rst#vmDirectPathGen2UnsupportedReasonExtended>`_ will be populated with an additional explanation provided by the platform.Note that this list of reasons is not guaranteed to be exhaustive.If the reason "hostNptIncompatibleProduct" is provided, then that will be the only provided reason, as the host software is incapable of providing additional information.
    vmDirectPathGen2UnsupportedReasonExtended (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       If `vmDirectPathGen2Supported <vim/host/Capability.rst#vmDirectPathGen2Supported>`_ is false, this property may contain an explanation provided by the platform, beyond the reasons (if any) enumerated in `vmDirectPathGen2UnsupportedReason <vim/host/Capability.rst#vmDirectPathGen2UnsupportedReason>`_ .
    supportedVmfsMajorVersion ([`int <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       List of VMFS major versions supported by the host.
    vStorageCapable (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether the host supports vStorage Hardware acceleration.
    snapshotRelayoutSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether this host supports unrestricted relocation of virtual machines with snapshots. Only needs to be true on the destination host for the unrestricted relocation to work. The full snapshot relocation does not restrict the layout of snapshot files or disks of the virtual machine, nor its power state. If the virtual machine is powered on, a storage vmotion will be performed to relocate its snapshots and disks.
    firewallIpRulesSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Indicates whether this host supports ip address based restrictions in the firewall configuration.
    servicePackageInfoSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Indicates whether this host supports package information in service configuration.
    maxHostRunningVms (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The maximum number of virtual machines that can be run on the host. An unset value indicates that the value could not be obtained. In contrast to `maxRunningVMs <vim/host/Capability.rst#maxRunningVMs>`_ , this value is the minimum of (i) the maximum number supported by the hardware and (ii) the maximum number permitted by the host license.
    maxHostSupportedVcpus (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The maximum number of virtual CPUs that can be run on the host. An unset value indicates that the value could not be obtained. In contrast to `maxSupportedVcpus <vim/host/Capability.rst#maxSupportedVcpus>`_ , this value is the minimum of (i) the maximum number supported by the hardware and (ii) the maximum number permitted by the host license.
    vmfsDatastoreMountCapable (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether the host is capable of mounting/unmounting VMFS datastores.
    eightPlusHostVmfsSharedAccessSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether the host is capable of accessing a VMFS disk when there are eight or more hosts accessing the disk already.
    nestedHVSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether the host supports nested hardware-assisted virtualization.
    vPMCSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether the host supports vurtual CPU performance counters.
    interVMCommunicationThroughVMCISupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether the host supports VMCI for communication between virtual machines.
    scheduledHardwareUpgradeSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Indicates whether the host supports scheduled hardware upgrades.See `scheduledHardwareUpgradeInfo <vim/vm/ConfigInfo.rst#scheduledHardwareUpgradeInfo>`_ 
    featureCapabilitiesSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicated whether the host supports feature capabilities for EVC mode.
    latencySensitivitySupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether the host supports latency sensitivity for the virtual machines.
    storagePolicySupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Indicates that host supports Object-based Storage System and Storage-Profile based disk provisioning.
    accel3dSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates if 3D hardware acceleration for virtual machines is supported.
    reliableMemoryAware (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Indicates that this host uses a reliable memory aware allocation policy.
    multipleNetworkStackInstanceSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Indicates whether the host supports Multiple Instance TCP/IP stack
    vsanSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Indicates whether the host supports VSAN functionality.See `HostVsanSystem <vim/host/VsanSystem.rst>`_ 
    vFlashSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Indicates whether the host supports vFlash.
