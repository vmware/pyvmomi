
vim.host.ConfigInfo
===================
  This data object type encapsulates a typical set of host configuration information that is useful for displaying and configuring a host.VirtualCenter can retrieve this set of information very efficiently even for a large set of hosts.
:extends: vmodl.DynamicData_

Attributes:
    host (`vim.HostSystem <vim/HostSystem.rst>`_):

       A reference to a managed object on a host.
    product (`vim.AboutInfo <vim/AboutInfo.rst>`_):

       Information about a product.
    hyperThread (`vim.host.CpuSchedulerSystem.HyperThreadScheduleInfo <vim/host/CpuSchedulerSystem/HyperThreadScheduleInfo.rst>`_, optional):

       If hyperthreading is supported, this is the CPU configuration for optimizing hyperthreading.
    consoleReservation (`vim.host.MemoryManagerSystem.ServiceConsoleReservationInfo <vim/host/MemoryManagerSystem/ServiceConsoleReservationInfo.rst>`_, optional):

       Memory configuration.
    virtualMachineReservation (`vim.host.MemoryManagerSystem.VirtualMachineReservationInfo <vim/host/MemoryManagerSystem/VirtualMachineReservationInfo.rst>`_, optional):

       Virtual machine memory configuration.
    storageDevice (`vim.host.StorageDeviceInfo <vim/host/StorageDeviceInfo.rst>`_, optional):

       Storage system information.
    multipathState (`vim.host.MultipathStateInfo <vim/host/MultipathStateInfo.rst>`_, optional):

       Storage multipath state information.
    fileSystemVolume (`vim.host.FileSystemVolumeInfo <vim/host/FileSystemVolumeInfo.rst>`_, optional):

       Storage system file system volume information.
    systemFile ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       Datastore paths of files used by the host system on mounted volumes, for instance, the COS vmdk file of the host. For information on datastore paths, see `Datastore <vim/Datastore.rst>`_ .
    network (`vim.host.NetworkInfo <vim/host/NetworkInfo.rst>`_, optional):

       Network system information.
    vmotion (`vim.host.VMotionInfo <vim/host/VMotionInfo.rst>`_, optional):

       VMotion system information.
    virtualNicManagerInfo (`vim.host.VirtualNicManagerInfo <vim/host/VirtualNicManagerInfo.rst>`_, optional):

       VirtualNic manager information.
    capabilities (`vim.host.NetCapabilities <vim/host/NetCapabilities.rst>`_, optional):

       Capability vector indicating the available network features.
    datastoreCapabilities (`vim.host.DatastoreSystem.Capabilities <vim/host/DatastoreSystem/Capabilities.rst>`_, optional):

       Capability vector indicating available datastore features.
    offloadCapabilities (`vim.host.NetOffloadCapabilities <vim/host/NetOffloadCapabilities.rst>`_, optional):

       capabilities to offload operations either to the host or to physical hardware when a virtual machine is transmitting on a network
    service (`vim.host.ServiceInfo <vim/host/ServiceInfo.rst>`_, optional):

       Host service configuration.
    firewall (`vim.host.FirewallInfo <vim/host/FirewallInfo.rst>`_, optional):

       Firewall configuration.
    autoStart (`vim.host.AutoStartManager.Config <vim/host/AutoStartManager/Config.rst>`_, optional):

       AutoStart configuration.
    activeDiagnosticPartition (`vim.host.DiagnosticPartition <vim/host/DiagnosticPartition.rst>`_, optional):

       The diagnostic partition that will be set as the current diagnostic partition on the host.
    option ([`vim.option.OptionValue <vim/option/OptionValue.rst>`_], optional):

       Host configuration options as defined by the `OptionValue <vim/option/OptionValue.rst>`_ data object type.
    optionDef ([`vim.option.OptionDef <vim/option/OptionDef.rst>`_], optional):

       A list of supported options.
    datastorePrincipal (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Datastore principal user
    localSwapDatastore (`vim.Datastore <vim/Datastore.rst>`_, optional):

       Datastore visible to this host that may be used to store virtual machine swapfiles, for virtual machines executing on this host. The value of this property is set or unset by invoking `UpdateLocalSwapDatastore <vim/host/DatastoreSystem.rst#updateLocalSwapDatastore>`_ . The policy for using this datastore is determined by the compute resource configuration's `vmSwapPlacement <vim/ComputeResource/ConfigInfo.rst#vmSwapPlacement>`_ property in concert with each individual virtual machine configuration's `swapPlacement <vim/vm/ConfigInfo.rst#swapPlacement>`_ property.Note: Using a host-specific swap location may degrade VMotion performance.
    systemSwapConfiguration (`vim.host.SystemSwapConfiguration <vim/host/SystemSwapConfiguration.rst>`_, optional):

       The system swap configuration specifies which options are currently enabled.See `HostSystemSwapConfiguration <vim/host/SystemSwapConfiguration.rst>`_ 
    systemResources (`vim.host.SystemResourceInfo <vim/host/SystemResourceInfo.rst>`_, optional):

       Reference for the system resource hierarchy, used for configuring the set of resources reserved to the system and unavailable to virtual machines.
    dateTimeInfo (`vim.host.DateTimeInfo <vim/host/DateTimeInfo.rst>`_, optional):

       Date/Time related configuration
    flags (`vim.host.FlagInfo <vim/host/FlagInfo.rst>`_, optional):

       Additional flags for a host.
    adminDisabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       If the flag is true, the permissions on the host have been modified such that it is only accessible through local console or an authorized centralized management application. This flag is affected by the `EnterLockdownMode <vim/HostSystem.rst#enterLockdownMode>`_ and `ExitLockdownMode <vim/HostSystem.rst#exitLockdownMode>`_ operations.This flag is supported in VirtualCenter only. The value returned from host should be ignored.See `EnterLockdownMode <vim/HostSystem.rst#enterLockdownMode>`_ See `ExitLockdownMode <vim/HostSystem.rst#exitLockdownMode>`_ 
    ipmi (`vim.host.IpmiInfo <vim/host/IpmiInfo.rst>`_, optional):

       IPMI (Intelligent Platform Management Interface) info for the host.
    sslThumbprintInfo (`vim.host.SslThumbprintInfo <vim/host/SslThumbprintInfo.rst>`_, optional):

       SSL Thumbprint info for hosts registered on this host.
    sslThumbprintData ([`vim.host.SslThumbprintInfo <vim/host/SslThumbprintInfo.rst>`_], optional):

       SSL Thumbprints registered on this host.
    certificate ([`int <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       Full Host Certificate in PEM format, if known
    pciPassthruInfo ([`vim.host.PciPassthruInfo <vim/host/PciPassthruInfo.rst>`_], optional):

       PCI passthrough information.
    authenticationManagerInfo (`vim.host.AuthenticationManagerInfo <vim/host/AuthenticationManagerInfo.rst>`_, optional):

       Current authentication configuration.
    featureVersion ([`vim.host.FeatureVersionInfo <vim/host/FeatureVersionInfo.rst>`_], optional):

       List of feature-specific version information. Each element refers to the version information for a specific feature.
    powerSystemCapability (`vim.host.PowerSystem.Capability <vim/host/PowerSystem/Capability.rst>`_, optional):

       Host power management capability.
    powerSystemInfo (`vim.host.PowerSystem.Info <vim/host/PowerSystem/Info.rst>`_, optional):

       Host power management information.
    cacheConfigurationInfo ([`vim.host.CacheConfigurationManager.CacheConfigurationInfo <vim/host/CacheConfigurationManager/CacheConfigurationInfo.rst>`_], optional):

       Host solid stats drive cache configuration information.
    wakeOnLanCapable (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Indicates if a host is wake on lan capable. A host is deemed wake on lan capable if there exists at least one physical network card that is both backing the vmotion interface and is itself wake on lan capable.
    featureCapability ([`vim.host.FeatureCapability <vim/host/FeatureCapability.rst>`_], optional):

       Array of the feature capabilities that the host has. This is not expected to change after the host boots. It may change between reboots in the case BIOS options are changed, or hardware, or firmware is changed or upgraded.
    maskedFeatureCapability ([`vim.host.FeatureCapability <vim/host/FeatureCapability.rst>`_], optional):

       Array of the feature capabilities that the host has after the mask has been applied.
    vFlashConfigInfo (`vim.host.VFlashManager.VFlashConfigInfo <vim/host/VFlashManager/VFlashConfigInfo.rst>`_, optional):

       Host vFlash configuration information
    vsanHostConfig (`vim.vsan.host.ConfigInfo <vim/vsan/host/ConfigInfo.rst>`_, optional):

       VSAN configuration for a host.
    graphicsInfo ([`vim.host.GraphicsInfo <vim/host/GraphicsInfo.rst>`_], optional):

       The list of graphics devices available on this host.
