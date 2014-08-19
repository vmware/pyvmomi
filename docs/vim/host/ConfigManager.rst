
vim.host.ConfigManager
======================
  This data object type describes the configuration of a host across products and versions.
:extends: vmodl.DynamicData_

Attributes:
    cpuScheduler (`vim.host.CpuSchedulerSystem <vim/host/CpuSchedulerSystem.rst>`_, optional):

       The CPU scheduler that determines which threads execute on a CPU at any given time.
    datastoreSystem (`vim.host.DatastoreSystem <vim/host/DatastoreSystem.rst>`_, optional):

       The datastore manager.
    memoryManager (`vim.host.MemoryManagerSystem <vim/host/MemoryManagerSystem.rst>`_, optional):

       The memory manager on the host.
    storageSystem (`vim.host.StorageSystem <vim/host/StorageSystem.rst>`_, optional):

       The storage configuration.
    networkSystem (`vim.host.NetworkSystem <vim/host/NetworkSystem.rst>`_, optional):

       The network system configuration.
    vmotionSystem (`vim.host.VMotionSystem <vim/host/VMotionSystem.rst>`_, optional):

       The VMotion configuration.
    virtualNicManager (`vim.host.VirtualNicManager <vim/host/VirtualNicManager.rst>`_, optional):

       The VirtualNic configuration.
    serviceSystem (`vim.host.ServiceSystem <vim/host/ServiceSystem.rst>`_, optional):

       The configuration of the host services (for example, SSH, FTP, and Telnet).
    firewallSystem (`vim.host.FirewallSystem <vim/host/FirewallSystem.rst>`_, optional):

       The firewall configuration.
    advancedOption (`vim.option.OptionManager <vim/option/OptionManager.rst>`_, optional):

       Advanced options.
    diagnosticSystem (`vim.host.DiagnosticSystem <vim/host/DiagnosticSystem.rst>`_, optional):

       The diagnostic for the ESX Server system.
    autoStartManager (`vim.host.AutoStartManager <vim/host/AutoStartManager.rst>`_, optional):

       Auto-start and auto-stop configuration.
    snmpSystem (`vim.host.SnmpSystem <vim/host/SnmpSystem.rst>`_, optional):

       Snmp configuration
    dateTimeSystem (`vim.host.DateTimeSystem <vim/host/DateTimeSystem.rst>`_, optional):

       DateTime configuration
    patchManager (`vim.host.PatchManager <vim/host/PatchManager.rst>`_, optional):

       Host patch management.
    imageConfigManager (`vim.host.ImageConfigManager <vim/host/ImageConfigManager.rst>`_, optional):

       Host image configuration management.
    bootDeviceSystem (`vim.host.BootDeviceSystem <vim/host/BootDeviceSystem.rst>`_, optional):

       Boot device order management.
    firmwareSystem (`vim.host.FirmwareSystem <vim/host/FirmwareSystem.rst>`_, optional):

       Firmware management.
    healthStatusSystem (`vim.host.HealthStatusSystem <vim/host/HealthStatusSystem.rst>`_, optional):

       System health status manager.
    pciPassthruSystem (`vim.host.PciPassthruSystem <vim/host/PciPassthruSystem.rst>`_, optional):

       PciDeviceSystem for passthru.
    licenseManager (`vim.LicenseManager <vim/LicenseManager.rst>`_, optional):

       License manager
    kernelModuleSystem (`vim.host.KernelModuleSystem <vim/host/KernelModuleSystem.rst>`_, optional):

       Kernel module configuration management.
    authenticationManager (`vim.host.AuthenticationManager <vim/host/AuthenticationManager.rst>`_, optional):

       Authentication method configuration - for example, for Active Directory membership.
    powerSystem (`vim.host.PowerSystem <vim/host/PowerSystem.rst>`_, optional):

       Power System manager.
    cacheConfigurationManager (`vim.host.CacheConfigurationManager <vim/host/CacheConfigurationManager.rst>`_, optional):

       Host solid state drive cache configuration manager.
    esxAgentHostManager (`vim.host.EsxAgentHostManager <vim/host/EsxAgentHostManager.rst>`_, optional):

       Esx Agent resource configuration manager
    iscsiManager (`vim.host.IscsiManager <vim/host/IscsiManager.rst>`_, optional):

       Iscsi Management Operations managed entity
    vFlashManager (`vim.host.VFlashManager <vim/host/VFlashManager.rst>`_, optional):

       vFlash Manager
    vsanSystem (`vim.host.VsanSystem <vim/host/VsanSystem.rst>`_, optional):

       VsanSystem managed entity.
    graphicsManager (`vim.host.GraphicsManager <vim/host/GraphicsManager.rst>`_, optional):

       Host graphics manager.
    vsanInternalSystem (`vim.host.VsanInternalSystem <vim/host/VsanInternalSystem.rst>`_, optional):

       VsanInternalSystem managed entity.
