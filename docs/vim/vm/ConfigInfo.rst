.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _long: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _short: https://docs.python.org/2/library/stdtypes.html

.. _datetime: https://docs.python.org/2/library/stdtypes.html

.. _managedBy: ../../vim/vm/ConfigSpec.rst#managedBy

.. _guestFullName: ../../vim/vm/ConfigInfo.rst#guestFullName

.. _vim.vm.FlagInfo: ../../vim/vm/FlagInfo.rst

.. _vim.vm.FileInfo: ../../vim/vm/FileInfo.rst

.. _GuestOsDescriptor: ../../vim/vm/GuestOsDescriptor.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.vm.BootOptions: ../../vim/vm/BootOptions.rst

.. _alternateGuestName: ../../vim/vm/ConfigInfo.rst#alternateGuestName

.. _vim.host.CpuIdInfo: ../../vim/host/CpuIdInfo.rst

.. _memoryHotAddEnabled: ../../vim/vm/ConfigSpec.rst#memoryHotAddEnabled

.. _vim.vm.AffinityInfo: ../../vim/vm/AffinityInfo.rst

.. _vFlashCacheAllocation: ../../vim/vm/RuntimeInfo.rst#vFlashCacheAllocation

.. _vim.ext.ManagedByInfo: ../../vim/ext/ManagedByInfo.rst

.. _npivNodeWorldWideName: ../../vim/vm/ConfigInfo.rst#npivNodeWorldWideName

.. _npivPortWorldWideName: ../../vim/vm/ConfigInfo.rst#npivPortWorldWideName

.. _vim.vApp.VmConfigInfo: ../../vim/vApp/VmConfigInfo.rst

.. _vim.LatencySensitivity: ../../vim/LatencySensitivity.rst

.. _vim.option.OptionValue: ../../vim/option/OptionValue.rst

.. _swapPlacementSupported: ../../vim/vm/Capability.rst#swapPlacementSupported

.. _vim.vm.ToolsConfigInfo: ../../vim/vm/ToolsConfigInfo.rst

.. _vim.vm.VirtualHardware: ../../vim/vm/VirtualHardware.rst

.. _vim.vm.NetworkShaperInfo: ../../vim/vm/NetworkShaperInfo.rst

.. _vim.vm.ConsolePreferences: ../../vim/vm/ConsolePreferences.rst

.. _vim.vm.DefaultPowerOpInfo: ../../vim/vm/DefaultPowerOpInfo.rst

.. _vim.ResourceAllocationInfo: ../../vim/ResourceAllocationInfo.rst

.. _ScheduledHardwareUpgradeInfo: ../../vim/vm/ScheduledHardwareUpgradeInfo.rst

.. _GuestOsDescriptorFirmwareType: ../../vim/vm/GuestOsDescriptor/FirmwareType.rst

.. _vim.vm.ConfigInfo.OverheadInfo: ../../vim/vm/ConfigInfo/OverheadInfo.rst

.. _VirtualMachineGuestOsIdentifier: ../../vim/vm/GuestOsDescriptor/GuestOsIdentifier.rst

.. _vim.vm.FaultToleranceConfigInfo: ../../vim/vm/FaultToleranceConfigInfo.rst

.. _vim.vm.ConfigInfo.DatastoreUrlPair: ../../vim/vm/ConfigInfo/DatastoreUrlPair.rst

.. _vim.vm.ScheduledHardwareUpgradeInfo: ../../vim/vm/ScheduledHardwareUpgradeInfo.rst

.. _VirtualMachineConfigInfoNpivWwnType: ../../vim/vm/ConfigInfo/NpivWwnType.rst

.. _VirtualMachineConfigInfoSwapPlacementType: ../../vim/vm/ConfigInfo/SwapPlacementType.rst


vim.vm.ConfigInfo
=================
  The ConfigInfo data object type encapsulates the configuration settings and virtual hardware for a virtual machine. This type holds all the information that is present in the .vmx configuration file for the virtual machine.
:extends: vmodl.DynamicData_

Attributes:
    changeVersion (`str`_):

       The changeVersion is a unique identifier for a given version of the configuration. Each change to the configuration updates this value. This is typically implemented as an ever increasing count or a time-stamp. However, a client should always treat this as an opaque string.
    modified (`datetime`_):

       Last time a virtual machine's configuration was modified.
    name (`str`_):

       Display name of the virtual machine.Any / (slash), \ (backslash), character used in this name element is escaped. Similarly, any % (percent) character used in this name element is escaped, unless it is used to start an escape sequence. A slash is escaped as %2F or %2f. A backslash is escaped as %5C or %5c, and a percent is escaped as %25.
    guestFullName (`str`_):

       This is the full name of the guest operating system for the virtual machine. For example: Windows 2000 Professional.See `alternateGuestName`_ 
    version (`str`_):

       The version string for this virtual machine.
    uuid (`str`_):

       128-bit SMBIOS UUID of a virtual machine represented as a hexadecimal string in "12345678-abcd-1234-cdef-123456789abc" format.
    instanceUuid (`str`_, optional):

       VirtualCenter-specific 128-bit UUID of a virtual machine, represented as a hexademical string. This identifier is used by VirtualCenter to uniquely identify all virtual machine instances, including those that may share the same SMBIOS UUID.
    npivNodeWorldWideName (`long`_, optional):

       A 64-bit node WWN (World Wide Name). These WWNs are paired with the `npivPortWorldWideName`_ to be used by the NPIV VPORTs instantiated for the virtual machine on the physical HBAs of the host. A pair of node and port WWNs serves as a unique identifier in accessing a LUN, so that it can be monitored or controlled by the storage administrator.If this property contains a single node WWN, the same node WWN is used to pair with all port WWNs listed in `npivPortWorldWideName`_ . If this property or `npivPortWorldWideName`_ is empty or unset, NPIV WWN is disabled for the virtual machine.
    npivPortWorldWideName (`long`_, optional):

       A 64-bit port WWN (World Wide Name). For detail description on WWN, see `npivNodeWorldWideName`_ .
    npivWorldWideNameType (`str`_, optional):

       The source that provides/generates the assigned WWNs.See `VirtualMachineConfigInfoNpivWwnType`_ 
    npivDesiredNodeWwns (`short`_, optional):

       The NPIV node WWNs to be extended from the original list of WWN nummbers. This property should be set to desired number which is an aggregate of existing plus new numbers. Desired Node WWNs should always be greater than the existing number of node WWNs
    npivDesiredPortWwns (`short`_, optional):

       The NPIV port WWNs to be extended from the original list of WWN nummbers. This property should be set to desired number which is an aggregate of existing plus new numbers. Desired Node WWNs should always be greater than the existing number of port WWNs
    npivTemporaryDisabled (`bool`_, optional):

       This property is used to enable or disable the NPIV capability on a desired virtual machine on a temporary basis. When this property is set NPIV Vport will not be instantiated by the VMX process of the Virtual Machine. When this property is set port WWNs and node WWNs in the VM configuration are preserved.
    npivOnNonRdmDisks (`bool`_, optional):

       This property is used to check whether the NPIV can be enabled on the Virtual machine with non-rdm disks in the configuration, so this is potentially not enabling npiv on vmfs disks. Also this property is used to check whether RDM is required to generate WWNs for a virtual machine.
    locationId (`str`_, optional):

       Hash incorporating the virtual machine's config file location and the UUID of the host assigned to run the virtual machine.
    template (`bool`_):

       Flag indicating whether or not a virtual machine is a template.
    guestId (`str`_):

       Guest operating system configured on a virtual machine. This is a guest identifier that can be used to access the `GuestOsDescriptor`_ list for information about default configuration. For more information on possible values, see `VirtualMachineGuestOsIdentifier`_ .
    alternateGuestName (`str`_):

       Used as display name for the operating system if guestId isotherorother-64.See `guestFullName`_ 
    annotation (`str`_, optional):

       Description for the virtual machine.
    files (`vim.vm.FileInfo`_):

       Information about the files associated with a virtual machine. This information does not include files for specific virtual disks or snapshots.
    tools (`vim.vm.ToolsConfigInfo`_, optional):

       Configuration of VMware Tools running in the guest operating system.
    flags (`vim.vm.FlagInfo`_):

       Additional flags for a virtual machine.
    consolePreferences (`vim.vm.ConsolePreferences`_, optional):

       Legacy console viewer preferences when doing power operations.
    defaultPowerOps (`vim.vm.DefaultPowerOpInfo`_):

       Configuration of default power operations.
    hardware (`vim.vm.VirtualHardware`_):

       Processor, memory, and virtual devices for a virtual machine.
    cpuAllocation (`vim.ResourceAllocationInfo`_, optional):

       Resource limits for CPU.
    memoryAllocation (`vim.ResourceAllocationInfo`_, optional):

       Resource limits for memory.
    latencySensitivity (`vim.LatencySensitivity`_, optional):

       The latency-sensitivity of the virtual machine.
    memoryHotAddEnabled (`bool`_, optional):

       Whether memory can be added while this virtual machine is running.
    cpuHotAddEnabled (`bool`_, optional):

       Whether virtual processors can be added while this virtual machine is running.
    cpuHotRemoveEnabled (`bool`_, optional):

       Whether virtual processors can be removed while this virtual machine is running.
    hotPlugMemoryLimit (`long`_, optional):

       The maximum amount of memory, in MB, than can be added to a running virtual machine. This value is determined by the virtual machine and is specified only if `memoryHotAddEnabled`_ is set to true.
    hotPlugMemoryIncrementSize (`long`_, optional):

       Memory, in MB that can be added to a running virtual machine must be in increments of this value and needs be a multiple of this value. This value is determined by the virtual machine and is specified only if `memoryHotAddEnabled`_ has been set to true.
    cpuAffinity (`vim.vm.AffinityInfo`_, optional):

       Affinity settings for CPU.
    memoryAffinity (`vim.vm.AffinityInfo`_, optional):

       Affinity settings for memory.
    networkShaper (`vim.vm.NetworkShaperInfo`_, optional):

       Resource limits for network.
    extraConfig (`vim.option.OptionValue`_, optional):

       Additional configuration information for the virtual machine.
    cpuFeatureMask (`vim.host.CpuIdInfo`_, optional):

       Specifies CPU feature compatibility masks that override the defaults from the `GuestOsDescriptor`_ of the virtual machine's guest OS.
    datastoreUrl (`vim.vm.ConfigInfo.DatastoreUrlPair`_, optional):

       Enumerates the set of datastores that this virtual machine is stored on, as well as the URL identification for each of these.Changes to datastores do not generate property updates on this property. However, when this property is retrieved it returns the current datastore information.
    swapPlacement (`str`_, optional):

       Virtual machine swapfile placement policy. This will be unset if the virtual machine's `swapPlacementSupported`_ capability is false. If swapPlacementSupported is true, the default policy is "inherit".See `VirtualMachineConfigInfoSwapPlacementType`_ 
    bootOptions (`vim.vm.BootOptions`_, optional):

       Configuration options for the boot behavior of the virtual machine.
    ftInfo (`vim.vm.FaultToleranceConfigInfo`_, optional):

       Fault Tolerance settings for this virtual machine.
    vAppConfig (`vim.vApp.VmConfigInfo`_, optional):

       vApp meta-data for the virtual machine
    vAssertsEnabled (`bool`_, optional):

       Indicates whether user-configured virtual asserts will be triggered during virtual machine replay.
    changeTrackingEnabled (`bool`_, optional):

       Indicates whether changed block tracking for this VM's disks is active.
    firmware (`str`_, optional):

       Information about firmware type for this Virtual Machine. Possible values are described in `GuestOsDescriptorFirmwareType`_ 
    maxMksConnections (`int`_, optional):

       Indicates the maximum number of active remote display connections that the virtual machine will support.
    guestAutoLockEnabled (`bool`_, optional):

       Indicates whether the guest operating system will logout any active sessions whenever there are no remote display connections open to the virtual machine.
    managedBy (`vim.ext.ManagedByInfo`_, optional):

       Specifies that this VM is managed by a VC Extension. See the `managedBy`_ property in the ConfigSpec for more details.
    memoryReservationLockedToMax (`bool`_, optional):

       If set true, memory resource reservation for this virtual machine will always be equal to the virtual machine's memory size; increases in memory size will be rejected when a corresponding reservation increase is not possible.
    initialOverhead (`vim.vm.ConfigInfo.OverheadInfo`_, optional):

       Set of values to be used only to perform admission control when determining if a host has sufficient resources for the virtual machine to power on.
    nestedHVEnabled (`bool`_, optional):

       Indicates whether this VM is configured to use nested hardware-assisted virtualization.
    vPMCEnabled (`bool`_, optional):

       Indicates whether this VM have vurtual CPU performance counters enabled.
    scheduledHardwareUpgradeInfo (`vim.vm.ScheduledHardwareUpgradeInfo`_, optional):

       Configuration of scheduled hardware upgrades and result from last attempt to run scheduled hardware upgrade.See `ScheduledHardwareUpgradeInfo`_ 
    vFlashCacheReservation (`long`_, optional):

       Specifies the total vFlash resource reservation for the vFlash caches associated with this VM's virtual disks, in bytes. This reservation must be allocated to power on the VM. See `vFlashCacheAllocation`_ for allocated reservation when VM is powered on.
