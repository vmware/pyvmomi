# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import LicenseManager
from pyVmomi.vim import UserDirectory

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.encryption import CryptoManager

from pyVmomi.vim.host import AssignableHardwareManager
from pyVmomi.vim.host import AuthenticationManager
from pyVmomi.vim.host import AutoStartManager
from pyVmomi.vim.host import BootDeviceSystem
from pyVmomi.vim.host import CacheConfigurationManager
from pyVmomi.vim.host import CertificateManager
from pyVmomi.vim.host import CpuSchedulerSystem
from pyVmomi.vim.host import DatastoreSystem
from pyVmomi.vim.host import DateTimeSystem
from pyVmomi.vim.host import DiagnosticSystem
from pyVmomi.vim.host import EsxAgentHostManager
from pyVmomi.vim.host import FirewallSystem
from pyVmomi.vim.host import FirmwareSystem
from pyVmomi.vim.host import GraphicsManager
from pyVmomi.vim.host import HealthStatusSystem
from pyVmomi.vim.host import HostAccessManager
from pyVmomi.vim.host import ImageConfigManager
from pyVmomi.vim.host import IscsiManager
from pyVmomi.vim.host import KernelModuleSystem
from pyVmomi.vim.host import LocalAccountManager
from pyVmomi.vim.host import MemoryManagerSystem
from pyVmomi.vim.host import MessageBusProxy
from pyVmomi.vim.host import NetworkSystem
from pyVmomi.vim.host import NvdimmSystem
from pyVmomi.vim.host import PatchManager
from pyVmomi.vim.host import PciPassthruSystem
from pyVmomi.vim.host import PowerSystem
from pyVmomi.vim.host import ServiceSystem
from pyVmomi.vim.host import SnmpSystem
from pyVmomi.vim.host import StorageSystem
from pyVmomi.vim.host import VFlashManager
from pyVmomi.vim.host import VMotionSystem
from pyVmomi.vim.host import VirtualNicManager
from pyVmomi.vim.host import VsanInternalSystem
from pyVmomi.vim.host import VsanSystem

from pyVmomi.vim.option import OptionManager

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
