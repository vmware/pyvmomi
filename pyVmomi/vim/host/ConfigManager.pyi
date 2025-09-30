# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.LicenseManager import LicenseManager

from pyVmomi.vim.UserDirectory import UserDirectory

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.encryption.CryptoManager import CryptoManager

from pyVmomi.vim.host.AssignableHardwareManager import AssignableHardwareManager

from pyVmomi.vim.host.AuthenticationManager import AuthenticationManager

from pyVmomi.vim.host.AutoStartManager import AutoStartManager

from pyVmomi.vim.host.BootDeviceSystem import BootDeviceSystem

from pyVmomi.vim.host.CacheConfigurationManager import CacheConfigurationManager

from pyVmomi.vim.host.CertificateManager import CertificateManager

from pyVmomi.vim.host.CpuSchedulerSystem import CpuSchedulerSystem

from pyVmomi.vim.host.DatastoreSystem import DatastoreSystem

from pyVmomi.vim.host.DateTimeSystem import DateTimeSystem

from pyVmomi.vim.host.DiagnosticSystem import DiagnosticSystem

from pyVmomi.vim.host.EsxAgentHostManager import EsxAgentHostManager

from pyVmomi.vim.host.FirewallSystem import FirewallSystem

from pyVmomi.vim.host.FirmwareSystem import FirmwareSystem

from pyVmomi.vim.host.GraphicsManager import GraphicsManager

from pyVmomi.vim.host.HealthStatusSystem import HealthStatusSystem

from pyVmomi.vim.host.HostAccessManager import HostAccessManager

from pyVmomi.vim.host.ImageConfigManager import ImageConfigManager

from pyVmomi.vim.host.IscsiManager import IscsiManager

from pyVmomi.vim.host.KernelModuleSystem import KernelModuleSystem

from pyVmomi.vim.host.LocalAccountManager import LocalAccountManager

from pyVmomi.vim.host.MemoryManagerSystem import MemoryManagerSystem

from pyVmomi.vim.host.MessageBusProxy import MessageBusProxy

from pyVmomi.vim.host.NetworkSystem import NetworkSystem

from pyVmomi.vim.host.NvdimmSystem import NvdimmSystem

from pyVmomi.vim.host.PatchManager import PatchManager

from pyVmomi.vim.host.PciPassthruSystem import PciPassthruSystem

from pyVmomi.vim.host.PowerSystem import PowerSystem

from pyVmomi.vim.host.ServiceSystem import ServiceSystem

from pyVmomi.vim.host.SnmpSystem import SnmpSystem

from pyVmomi.vim.host.StorageSystem import StorageSystem

from pyVmomi.vim.host.VFlashManager import VFlashManager

from pyVmomi.vim.host.VMotionSystem import VMotionSystem

from pyVmomi.vim.host.VirtualNicManager import VirtualNicManager

from pyVmomi.vim.host.VsanInternalSystem import VsanInternalSystem

from pyVmomi.vim.host.VsanSystem import VsanSystem

from pyVmomi.vim.option.OptionManager import OptionManager

class ConfigManager(DynamicData):
   cpuScheduler: Optional[CpuSchedulerSystem] = None
   datastoreSystem: Optional[DatastoreSystem] = None
   memoryManager: Optional[MemoryManagerSystem] = None
   storageSystem: Optional[StorageSystem] = None
   networkSystem: Optional[NetworkSystem] = None
   vmotionSystem: Optional[VMotionSystem] = None
   virtualNicManager: Optional[VirtualNicManager] = None
   serviceSystem: Optional[ServiceSystem] = None
   firewallSystem: Optional[FirewallSystem] = None
   advancedOption: Optional[OptionManager] = None
   diagnosticSystem: Optional[DiagnosticSystem] = None
   autoStartManager: Optional[AutoStartManager] = None
   snmpSystem: Optional[SnmpSystem] = None
   dateTimeSystem: Optional[DateTimeSystem] = None
   patchManager: Optional[PatchManager] = None
   imageConfigManager: Optional[ImageConfigManager] = None
   bootDeviceSystem: Optional[BootDeviceSystem] = None
   firmwareSystem: Optional[FirmwareSystem] = None
   healthStatusSystem: Optional[HealthStatusSystem] = None
   pciPassthruSystem: Optional[PciPassthruSystem] = None
   licenseManager: Optional[LicenseManager] = None
   kernelModuleSystem: Optional[KernelModuleSystem] = None
   authenticationManager: Optional[AuthenticationManager] = None
   powerSystem: Optional[PowerSystem] = None
   cacheConfigurationManager: Optional[CacheConfigurationManager] = None
   esxAgentHostManager: Optional[EsxAgentHostManager] = None
   iscsiManager: Optional[IscsiManager] = None
   vFlashManager: Optional[VFlashManager] = None
   vsanSystem: Optional[VsanSystem] = None
   messageBusProxy: Optional[MessageBusProxy] = None
   userDirectory: Optional[UserDirectory] = None
   accountManager: Optional[LocalAccountManager] = None
   hostAccessManager: Optional[HostAccessManager] = None
   graphicsManager: Optional[GraphicsManager] = None
   vsanInternalSystem: Optional[VsanInternalSystem] = None
   certificateManager: Optional[CertificateManager] = None
   cryptoManager: Optional[CryptoManager] = None
   nvdimmSystem: Optional[NvdimmSystem] = None
   assignableHardwareManager: Optional[AssignableHardwareManager] = None
