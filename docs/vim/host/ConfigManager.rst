.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.LicenseManager: ../../vim/LicenseManager.rst

.. _vim.host.VsanSystem: ../../vim/host/VsanSystem.rst

.. _vim.host.SnmpSystem: ../../vim/host/SnmpSystem.rst

.. _vim.host.PowerSystem: ../../vim/host/PowerSystem.rst

.. _vim.host.PatchManager: ../../vim/host/PatchManager.rst

.. _vim.host.IscsiManager: ../../vim/host/IscsiManager.rst

.. _vim.host.StorageSystem: ../../vim/host/StorageSystem.rst

.. _vim.host.VFlashManager: ../../vim/host/VFlashManager.rst

.. _vim.host.ServiceSystem: ../../vim/host/ServiceSystem.rst

.. _vim.host.VMotionSystem: ../../vim/host/VMotionSystem.rst

.. _vim.host.NetworkSystem: ../../vim/host/NetworkSystem.rst

.. _vim.host.FirmwareSystem: ../../vim/host/FirmwareSystem.rst

.. _vim.host.DateTimeSystem: ../../vim/host/DateTimeSystem.rst

.. _vim.host.FirewallSystem: ../../vim/host/FirewallSystem.rst

.. _vim.host.GraphicsManager: ../../vim/host/GraphicsManager.rst

.. _vim.host.DatastoreSystem: ../../vim/host/DatastoreSystem.rst

.. _vim.option.OptionManager: ../../vim/option/OptionManager.rst

.. _vim.host.BootDeviceSystem: ../../vim/host/BootDeviceSystem.rst

.. _vim.host.AutoStartManager: ../../vim/host/AutoStartManager.rst

.. _vim.host.DiagnosticSystem: ../../vim/host/DiagnosticSystem.rst

.. _vim.host.PciPassthruSystem: ../../vim/host/PciPassthruSystem.rst

.. _vim.host.VirtualNicManager: ../../vim/host/VirtualNicManager.rst

.. _vim.host.KernelModuleSystem: ../../vim/host/KernelModuleSystem.rst

.. _vim.host.CpuSchedulerSystem: ../../vim/host/CpuSchedulerSystem.rst

.. _vim.host.ImageConfigManager: ../../vim/host/ImageConfigManager.rst

.. _vim.host.VsanInternalSystem: ../../vim/host/VsanInternalSystem.rst

.. _vim.host.HealthStatusSystem: ../../vim/host/HealthStatusSystem.rst

.. _vim.host.EsxAgentHostManager: ../../vim/host/EsxAgentHostManager.rst

.. _vim.host.MemoryManagerSystem: ../../vim/host/MemoryManagerSystem.rst

.. _vim.host.AuthenticationManager: ../../vim/host/AuthenticationManager.rst

.. _vim.host.CacheConfigurationManager: ../../vim/host/CacheConfigurationManager.rst


vim.host.ConfigManager
======================
  This data object type describes the configuration of a host across products and versions.
:extends: vmodl.DynamicData_

Attributes:
    cpuScheduler (`vim.host.CpuSchedulerSystem`_, optional):

       The CPU scheduler that determines which threads execute on a CPU at any given time.
    datastoreSystem (`vim.host.DatastoreSystem`_, optional):

       The datastore manager.
    memoryManager (`vim.host.MemoryManagerSystem`_, optional):

       The memory manager on the host.
    storageSystem (`vim.host.StorageSystem`_, optional):

       The storage configuration.
    networkSystem (`vim.host.NetworkSystem`_, optional):

       The network system configuration.
    vmotionSystem (`vim.host.VMotionSystem`_, optional):

       The VMotion configuration.
    virtualNicManager (`vim.host.VirtualNicManager`_, optional):

       The VirtualNic configuration.
    serviceSystem (`vim.host.ServiceSystem`_, optional):

       The configuration of the host services (for example, SSH, FTP, and Telnet).
    firewallSystem (`vim.host.FirewallSystem`_, optional):

       The firewall configuration.
    advancedOption (`vim.option.OptionManager`_, optional):

       Advanced options.
    diagnosticSystem (`vim.host.DiagnosticSystem`_, optional):

       The diagnostic for the ESX Server system.
    autoStartManager (`vim.host.AutoStartManager`_, optional):

       Auto-start and auto-stop configuration.
    snmpSystem (`vim.host.SnmpSystem`_, optional):

       Snmp configuration
    dateTimeSystem (`vim.host.DateTimeSystem`_, optional):

       DateTime configuration
    patchManager (`vim.host.PatchManager`_, optional):

       Host patch management.
    imageConfigManager (`vim.host.ImageConfigManager`_, optional):

       Host image configuration management.
    bootDeviceSystem (`vim.host.BootDeviceSystem`_, optional):

       Boot device order management.
    firmwareSystem (`vim.host.FirmwareSystem`_, optional):

       Firmware management.
    healthStatusSystem (`vim.host.HealthStatusSystem`_, optional):

       System health status manager.
    pciPassthruSystem (`vim.host.PciPassthruSystem`_, optional):

       PciDeviceSystem for passthru.
    licenseManager (`vim.LicenseManager`_, optional):

       License manager
    kernelModuleSystem (`vim.host.KernelModuleSystem`_, optional):

       Kernel module configuration management.
    authenticationManager (`vim.host.AuthenticationManager`_, optional):

       Authentication method configuration - for example, for Active Directory membership.
    powerSystem (`vim.host.PowerSystem`_, optional):

       Power System manager.
    cacheConfigurationManager (`vim.host.CacheConfigurationManager`_, optional):

       Host solid state drive cache configuration manager.
    esxAgentHostManager (`vim.host.EsxAgentHostManager`_, optional):

       Esx Agent resource configuration manager
    iscsiManager (`vim.host.IscsiManager`_, optional):

       Iscsi Management Operations managed entity
    vFlashManager (`vim.host.VFlashManager`_, optional):

       vFlash Manager
    vsanSystem (`vim.host.VsanSystem`_, optional):

       VsanSystem managed entity.
    graphicsManager (`vim.host.GraphicsManager`_, optional):

       Host graphics manager.
    vsanInternalSystem (`vim.host.VsanInternalSystem`_, optional):

       VsanInternalSystem managed entity.
