# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import long
from pyVmomi.VmomiSupport import short

from pyVmomi.vim import LatencySensitivity
from pyVmomi.vim import ResourceAllocationInfo

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.encryption import CryptoSpec

from pyVmomi.vim.ext import ManagedByInfo

from pyVmomi.vim.host import CpuIdInfo

from pyVmomi.vim.option import ArrayUpdateSpec
from pyVmomi.vim.option import OptionValue

from pyVmomi.vim.vApp import VmConfigSpec

from pyVmomi.vim.vm import AffinityInfo
from pyVmomi.vim.vm import BootOptions
from pyVmomi.vim.vm import ConsolePreferences
from pyVmomi.vim.vm import DefaultPowerOpInfo
from pyVmomi.vim.vm import FaultToleranceConfigInfo
from pyVmomi.vim.vm import FileInfo
from pyVmomi.vim.vm import FlagInfo
from pyVmomi.vim.vm import GuestMonitoringModeInfo
from pyVmomi.vim.vm import NetworkShaperInfo
from pyVmomi.vim.vm import ProfileSpec
from pyVmomi.vim.vm import ReplicationConfigSpec
from pyVmomi.vim.vm import ScheduledHardwareUpgradeInfo
from pyVmomi.vim.vm import SgxInfo
from pyVmomi.vim.vm import ToolsConfigInfo
from pyVmomi.vim.vm import VcpuConfig
from pyVmomi.vim.vm import VirtualDeviceGroups
from pyVmomi.vim.vm import VirtualDeviceSwap
from pyVmomi.vim.vm import VirtualNuma
from pyVmomi.vim.vm import VirtualPMem

from pyVmomi.vim.vm.device import VirtualDeviceSpec

class ConfigSpec(DynamicData):
   class NpivWwnOp(Enum):
      generate: ClassVar['NpivWwnOp'] = 'generate'
      set: ClassVar['NpivWwnOp'] = 'set'
      remove: ClassVar['NpivWwnOp'] = 'remove'
      extend: ClassVar['NpivWwnOp'] = 'extend'

   class EncryptedFtModes(Enum):
      ftEncryptionDisabled: ClassVar['EncryptedFtModes'] = 'ftEncryptionDisabled'
      ftEncryptionOpportunistic: ClassVar['EncryptedFtModes'] = 'ftEncryptionOpportunistic'
      ftEncryptionRequired: ClassVar['EncryptedFtModes'] = 'ftEncryptionRequired'

   class EncryptedVMotionModes(Enum):
      disabled: ClassVar['EncryptedVMotionModes'] = 'disabled'
      opportunistic: ClassVar['EncryptedVMotionModes'] = 'opportunistic'
      required: ClassVar['EncryptedVMotionModes'] = 'required'

   class CpuIdInfoSpec(ArrayUpdateSpec):
      info: Optional[CpuIdInfo] = None

   changeVersion: Optional[str] = None
   name: Optional[str] = None
   version: Optional[str] = None
   createDate: Optional[datetime] = None
   uuid: Optional[str] = None
   instanceUuid: Optional[str] = None
   npivNodeWorldWideName: list[long] = []
   npivPortWorldWideName: list[long] = []
   npivWorldWideNameType: Optional[str] = None
   npivDesiredNodeWwns: Optional[short] = None
   npivDesiredPortWwns: Optional[short] = None
   npivTemporaryDisabled: Optional[bool] = None
   npivOnNonRdmDisks: Optional[bool] = None
   npivWorldWideNameOp: Optional[str] = None
   locationId: Optional[str] = None
   guestId: Optional[str] = None
   alternateGuestName: Optional[str] = None
   annotation: Optional[str] = None
   files: Optional[FileInfo] = None
   tools: Optional[ToolsConfigInfo] = None
   flags: Optional[FlagInfo] = None
   consolePreferences: Optional[ConsolePreferences] = None
   powerOpInfo: Optional[DefaultPowerOpInfo] = None
   rebootPowerOff: Optional[bool] = None
   numCPUs: Optional[int] = None
   vcpuConfig: list[VcpuConfig] = []
   numCoresPerSocket: Optional[int] = None
   memoryMB: Optional[long] = None
   memoryHotAddEnabled: Optional[bool] = None
   cpuHotAddEnabled: Optional[bool] = None
   cpuHotRemoveEnabled: Optional[bool] = None
   virtualICH7MPresent: Optional[bool] = None
   virtualSMCPresent: Optional[bool] = None
   deviceChange: list[VirtualDeviceSpec] = []
   cpuAllocation: Optional[ResourceAllocationInfo] = None
   memoryAllocation: Optional[ResourceAllocationInfo] = None
   latencySensitivity: Optional[LatencySensitivity] = None
   cpuAffinity: Optional[AffinityInfo] = None
   memoryAffinity: Optional[AffinityInfo] = None
   networkShaper: Optional[NetworkShaperInfo] = None
   cpuFeatureMask: list[CpuIdInfoSpec] = []
   extraConfig: list[OptionValue] = []
   swapPlacement: Optional[str] = None
   bootOptions: Optional[BootOptions] = None
   vAppConfig: Optional[VmConfigSpec] = None
   ftInfo: Optional[FaultToleranceConfigInfo] = None
   repConfig: Optional[ReplicationConfigSpec] = None
   vAppConfigRemoved: Optional[bool] = None
   vAssertsEnabled: Optional[bool] = None
   changeTrackingEnabled: Optional[bool] = None
   firmware: Optional[str] = None
   maxMksConnections: Optional[int] = None
   guestAutoLockEnabled: Optional[bool] = None
   managedBy: Optional[ManagedByInfo] = None
   memoryReservationLockedToMax: Optional[bool] = None
   nestedHVEnabled: Optional[bool] = None
   vPMCEnabled: Optional[bool] = None
   scheduledHardwareUpgradeInfo: Optional[ScheduledHardwareUpgradeInfo] = None
   vmProfile: list[ProfileSpec] = []
   messageBusTunnelEnabled: Optional[bool] = None
   crypto: Optional[CryptoSpec] = None
   migrateEncryption: Optional[str] = None
   sgxInfo: Optional[SgxInfo] = None
   ftEncryptionMode: Optional[str] = None
   guestMonitoringModeInfo: Optional[GuestMonitoringModeInfo] = None
   sevEnabled: Optional[bool] = None
   virtualNuma: Optional[VirtualNuma] = None
   motherboardLayout: Optional[str] = None
   pmemFailoverEnabled: Optional[bool] = None
   vmxStatsCollectionEnabled: Optional[bool] = None
   vmOpNotificationToAppEnabled: Optional[bool] = None
   vmOpNotificationTimeout: Optional[long] = None
   deviceSwap: Optional[VirtualDeviceSwap] = None
   simultaneousThreads: Optional[int] = None
   pmem: Optional[VirtualPMem] = None
   deviceGroups: Optional[VirtualDeviceGroups] = None
   fixedPassthruHotPlugEnabled: Optional[bool] = None
   metroFtEnabled: Optional[bool] = None
   metroFtHostGroup: Optional[str] = None
