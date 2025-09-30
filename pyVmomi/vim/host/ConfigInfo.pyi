# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import binary
from pyVmomi.VmomiSupport import byte

from pyVmomi.vim.AboutInfo import AboutInfo

from pyVmomi.vim.Datastore import Datastore

from pyVmomi.vim.HostSystem import HostSystem

from pyVmomi.vim.IoFilterManager import IoFilterManager

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.host.AssignableHardwareBinding import AssignableHardwareBinding

from pyVmomi.vim.host.AssignableHardwareConfig import AssignableHardwareConfig

from pyVmomi.vim.host.AuthenticationInfo import AuthenticationInfo

from pyVmomi.vim.host.AuthenticationManagerInfo import AuthenticationManagerInfo

from pyVmomi.vim.host.AutoStartManager import AutoStartManager

from pyVmomi.vim.host.CacheConfigurationManager import CacheConfigurationManager

from pyVmomi.vim.host.CpuSchedulerSystem import CpuSchedulerSystem

from pyVmomi.vim.host.DatastoreSystem import DatastoreSystem

from pyVmomi.vim.host.DateTimeInfo import DateTimeInfo

from pyVmomi.vim.host.DeploymentInfo import DeploymentInfo

from pyVmomi.vim.host.DiagnosticPartition import DiagnosticPartition

from pyVmomi.vim.host.FeatureCapability import FeatureCapability

from pyVmomi.vim.host.FeatureVersionInfo import FeatureVersionInfo

from pyVmomi.vim.host.FileSystemVolumeInfo import FileSystemVolumeInfo

from pyVmomi.vim.host.FirewallInfo import FirewallInfo

from pyVmomi.vim.host.FlagInfo import FlagInfo

from pyVmomi.vim.host.GraphicsConfig import GraphicsConfig

from pyVmomi.vim.host.GraphicsInfo import GraphicsInfo

from pyVmomi.vim.host.HostAccessManager import HostAccessManager

from pyVmomi.vim.host.IpmiInfo import IpmiInfo

from pyVmomi.vim.host.MemoryManagerSystem import MemoryManagerSystem

from pyVmomi.vim.host.MultipathStateInfo import MultipathStateInfo

from pyVmomi.vim.host.NetCapabilities import NetCapabilities

from pyVmomi.vim.host.NetOffloadCapabilities import NetOffloadCapabilities

from pyVmomi.vim.host.NetworkInfo import NetworkInfo

from pyVmomi.vim.host.PciPassthruInfo import PciPassthruInfo

from pyVmomi.vim.host.PowerSystem import PowerSystem

from pyVmomi.vim.host.ServiceInfo import ServiceInfo

from pyVmomi.vim.host.SharedGpuCapabilities import SharedGpuCapabilities

from pyVmomi.vim.host.SriovDevicePoolInfo import SriovDevicePoolInfo

from pyVmomi.vim.host.SslThumbprintInfo import SslThumbprintInfo

from pyVmomi.vim.host.StorageDeviceInfo import StorageDeviceInfo

from pyVmomi.vim.host.SystemResourceInfo import SystemResourceInfo

from pyVmomi.vim.host.SystemSwapConfiguration import SystemSwapConfiguration

from pyVmomi.vim.host.VFlashManager import VFlashManager

from pyVmomi.vim.host.VMotionInfo import VMotionInfo

from pyVmomi.vim.host.VirtualNicManagerInfo import VirtualNicManagerInfo

from pyVmomi.vim.option.OptionDef import OptionDef

from pyVmomi.vim.option.OptionValue import OptionValue

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
   authenticationData: list[AuthenticationInfo] = []
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
