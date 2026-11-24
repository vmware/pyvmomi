# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import datetime as _datetime
import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vim
import pyVmomi.vmodl
import pyVmomi.vim.alarm
import pyVmomi.vim.dvs
import pyVmomi.vim.host
import pyVmomi.vim.profile
import pyVmomi.vim.scheduler
import pyVmomi.vim.vm
import pyVmomi.vim.profile.host



class AccountCreatedEvent(HostEvent):
   spec: pyVmomi.vim.host.LocalAccountManager.AccountSpecification
   group: bool

class AccountRemovedEvent(HostEvent):
   account: str
   group: bool


class AccountUpdatedEvent(HostEvent):
   spec: pyVmomi.vim.host.LocalAccountManager.AccountSpecification
   group: bool
   prevDescription: _typing.Optional[str] = None

class AdminPasswordNotChangedEvent(HostEvent):
   pass

class AlarmAcknowledgedEvent(AlarmEvent):
   source: ManagedEntityEventArgument
   entity: ManagedEntityEventArgument

class AlarmActionTriggeredEvent(AlarmEvent):
   source: ManagedEntityEventArgument
   entity: ManagedEntityEventArgument

class AlarmClearedEvent(AlarmEvent):
   source: ManagedEntityEventArgument
   entity: ManagedEntityEventArgument
   # Reserved python keyword: commenting out.
   # from: str

class AlarmCreatedEvent(AlarmEvent):
   entity: ManagedEntityEventArgument

class AlarmEmailCompletedEvent(AlarmEvent):
   entity: ManagedEntityEventArgument
   to: str


class AlarmEmailFailedEvent(AlarmEvent):
   entity: ManagedEntityEventArgument
   to: str
   reason: pyVmomi.vmodl.MethodFault

class AlarmEvent(Event):
   alarm: AlarmEventArgument


class AlarmEventArgument(EntityEventArgument):
   alarm: pyVmomi.vim.alarm.Alarm


class AlarmReconfiguredEvent(AlarmEvent):
   entity: ManagedEntityEventArgument
   configChanges: _typing.Optional[ChangesInfoEventArgument] = None

class AlarmRemovedEvent(AlarmEvent):
   entity: ManagedEntityEventArgument

class AlarmScriptCompleteEvent(AlarmEvent):
   entity: ManagedEntityEventArgument
   script: str


class AlarmScriptFailedEvent(AlarmEvent):
   entity: ManagedEntityEventArgument
   script: str
   reason: pyVmomi.vmodl.MethodFault

class AlarmSnmpCompletedEvent(AlarmEvent):
   entity: ManagedEntityEventArgument


class AlarmSnmpFailedEvent(AlarmEvent):
   entity: ManagedEntityEventArgument
   reason: pyVmomi.vmodl.MethodFault

class AlarmStatusChangedEvent(AlarmEvent):
   source: ManagedEntityEventArgument
   entity: ManagedEntityEventArgument
   # Reserved python keyword: commenting out.
   # from: str
   to: str

class AllVirtualMachinesLicensedEvent(LicenseEvent):
   pass

class AlreadyAuthenticatedSessionEvent(SessionEvent):
   pass

class AuthorizationEvent(Event):
   pass

class BadUsernameSessionEvent(SessionEvent):
   ipAddress: str

class CanceledHostOperationEvent(HostEvent):
   pass


class ChangesInfoEventArgument(pyVmomi.vmodl.DynamicData):
   modified: _typing.Optional[str] = None
   added: _typing.Optional[str] = None
   deleted: _typing.Optional[str] = None

class ClusterComplianceCheckedEvent(ClusterEvent):
   profile: ProfileEventArgument

class ClusterCreatedEvent(ClusterEvent):
   parent: FolderEventArgument

class ClusterDestroyedEvent(ClusterEvent):
   pass

class ClusterEvent(Event):
   pass

class ClusterOvercommittedEvent(ClusterEvent):
   pass


class ClusterReconfiguredEvent(ClusterEvent):
   configChanges: _typing.Optional[ChangesInfoEventArgument] = None

class ClusterStatusChangedEvent(ClusterEvent):
   oldStatus: str
   newStatus: str


class ComputeResourceEventArgument(EntityEventArgument):
   computeResource: pyVmomi.vim.ComputeResource

class CustomFieldDefAddedEvent(CustomFieldDefEvent):
   pass

class CustomFieldDefEvent(CustomFieldEvent):
   fieldKey: int
   name: str

class CustomFieldDefRemovedEvent(CustomFieldDefEvent):
   pass

class CustomFieldDefRenamedEvent(CustomFieldDefEvent):
   newName: str

class CustomFieldEvent(Event):
   pass


class CustomFieldValueChangedEvent(CustomFieldEvent):
   entity: ManagedEntityEventArgument
   fieldKey: int
   name: str
   value: str
   prevState: _typing.Optional[str] = None


class CustomizationEvent(VmEvent):
   logLocation: _typing.Optional[str] = None


class CustomizationFailed(CustomizationEvent):
   class ReasonCode(pyVmomi.VmomiSupport.Enum):
      userDefinedScriptDisabled: _typing.ClassVar['ReasonCode'] = 'userDefinedScriptDisabled'
      customizationDisabled: _typing.ClassVar['ReasonCode'] = 'customizationDisabled'
      rawDataIsNotSupported: _typing.ClassVar['ReasonCode'] = 'rawDataIsNotSupported'
      wrongMetadataFormat: _typing.ClassVar['ReasonCode'] = 'wrongMetadataFormat'

   reason: _typing.Optional[str] = None

class CustomizationLinuxIdentityFailed(CustomizationFailed):
   pass

class CustomizationNetworkSetupFailed(CustomizationFailed):
   pass

class CustomizationStartedEvent(CustomizationEvent):
   pass

class CustomizationSucceeded(CustomizationEvent):
   pass

class CustomizationSysprepFailed(CustomizationFailed):
   sysprepVersion: str
   systemVersion: str

class CustomizationUnknownFailure(CustomizationFailed):
   pass

class DVPortgroupCreatedEvent(DVPortgroupEvent):
   pass

class DVPortgroupDestroyedEvent(DVPortgroupEvent):
   pass

class DVPortgroupEvent(Event):
   pass


class DVPortgroupReconfiguredEvent(DVPortgroupEvent):
   configSpec: pyVmomi.vim.dvs.DistributedVirtualPortgroup.ConfigSpec
   configChanges: _typing.Optional[ChangesInfoEventArgument] = None

class DVPortgroupRenamedEvent(DVPortgroupEvent):
   oldName: str
   newName: str

class DasAdmissionControlDisabledEvent(ClusterEvent):
   pass

class DasAdmissionControlEnabledEvent(ClusterEvent):
   pass

class DasAgentFoundEvent(ClusterEvent):
   pass

class DasAgentUnavailableEvent(ClusterEvent):
   pass

class DasClusterIsolatedEvent(ClusterEvent):
   pass

class DasDisabledEvent(ClusterEvent):
   pass

class DasEnabledEvent(ClusterEvent):
   pass

class DasHostFailedEvent(ClusterEvent):
   failedHost: HostEventArgument

class DasHostIsolatedEvent(ClusterEvent):
   isolatedHost: HostEventArgument

class DatacenterCreatedEvent(DatacenterEvent):
   parent: FolderEventArgument

class DatacenterEvent(Event):
   pass


class DatacenterEventArgument(EntityEventArgument):
   datacenter: pyVmomi.vim.Datacenter

class DatacenterRenamedEvent(DatacenterEvent):
   oldName: str
   newName: str


class DatastoreCapacityIncreasedEvent(DatastoreEvent):
   oldCapacity: pyVmomi.VmomiSupport.long
   newCapacity: pyVmomi.VmomiSupport.long

class DatastoreDestroyedEvent(DatastoreEvent):
   pass

class DatastoreDiscoveredEvent(HostEvent):
   datastore: DatastoreEventArgument

class DatastoreDuplicatedEvent(DatastoreEvent):
   pass


class DatastoreEvent(Event):
   datastore: _typing.Optional[DatastoreEventArgument] = None


class DatastoreEventArgument(EntityEventArgument):
   datastore: pyVmomi.vim.Datastore

class DatastoreFileCopiedEvent(DatastoreFileEvent):
   sourceDatastore: DatastoreEventArgument
   sourceFile: str

class DatastoreFileDeletedEvent(DatastoreFileEvent):
   pass


class DatastoreFileEvent(DatastoreEvent):
   targetFile: str
   sourceOfOperation: _typing.Optional[str] = None
   succeeded: _typing.Optional[bool] = None

class DatastoreFileMovedEvent(DatastoreFileEvent):
   sourceDatastore: DatastoreEventArgument
   sourceFile: str

class DatastoreIORMReconfiguredEvent(DatastoreEvent):
   pass

class DatastorePrincipalConfigured(HostEvent):
   datastorePrincipal: str

class DatastoreRemovedOnHostEvent(HostEvent):
   datastore: DatastoreEventArgument

class DatastoreRenamedEvent(DatastoreEvent):
   oldName: str
   newName: str

class DatastoreRenamedOnHostEvent(HostEvent):
   oldName: str
   newName: str

class DrsDisabledEvent(ClusterEvent):
   pass

class DrsEnabledEvent(ClusterEvent):
   behavior: str

class DrsEnteredStandbyModeEvent(EnteredStandbyModeEvent):
   pass

class DrsEnteringStandbyModeEvent(EnteringStandbyModeEvent):
   pass

class DrsExitStandbyModeFailedEvent(ExitStandbyModeFailedEvent):
   pass

class DrsExitedStandbyModeEvent(ExitedStandbyModeEvent):
   pass

class DrsExitingStandbyModeEvent(ExitingStandbyModeEvent):
   pass

class DrsInvocationFailedEvent(ClusterEvent):
   pass

class DrsRecoveredFromFailureEvent(ClusterEvent):
   pass


class DrsResourceConfigureFailedEvent(HostEvent):
   reason: pyVmomi.vmodl.MethodFault

class DrsResourceConfigureSyncedEvent(HostEvent):
   pass

class DrsRuleComplianceEvent(VmEvent):
   pass

class DrsRuleViolationEvent(VmEvent):
   pass

class DrsSoftRuleViolationEvent(VmEvent):
   pass

class DrsVmMigratedEvent(VmMigratedEvent):
   pass

class DrsVmPoweredOnEvent(VmPoweredOnEvent):
   pass

class DuplicateIpDetectedEvent(HostEvent):
   duplicateIP: str
   macAddress: str

class DvpgImportEvent(DVPortgroupEvent):
   importType: str

class DvpgRestoreEvent(DVPortgroupEvent):
   pass

class DvsCreatedEvent(DvsEvent):
   parent: FolderEventArgument

class DvsDestroyedEvent(DvsEvent):
   pass


class DvsEvent(Event):
   class PortBlockState(pyVmomi.VmomiSupport.Enum):
      unset: _typing.ClassVar['PortBlockState'] = 'unset'
      blocked: _typing.ClassVar['PortBlockState'] = 'blocked'
      unblocked: _typing.ClassVar['PortBlockState'] = 'unblocked'
      unknown: _typing.ClassVar['PortBlockState'] = 'unknown'


class DvsEventArgument(EntityEventArgument):
   dvs: pyVmomi.vim.DistributedVirtualSwitch


class DvsHealthStatusChangeEvent(HostEvent):
   switchUuid: str
   healthResult: _typing.Optional[pyVmomi.vim.dvs.HostMember.HealthCheckResult] = None

class DvsHostBackInSyncEvent(DvsEvent):
   hostBackInSync: HostEventArgument

class DvsHostJoinedEvent(DvsEvent):
   hostJoined: HostEventArgument

class DvsHostLeftEvent(DvsEvent):
   hostLeft: HostEventArgument


class DvsHostStatusUpdated(DvsEvent):
   hostMember: HostEventArgument
   oldStatus: _typing.Optional[str] = None
   newStatus: _typing.Optional[str] = None
   oldStatusDetail: _typing.Optional[str] = None
   newStatusDetail: _typing.Optional[str] = None

class DvsHostWentOutOfSyncEvent(DvsEvent):
   hostOutOfSync: DvsOutOfSyncHostArgument

class DvsImportEvent(DvsEvent):
   importType: str

class DvsMergedEvent(DvsEvent):
   sourceDvs: DvsEventArgument
   destinationDvs: DvsEventArgument


class DvsOutOfSyncHostArgument(pyVmomi.vmodl.DynamicData):
   outOfSyncHost: HostEventArgument
   configParamters: list[str] = []


class DvsPortBlockedEvent(DvsEvent):
   portKey: str
   statusDetail: _typing.Optional[str] = None
   runtimeInfo: _typing.Optional[pyVmomi.vim.dvs.DistributedVirtualPort.RuntimeInfo] = None
   prevBlockState: _typing.Optional[str] = None


class DvsPortConnectedEvent(DvsEvent):
   portKey: str
   connectee: _typing.Optional[pyVmomi.vim.dvs.PortConnectee] = None

class DvsPortCreatedEvent(DvsEvent):
   portKey: list[str] = []

class DvsPortDeletedEvent(DvsEvent):
   portKey: list[str] = []


class DvsPortDisconnectedEvent(DvsEvent):
   portKey: str
   connectee: _typing.Optional[pyVmomi.vim.dvs.PortConnectee] = None


class DvsPortEnteredPassthruEvent(DvsEvent):
   portKey: str
   runtimeInfo: _typing.Optional[pyVmomi.vim.dvs.DistributedVirtualPort.RuntimeInfo] = None


class DvsPortExitedPassthruEvent(DvsEvent):
   portKey: str
   runtimeInfo: _typing.Optional[pyVmomi.vim.dvs.DistributedVirtualPort.RuntimeInfo] = None

class DvsPortJoinPortgroupEvent(DvsEvent):
   portKey: str
   portgroupKey: str
   portgroupName: str

class DvsPortLeavePortgroupEvent(DvsEvent):
   portKey: str
   portgroupKey: str
   portgroupName: str


class DvsPortLinkDownEvent(DvsEvent):
   portKey: str
   runtimeInfo: _typing.Optional[pyVmomi.vim.dvs.DistributedVirtualPort.RuntimeInfo] = None


class DvsPortLinkUpEvent(DvsEvent):
   portKey: str
   runtimeInfo: _typing.Optional[pyVmomi.vim.dvs.DistributedVirtualPort.RuntimeInfo] = None


class DvsPortReconfiguredEvent(DvsEvent):
   portKey: list[str] = []
   configChanges: list[ChangesInfoEventArgument] = []


class DvsPortRuntimeChangeEvent(DvsEvent):
   portKey: str
   runtimeInfo: pyVmomi.vim.dvs.DistributedVirtualPort.RuntimeInfo


class DvsPortUnblockedEvent(DvsEvent):
   portKey: str
   runtimeInfo: _typing.Optional[pyVmomi.vim.dvs.DistributedVirtualPort.RuntimeInfo] = None
   prevBlockState: _typing.Optional[str] = None

class DvsPortVendorSpecificStateChangeEvent(DvsEvent):
   portKey: str


class DvsReconfiguredEvent(DvsEvent):
   configSpec: pyVmomi.vim.DistributedVirtualSwitch.ConfigSpec
   configChanges: _typing.Optional[ChangesInfoEventArgument] = None

class DvsRenamedEvent(DvsEvent):
   oldName: str
   newName: str

class DvsRestoreEvent(DvsEvent):
   pass


class DvsUpgradeAvailableEvent(DvsEvent):
   productInfo: pyVmomi.vim.dvs.ProductSpec


class DvsUpgradeInProgressEvent(DvsEvent):
   productInfo: pyVmomi.vim.dvs.ProductSpec


class DvsUpgradeRejectedEvent(DvsEvent):
   productInfo: pyVmomi.vim.dvs.ProductSpec


class DvsUpgradedEvent(DvsEvent):
   productInfo: pyVmomi.vim.dvs.ProductSpec

class EnteredMaintenanceModeEvent(HostEvent):
   pass

class EnteredStandbyModeEvent(HostEvent):
   pass

class EnteringMaintenanceModeEvent(HostEvent):
   pass

class EnteringStandbyModeEvent(HostEvent):
   pass

class EntityEventArgument(EventArgument):
   name: str

class ErrorUpgradeEvent(UpgradeEvent):
   pass


class Event(pyVmomi.vmodl.DynamicData):
   class EventSeverity(pyVmomi.VmomiSupport.Enum):
      error: _typing.ClassVar['EventSeverity'] = 'error'
      warning: _typing.ClassVar['EventSeverity'] = 'warning'
      info: _typing.ClassVar['EventSeverity'] = 'info'
      user: _typing.ClassVar['EventSeverity'] = 'user'

   key: int
   chainId: int
   createdTime: _datetime.datetime
   userName: str
   datacenter: _typing.Optional[DatacenterEventArgument] = None
   computeResource: _typing.Optional[ComputeResourceEventArgument] = None
   host: _typing.Optional[HostEventArgument] = None
   vm: _typing.Optional[VmEventArgument] = None
   ds: _typing.Optional[DatastoreEventArgument] = None
   net: _typing.Optional[NetworkEventArgument] = None
   dvs: _typing.Optional[DvsEventArgument] = None
   tgw: _typing.Optional[TgwEventArgument] = None
   fullFormattedMessage: _typing.Optional[str] = None
   changeTag: _typing.Optional[str] = None
   auditId: _typing.Optional[str] = None


class EventArgument(pyVmomi.vmodl.DynamicData):
   pass


class EventDescription(pyVmomi.vmodl.DynamicData):
   class EventCategory(pyVmomi.VmomiSupport.Enum):
      info: _typing.ClassVar['EventCategory'] = 'info'
      warning: _typing.ClassVar['EventCategory'] = 'warning'
      error: _typing.ClassVar['EventCategory'] = 'error'
      user: _typing.ClassVar['EventCategory'] = 'user'

   class EventArgDesc(pyVmomi.vmodl.DynamicData):
      name: str
      type: str
      description: _typing.Optional[pyVmomi.vim.ElementDescription] = None

   class EventDetail(pyVmomi.vmodl.DynamicData):
      key: type
      description: _typing.Optional[str] = None
      category: str
      formatOnDatacenter: str
      formatOnComputeResource: str
      formatOnHost: str
      formatOnVm: str
      fullFormat: str
      longDescription: _typing.Optional[str] = None

   category: list[pyVmomi.vim.ElementDescription] = []
   eventInfo: list[EventDetail] = []
   enumeratedTypes: list[pyVmomi.vim.EnumDescription] = []


class EventEx(Event):
   eventTypeId: str
   severity: _typing.Optional[str] = None
   message: _typing.Optional[str] = None
   arguments: list[pyVmomi.vmodl.KeyAnyValue] = []
   objectId: _typing.Optional[str] = None
   objectType: _typing.Optional[type] = None
   objectName: _typing.Optional[str] = None
   fault: _typing.Optional[pyVmomi.vmodl.MethodFault] = None


class EventFilterSpec(pyVmomi.vmodl.DynamicData):
   class RecursionOption(pyVmomi.VmomiSupport.Enum):
      self: _typing.ClassVar['RecursionOption'] = 'self'
      children: _typing.ClassVar['RecursionOption'] = 'children'
      all: _typing.ClassVar['RecursionOption'] = 'all'

   class ByEntity(pyVmomi.vmodl.DynamicData):
      entity: pyVmomi.vim.ManagedEntity
      recursion: RecursionOption

   class ByTime(pyVmomi.vmodl.DynamicData):
      beginTime: _typing.Optional[_datetime.datetime] = None
      endTime: _typing.Optional[_datetime.datetime] = None

   class ByUsername(pyVmomi.vmodl.DynamicData):
      systemUser: bool
      userList: list[str] = []

   entity: _typing.Optional[ByEntity] = None
   time: _typing.Optional[ByTime] = None
   userName: _typing.Optional[ByUsername] = None
   eventChainId: _typing.Optional[int] = None
   alarm: _typing.Optional[pyVmomi.vim.alarm.Alarm] = None
   scheduledTask: _typing.Optional[pyVmomi.vim.scheduler.ScheduledTask] = None
   disableFullMessage: _typing.Optional[bool] = None
   category: list[str] = []
   type: list[type] = []
   tag: list[str] = []
   eventTypeId: list[str] = []
   maxCount: _typing.Optional[int] = None
   delayedInit: _typing.Optional[bool] = None
   auditable: _typing.Optional[bool] = None
   auditId: list[str] = []


class EventHistoryCollector(pyVmomi.vim.HistoryCollector):
   @property
   def latestPage(self) -> list[Event]: ...
   @property
   def initialized(self) -> _typing.Optional[bool]: ...

   def ReadNext(self, maxCount: int) -> list[Event]: ...
   def ReadPrev(self, maxCount: int) -> list[Event]: ...


class EventManager(pyVmomi.VmomiSupport.ManagedObject):
   class EventViewSpec(pyVmomi.vmodl.DynamicData):
      pass

   class ViewByStartId(EventViewSpec):
      startEventId: int
      isForward: bool

   @property
   def description(self) -> EventDescription: ...
   @property
   def latestEvent(self) -> _typing.Optional[Event]: ...
   @property
   def maxCollector(self) -> int: ...

   def RetrieveArgumentDescription(self, eventTypeId: str) -> list[EventDescription.EventArgDesc]: ...
   def CreateCollector(self, filter: EventFilterSpec) -> EventHistoryCollector: ...
   def LogUserEvent(self, entity: pyVmomi.vim.ManagedEntity, msg: str) -> None: ...
   def QueryEvent(self, filter: EventFilterSpec, eventViewSpec: _typing.Optional[EventViewSpec]) -> list[Event]: ...
   def PostEvent(self, eventToPost: Event, taskInfo: _typing.Optional[pyVmomi.vim.TaskInfo]) -> None: ...

class ExitMaintenanceModeEvent(HostEvent):
   pass

class ExitStandbyModeFailedEvent(HostEvent):
   pass

class ExitedStandbyModeEvent(HostEvent):
   pass

class ExitingStandbyModeEvent(HostEvent):
   pass


class ExtendedEvent(GeneralEvent):
   class Pair(pyVmomi.vmodl.DynamicData):
      key: str
      value: str

   eventTypeId: str
   managedObject: pyVmomi.VmomiSupport.ManagedObject
   data: list[Pair] = []

class FailoverLevelRestored(ClusterEvent):
   pass


class FolderEventArgument(EntityEventArgument):
   folder: pyVmomi.vim.Folder

class GeneralEvent(Event):
   message: str

class GeneralHostErrorEvent(GeneralEvent):
   pass

class GeneralHostInfoEvent(GeneralEvent):
   pass

class GeneralHostWarningEvent(GeneralEvent):
   pass


class GeneralUserEvent(GeneralEvent):
   entity: _typing.Optional[ManagedEntityEventArgument] = None

class GeneralVmErrorEvent(GeneralEvent):
   pass

class GeneralVmInfoEvent(GeneralEvent):
   pass

class GeneralVmWarningEvent(GeneralEvent):
   pass

class GhostDvsProxySwitchDetectedEvent(HostEvent):
   switchUuid: list[str] = []

class GhostDvsProxySwitchRemovedEvent(HostEvent):
   switchUuid: list[str] = []


class GlobalMessageChangedEvent(SessionEvent):
   message: str
   prevMessage: _typing.Optional[str] = None


class HealthStatusChangedEvent(Event):
   componentId: str
   oldStatus: str
   newStatus: str
   componentName: str
   serviceId: _typing.Optional[str] = None

class HostAddFailedEvent(HostEvent):
   hostname: str

class HostAddedEvent(HostEvent):
   pass

class HostAdminDisableEvent(HostEvent):
   pass

class HostAdminEnableEvent(HostEvent):
   pass

class HostCnxFailedAccountFailedEvent(HostEvent):
   pass

class HostCnxFailedAlreadyManagedEvent(HostEvent):
   serverName: str

class HostCnxFailedBadCcagentEvent(HostEvent):
   pass

class HostCnxFailedBadUsernameEvent(HostEvent):
   pass

class HostCnxFailedBadVersionEvent(HostEvent):
   pass

class HostCnxFailedCcagentUpgradeEvent(HostEvent):
   pass

class HostCnxFailedEvent(HostEvent):
   pass

class HostCnxFailedNetworkErrorEvent(HostEvent):
   pass

class HostCnxFailedNoAccessEvent(HostEvent):
   pass

class HostCnxFailedNoConnectionEvent(HostEvent):
   pass

class HostCnxFailedNoLicenseEvent(HostEvent):
   pass

class HostCnxFailedNotFoundEvent(HostEvent):
   pass

class HostCnxFailedTimeoutEvent(HostEvent):
   pass

class HostComplianceCheckedEvent(HostEvent):
   profile: ProfileEventArgument

class HostCompliantEvent(HostEvent):
   pass

class HostConfigAppliedEvent(HostEvent):
   pass

class HostConnectedEvent(HostEvent):
   pass

class HostConnectionLostEvent(HostEvent):
   pass

class HostDasDisabledEvent(HostEvent):
   pass

class HostDasDisablingEvent(HostEvent):
   pass

class HostDasEnabledEvent(HostEvent):
   pass

class HostDasEnablingEvent(HostEvent):
   pass


class HostDasErrorEvent(HostEvent):
   class HostDasErrorReason(pyVmomi.VmomiSupport.Enum):
      configFailed: _typing.ClassVar['HostDasErrorReason'] = 'configFailed'
      timeout: _typing.ClassVar['HostDasErrorReason'] = 'timeout'
      communicationInitFailed: _typing.ClassVar['HostDasErrorReason'] = 'communicationInitFailed'
      healthCheckScriptFailed: _typing.ClassVar['HostDasErrorReason'] = 'healthCheckScriptFailed'
      agentFailed: _typing.ClassVar['HostDasErrorReason'] = 'agentFailed'
      agentShutdown: _typing.ClassVar['HostDasErrorReason'] = 'agentShutdown'
      isolationAddressUnpingable: _typing.ClassVar['HostDasErrorReason'] = 'isolationAddressUnpingable'
      other: _typing.ClassVar['HostDasErrorReason'] = 'other'

   message: _typing.Optional[str] = None
   reason: _typing.Optional[str] = None

class HostDasEvent(HostEvent):
   pass

class HostDasOkEvent(HostEvent):
   pass


class HostDisconnectedEvent(HostEvent):
   class ReasonCode(pyVmomi.VmomiSupport.Enum):
      sslThumbprintVerifyFailed: _typing.ClassVar['ReasonCode'] = 'sslThumbprintVerifyFailed'
      licenseExpired: _typing.ClassVar['ReasonCode'] = 'licenseExpired'
      agentUpgrade: _typing.ClassVar['ReasonCode'] = 'agentUpgrade'
      userRequest: _typing.ClassVar['ReasonCode'] = 'userRequest'
      insufficientLicenses: _typing.ClassVar['ReasonCode'] = 'insufficientLicenses'
      agentOutOfDate: _typing.ClassVar['ReasonCode'] = 'agentOutOfDate'
      passwordDecryptFailure: _typing.ClassVar['ReasonCode'] = 'passwordDecryptFailure'
      unknown: _typing.ClassVar['ReasonCode'] = 'unknown'
      vcVRAMCapacityExceeded: _typing.ClassVar['ReasonCode'] = 'vcVRAMCapacityExceeded'

   reason: _typing.Optional[str] = None


class HostEnableAdminFailedEvent(HostEvent):
   permissions: list[pyVmomi.vim.AuthorizationManager.Permission] = []

class HostEvent(Event):
   pass


class HostEventArgument(EntityEventArgument):
   host: pyVmomi.vim.HostSystem


class HostExtraNetworksEvent(HostDasEvent):
   ips: _typing.Optional[str] = None

class HostGetShortNameFailedEvent(HostEvent):
   pass

class HostInAuditModeEvent(HostEvent):
   pass

class HostInventoryFullEvent(LicenseEvent):
   capacity: int

class HostInventoryUnreadableEvent(Event):
   pass

class HostIpChangedEvent(HostEvent):
   oldIP: str
   newIP: str

class HostIpInconsistentEvent(HostEvent):
   ipAddress: str
   ipAddress2: str

class HostIpToShortNameFailedEvent(HostEvent):
   pass

class HostIsolationIpPingFailedEvent(HostDasEvent):
   isolationIp: str

class HostLicenseExpiredEvent(LicenseEvent):
   pass


class HostLocalPortCreatedEvent(DvsEvent):
   hostLocalPort: pyVmomi.vim.dvs.DistributedVirtualPort.HostLocalPortInfo


class HostMissingNetworksEvent(HostDasEvent):
   ips: _typing.Optional[str] = None


class HostMonitoringStateChangedEvent(ClusterEvent):
   state: str
   prevState: _typing.Optional[str] = None


class HostNoAvailableNetworksEvent(HostDasEvent):
   ips: _typing.Optional[str] = None

class HostNoHAEnabledPortGroupsEvent(HostDasEvent):
   pass

class HostNoRedundantManagementNetworkEvent(HostDasEvent):
   pass

class HostNonCompliantEvent(HostEvent):
   pass

class HostNotInClusterEvent(HostDasEvent):
   pass

class HostOvercommittedEvent(ClusterOvercommittedEvent):
   pass

class HostPrimaryAgentNotShortNameEvent(HostDasEvent):
   primaryAgent: str

class HostProfileAppliedEvent(HostEvent):
   profile: ProfileEventArgument

class HostReconnectionFailedEvent(HostEvent):
   pass

class HostRemovedEvent(HostEvent):
   pass

class HostShortNameInconsistentEvent(HostDasEvent):
   shortName: str
   shortName2: str

class HostShortNameToIpFailedEvent(HostEvent):
   shortName: str

class HostShutdownEvent(HostEvent):
   reason: str

class HostSpecificationChangedEvent(HostEvent):
   pass

class HostSpecificationRequireEvent(HostEvent):
   pass


class HostSpecificationUpdateEvent(HostEvent):
   hostSpec: pyVmomi.vim.profile.host.HostSpecification

class HostStatusChangedEvent(ClusterStatusChangedEvent):
   pass

class HostSubSpecificationDeleteEvent(HostEvent):
   subSpecName: str


class HostSubSpecificationUpdateEvent(HostEvent):
   hostSubSpec: pyVmomi.vim.profile.host.HostSubSpecification


class HostSyncFailedEvent(HostEvent):
   reason: pyVmomi.vmodl.MethodFault

class HostUpgradeFailedEvent(HostEvent):
   pass

class HostUserWorldSwapNotEnabledEvent(HostEvent):
   pass


class HostVnicConnectedToCustomizedDVPortEvent(HostEvent):
   vnic: VnicPortArgument
   prevPortKey: _typing.Optional[str] = None


class HostWwnChangedEvent(HostEvent):
   oldNodeWwns: list[pyVmomi.VmomiSupport.long] = []
   oldPortWwns: list[pyVmomi.VmomiSupport.long] = []
   newNodeWwns: list[pyVmomi.VmomiSupport.long] = []
   newPortWwns: list[pyVmomi.VmomiSupport.long] = []


class HostWwnConflictEvent(HostEvent):
   conflictedVms: list[VmEventArgument] = []
   conflictedHosts: list[HostEventArgument] = []
   wwn: pyVmomi.VmomiSupport.long

class IncorrectHostInformationEvent(LicenseEvent):
   pass

class InfoUpgradeEvent(UpgradeEvent):
   pass

class InsufficientFailoverResourcesEvent(ClusterEvent):
   pass

class InvalidEditionEvent(LicenseEvent):
   feature: str

class LicenseEvent(Event):
   pass


class LicenseExpiredEvent(Event):
   feature: pyVmomi.vim.LicenseManager.FeatureInfo

class LicenseNonComplianceEvent(LicenseEvent):
   url: str

class LicenseRestrictedEvent(LicenseEvent):
   pass

class LicenseServerAvailableEvent(LicenseEvent):
   licenseServer: str

class LicenseServerUnavailableEvent(LicenseEvent):
   licenseServer: str


class LocalDatastoreCreatedEvent(HostEvent):
   datastore: DatastoreEventArgument
   datastoreUrl: _typing.Optional[str] = None

class LocalTSMEnabledEvent(HostEvent):
   pass

class LockerMisconfiguredEvent(Event):
   datastore: DatastoreEventArgument


class LockerReconfiguredEvent(Event):
   oldDatastore: _typing.Optional[DatastoreEventArgument] = None
   newDatastore: _typing.Optional[DatastoreEventArgument] = None


class ManagedEntityEventArgument(EntityEventArgument):
   entity: pyVmomi.vim.ManagedEntity

class MigrationErrorEvent(MigrationEvent):
   pass


class MigrationEvent(VmEvent):
   fault: pyVmomi.vmodl.MethodFault

class MigrationHostErrorEvent(MigrationEvent):
   dstHost: HostEventArgument

class MigrationHostWarningEvent(MigrationEvent):
   dstHost: HostEventArgument

class MigrationResourceErrorEvent(MigrationEvent):
   dstPool: ResourcePoolEventArgument
   dstHost: HostEventArgument

class MigrationResourceWarningEvent(MigrationEvent):
   dstPool: ResourcePoolEventArgument
   dstHost: HostEventArgument

class MigrationWarningEvent(MigrationEvent):
   pass

class MtuMatchEvent(DvsHealthStatusChangeEvent):
   pass

class MtuMismatchEvent(DvsHealthStatusChangeEvent):
   pass


class NASDatastoreCreatedEvent(HostEvent):
   datastore: DatastoreEventArgument
   datastoreUrl: _typing.Optional[str] = None


class NetworkEventArgument(EntityEventArgument):
   network: pyVmomi.vim.Network

class NetworkRollbackEvent(Event):
   methodName: str
   transactionId: str

class NoAccessUserEvent(SessionEvent):
   ipAddress: str

class NoDatastoresConfiguredEvent(HostEvent):
   pass


class NoLicenseEvent(LicenseEvent):
   feature: pyVmomi.vim.LicenseManager.FeatureInfo

class NoMaintenanceModeDrsRecommendationForVM(VmEvent):
   pass

class NonVIWorkloadDetectedOnDatastoreEvent(DatastoreEvent):
   pass

class NotEnoughResourcesToStartVmEvent(VmEvent):
   reason: str

class OutOfSyncDvsHost(DvsEvent):
   hostOutOfSync: list[DvsOutOfSyncHostArgument] = []

class PermissionAddedEvent(PermissionEvent):
   role: RoleEventArgument
   propagate: bool

class PermissionEvent(AuthorizationEvent):
   entity: ManagedEntityEventArgument
   principal: str
   group: bool

class PermissionRemovedEvent(PermissionEvent):
   pass


class PermissionUpdatedEvent(PermissionEvent):
   role: RoleEventArgument
   propagate: bool
   prevRole: _typing.Optional[RoleEventArgument] = None
   prevPropagate: _typing.Optional[bool] = None

class ProfileAssociatedEvent(ProfileEvent):
   pass

class ProfileChangedEvent(ProfileEvent):
   pass

class ProfileCreatedEvent(ProfileEvent):
   pass

class ProfileDissociatedEvent(ProfileEvent):
   pass

class ProfileEvent(Event):
   profile: ProfileEventArgument


class ProfileEventArgument(EventArgument):
   profile: pyVmomi.vim.profile.Profile
   name: str


class ProfileReferenceHostChangedEvent(ProfileEvent):
   referenceHost: _typing.Optional[pyVmomi.vim.HostSystem] = None
   referenceHostName: _typing.Optional[str] = None
   prevReferenceHostName: _typing.Optional[str] = None

class ProfileRemovedEvent(ProfileEvent):
   pass


class RecoveryEvent(DvsEvent):
   hostName: str
   portKey: str
   dvsUuid: _typing.Optional[str] = None
   vnic: _typing.Optional[str] = None

class RemoteTSMEnabledEvent(HostEvent):
   pass

class ResourcePoolCreatedEvent(ResourcePoolEvent):
   parent: ResourcePoolEventArgument

class ResourcePoolDestroyedEvent(ResourcePoolEvent):
   pass

class ResourcePoolEvent(Event):
   resourcePool: ResourcePoolEventArgument


class ResourcePoolEventArgument(EntityEventArgument):
   resourcePool: pyVmomi.vim.ResourcePool

class ResourcePoolMovedEvent(ResourcePoolEvent):
   oldParent: ResourcePoolEventArgument
   newParent: ResourcePoolEventArgument


class ResourcePoolReconfiguredEvent(ResourcePoolEvent):
   configChanges: _typing.Optional[ChangesInfoEventArgument] = None

class ResourceViolatedEvent(ResourcePoolEvent):
   pass


class RoleAddedEvent(RoleEvent):
   privilegeList: list[str] = []

class RoleEvent(AuthorizationEvent):
   role: RoleEventArgument

class RoleEventArgument(EventArgument):
   roleId: int
   name: str

class RoleRemovedEvent(RoleEvent):
   pass


class RoleUpdatedEvent(RoleEvent):
   privilegeList: list[str] = []
   prevRoleName: _typing.Optional[str] = None
   privilegesAdded: list[str] = []
   privilegesRemoved: list[str] = []


class RollbackEvent(DvsEvent):
   hostName: str
   methodName: _typing.Optional[str] = None

class ScheduledTaskCompletedEvent(ScheduledTaskEvent):
   pass

class ScheduledTaskCreatedEvent(ScheduledTaskEvent):
   pass

class ScheduledTaskEmailCompletedEvent(ScheduledTaskEvent):
   to: str


class ScheduledTaskEmailFailedEvent(ScheduledTaskEvent):
   to: str
   reason: pyVmomi.vmodl.MethodFault

class ScheduledTaskEvent(Event):
   scheduledTask: ScheduledTaskEventArgument
   entity: ManagedEntityEventArgument


class ScheduledTaskEventArgument(EntityEventArgument):
   scheduledTask: pyVmomi.vim.scheduler.ScheduledTask


class ScheduledTaskFailedEvent(ScheduledTaskEvent):
   reason: pyVmomi.vmodl.MethodFault


class ScheduledTaskReconfiguredEvent(ScheduledTaskEvent):
   configChanges: _typing.Optional[ChangesInfoEventArgument] = None

class ScheduledTaskRemovedEvent(ScheduledTaskEvent):
   pass

class ScheduledTaskStartedEvent(ScheduledTaskEvent):
   pass

class ServerLicenseExpiredEvent(LicenseEvent):
   product: str

class ServerStartedSessionEvent(SessionEvent):
   pass

class SessionEvent(Event):
   pass

class SessionTerminatedEvent(SessionEvent):
   sessionId: str
   terminatedUsername: str


class TaskEvent(Event):
   info: pyVmomi.vim.TaskInfo

class TaskTimeoutEvent(TaskEvent):
   pass

class TeamingMatchEvent(DvsHealthStatusChangeEvent):
   pass

class TeamingMisMatchEvent(DvsHealthStatusChangeEvent):
   pass

class TemplateBeingUpgradedEvent(TemplateUpgradeEvent):
   pass

class TemplateUpgradeEvent(Event):
   legacyTemplate: str


class TemplateUpgradeFailedEvent(TemplateUpgradeEvent):
   reason: pyVmomi.vmodl.MethodFault

class TemplateUpgradedEvent(TemplateUpgradeEvent):
   pass


class TgwEventArgument(EntityEventArgument):
   tgw: pyVmomi.vim.TransitGateway

class TimedOutHostOperationEvent(HostEvent):
   pass

class UnlicensedVirtualMachinesEvent(LicenseEvent):
   unlicensed: int
   available: int

class UnlicensedVirtualMachinesFoundEvent(LicenseEvent):
   available: int

class UpdatedAgentBeingRestartedEvent(HostEvent):
   pass

class UpgradeEvent(Event):
   message: str

class UplinkPortMtuNotSupportEvent(DvsHealthStatusChangeEvent):
   pass

class UplinkPortMtuSupportEvent(DvsHealthStatusChangeEvent):
   pass

class UplinkPortVlanTrunkedEvent(DvsHealthStatusChangeEvent):
   pass

class UplinkPortVlanUntrunkedEvent(DvsHealthStatusChangeEvent):
   pass

class UserAssignedToGroup(HostEvent):
   userLogin: str
   group: str


class UserLoginSessionEvent(SessionEvent):
   ipAddress: str
   userAgent: _typing.Optional[str] = None
   locale: str
   sessionId: str


class UserLogoutSessionEvent(SessionEvent):
   ipAddress: _typing.Optional[str] = None
   userAgent: _typing.Optional[str] = None
   callCount: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   sessionId: _typing.Optional[str] = None
   loginTime: _typing.Optional[_datetime.datetime] = None

class UserPasswordChanged(HostEvent):
   userLogin: str

class UserUnassignedFromGroup(HostEvent):
   userLogin: str
   group: str

class UserUpgradeEvent(UpgradeEvent):
   pass


class VMFSDatastoreCreatedEvent(HostEvent):
   datastore: DatastoreEventArgument
   datastoreUrl: _typing.Optional[str] = None

class VMFSDatastoreExpandedEvent(HostEvent):
   datastore: DatastoreEventArgument

class VMFSDatastoreExtendedEvent(HostEvent):
   datastore: DatastoreEventArgument

class VMotionLicenseExpiredEvent(LicenseEvent):
   pass


class VcAgentUninstallFailedEvent(HostEvent):
   reason: _typing.Optional[str] = None

class VcAgentUninstalledEvent(HostEvent):
   pass


class VcAgentUpgradeFailedEvent(HostEvent):
   reason: _typing.Optional[str] = None

class VcAgentUpgradedEvent(HostEvent):
   pass

class VimAccountPasswordChangedEvent(HostEvent):
   pass

class VmAcquiredMksTicketEvent(VmEvent):
   pass

class VmAcquiredTicketEvent(VmEvent):
   ticketType: str

class VmAutoRenameEvent(VmEvent):
   oldName: str
   newName: str

class VmBeingClonedEvent(VmCloneEvent):
   destFolder: FolderEventArgument
   destName: str
   destHost: HostEventArgument

class VmBeingClonedNoFolderEvent(VmCloneEvent):
   destName: str
   destHost: HostEventArgument


class VmBeingCreatedEvent(VmEvent):
   configSpec: _typing.Optional[pyVmomi.vim.vm.ConfigSpec] = None

class VmBeingDeployedEvent(VmEvent):
   srcTemplate: VmEventArgument


class VmBeingHotMigratedEvent(VmEvent):
   destHost: HostEventArgument
   destDatacenter: _typing.Optional[DatacenterEventArgument] = None
   destDatastore: _typing.Optional[DatastoreEventArgument] = None


class VmBeingMigratedEvent(VmEvent):
   destHost: HostEventArgument
   destDatacenter: _typing.Optional[DatacenterEventArgument] = None
   destDatastore: _typing.Optional[DatastoreEventArgument] = None


class VmBeingRelocatedEvent(VmRelocateSpecEvent):
   destHost: HostEventArgument
   destDatacenter: _typing.Optional[DatacenterEventArgument] = None
   destDatastore: _typing.Optional[DatastoreEventArgument] = None

class VmCloneEvent(VmEvent):
   pass


class VmCloneFailedEvent(VmCloneEvent):
   destFolder: FolderEventArgument
   destName: str
   destHost: HostEventArgument
   reason: pyVmomi.vmodl.MethodFault

class VmClonedEvent(VmCloneEvent):
   sourceVm: VmEventArgument

class VmConfigMissingEvent(VmEvent):
   pass

class VmConnectedEvent(VmEvent):
   pass

class VmCreatedEvent(VmEvent):
   pass


class VmDasBeingResetEvent(VmEvent):
   class ReasonCode(pyVmomi.VmomiSupport.Enum):
      vmtoolsHeartbeatFailure: _typing.ClassVar['ReasonCode'] = 'vmtoolsHeartbeatFailure'
      appHeartbeatFailure: _typing.ClassVar['ReasonCode'] = 'appHeartbeatFailure'
      appImmediateResetRequest: _typing.ClassVar['ReasonCode'] = 'appImmediateResetRequest'
      vmcpResetApdCleared: _typing.ClassVar['ReasonCode'] = 'vmcpResetApdCleared'
      guestOsCrashFailure: _typing.ClassVar['ReasonCode'] = 'guestOsCrashFailure'

   reason: _typing.Optional[str] = None

class VmDasBeingResetWithScreenshotEvent(VmDasBeingResetEvent):
   screenshotFilePath: str

class VmDasResetFailedEvent(VmEvent):
   pass

class VmDasUpdateErrorEvent(VmEvent):
   pass

class VmDasUpdateOkEvent(VmEvent):
   pass

class VmDateRolledBackEvent(VmEvent):
   pass


class VmDeployFailedEvent(VmEvent):
   destDatastore: EntityEventArgument
   reason: pyVmomi.vmodl.MethodFault

class VmDeployedEvent(VmEvent):
   srcTemplate: VmEventArgument

class VmDisconnectedEvent(VmEvent):
   pass

class VmDiscoveredEvent(VmEvent):
   pass


class VmDiskFailedEvent(VmEvent):
   disk: str
   reason: pyVmomi.vmodl.MethodFault

class VmEmigratingEvent(VmEvent):
   pass

class VmEndRecordingEvent(VmEvent):
   pass

class VmEndReplayingEvent(VmEvent):
   pass

class VmEvent(Event):
   template: bool


class VmEventArgument(EntityEventArgument):
   vm: pyVmomi.vim.VirtualMachine


class VmFailedMigrateEvent(VmEvent):
   destHost: HostEventArgument
   reason: pyVmomi.vmodl.MethodFault
   destDatacenter: _typing.Optional[DatacenterEventArgument] = None
   destDatastore: _typing.Optional[DatastoreEventArgument] = None


class VmFailedRelayoutEvent(VmEvent):
   reason: pyVmomi.vmodl.MethodFault

class VmFailedRelayoutOnVmfs2DatastoreEvent(VmEvent):
   pass


class VmFailedStartingSecondaryEvent(VmEvent):
   class FailureReason(pyVmomi.VmomiSupport.Enum):
      incompatibleHost: _typing.ClassVar['FailureReason'] = 'incompatibleHost'
      loginFailed: _typing.ClassVar['FailureReason'] = 'loginFailed'
      registerVmFailed: _typing.ClassVar['FailureReason'] = 'registerVmFailed'
      migrateFailed: _typing.ClassVar['FailureReason'] = 'migrateFailed'

   reason: _typing.Optional[str] = None


class VmFailedToPowerOffEvent(VmEvent):
   reason: pyVmomi.vmodl.MethodFault


class VmFailedToPowerOnEvent(VmEvent):
   reason: pyVmomi.vmodl.MethodFault


class VmFailedToRebootGuestEvent(VmEvent):
   reason: pyVmomi.vmodl.MethodFault


class VmFailedToResetEvent(VmEvent):
   reason: pyVmomi.vmodl.MethodFault


class VmFailedToShutdownGuestEvent(VmEvent):
   reason: pyVmomi.vmodl.MethodFault


class VmFailedToStandbyGuestEvent(VmEvent):
   reason: pyVmomi.vmodl.MethodFault


class VmFailedToSuspendEvent(VmEvent):
   reason: pyVmomi.vmodl.MethodFault

class VmFailedUpdatingSecondaryConfig(VmEvent):
   pass


class VmFailoverFailed(VmEvent):
   reason: _typing.Optional[pyVmomi.vmodl.MethodFault] = None


class VmFaultToleranceStateChangedEvent(VmEvent):
   oldState: pyVmomi.vim.VirtualMachine.FaultToleranceState
   newState: pyVmomi.vim.VirtualMachine.FaultToleranceState

class VmFaultToleranceTurnedOffEvent(VmEvent):
   pass


class VmFaultToleranceVmTerminatedEvent(VmEvent):
   reason: _typing.Optional[str] = None

class VmGuestOSCrashedEvent(VmEvent):
   pass

class VmGuestRebootEvent(VmEvent):
   pass

class VmGuestShutdownEvent(VmEvent):
   pass

class VmGuestStandbyEvent(VmEvent):
   pass


class VmHealthMonitoringStateChangedEvent(ClusterEvent):
   state: str
   prevState: _typing.Optional[str] = None

class VmInstanceUuidAssignedEvent(VmEvent):
   instanceUuid: str

class VmInstanceUuidChangedEvent(VmEvent):
   oldInstanceUuid: str
   newInstanceUuid: str

class VmInstanceUuidConflictEvent(VmEvent):
   conflictedVm: VmEventArgument
   instanceUuid: str

class VmMacAssignedEvent(VmEvent):
   adapter: str
   mac: str

class VmMacChangedEvent(VmEvent):
   adapter: str
   oldMac: str
   newMac: str

class VmMacConflictEvent(VmEvent):
   conflictedVm: VmEventArgument
   mac: str

class VmMaxFTRestartCountReached(VmEvent):
   pass

class VmMaxRestartCountReached(VmEvent):
   pass


class VmMessageErrorEvent(VmEvent):
   message: str
   messageInfo: list[pyVmomi.vim.vm.Message] = []


class VmMessageEvent(VmEvent):
   message: str
   messageInfo: list[pyVmomi.vim.vm.Message] = []


class VmMessageWarningEvent(VmEvent):
   message: str
   messageInfo: list[pyVmomi.vim.vm.Message] = []


class VmMigratedEvent(VmEvent):
   sourceHost: HostEventArgument
   sourceDatacenter: _typing.Optional[DatacenterEventArgument] = None
   sourceDatastore: _typing.Optional[DatastoreEventArgument] = None

class VmNoCompatibleHostForSecondaryEvent(VmEvent):
   pass

class VmNoNetworkAccessEvent(VmEvent):
   destHost: HostEventArgument

class VmOrphanedEvent(VmEvent):
   pass

class VmPowerOffOnIsolationEvent(VmPoweredOffEvent):
   isolatedHost: HostEventArgument

class VmPoweredOffEvent(VmEvent):
   pass

class VmPoweredOnEvent(VmEvent):
   pass

class VmPoweringOnWithCustomizedDVPortEvent(VmEvent):
   vnic: list[VnicPortArgument] = []


class VmPrimaryFailoverEvent(VmEvent):
   reason: _typing.Optional[str] = None


class VmReconfiguredEvent(VmEvent):
   configSpec: pyVmomi.vim.vm.ConfigSpec
   configChanges: _typing.Optional[ChangesInfoEventArgument] = None

class VmRegisteredEvent(VmEvent):
   pass

class VmRelayoutSuccessfulEvent(VmEvent):
   pass

class VmRelayoutUpToDateEvent(VmEvent):
   pass

class VmReloadFromPathEvent(VmEvent):
   configPath: str

class VmReloadFromPathFailedEvent(VmEvent):
   configPath: str


class VmRelocateFailedEvent(VmRelocateSpecEvent):
   destHost: HostEventArgument
   reason: pyVmomi.vmodl.MethodFault
   destDatacenter: _typing.Optional[DatacenterEventArgument] = None
   destDatastore: _typing.Optional[DatastoreEventArgument] = None

class VmRelocateSpecEvent(VmEvent):
   pass


class VmRelocatedEvent(VmRelocateSpecEvent):
   sourceHost: HostEventArgument
   sourceDatacenter: _typing.Optional[DatacenterEventArgument] = None
   sourceDatastore: _typing.Optional[DatastoreEventArgument] = None

class VmRemoteConsoleConnectedEvent(VmEvent):
   pass

class VmRemoteConsoleDisconnectedEvent(VmEvent):
   pass

class VmRemovedEvent(VmEvent):
   pass

class VmRenamedEvent(VmEvent):
   oldName: str
   newName: str

class VmRequirementsExceedCurrentEVCModeEvent(VmEvent):
   pass

class VmResettingEvent(VmEvent):
   pass

class VmResourcePoolMovedEvent(VmEvent):
   oldParent: ResourcePoolEventArgument
   newParent: ResourcePoolEventArgument


class VmResourceReallocatedEvent(VmEvent):
   configChanges: _typing.Optional[ChangesInfoEventArgument] = None

class VmRestartedOnAlternateHostEvent(VmPoweredOnEvent):
   sourceHost: HostEventArgument

class VmResumingEvent(VmEvent):
   pass

class VmSecondaryAddedEvent(VmEvent):
   pass


class VmSecondaryDisabledBySystemEvent(VmEvent):
   reason: _typing.Optional[pyVmomi.vmodl.MethodFault] = None

class VmSecondaryDisabledEvent(VmEvent):
   pass

class VmSecondaryEnabledEvent(VmEvent):
   pass

class VmSecondaryStartedEvent(VmEvent):
   pass


class VmShutdownOnIsolationEvent(VmPoweredOffEvent):
   class Operation(pyVmomi.VmomiSupport.Enum):
      shutdown: _typing.ClassVar['Operation'] = 'shutdown'
      poweredOff: _typing.ClassVar['Operation'] = 'poweredOff'

   isolatedHost: HostEventArgument
   shutdownResult: _typing.Optional[str] = None

class VmStartRecordingEvent(VmEvent):
   pass

class VmStartReplayingEvent(VmEvent):
   pass

class VmStartingEvent(VmEvent):
   pass

class VmStartingSecondaryEvent(VmEvent):
   pass

class VmStaticMacConflictEvent(VmEvent):
   conflictedVm: VmEventArgument
   mac: str

class VmStoppingEvent(VmEvent):
   pass

class VmSuspendedEvent(VmEvent):
   pass

class VmSuspendingEvent(VmEvent):
   pass


class VmTimedoutStartingSecondaryEvent(VmEvent):
   timeout: _typing.Optional[pyVmomi.VmomiSupport.long] = None

class VmUnsupportedStartingEvent(VmStartingEvent):
   guestId: str

class VmUpgradeCompleteEvent(VmEvent):
   version: str

class VmUpgradeFailedEvent(VmEvent):
   pass

class VmUpgradingEvent(VmEvent):
   version: str

class VmUuidAssignedEvent(VmEvent):
   uuid: str

class VmUuidChangedEvent(VmEvent):
   oldUuid: str
   newUuid: str

class VmUuidConflictEvent(VmEvent):
   conflictedVm: VmEventArgument
   uuid: str


class VmVnicPoolReservationViolationClearEvent(DvsEvent):
   vmVnicResourcePoolKey: str
   vmVnicResourcePoolName: _typing.Optional[str] = None


class VmVnicPoolReservationViolationRaiseEvent(DvsEvent):
   vmVnicResourcePoolKey: str
   vmVnicResourcePoolName: _typing.Optional[str] = None


class VmWwnAssignedEvent(VmEvent):
   nodeWwns: list[pyVmomi.VmomiSupport.long] = []
   portWwns: list[pyVmomi.VmomiSupport.long] = []


class VmWwnChangedEvent(VmEvent):
   oldNodeWwns: list[pyVmomi.VmomiSupport.long] = []
   oldPortWwns: list[pyVmomi.VmomiSupport.long] = []
   newNodeWwns: list[pyVmomi.VmomiSupport.long] = []
   newPortWwns: list[pyVmomi.VmomiSupport.long] = []


class VmWwnConflictEvent(VmEvent):
   conflictedVms: list[VmEventArgument] = []
   conflictedHosts: list[HostEventArgument] = []
   wwn: pyVmomi.VmomiSupport.long


class VnicPortArgument(pyVmomi.vmodl.DynamicData):
   vnic: str
   port: pyVmomi.vim.dvs.PortConnection

class WarningUpgradeEvent(UpgradeEvent):
   pass

class iScsiBootFailureEvent(HostEvent):
   pass
