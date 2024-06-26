# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import binary
from pyVmomi.VmomiSupport import byte

from pyVmomi.vim import AboutInfo
from pyVmomi.vim import Datastore
from pyVmomi.vim import HostSystem
from pyVmomi.vim import IoFilterManager

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import AssignableHardwareBinding
from pyVmomi.vim.host import AssignableHardwareConfig
from pyVmomi.vim.host import AuthenticationManagerInfo
from pyVmomi.vim.host import AutoStartManager
from pyVmomi.vim.host import CacheConfigurationManager
from pyVmomi.vim.host import CpuSchedulerSystem
from pyVmomi.vim.host import DatastoreSystem
from pyVmomi.vim.host import DateTimeInfo
from pyVmomi.vim.host import DeploymentInfo
from pyVmomi.vim.host import DiagnosticPartition
from pyVmomi.vim.host import FeatureCapability
from pyVmomi.vim.host import FeatureVersionInfo
from pyVmomi.vim.host import FileSystemVolumeInfo
from pyVmomi.vim.host import FirewallInfo
from pyVmomi.vim.host import FlagInfo
from pyVmomi.vim.host import GraphicsConfig
from pyVmomi.vim.host import GraphicsInfo
from pyVmomi.vim.host import HostAccessManager
from pyVmomi.vim.host import IpmiInfo
from pyVmomi.vim.host import MemoryManagerSystem
from pyVmomi.vim.host import MultipathStateInfo
from pyVmomi.vim.host import NetCapabilities
from pyVmomi.vim.host import NetOffloadCapabilities
from pyVmomi.vim.host import NetworkInfo
from pyVmomi.vim.host import PciPassthruInfo
from pyVmomi.vim.host import PowerSystem
from pyVmomi.vim.host import ServiceInfo
from pyVmomi.vim.host import SharedGpuCapabilities
from pyVmomi.vim.host import SriovDevicePoolInfo
from pyVmomi.vim.host import SslThumbprintInfo
from pyVmomi.vim.host import StorageDeviceInfo
from pyVmomi.vim.host import SystemResourceInfo
from pyVmomi.vim.host import SystemSwapConfiguration
from pyVmomi.vim.host import VFlashManager
from pyVmomi.vim.host import VMotionInfo
from pyVmomi.vim.host import VirtualNicManagerInfo

from pyVmomi.vim.option import OptionDef
from pyVmomi.vim.option import OptionValue

class ConfigInfo(DynamicData):
   host: HostSystem
   product: AboutInfo
   deploymentInfo: Optional[DeploymentInfo] = None
   hyperThread: Optional[CpuSchedulerSystem.HyperThreadScheduleInfo] = None
   cpuScheduler: Optional[CpuSchedulerSystem.CpuSchedulerInfo] = None
   consoleReservation: Optional[MemoryManagerSystem.ServiceConsoleReservationInfo] = None
   virtualMachineReservation: Optional[MemoryManagerSystem.VirtualMachineReservationInfo] = None
   storageDevice: Optional[StorageDeviceInfo] = None
   multipathState: Optional[MultipathStateInfo] = None
   fileSystemVolume: Optional[FileSystemVolumeInfo] = None
   systemFile: list[str] = []
   network: Optional[NetworkInfo] = None
   vmotion: Optional[VMotionInfo] = None
   virtualNicManagerInfo: Optional[VirtualNicManagerInfo] = None
   capabilities: Optional[NetCapabilities] = None
   datastoreCapabilities: Optional[DatastoreSystem.Capabilities] = None
   offloadCapabilities: Optional[NetOffloadCapabilities] = None
   service: Optional[ServiceInfo] = None
   firewall: Optional[FirewallInfo] = None
   autoStart: Optional[AutoStartManager.Config] = None
   activeDiagnosticPartition: Optional[DiagnosticPartition] = None
   option: list[OptionValue] = []
   optionDef: list[OptionDef] = []
   datastorePrincipal: Optional[str] = None
   localSwapDatastore: Optional[Datastore] = None
   systemSwapConfiguration: Optional[SystemSwapConfiguration] = None
   systemResources: Optional[SystemResourceInfo] = None
   dateTimeInfo: Optional[DateTimeInfo] = None
   flags: Optional[FlagInfo] = None
   adminDisabled: Optional[bool] = None
   lockdownMode: Optional[HostAccessManager.LockdownMode] = None
   ipmi: Optional[IpmiInfo] = None
   sslThumbprintInfo: Optional[SslThumbprintInfo] = None
   sslThumbprintData: list[SslThumbprintInfo] = []
   certificate: list[byte] = []
   pciPassthruInfo: list[PciPassthruInfo] = []
   authenticationManagerInfo: Optional[AuthenticationManagerInfo] = None
   featureVersion: list[FeatureVersionInfo] = []
   powerSystemCapability: Optional[PowerSystem.Capability] = None
   powerSystemInfo: Optional[PowerSystem.Info] = None
   cacheConfigurationInfo: list[CacheConfigurationManager.CacheConfigurationInfo] = []
   wakeOnLanCapable: Optional[bool] = None
   featureCapability: list[FeatureCapability] = []
   maskedFeatureCapability: list[FeatureCapability] = []
   vFlashConfigInfo: Optional[VFlashManager.VFlashConfigInfo] = None
   vsanHostConfig: Optional[ConfigInfo] = None
   domainList: list[str] = []
   scriptCheckSum: Optional[binary] = None
   hostConfigCheckSum: Optional[binary] = None
   descriptionTreeCheckSum: Optional[binary] = None
   graphicsInfo: list[GraphicsInfo] = []
   sharedPassthruGpuTypes: list[str] = []
   graphicsConfig: Optional[GraphicsConfig] = None
   sharedGpuCapabilities: list[SharedGpuCapabilities] = []
   ioFilterInfo: list[IoFilterManager.HostIoFilterInfo] = []
   sriovDevicePool: list[SriovDevicePoolInfo] = []
   assignableHardwareBinding: list[AssignableHardwareBinding] = []
   assignableHardwareConfig: Optional[AssignableHardwareConfig] = None
