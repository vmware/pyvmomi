.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _parent: ../../vim/vm/device/VirtualDisk/RawDiskMappingVer1BackingInfo.rst#parent

.. _swapFile: ../../vim/vm/FileLayout.rst#swapFile

.. _snapshot: ../../vim/vm/CloneSpec.rst#snapshot

.. _unitNumber: ../../vim/vm/device/VirtualDevice.rst#unitNumber

.. _cpuFeature: ../../vim/host/HardwareInfo.rst#cpuFeature

.. _HostSystem: ../../vim/HostSystem.rst

.. _configIssue: ../../vim/ManagedEntity.rst#configIssue

.. _diskMoveType: ../../vim/vm/RelocateSpec/DiskLocator.rst#diskMoveType

.. _NotSupported: ../../vmodl/fault/NotSupported.rst

.. _UpdateConfig: ../../vim/ResourcePool.rst#updateConfig

.. _maxRunningVMs: ../../vim/host/Capability.rst#maxRunningVMs

.. _HostVsanSystem: ../../vim/host/VsanSystem.rst

.. _maxSupportedVcpus: ../../vim/host/Capability.rst#maxSupportedVcpus

.. _PromoteDisks_Task: ../../vim/VirtualMachine.rst#promoteDisks

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.host.CpuIdInfo: ../../vim/host/CpuIdInfo.rst

.. _ftCompatibilityIssues: ../../vim/host/Capability.rst#ftCompatibilityIssues

.. _replayCompatibilityIssues: ../../vim/host/Capability.rst#replayCompatibilityIssues

.. _vmDirectPathGen2Supported: ../../vim/host/Capability.rst#vmDirectPathGen2Supported

.. _HostReplayUnsupportedReason: ../../vim/host/Capability/ReplayUnsupportedReason.rst

.. _scheduledHardwareUpgradeInfo: ../../vim/vm/ConfigInfo.rst#scheduledHardwareUpgradeInfo

.. _UpdateChildResourceConfiguration: ../../vim/ResourcePool.rst#updateChildResourceConfiguration

.. _HostCapabilityFtUnsupportedReason: ../../vim/host/Capability/FtUnsupportedReason.rst

.. _vmDirectPathGen2UnsupportedReason: ../../vim/host/Capability.rst#vmDirectPathGen2UnsupportedReason

.. _vmDirectPathGen2UnsupportedReasonExtended: ../../vim/host/Capability.rst#vmDirectPathGen2UnsupportedReasonExtended


vim.host.Capability
===================
  Specifies the capabilities of the particular host. This set of capabilities is referenced in other parts of the API specification to indicate under what circumstances an API will throw a `NotSupported`_ fault.
:extends: vmodl.DynamicData_

Attributes:
    recursiveResourcePoolsSupported (`bool`_):

    cpuMemoryResourceConfigurationSupported (`bool`_):

       Flag indicating whether cpu and memory resource configuration is supported. If this is set to false, `UpdateConfig`_ , `UpdateChildResourceConfiguration`_ cannot be used for changing the cpu/memory resource configurations.
    rebootSupported (`bool`_):

       Flag indicating whether rebooting the host is supported.
    shutdownSupported (`bool`_):

       Flag indicating whether the host can be powered off
    vmotionSupported (`bool`_):

       Flag indicating whether you can perform VMotion.
    standbySupported (`bool`_):

       Flag indicating whether you can put the host in a power down state, from which it can be powered up automatically.
    ipmiSupported (`bool`_, optional):

       Flag indicating whether the host supports IPMI (Intelligent Platform Management Interface). XXX - Make ipmiSupported optional until there is a compatible hostagent.
    maxSupportedVMs (`int`_, optional):

       The maximum number of virtual machines that can exist on this host. If this capability is not set, the number of virtual machines is unlimited.
    maxRunningVMs (`int`_, optional):

       The maximum number of virtual machines that can be running simultaneously on this host. If this capability is not set, the number of virtual machines running simultaneously is unlimited.
    maxSupportedVcpus (`int`_, optional):

       The maximum number of virtual CPUs supported per virtual machine. If this capability is not set, the number is unlimited.
    maxRegisteredVMs (`int`_, optional):

       The maximum number of registered virtual machines supported by the host. If this limit is exceeded, the management agent will be at risk of running out of system resources. `configIssue`_ will be posted on `HostSystem`_ in this case.If this capability is not set, the number is unknown.
    datastorePrincipalSupported (`bool`_):

       Flag indicating whether datastore principal user is supported on the host.
    sanSupported (`bool`_):

       Flag indicating whether access to SAN devices is supported.
    nfsSupported (`bool`_):

       Is access to NFS devices supported.
    iscsiSupported (`bool`_):

       Is access to iSCSI devices supported.
    vlanTaggingSupported (`bool`_):

       Is VLAN Tagging supported.
    nicTeamingSupported (`bool`_):

       Is NIC teaming supported.
    highGuestMemSupported (`bool`_):

       Is high guest memory supported.
    maintenanceModeSupported (`bool`_):

       Is maintenance mode supported
    suspendedRelocateSupported (`bool`_):

       Indicates whether this host supports relocation of suspended virtual machines. Must be true on the source and destination hosts for the relocation to work.
    restrictedSnapshotRelocateSupported (`bool`_):

       Indicates whether this host supports relocation of virtual machines with snapshots. Must be true on the source and destination hosts for the relocation to work. Even if this is true, the following conditions must hold: 1) All the the vm's files are in one directory prior to the relocate. 2) All of the vm's files will be in one directory after the relocate. 3) The source and destination hosts are the same product version.
    perVmSwapFiles (`bool`_):

       Flag indicating whether virtual machine execution on this host involves a swapfile for each virtual machine. If true, the swapfile placement for a powered-on virtual machine is advertised in its FileLayout by the `swapFile`_ property.
    localSwapDatastoreSupported (`bool`_):

       Flag indicating whether the host supports selecting a datastore that that may be used to store virtual machine swapfiles.
    unsharedSwapVMotionSupported (`bool`_):

       Flag indicating whether the host supports participating in a VMotion where the virtual machine swapfile is not visible to the destination.
    backgroundSnapshotsSupported (`bool`_):

       Flag indicating whether background snapshots are supported on this host.
    preAssignedPCIUnitNumbersSupported (`bool`_):

       Flag to indicate whether the server returns unit numbers in a pre-assigned range for devices on the PCI bus. When the server supports this flag, the device unit number namespace is partitioned by device type. Different types of devices will sit in a specific range of unit numbers that may not correspond to physical slots in the pci bus but present a relative ordering of the devices with respect to other devices of the same type. Note that this does not mean that the user can set the relative ordering between device types, but only allows stable orderings between devices of the same type. The unit number will now clearly represent an ordering between devices of the same type. `unitNumber`_ This property is only available for devices on the pci controller.
    screenshotSupported (`bool`_):

       Indicates whether the screenshot retrival over https is supported for this host's virtual machines. If true, a screenshot can be retrieved at the HTTPS relative path/screen?id=managed object ID of virtual machine or snapshot. If any of the optional parameters 'top', 'left', 'bottom', and 'right' is specified, the returned image will be cropped from the rectangle with upper left corner (left, top) and bottom right corner (right - 1, bottom - 1). These values default to the top, left, bottom and right edges of the image. The client must use an authenticated session with privilege VirtualMachine.Interact.ConsoleInteract on the requested virtual machine or, in the case of a snapshot, the virtual machine associated with that snapshot.
    scaledScreenshotSupported (`bool`_):

       Indicates whether scaling is supported for screenshots retrieved over https. If true, screenshot retrieval supports the additional optional parameters 'width' and 'height'. After cropping, the returned image will be scaled to these dimensions. If only one of these parameters is specified, default behavior is to return an image roughly proportional to the source image.
    storageVMotionSupported (`bool`_):

       Indicates whether the storage of a powered-on virtual machine may be relocated.
    vmotionWithStorageVMotionSupported (`bool`_):

       Indicates whether the storage of a powered-on virtual machine may be relocated while simultaneously changing the execution host of the virtual machine.
    vmotionAcrossNetworkSupported (`bool`_, optional):

       Indicates whether the network of a powered-on virtual machine can be changed while simultaneously changing the execution host of the virtual machine.
    hbrNicSelectionSupported (`bool`_):

       Indicates whether a dedicated nic can be selected for vSphere Replication LWD traffic, i.e., from the primary host to the VR server.
    recordReplaySupported (`bool`_):

       Indicates whether this host supports record and replay
    ftSupported (`bool`_):

       Indicates whether this host supports Fault Tolerance There can be many reasons why a host does not support Fault Tolerance, which includes CPU compatibility, product compatibility as well as other host configuration settings. For specific reasons, look into `replayCompatibilityIssues`_ and `ftCompatibilityIssues`_ In releases after vSphere API 5.0, vSphere Servers might not generate property collector update notifications for this property. To obtain the latest value of the property, you can use PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx. If you use the PropertyCollector.WaitForUpdatesEx method, specify an empty string for the version parameter. Since this property is on a DataObject, an update returned by WaitForUpdatesEx may contain values for this property when some other property on the DataObject changes. If this update is a result of a call to WaitForUpdatesEx with a non-empty version parameter, the value for this property may not be current.
    replayUnsupportedReason (`str`_, optional):

       For a host whose CPU doesn't support replay, indicates the reason for the incompatibility. `HostReplayUnsupportedReason`_ represents the set of possible values.
    replayCompatibilityIssues ([`str`_], optional):

       For a host which doesn't support replay, indicates all the reasons for the incompatibility. `HostReplayUnsupportedReason`_ lists the set of possible values.
    ftCompatibilityIssues ([`str`_], optional):

       For a host which doesn't support Fault Tolerance, indicates all the reasons for the incompatibility. `HostCapabilityFtUnsupportedReason`_ lists the set of possible values.
    loginBySSLThumbprintSupported (`bool`_, optional):

       Flag indicating whether this host supports SSL thumbprint authentication
    cloneFromSnapshotSupported (`bool`_):

       Indicates whether or not cloning a virtual machine from a snapshot point is allowed.This property must be true on the host where the virtual machine is currently residing. This property need not be true on the destination host for the clone.See `snapshot`_ 
    deltaDiskBackingsSupported (`bool`_):

       Flag indicating whether explicitly creating arbirary configurations of delta disk backings is supported.A delta disk backing is a way to preserve a virtual disk backing at some point in time. A delta disk backing is a file backing which in turn points to the original virtual disk backing (the parent). After a delta disk backing is added, all writes go to the delta disk backing. All reads first try the delta disk backing and then try the parent backing if needed.If this property is false, then delta disk backings can only be implicitly created through using snapshot operations and two virtual machines cannot safely share a parent disk backing.If this property is true, then delta disk backings can be explicitly created and managed, and two virtual machines may safely share a parent disk backing.In the context above, "safely" means that performing operations on one of the virtual machines will not affect the operation of the other virtual machine.See `parent`_ See `parent`_ See `parent`_ See `parent`_ See `parent`_ See `PromoteDisks_Task`_ See `diskMoveType`_ See `diskMoveType`_ 
    perVMNetworkTrafficShapingSupported (`bool`_):

       Indicates whether network traffic shaping on a per virtual machine basis is supported.
    tpmSupported (`bool`_):

       Flag indicating whether this host supports the integrity measurement using a TPM device.
    supportedCpuFeature ([`vim.host.CpuIdInfo`_], optional):

       CPU feature set that is supported by the virtualization platform. This feature set may reflect characteristics of the product capabilities and licensing. For any feature marked '-', reference the `cpuFeature`_ array of the host's HardwareInfo to determine the correct value.
    virtualExecUsageSupported (`bool`_):

       Indicates whether the host supports configuring hardware virtualization (HV) support for virtual machines.
    storageIORMSupported (`bool`_):

       Indicates whether the host supports storage I/O resource management.
    vmDirectPathGen2Supported (`bool`_):

       Indicates whether the host supports network passthrough using VMDirectPath Gen 2. Note that this is a general capability for the host and is independent of support by a given physical NIC. If false, the reason(s) for lack of support will be provided in `vmDirectPathGen2UnsupportedReason`_ and/or in `vmDirectPathGen2UnsupportedReasonExtended`_ .See `vmDirectPathGen2Supported`_ 
    vmDirectPathGen2UnsupportedReason ([`str`_], optional):

       If `vmDirectPathGen2Supported`_ is false, this array will be populated with reasons for the lack of support (chosen from VmDirectPathGen2UnsupportedReason). If there is a reason for the lack of support that cannot be described by the available constants, `vmDirectPathGen2UnsupportedReasonExtended`_ will be populated with an additional explanation provided by the platform.Note that this list of reasons is not guaranteed to be exhaustive.If the reason "hostNptIncompatibleProduct" is provided, then that will be the only provided reason, as the host software is incapable of providing additional information.
    vmDirectPathGen2UnsupportedReasonExtended (`str`_, optional):

       If `vmDirectPathGen2Supported`_ is false, this property may contain an explanation provided by the platform, beyond the reasons (if any) enumerated in `vmDirectPathGen2UnsupportedReason`_ .
    supportedVmfsMajorVersion ([`int`_], optional):

       List of VMFS major versions supported by the host.
    vStorageCapable (`bool`_):

       Indicates whether the host supports vStorage Hardware acceleration.
    snapshotRelayoutSupported (`bool`_):

       Indicates whether this host supports unrestricted relocation of virtual machines with snapshots. Only needs to be true on the destination host for the unrestricted relocation to work. The full snapshot relocation does not restrict the layout of snapshot files or disks of the virtual machine, nor its power state. If the virtual machine is powered on, a storage vmotion will be performed to relocate its snapshots and disks.
    firewallIpRulesSupported (`bool`_, optional):

       Indicates whether this host supports ip address based restrictions in the firewall configuration.
    servicePackageInfoSupported (`bool`_, optional):

       Indicates whether this host supports package information in service configuration.
    maxHostRunningVms (`int`_, optional):

       The maximum number of virtual machines that can be run on the host. An unset value indicates that the value could not be obtained. In contrast to `maxRunningVMs`_ , this value is the minimum of (i) the maximum number supported by the hardware and (ii) the maximum number permitted by the host license.
    maxHostSupportedVcpus (`int`_, optional):

       The maximum number of virtual CPUs that can be run on the host. An unset value indicates that the value could not be obtained. In contrast to `maxSupportedVcpus`_ , this value is the minimum of (i) the maximum number supported by the hardware and (ii) the maximum number permitted by the host license.
    vmfsDatastoreMountCapable (`bool`_):

       Indicates whether the host is capable of mounting/unmounting VMFS datastores.
    eightPlusHostVmfsSharedAccessSupported (`bool`_):

       Indicates whether the host is capable of accessing a VMFS disk when there are eight or more hosts accessing the disk already.
    nestedHVSupported (`bool`_):

       Indicates whether the host supports nested hardware-assisted virtualization.
    vPMCSupported (`bool`_):

       Indicates whether the host supports vurtual CPU performance counters.
    interVMCommunicationThroughVMCISupported (`bool`_):

       Indicates whether the host supports VMCI for communication between virtual machines.
    scheduledHardwareUpgradeSupported (`bool`_, optional):

       Indicates whether the host supports scheduled hardware upgrades.See `scheduledHardwareUpgradeInfo`_ 
    featureCapabilitiesSupported (`bool`_):

       Indicated whether the host supports feature capabilities for EVC mode.
    latencySensitivitySupported (`bool`_):

       Indicates whether the host supports latency sensitivity for the virtual machines.
    storagePolicySupported (`bool`_, optional):

       Indicates that host supports Object-based Storage System and Storage-Profile based disk provisioning.
    accel3dSupported (`bool`_):

       Indicates if 3D hardware acceleration for virtual machines is supported.
    reliableMemoryAware (`bool`_, optional):

       Indicates that this host uses a reliable memory aware allocation policy.
    multipleNetworkStackInstanceSupported (`bool`_, optional):

       Indicates whether the host supports Multiple Instance TCP/IP stack
    vsanSupported (`bool`_, optional):

       Indicates whether the host supports VSAN functionality.See `HostVsanSystem`_ 
    vFlashSupported (`bool`_, optional):

       Indicates whether the host supports vFlash.
