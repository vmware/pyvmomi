
vim.vm.ConfigSpec
=================
  This data object type encapsulates configuration settings when creating or reconfiguring a virtual machine. To support incremental changes, these properties are all optional. If an optional property is unset, or any nested optional property is unset, the property will not be changed unless 'unset' is a valid value for the property. To determine whether 'unset' is a valid value for a particular property, refer to the documentation for that property.
:extends: vmodl.DynamicData_

Attributes:
    changeVersion (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       If specified, the changes are only applied if the current changeVersion matches the specified changeVersion. This field can be used to guard against updates that have happened between when configInfo is read and when it is applied.For more information about how configurations are uniquely identified, see `changeVersion <vim/vm/ConfigInfo.rst#changeVersion>`_ .
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Display name of the virtual machine.Any % (percent) character used in this name parameter must be escaped, unless it is used to start an escape sequence. Clients may also escape any other characters in this name parameter. Snapshots of virtual machines that have spaces in their names and are associated with ESX 2.x servers are not supported. Therefore, if you want the option to take snapshots of this virtual machine and you are associating it with an ESX 2.x server, do not use spaces in the name.Reconfigure privilege: VirtualMachine.Config.Rename
    version (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The version string for this virtual machine. This is used only while creating a new virtual machine, and can be updated by invoking `UpgradeVM_Task <vim/VirtualMachine.rst#upgradeVirtualHardware>`_ for this virtual machine.
    uuid (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       128-bit SMBIOS UUID of a virtual machine represented as a hexadecimal string in "12345678-abcd-1234-cdef-123456789abc" format.Normally, this property is not set by a client, allowing the Virtual Infrastructure environment to assign a UUID when the virtual machine is created. However, in some rare cases, such as a manual copy of a virtual machine, it may be necessary to set this property.Reconfigure privilege: VirtualMachine.Config.Settings
    instanceUuid (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       VirtualCenter-specific 128-bit UUID of a virtual machine, represented as a hexadecimal string. This identifier is used by VirtalCenter to uniquely identify all virtual machine instances in the Virtual Infrastructure environment, including those that may share the same SMBIOS UUID.Normally, this property is not set by a client, allowing the Virtual Infrastructure environment to assign or change it when VirtualCenter detects an identifier conflict between virtual machines. This identifier can be modified even when a virtual machine is powered on. Clients can specify that vCenter Server reassign a new identifier by a providing an empty string. Reassigning the identifer is not allowed for Fault Tolerance virtual machines.Reconfigure privilege: VirtualMachine.Config.Settings
    npivNodeWorldWideName ([`long <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       The NPIV node WWN to be assigned to a virtual machine. This property should only be used or set when the value of `npivWorldWideNameOp <vim/vm/ConfigSpec.rst#npivWorldWideNameOp>`_ property is "set". Otherwise, an `InvalidVmConfig <vim/fault/InvalidVmConfig.rst>`_ fault will be thrown. If the specified node WWN is currently being used by another virtual machine, a `VmWwnConflict <vim/fault/VmWwnConflict.rst>`_ fault will be thrown.For detail description on WWN, see `npivNodeWorldWideName <vim/vm/ConfigInfo.rst#npivNodeWorldWideName>`_ .Reconfigure privilege: VirtualMachine.Config.Settings.
    npivPortWorldWideName ([`long <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       The NPIV port WWN to be assigned to a virtual machine. This property should only be used or set when the value of `npivWorldWideNameOp <vim/vm/ConfigSpec.rst#npivWorldWideNameOp>`_ property is "set". Otherwise, an `InvalidVmConfig <vim/fault/InvalidVmConfig.rst>`_ fault will be thrown. If the specified port WWN is currently being used by another virtual machine, a `VmWwnConflict <vim/fault/VmWwnConflict.rst>`_ fault will be thrown.For detail description on WWN, see `npivPortWorldWideName <vim/vm/ConfigInfo.rst#npivPortWorldWideName>`_ .Reconfigure privilege: VirtualMachine.Config.Settings.
    npivWorldWideNameType (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       This property is used internally in the communication between the VirtualCenter server and ESX Server to indicate the source for `npivNodeWorldWideName <vim/vm/ConfigSpec.rst#npivNodeWorldWideName>`_ and `npivPortWorldWideName <vim/vm/ConfigSpec.rst#npivPortWorldWideName>`_ when `npivWorldWideNameOp <vim/vm/ConfigSpec.rst#npivWorldWideNameOp>`_ is "set". This property should only be set by the VirtualCenter server.If this property is set in a call to a VirtualCenter server, an `InvalidVmConfig <vim/fault/InvalidVmConfig.rst>`_ fault will always be thrown. In a call to an ESX Server host, an `InvalidVmConfig <vim/fault/InvalidVmConfig.rst>`_ fault will be thrown if the value of `npivWorldWideNameOp <vim/vm/ConfigSpec.rst#npivWorldWideNameOp>`_ is not set to "set".Reconfigure privilege: VirtualMachine.Config.Settings.
    npivDesiredNodeWwns (`short <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The NPIV node WWNs to be extended from the original list of WWN nummbers. This property should be set to desired number which is an aggregate of existing plus new numbers. Desired Node WWNs should always be greater than the existing number of node WWNs
    npivDesiredPortWwns (`short <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The NPIV port WWNs to be extended from the original list of WWN nummbers. This property should be set to desired number which is an aggregate of existing plus new numbers. Desired Node WWNs should always be greater than the existing number of port WWNs
    npivTemporaryDisabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       This property is used to enable or disable the NPIV capability on a desired virtual machine on a temporary basis. When this property is set NPIV Vport will not be instantiated by the VMX process of the Virtual Machine. When this property is set port WWNs and node WWNs in the VM configuration are preserved.Reconfigure privilege: VirtualMachine.Config.Settings.
    npivOnNonRdmDisks (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       This property is used to check whether the NPIV can be enabled on the Virtual machine with non-rdm disks in the configuration, so this is potentially not enabling npiv on vmfs disks. Also this property is used to check whether RDM is required to generate WWNs for a virtual machine.
    npivWorldWideNameOp (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The flag to indicate what type of NPIV WWN operation is going to be performed on the virtual machine. If unset, it indicates no change to existing NPIV WWN assignment (or not assigned) in the virtual machine.Reconfigure privilege: VirtualMachine.Config.Settings.See NpivWwnOp
    locationId (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       128-bit hash based on the virtual machine's configuration file location and the UUID of the host assigned to run the virtual machine.Normally, this property is not set by a client, allowing the Virtual Infrastructure environment to assign a location ID when the virtual machine is created. However, if the virtual machine's configuration file has been manually moved, it may be desirable to clear this property, setting it to an empty string, so the property is regenerated.Reconfigure privilege: VirtualMachine.Config.Settings
    guestId (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Short guest operating system identifier.Reconfigure privilege: VirtualMachine.Config.Settings
    alternateGuestName (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Full name for guest, if guestId is specified asotherorother-64.Reconfigure privilege: VirtualMachine.Config.Settings
    annotation (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       User-provided description of the virtual machine. Because this property is optional in the virtual machine configuration, it is necessary to pass an explicit empty string in a ConfigSpec object to remove an annotation that is already present in the `VirtualMachineConfigInfo <vim/vm/ConfigInfo.rst>`_ for a virtual machine.Reconfigure privilege: VirtualMachine.Config.Rename
    files (`vim.vm.FileInfo <vim/vm/FileInfo.rst>`_, optional):

       Information about virtual machine files.Reconfigure privilege: VirtualMachine.Config.Settings
    tools (`vim.vm.ToolsConfigInfo <vim/vm/ToolsConfigInfo.rst>`_, optional):

       Configuration of VMware Tools running in the guest operating system.Reconfigure privilege: VirtualMachine.Config.Settings
    flags (`vim.vm.FlagInfo <vim/vm/FlagInfo.rst>`_, optional):

       Additional flags for a virtual machine.Reconfigure privilege: VirtualMachine.Config.Settings
    consolePreferences (`vim.vm.ConsolePreferences <vim/vm/ConsolePreferences.rst>`_, optional):

       Legacy console viewer preferences that are used with power operations. For example, power on.Reconfigure privilege: VirtualMachine.Config.Settings
    powerOpInfo (`vim.vm.DefaultPowerOpInfo <vim/vm/DefaultPowerOpInfo.rst>`_, optional):

       Configuration for default power operations.Reconfigure privilege: VirtualMachine.Config.Settings
    numCPUs (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Number of virtual processors in a virtual machine.Reconfigure privilege: VirtualMachine.Config.CpuCount
    numCoresPerSocket (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Number of cores among which to distribute CPUs in this virtual machine.
    memoryMB (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Size of a virtual machine's memory, in MB.Reconfigure privilege: VirtualMachine.Config.Memory
    memoryHotAddEnabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Indicates whether or not memory can be added to the virtual machine while it is running. This attribute can only be set when the virtual machine is powered-off.Reconfigure privilege: VirtualMachine.Config.Memory
    cpuHotAddEnabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Indicates whether or not virtual processors can be added to the virtual machine while it is running. This attribute can only be set when the virtual machine is powered-off.Reconfigure privilege: VirtualMachine.Config.CpuCount
    cpuHotRemoveEnabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Indicates whether or not virtual processors can be removed from the virtual machine while it is running. This attribute can only be set when the virtual machine is powered-off.Reconfigure privilege: VirtualMachine.Config.CpuCount
    virtualICH7MPresent (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Does this virtual machine have Virtual Intel I/O Controller Hub 7
    virtualSMCPresent (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Does this virtual machine have System Management Controller
    deviceChange ([`vim.vm.device.VirtualDeviceSpec <vim/vm/device/VirtualDeviceSpec.rst>`_], optional):

       Set of virtual devices being modified by the configuration operation.Reconfigure privileges:
        * VirtualMachine.Config.Resource if setting the "shares" property of a new or existing VirtualDisk device
        * VirtualMachine.Config.RawDevice if adding, removing, or modifying a raw device (also required when creating a virtual machine)
        * VirtualMachine.Config.HostUSBDevice if adding, removing, or modifying a VirtualUSB device backed by a host USB device (also required when creating a virtual machine).
        * VirtualMachine.Interact.DeviceConnection if setting the "connectable" property of a connectable device
        * VirtualMachine.Interact.SetCDMedia if setting the "backing" property of a VirtualCdrom device
        * VirtualMachine.Interact.SetFloppyMedia if setting the "backing" property of a VirtualFloppy device
        * VirtualMachine.Config.EditDevice if setting any property of a non-CDROM non-Floppy device
        * VirtualMachine.Config.AddExistingDisk if adding a VirtualDisk, and the fileOperation is unset (also required when creating a virtual machine)
        * VirtualMachine.Config.AddNewDisk if adding a VirtualDisk and the fileOperation is set (also required when creating a virtual machine)
        * VirtualMachine.Config.RemoveDisk if removing a VirtualDisk device
        * VirtualMachine.Config.AddRemoveDevice if adding or removing any device other than disk, raw, or USB device.
        * Network.Assign if if setting the "backing" property of a VirtualEthernetCard device.
        * 
    cpuAllocation (`vim.ResourceAllocationInfo <vim/ResourceAllocationInfo.rst>`_, optional):

       Resource limits for CPU.Reconfigure privilege: VirtualMachine.Config.Resource
    memoryAllocation (`vim.ResourceAllocationInfo <vim/ResourceAllocationInfo.rst>`_, optional):

       Resource limits for memory.Reconfigure privilege: VirtualMachine.Config.Resource
    latencySensitivity (`vim.LatencySensitivity <vim/LatencySensitivity.rst>`_, optional):

       The latency-sensitivity setting of the virtual machine.Reconfigure privilege: VirtualMachine.Config.Resource
    cpuAffinity (`vim.vm.AffinityInfo <vim/vm/AffinityInfo.rst>`_, optional):

       Affinity settings for CPU.Reconfigure privilege: VirtualMachine.Config.Resource
    memoryAffinity (`vim.vm.AffinityInfo <vim/vm/AffinityInfo.rst>`_, optional):

       Affinity settings for memory.Reconfigure privilege: VirtualMachine.Config.Resource
    networkShaper (`vim.vm.NetworkShaperInfo <vim/vm/NetworkShaperInfo.rst>`_, optional):

       Resource limits for network.Reconfigure privilege: VirtualMachine.Config.Resource
    cpuFeatureMask ([`vim.vm.ConfigSpec.CpuIdInfoSpec <vim/vm/ConfigSpec/CpuIdInfoSpec.rst>`_], optional):

       Specifies the CPU feature compatibility masks.Reconfigure privilege: VirtualMachine.Config.Settings
    extraConfig ([`vim.option.OptionValue <vim/option/OptionValue.rst>`_], optional):

       Additional configuration information for the virtual machine. This describes a set of modifications to the additional options. If the key is already present, it will be reset with the new value provided. Otherwise, a new option is added. Keys with empty values will be removed.Configuration keys that would conflict with parameters that are explicitly configurable through other fields in the ConfigSpec object are silently ignored.Reconfigure privilege: VirtualMachine.Config.AdvancedConfig (also required when setting this property while creating a virtual machine)
    swapPlacement (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Virtual machine swapfile placement policy. This may only be set if the `swapPlacementSupported <vim/vm/Capability.rst#swapPlacementSupported>`_ capability is true for this virtual machine. Any change to this policy will take effect the next time the virtual machine powers on, resumes from a suspended state, or migrates while powered on.Reconfigure privilege: VirtualMachine.Config.SwapPlacement (also required when setting this property while creating a virtual machine)See `VirtualMachineConfigInfoSwapPlacementType <vim/vm/ConfigInfo/SwapPlacementType.rst>`_ 
    bootOptions (`vim.vm.BootOptions <vim/vm/BootOptions.rst>`_, optional):

       Settings that control the boot behavior of the virtual machine. These settings take effect during the next power-on of the virtual machine.Reconfigure privilege: VirtualMachine.Config.Settings
    vAppConfig (`vim.vApp.VmConfigSpec <vim/vApp/VmConfigSpec.rst>`_, optional):

       Configuration of vApp meta-data for a virtual machine
    ftInfo (`vim.vm.FaultToleranceConfigInfo <vim/vm/FaultToleranceConfigInfo.rst>`_, optional):

       Fault Tolerance settings for this virtual machine.
    vAppConfigRemoved (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Set to true, if the vApp configuration should be removedReconfigure privilege: VApp.ApplicationConfig
    vAssertsEnabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Indicates whether user-configured virtual asserts will be triggered during virtual machine replay. This setting takes effect during the next replay of the virtual machine.Enabling this functionality can potentially cause some performance overhead during virtual machine execution.
    changeTrackingEnabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Setting to control enabling/disabling changed block tracking for the virtual disks of this VM. This may only be set if the `changeTrackingSupported <vim/vm/Capability.rst#changeTrackingSupported>`_ capability is true for this virtual machine. Any change to this property will take effect the next time the virtual machine powers on, resumes from a suspended state, performs a snapshot create/delete/revert operation or migrates while powered on.Reconfigure privilege: VirtualMachine.Config.ChangeTracking (also required when setting this property while creating a virtual machine)
    firmware (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Set the desired firmware type for this Virtual Machine. Possible values are described in `GuestOsDescriptorFirmwareType <vim/vm/GuestOsDescriptor/FirmwareType.rst>`_ 
    maxMksConnections (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       If set, this setting limits the maximum number of active remote display connections that the virtual machine will support to the specified value.Reconfigure privilege: VirtualMachine.Config.MksControl
    guestAutoLockEnabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       If set to True, this causes the guest operating system to automatically logout any active sessions whenever there are no remote display connections open to the virtual machine.Reconfigure privilege: VirtualMachine.Config.MksControl
    managedBy (`vim.ext.ManagedByInfo <vim/ext/ManagedByInfo.rst>`_, optional):

       Specifies that this VM is managed by a VC Extension.This information is primarily used in the Client to show a custom icon for managed virtual machines, and a description of the function of the virtual machine. If no extension can be found with the extension key in the `managedBy <vim/ext/ManagedByInfo.rst>`_ object, or the type is not found in the `managedEntityInfo <vim/Extension.rst#managedEntityInfo>`_ list of the extension, the default virtual machine icon is used, and no description is shown.Reconfigure privilege: VirtualMachine.Config.ManagedBy
    memoryReservationLockedToMax (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       If set true, memory resource reservation for this virtual machine will always be equal to the virtual machine's memory size; increases in memory size will be rejected when a corresponding reservation increase is not possible. This feature may only be enabled if it is currently possible to reserve all of the virtual machine's memory.Reconfigure privilege: VirtualMachine.Config.Resource
    nestedHVEnabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Specifies that this VM will use nested hardware-assisted virtualization.Reconfigure privilege: VirtualMachine.Config.Settings
    vPMCEnabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Specifies that this VM will have vurtual CPU performance counters enabled.Reconfigure privilege: VirtualMachine.Config.Settings
    scheduledHardwareUpgradeInfo (`vim.vm.ScheduledHardwareUpgradeInfo <vim/vm/ScheduledHardwareUpgradeInfo.rst>`_, optional):

       Configuration of scheduled hardware upgrades.See `ScheduledHardwareUpgradeInfo <vim/vm/ScheduledHardwareUpgradeInfo.rst>`_ 
    vmProfile ([`vim.vm.ProfileSpec <vim/vm/ProfileSpec.rst>`_], optional):

       Virtual Machine Profile requirement. Profiles are solution specific. Profile Based Storage Management is a vSphere server extension. API users who want to provision VMs using Storage Profiles, need to interact with it. This is an optional parameter and if user doesn't specify profile, the default behavior will apply.
