# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import long

from pyVmomi.vim.Datastore import Datastore

from pyVmomi.vim.EnvironmentBrowser import EnvironmentBrowser

from pyVmomi.vim.Folder import Folder

from pyVmomi.vim.HostSystem import HostSystem

from pyVmomi.vim.HttpNfcLease import HttpNfcLease

from pyVmomi.vim.ManagedEntity import ManagedEntity

from pyVmomi.vim.Network import Network

from pyVmomi.vim.ResourceConfigSpec import ResourceConfigSpec

from pyVmomi.vim.ResourcePool import ResourcePool

from pyVmomi.vim.Task import Task

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vmodl.MethodFault import MethodFault

from pyVmomi.vim.host.FeatureMask import FeatureMask

from pyVmomi.vim.vm.Capability import Capability

from pyVmomi.vim.vm.CertThumbprint import CertThumbprint

from pyVmomi.vim.vm.CloneSpec import CloneSpec

from pyVmomi.vim.vm.ConfigInfo import ConfigInfo

from pyVmomi.vim.vm.ConfigSpec import ConfigSpec

from pyVmomi.vim.vm.FaultToleranceConfigSpec import FaultToleranceConfigSpec

from pyVmomi.vim.vm.FileLayout import FileLayout

from pyVmomi.vim.vm.FileLayoutEx import FileLayoutEx

from pyVmomi.vim.vm.GuestInfo import GuestInfo

from pyVmomi.vim.vm.GuestQuiesceSpec import GuestQuiesceSpec

from pyVmomi.vim.vm.InstantCloneSpec import InstantCloneSpec

from pyVmomi.vim.vm.RelocateSpec import RelocateSpec

from pyVmomi.vim.vm.RuntimeInfo import RuntimeInfo

from pyVmomi.vim.vm.Snapshot import Snapshot

from pyVmomi.vim.vm.SnapshotInfo import SnapshotInfo

from pyVmomi.vim.vm.SnapshotSelectionSpec import SnapshotSelectionSpec

from pyVmomi.vim.vm.StorageInfo import StorageInfo

from pyVmomi.vim.vm.Summary import Summary

from pyVmomi.vim.vm.UsbScanCodeSpec import UsbScanCodeSpec

from pyVmomi.vim.vslm.ID import ID

from pyVmomi.vim.vm.customization.Specification import Specification

from pyVmomi.vim.vm.device.VirtualDisk import VirtualDisk

class VirtualMachine(ManagedEntity):
   class StorageRequirement(DynamicData):
      datastore: Datastore
      freeSpaceRequiredInKb: long

   class PowerState(Enum):
      poweredOff: ClassVar['PowerState'] = 'poweredOff'
      poweredOn: ClassVar['PowerState'] = 'poweredOn'
      suspended: ClassVar['PowerState'] = 'suspended'

   class AppHeartbeatStatusType(Enum):
      appStatusGray: ClassVar['AppHeartbeatStatusType'] = 'appStatusGray'
      appStatusGreen: ClassVar['AppHeartbeatStatusType'] = 'appStatusGreen'
      appStatusRed: ClassVar['AppHeartbeatStatusType'] = 'appStatusRed'

   class ConnectionState(Enum):
      connected: ClassVar['ConnectionState'] = 'connected'
      disconnected: ClassVar['ConnectionState'] = 'disconnected'
      orphaned: ClassVar['ConnectionState'] = 'orphaned'
      inaccessible: ClassVar['ConnectionState'] = 'inaccessible'
      invalid: ClassVar['ConnectionState'] = 'invalid'

   class CryptoState(Enum):
      unlocked: ClassVar['CryptoState'] = 'unlocked'
      locked: ClassVar['CryptoState'] = 'locked'

   class MovePriority(Enum):
      lowPriority: ClassVar['MovePriority'] = 'lowPriority'
      highPriority: ClassVar['MovePriority'] = 'highPriority'
      defaultPriority: ClassVar['MovePriority'] = 'defaultPriority'

   class Ticket(DynamicData):
      ticket: str
      cfgFile: str
      host: Optional[str] = None
      port: Optional[int] = None
      sslThumbprint: Optional[str] = None
      certThumbprintList: list[CertThumbprint] = []
      sslCertificate: Optional[str] = None
      url: Optional[str] = None

   class MksTicket(DynamicData):
      ticket: str
      cfgFile: str
      host: Optional[str] = None
      port: Optional[int] = None
      sslThumbprint: Optional[str] = None

   class FaultToleranceState(Enum):
      notConfigured: ClassVar['FaultToleranceState'] = 'notConfigured'
      disabled: ClassVar['FaultToleranceState'] = 'disabled'
      enabled: ClassVar['FaultToleranceState'] = 'enabled'
      needSecondary: ClassVar['FaultToleranceState'] = 'needSecondary'
      starting: ClassVar['FaultToleranceState'] = 'starting'
      running: ClassVar['FaultToleranceState'] = 'running'

   class RecordReplayState(Enum):
      recording: ClassVar['RecordReplayState'] = 'recording'
      replaying: ClassVar['RecordReplayState'] = 'replaying'
      inactive: ClassVar['RecordReplayState'] = 'inactive'

   class NeedSecondaryReason(Enum):
      initializing: ClassVar['NeedSecondaryReason'] = 'initializing'
      divergence: ClassVar['NeedSecondaryReason'] = 'divergence'
      lostConnection: ClassVar['NeedSecondaryReason'] = 'lostConnection'
      partialHardwareFailure: ClassVar['NeedSecondaryReason'] = 'partialHardwareFailure'
      userAction: ClassVar['NeedSecondaryReason'] = 'userAction'
      checkpointError: ClassVar['NeedSecondaryReason'] = 'checkpointError'
      other: ClassVar['NeedSecondaryReason'] = 'other'

   class FaultToleranceType(Enum):
      unset: ClassVar['FaultToleranceType'] = 'unset'
      recordReplay: ClassVar['FaultToleranceType'] = 'recordReplay'
      checkpointing: ClassVar['FaultToleranceType'] = 'checkpointing'

   class Connection(DynamicData):
      label: str
      client: str
      userName: str

   class MksConnection(Connection):
      pass

   class TicketType(Enum):
      mks: ClassVar['TicketType'] = 'mks'
      device: ClassVar['TicketType'] = 'device'
      guestControl: ClassVar['TicketType'] = 'guestControl'
      dnd: ClassVar['TicketType'] = 'dnd'
      webmks: ClassVar['TicketType'] = 'webmks'
      guestIntegrity: ClassVar['TicketType'] = 'guestIntegrity'
      webRemoteDevice: ClassVar['TicketType'] = 'webRemoteDevice'

   class DisplayTopology(DynamicData):
      x: int
      y: int
      width: int
      height: int

   class DiskChangeInfo(DynamicData):
      class DiskChangeExtent(DynamicData):
         start: long
         length: long

      startOffset: long
      length: long
      changedArea: list[DiskChangeExtent] = []

   class WipeResult(DynamicData):
      diskId: int
      shrinkableDiskSpace: long

   @property
   def capability(self) -> Capability: ...
   @property
   def config(self) -> Optional[ConfigInfo]: ...
   @property
   def layout(self) -> Optional[FileLayout]: ...
   @property
   def layoutEx(self) -> Optional[FileLayoutEx]: ...
   @property
   def storage(self) -> Optional[StorageInfo]: ...
   @property
   def environmentBrowser(self) -> EnvironmentBrowser: ...
   @property
   def resourcePool(self) -> Optional[ResourcePool]: ...
   @property
   def parentVApp(self) -> Optional[ManagedEntity]: ...
   @property
   def resourceConfig(self) -> Optional[ResourceConfigSpec]: ...
   @property
   def runtime(self) -> RuntimeInfo: ...
   @property
   def guest(self) -> Optional[GuestInfo]: ...
   @property
   def summary(self) -> Summary: ...
   @property
   def datastore(self) -> list[Datastore]: ...
   @property
   def network(self) -> list[Network]: ...
   @property
   def snapshot(self) -> Optional[SnapshotInfo]: ...
   @property
   def rootSnapshot(self) -> list[Snapshot]: ...
   @property
   def guestHeartbeatStatus(self) -> ManagedEntity.Status: ...

   def RefreshStorageInfo(self) -> None: ...
   def CreateSnapshot(self, name: str, description: Optional[str], memory: bool, quiesce: bool) -> Task: ...
   def CreateSnapshotEx(self, name: str, description: Optional[str], memory: bool, quiesceSpec: Optional[GuestQuiesceSpec]) -> Task: ...
   def RevertToCurrentSnapshot(self, host: Optional[HostSystem], suppressPowerOn: Optional[bool]) -> Task: ...
   def RemoveAllSnapshots(self, consolidate: Optional[bool], spec: Optional[SnapshotSelectionSpec]) -> Task: ...
   def ConsolidateDisks(self) -> Task: ...
   def EstimateStorageRequirementForConsolidate(self) -> Task: ...
   def Reconfigure(self, spec: ConfigSpec) -> Task: ...
   def UpgradeVirtualHardware(self, version: Optional[str]) -> Task: ...
   def ExtractOvfEnvironment(self) -> str: ...
   def PowerOn(self, host: Optional[HostSystem]) -> Task: ...
   def PowerOff(self) -> Task: ...
   def Suspend(self) -> Task: ...
   def Reset(self) -> Task: ...
   def ShutdownGuest(self) -> None: ...
   def RebootGuest(self) -> None: ...
   def StandbyGuest(self) -> None: ...
   def Answer(self, questionId: str, answerChoice: str) -> None: ...
   def Customize(self, spec: Specification) -> Task: ...
   def CheckCustomizationSpec(self, spec: Specification) -> None: ...
   def Migrate(self, pool: Optional[ResourcePool], host: Optional[HostSystem], priority: MovePriority, state: Optional[PowerState]) -> Task: ...
   def Relocate(self, spec: RelocateSpec, priority: Optional[MovePriority]) -> Task: ...
   def Clone(self, folder: Folder, name: str, spec: CloneSpec) -> Task: ...
   def InstantClone(self, spec: InstantCloneSpec) -> Task: ...
   def ExportVm(self) -> HttpNfcLease: ...
   def MarkAsTemplate(self) -> None: ...
   def MarkAsVirtualMachine(self, pool: ResourcePool, host: Optional[HostSystem]) -> None: ...
   def Unregister(self) -> None: ...
   def ResetGuestInformation(self) -> None: ...
   def MountToolsInstaller(self) -> None: ...
   def UnmountToolsInstaller(self) -> None: ...
   def UpgradeTools(self, installerOptions: Optional[str]) -> Task: ...
   def AcquireMksTicket(self) -> MksTicket: ...
   def QueryConnections(self) -> list[Connection]: ...
   def DropConnections(self, listOfConnections: list[Connection]) -> bool: ...
   def AcquireTicket(self, ticketType: str) -> Ticket: ...
   def SetScreenResolution(self, width: int, height: int) -> None: ...
   def DefragmentAllDisks(self) -> None: ...
   def CreateSecondary(self, host: Optional[HostSystem]) -> Task: ...
   def CreateSecondaryEx(self, host: Optional[HostSystem], spec: Optional[FaultToleranceConfigSpec]) -> Task: ...
   def TurnOffFaultTolerance(self) -> Task: ...
   def MakePrimary(self, vm: VirtualMachine) -> Task: ...
   def TerminateFaultTolerantVM(self, vm: Optional[VirtualMachine]) -> Task: ...
   def DisableSecondary(self, vm: VirtualMachine) -> Task: ...
   def EnableSecondary(self, vm: VirtualMachine, host: Optional[HostSystem]) -> Task: ...
   def SetDisplayTopology(self, displays: list[DisplayTopology]) -> None: ...
   def StartRecording(self, name: str, description: Optional[str]) -> Task: ...
   def StopRecording(self) -> Task: ...
   def StartReplaying(self, replaySnapshot: Snapshot) -> Task: ...
   def StopReplaying(self) -> Task: ...
   def PromoteDisks(self, unlink: bool, disks: list[VirtualDisk]) -> Task: ...
   def CreateScreenshot(self) -> Task: ...
   def PutUsbScanCodes(self, spec: UsbScanCodeSpec) -> int: ...
   def QueryChangedDiskAreas(self, snapshot: Optional[Snapshot], deviceKey: int, startOffset: long, changeId: str) -> DiskChangeInfo: ...
   def QueryUnownedFiles(self) -> list[str]: ...
   def ReloadFromPath(self, configurationPath: str) -> Task: ...
   def QueryFaultToleranceCompatibility(self) -> list[MethodFault]: ...
   def QueryFaultToleranceCompatibilityEx(self, forLegacyFt: Optional[bool]) -> list[MethodFault]: ...
   def Terminate(self) -> None: ...
   def SendNMI(self) -> None: ...
   def AttachDisk(self, diskId: ID, datastore: Datastore, controllerKey: Optional[int], unitNumber: Optional[int]) -> Task: ...
   def DetachDisk(self, diskId: ID) -> Task: ...
   def ApplyEvcMode(self, mask: list[FeatureMask], completeMasks: Optional[bool]) -> Task: ...
   def CryptoUnlock(self) -> Task: ...
