# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import binary
from pyVmomi.VmomiSupport import long
from pyVmomi.VmomiSupport import short

from pyVmomi.vim import LatencySensitivity
from pyVmomi.vim import ResourceAllocationInfo

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.encryption import CryptoKeyId

from pyVmomi.vim.ext import ManagedByInfo

from pyVmomi.vim.host import CpuIdInfo

from pyVmomi.vim.option import OptionValue

from pyVmomi.vim.vApp import VmConfigInfo

from pyVmomi.vim.vm import AffinityInfo
from pyVmomi.vim.vm import BootOptions
from pyVmomi.vim.vm import ConsolePreferences
from pyVmomi.vim.vm import ContentLibraryItemInfo
from pyVmomi.vim.vm import DefaultPowerOpInfo
from pyVmomi.vim.vm import FaultToleranceConfigInfo
from pyVmomi.vim.vm import FileInfo
from pyVmomi.vim.vm import FlagInfo
from pyVmomi.vim.vm import ForkConfigInfo
from pyVmomi.vim.vm import GuestIntegrityInfo
from pyVmomi.vim.vm import GuestMonitoringModeInfo
from pyVmomi.vim.vm import NetworkShaperInfo
from pyVmomi.vim.vm import ReplicationConfigSpec
from pyVmomi.vim.vm import ScheduledHardwareUpgradeInfo
from pyVmomi.vim.vm import SgxInfo
from pyVmomi.vim.vm import ToolsConfigInfo
from pyVmomi.vim.vm import VcpuConfig
from pyVmomi.vim.vm import VirtualDeviceGroups
from pyVmomi.vim.vm import VirtualDeviceSwap
from pyVmomi.vim.vm import VirtualHardware
from pyVmomi.vim.vm import VirtualNumaInfo
from pyVmomi.vim.vm import VirtualPMem

class ConfigInfo(DynamicData):
   class NpivWwnType(Enum):
      vc: ClassVar['NpivWwnType'] = 'vc'
      host: ClassVar['NpivWwnType'] = 'host'
      external: ClassVar['NpivWwnType'] = 'external'

   class SwapPlacementType(Enum):
      inherit: ClassVar['SwapPlacementType'] = 'inherit'
      vmDirectory: ClassVar['SwapPlacementType'] = 'vmDirectory'
      hostLocal: ClassVar['SwapPlacementType'] = 'hostLocal'

   class DatastoreUrlPair(DynamicData):
      name: str
      url: str

   class OverheadInfo(DynamicData):
      initialMemoryReservation: Optional[long] = None
      initialSwapReservation: Optional[long] = None

   changeVersion: str
   modified: datetime
   name: str
   guestFullName: str
   version: str
   uuid: str
   createDate: Optional[datetime] = None
   instanceUuid: Optional[str] = None
   npivNodeWorldWideName: list[long] = []
   npivPortWorldWideName: list[long] = []
   npivWorldWideNameType: Optional[str] = None
   npivDesiredNodeWwns: Optional[short] = None
   npivDesiredPortWwns: Optional[short] = None
   npivTemporaryDisabled: Optional[bool] = None
   npivOnNonRdmDisks: Optional[bool] = None
   locationId: Optional[str] = None
   template: bool
   guestId: str
   alternateGuestName: str
   annotation: Optional[str] = None
   files: FileInfo
   tools: Optional[ToolsConfigInfo] = None
   flags: FlagInfo
   consolePreferences: Optional[ConsolePreferences] = None
   defaultPowerOps: DefaultPowerOpInfo
   rebootPowerOff: Optional[bool] = None
   hardware: VirtualHardware
   vcpuConfig: list[VcpuConfig] = []
   cpuAllocation: Optional[ResourceAllocationInfo] = None
   memoryAllocation: Optional[ResourceAllocationInfo] = None
   latencySensitivity: Optional[LatencySensitivity] = None
   memoryHotAddEnabled: Optional[bool] = None
   cpuHotAddEnabled: Optional[bool] = None
   cpuHotRemoveEnabled: Optional[bool] = None
   hotPlugMemoryLimit: Optional[long] = None
   hotPlugMemoryIncrementSize: Optional[long] = None
   cpuAffinity: Optional[AffinityInfo] = None
   memoryAffinity: Optional[AffinityInfo] = None
   networkShaper: Optional[NetworkShaperInfo] = None
   extraConfig: list[OptionValue] = []
   cpuFeatureMask: list[CpuIdInfo] = []
   datastoreUrl: list[DatastoreUrlPair] = []
   swapPlacement: Optional[str] = None
   bootOptions: Optional[BootOptions] = None
   ftInfo: Optional[FaultToleranceConfigInfo] = None
   repConfig: Optional[ReplicationConfigSpec] = None
   vAppConfig: Optional[VmConfigInfo] = None
   vAssertsEnabled: Optional[bool] = None
   changeTrackingEnabled: Optional[bool] = None
   firmware: Optional[str] = None
   maxMksConnections: Optional[int] = None
   guestAutoLockEnabled: Optional[bool] = None
   managedBy: Optional[ManagedByInfo] = None
   memoryReservationLockedToMax: Optional[bool] = None
   initialOverhead: Optional[OverheadInfo] = None
   nestedHVEnabled: Optional[bool] = None
   vPMCEnabled: Optional[bool] = None
   scheduledHardwareUpgradeInfo: Optional[ScheduledHardwareUpgradeInfo] = None
   forkConfigInfo: Optional[ForkConfigInfo] = None
   vFlashCacheReservation: Optional[long] = None
   vmxConfigChecksum: Optional[binary] = None
   messageBusTunnelEnabled: Optional[bool] = None
   vmStorageObjectId: Optional[str] = None
   swapStorageObjectId: Optional[str] = None
   keyId: Optional[CryptoKeyId] = None
   guestIntegrityInfo: Optional[GuestIntegrityInfo] = None
   migrateEncryption: Optional[str] = None
   sgxInfo: Optional[SgxInfo] = None
   contentLibItemInfo: Optional[ContentLibraryItemInfo] = None
   ftEncryptionMode: Optional[str] = None
   guestMonitoringModeInfo: Optional[GuestMonitoringModeInfo] = None
   sevEnabled: Optional[bool] = None
   numaInfo: Optional[VirtualNumaInfo] = None
   pmemFailoverEnabled: Optional[bool] = None
   vmxStatsCollectionEnabled: Optional[bool] = None
   vmOpNotificationToAppEnabled: Optional[bool] = None
   vmOpNotificationTimeout: Optional[long] = None
   deviceSwap: Optional[VirtualDeviceSwap] = None
   pmem: Optional[VirtualPMem] = None
   deviceGroups: Optional[VirtualDeviceGroups] = None
   fixedPassthruHotPlugEnabled: Optional[bool] = None
   metroFtEnabled: Optional[bool] = None
   metroFtHostGroup: Optional[str] = None
