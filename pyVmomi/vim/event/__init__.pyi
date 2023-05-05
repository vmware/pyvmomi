from typing import List
from enum import Enum
from pyVmomi import vim, vmodl
from datetime import datetime
from pyVmomi.VmomiSupport import ManagedObject, NoneType, long


class EventHistoryCollector(vim.HistoryCollector):
    @property
    def latestPage(self) -> List[Event]: ...
    def ReadNext(self, maxCount: int) -> List[Event]: ...
    def ReadPrev(self, maxCount: int) -> List[Event]: ...


class EventManager(ManagedObject):
    @property
    def description(self) -> EventDescription: ...
    @property
    def latestEvent(self) -> Event: ...
    @property
    def maxCollector(self) -> int: ...
    def RetrieveArgumentDescription(self, eventTypeId: str) -> List[EventDescription.EventArgDesc]: ...
    def CreateCollector(self, filter: EventFilterSpec) -> EventHistoryCollector: ...
    def LogUserEvent(self, entity: vim.ManagedEntity, msg: str) -> NoneType: ...
    def QueryEvent(self, filter: EventFilterSpec) -> List[Event]: ...
    def PostEvent(self, eventToPost: Event, taskInfo: vim.TaskInfo) -> NoneType: ...


class AccountCreatedEvent(HostEvent):
    @property
    def spec(self) -> vim.host.LocalAccountManager.AccountSpecification: ...
    @property
    def group(self) -> bool: ...


class AccountRemovedEvent(HostEvent):
    @property
    def account(self) -> str: ...
    @property
    def group(self) -> bool: ...


class AccountUpdatedEvent(HostEvent):
    @property
    def spec(self) -> vim.host.LocalAccountManager.AccountSpecification: ...
    @property
    def group(self) -> bool: ...
    @property
    def prevDescription(self) -> str: ...


class AdminPasswordNotChangedEvent(HostEvent): ...


class AlarmAcknowledgedEvent(AlarmEvent):
    @property
    def source(self) -> ManagedEntityEventArgument: ...
    @property
    def entity(self) -> ManagedEntityEventArgument: ...


class AlarmActionTriggeredEvent(AlarmEvent):
    @property
    def source(self) -> ManagedEntityEventArgument: ...
    @property
    def entity(self) -> ManagedEntityEventArgument: ...


class AlarmClearedEvent(AlarmEvent):
    @property
    def source(self) -> ManagedEntityEventArgument: ...
    @property
    def entity(self) -> ManagedEntityEventArgument: ...
    @property
    def from(self) -> str: ...


class AlarmCreatedEvent(AlarmEvent):
    @property
    def entity(self) -> ManagedEntityEventArgument: ...


class AlarmEmailCompletedEvent(AlarmEvent):
    @property
    def entity(self) -> ManagedEntityEventArgument: ...
    @property
    def to(self) -> str: ...


class AlarmEmailFailedEvent(AlarmEvent):
    @property
    def entity(self) -> ManagedEntityEventArgument: ...
    @property
    def to(self) -> str: ...
    @property
    def reason(self) -> vmodl.MethodFault: ...


class AlarmEvent(Event):
    @property
    def alarm(self) -> AlarmEventArgument: ...


class AlarmEventArgument(EntityEventArgument):
    @property
    def alarm(self) -> vim.alarm.Alarm: ...


class AlarmReconfiguredEvent(AlarmEvent):
    @property
    def entity(self) -> ManagedEntityEventArgument: ...
    @property
    def configChanges(self) -> ChangesInfoEventArgument: ...


class AlarmRemovedEvent(AlarmEvent):
    @property
    def entity(self) -> ManagedEntityEventArgument: ...


class AlarmScriptCompleteEvent(AlarmEvent):
    @property
    def entity(self) -> ManagedEntityEventArgument: ...
    @property
    def script(self) -> str: ...


class AlarmScriptFailedEvent(AlarmEvent):
    @property
    def entity(self) -> ManagedEntityEventArgument: ...
    @property
    def script(self) -> str: ...
    @property
    def reason(self) -> vmodl.MethodFault: ...


class AlarmSnmpCompletedEvent(AlarmEvent):
    @property
    def entity(self) -> ManagedEntityEventArgument: ...


class AlarmSnmpFailedEvent(AlarmEvent):
    @property
    def entity(self) -> ManagedEntityEventArgument: ...
    @property
    def reason(self) -> vmodl.MethodFault: ...


class AlarmStatusChangedEvent(AlarmEvent):
    @property
    def source(self) -> ManagedEntityEventArgument: ...
    @property
    def entity(self) -> ManagedEntityEventArgument: ...
    @property
    def from(self) -> str: ...
    @property
    def to(self) -> str: ...


class AllVirtualMachinesLicensedEvent(LicenseEvent): ...


class AlreadyAuthenticatedSessionEvent(SessionEvent): ...


class AuthorizationEvent(Event): ...


class BadUsernameSessionEvent(SessionEvent):
    @property
    def ipAddress(self) -> str: ...


class CanceledHostOperationEvent(HostEvent): ...


class ChangesInfoEventArgument(vmodl.DynamicData):
    @property
    def modified(self) -> str: ...
    @property
    def added(self) -> str: ...
    @property
    def deleted(self) -> str: ...


class ClusterComplianceCheckedEvent(ClusterEvent):
    @property
    def profile(self) -> ProfileEventArgument: ...


class ClusterCreatedEvent(ClusterEvent):
    @property
    def parent(self) -> FolderEventArgument: ...


class ClusterDestroyedEvent(ClusterEvent): ...


class ClusterEvent(Event): ...


class ClusterOvercommittedEvent(ClusterEvent): ...


class ClusterReconfiguredEvent(ClusterEvent):
    @property
    def configChanges(self) -> ChangesInfoEventArgument: ...


class ClusterStatusChangedEvent(ClusterEvent):
    @property
    def oldStatus(self) -> str: ...
    @property
    def newStatus(self) -> str: ...


class ComputeResourceEventArgument(EntityEventArgument):
    @property
    def computeResource(self) -> vim.ComputeResource: ...


class CustomFieldDefAddedEvent(CustomFieldDefEvent): ...


class CustomFieldDefEvent(CustomFieldEvent):
    @property
    def fieldKey(self) -> int: ...
    @property
    def name(self) -> str: ...


class CustomFieldDefRemovedEvent(CustomFieldDefEvent): ...


class CustomFieldDefRenamedEvent(CustomFieldDefEvent):
    @property
    def newName(self) -> str: ...


class CustomFieldEvent(Event): ...


class CustomFieldValueChangedEvent(CustomFieldEvent):
    @property
    def entity(self) -> ManagedEntityEventArgument: ...
    @property
    def fieldKey(self) -> int: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> str: ...
    @property
    def prevState(self) -> str: ...


class CustomizationEvent(VmEvent):
    @property
    def logLocation(self) -> str: ...


class CustomizationFailed(CustomizationEvent):
    @property
    def reason(self) -> str: ...


    class ReasonCode(Enum):
        userDefinedScriptDisabled = "userdefinedscriptdisabled"
        customizationDisabled = "customizationdisabled"
        rawDataIsNotSupported = "rawdataisnotsupported"
        wrongMetadataFormat = "wrongmetadataformat"


class CustomizationLinuxIdentityFailed(CustomizationFailed): ...


class CustomizationNetworkSetupFailed(CustomizationFailed): ...


class CustomizationStartedEvent(CustomizationEvent): ...


class CustomizationSucceeded(CustomizationEvent): ...


class CustomizationSysprepFailed(CustomizationFailed):
    @property
    def sysprepVersion(self) -> str: ...
    @property
    def systemVersion(self) -> str: ...


class CustomizationUnknownFailure(CustomizationFailed): ...


class DVPortgroupCreatedEvent(DVPortgroupEvent): ...


class DVPortgroupDestroyedEvent(DVPortgroupEvent): ...


class DVPortgroupEvent(Event): ...


class DVPortgroupReconfiguredEvent(DVPortgroupEvent):
    @property
    def configSpec(self) -> vim.dvs.DistributedVirtualPortgroup.ConfigSpec: ...
    @property
    def configChanges(self) -> ChangesInfoEventArgument: ...


class DVPortgroupRenamedEvent(DVPortgroupEvent):
    @property
    def oldName(self) -> str: ...
    @property
    def newName(self) -> str: ...


class DasAdmissionControlDisabledEvent(ClusterEvent): ...


class DasAdmissionControlEnabledEvent(ClusterEvent): ...


class DasAgentFoundEvent(ClusterEvent): ...


class DasAgentUnavailableEvent(ClusterEvent): ...


class DasClusterIsolatedEvent(ClusterEvent): ...


class DasDisabledEvent(ClusterEvent): ...


class DasEnabledEvent(ClusterEvent): ...


class DasHostFailedEvent(ClusterEvent):
    @property
    def failedHost(self) -> HostEventArgument: ...


class DasHostIsolatedEvent(ClusterEvent):
    @property
    def isolatedHost(self) -> HostEventArgument: ...


class DatacenterCreatedEvent(DatacenterEvent):
    @property
    def parent(self) -> FolderEventArgument: ...


class DatacenterEvent(Event): ...


class DatacenterEventArgument(EntityEventArgument):
    @property
    def datacenter(self) -> vim.Datacenter: ...


class DatacenterRenamedEvent(DatacenterEvent):
    @property
    def oldName(self) -> str: ...
    @property
    def newName(self) -> str: ...


class DatastoreCapacityIncreasedEvent(DatastoreEvent):
    @property
    def oldCapacity(self) -> long: ...
    @property
    def newCapacity(self) -> long: ...


class DatastoreDestroyedEvent(DatastoreEvent): ...


class DatastoreDiscoveredEvent(HostEvent):
    @property
    def datastore(self) -> DatastoreEventArgument: ...


class DatastoreDuplicatedEvent(DatastoreEvent): ...


class DatastoreEvent(Event):
    @property
    def datastore(self) -> DatastoreEventArgument: ...


class DatastoreEventArgument(EntityEventArgument):
    @property
    def datastore(self) -> vim.Datastore: ...


class DatastoreFileCopiedEvent(DatastoreFileEvent):
    @property
    def sourceDatastore(self) -> DatastoreEventArgument: ...
    @property
    def sourceFile(self) -> str: ...


class DatastoreFileDeletedEvent(DatastoreFileEvent): ...


class DatastoreFileEvent(DatastoreEvent):
    @property
    def targetFile(self) -> str: ...
    @property
    def sourceOfOperation(self) -> str: ...
    @property
    def succeeded(self) -> bool: ...


class DatastoreFileMovedEvent(DatastoreFileEvent):
    @property
    def sourceDatastore(self) -> DatastoreEventArgument: ...
    @property
    def sourceFile(self) -> str: ...


class DatastoreIORMReconfiguredEvent(DatastoreEvent): ...


class DatastorePrincipalConfigured(HostEvent):
    @property
    def datastorePrincipal(self) -> str: ...


class DatastoreRemovedOnHostEvent(HostEvent):
    @property
    def datastore(self) -> DatastoreEventArgument: ...


class DatastoreRenamedEvent(DatastoreEvent):
    @property
    def oldName(self) -> str: ...
    @property
    def newName(self) -> str: ...


class DatastoreRenamedOnHostEvent(HostEvent):
    @property
    def oldName(self) -> str: ...
    @property
    def newName(self) -> str: ...


class DrsDisabledEvent(ClusterEvent): ...


class DrsEnabledEvent(ClusterEvent):
    @property
    def behavior(self) -> str: ...


class DrsEnteredStandbyModeEvent(EnteredStandbyModeEvent): ...


class DrsEnteringStandbyModeEvent(EnteringStandbyModeEvent): ...


class DrsExitStandbyModeFailedEvent(ExitStandbyModeFailedEvent): ...


class DrsExitedStandbyModeEvent(ExitedStandbyModeEvent): ...


class DrsExitingStandbyModeEvent(ExitingStandbyModeEvent): ...


class DrsInvocationFailedEvent(ClusterEvent): ...


class DrsRecoveredFromFailureEvent(ClusterEvent): ...


class DrsResourceConfigureFailedEvent(HostEvent):
    @property
    def reason(self) -> vmodl.MethodFault: ...


class DrsResourceConfigureSyncedEvent(HostEvent): ...


class DrsRuleComplianceEvent(VmEvent): ...


class DrsRuleViolationEvent(VmEvent): ...


class DrsSoftRuleViolationEvent(VmEvent): ...


class DrsVmMigratedEvent(VmMigratedEvent): ...


class DrsVmPoweredOnEvent(VmPoweredOnEvent): ...


class DuplicateIpDetectedEvent(HostEvent):
    @property
    def duplicateIP(self) -> str: ...
    @property
    def macAddress(self) -> str: ...


class DvpgImportEvent(DVPortgroupEvent):
    @property
    def importType(self) -> str: ...


class DvpgRestoreEvent(DVPortgroupEvent): ...


class DvsCreatedEvent(DvsEvent):
    @property
    def parent(self) -> FolderEventArgument: ...


class DvsDestroyedEvent(DvsEvent): ...


class DvsEvent(Event):


    class PortBlockState(Enum):
        unset = "unset"
        blocked = "blocked"
        unblocked = "unblocked"
        unknown = "unknown"


class DvsEventArgument(EntityEventArgument):
    @property
    def dvs(self) -> vim.DistributedVirtualSwitch: ...


class DvsHealthStatusChangeEvent(HostEvent):
    @property
    def switchUuid(self) -> str: ...
    @property
    def healthResult(self) -> vim.dvs.HostMember.HealthCheckResult: ...


class DvsHostBackInSyncEvent(DvsEvent):
    @property
    def hostBackInSync(self) -> HostEventArgument: ...


class DvsHostJoinedEvent(DvsEvent):
    @property
    def hostJoined(self) -> HostEventArgument: ...


class DvsHostLeftEvent(DvsEvent):
    @property
    def hostLeft(self) -> HostEventArgument: ...


class DvsHostStatusUpdated(DvsEvent):
    @property
    def hostMember(self) -> HostEventArgument: ...
    @property
    def oldStatus(self) -> str: ...
    @property
    def newStatus(self) -> str: ...
    @property
    def oldStatusDetail(self) -> str: ...
    @property
    def newStatusDetail(self) -> str: ...


class DvsHostWentOutOfSyncEvent(DvsEvent):
    @property
    def hostOutOfSync(self) -> DvsOutOfSyncHostArgument: ...


class DvsImportEvent(DvsEvent):
    @property
    def importType(self) -> str: ...


class DvsMergedEvent(DvsEvent):
    @property
    def sourceDvs(self) -> DvsEventArgument: ...
    @property
    def destinationDvs(self) -> DvsEventArgument: ...


class DvsOutOfSyncHostArgument(vmodl.DynamicData):
    @property
    def outOfSyncHost(self) -> HostEventArgument: ...
    @property
    def configParamters(self) -> List[str]: ...


class DvsPortBlockedEvent(DvsEvent):
    @property
    def portKey(self) -> str: ...
    @property
    def statusDetail(self) -> str: ...
    @property
    def runtimeInfo(self) -> vim.dvs.DistributedVirtualPort.RuntimeInfo: ...
    @property
    def prevBlockState(self) -> str: ...


class DvsPortConnectedEvent(DvsEvent):
    @property
    def portKey(self) -> str: ...
    @property
    def connectee(self) -> vim.dvs.PortConnectee: ...


class DvsPortCreatedEvent(DvsEvent):
    @property
    def portKey(self) -> List[str]: ...


class DvsPortDeletedEvent(DvsEvent):
    @property
    def portKey(self) -> List[str]: ...


class DvsPortDisconnectedEvent(DvsEvent):
    @property
    def portKey(self) -> str: ...
    @property
    def connectee(self) -> vim.dvs.PortConnectee: ...


class DvsPortEnteredPassthruEvent(DvsEvent):
    @property
    def portKey(self) -> str: ...
    @property
    def runtimeInfo(self) -> vim.dvs.DistributedVirtualPort.RuntimeInfo: ...


class DvsPortExitedPassthruEvent(DvsEvent):
    @property
    def portKey(self) -> str: ...
    @property
    def runtimeInfo(self) -> vim.dvs.DistributedVirtualPort.RuntimeInfo: ...


class DvsPortJoinPortgroupEvent(DvsEvent):
    @property
    def portKey(self) -> str: ...
    @property
    def portgroupKey(self) -> str: ...
    @property
    def portgroupName(self) -> str: ...


class DvsPortLeavePortgroupEvent(DvsEvent):
    @property
    def portKey(self) -> str: ...
    @property
    def portgroupKey(self) -> str: ...
    @property
    def portgroupName(self) -> str: ...


class DvsPortLinkDownEvent(DvsEvent):
    @property
    def portKey(self) -> str: ...
    @property
    def runtimeInfo(self) -> vim.dvs.DistributedVirtualPort.RuntimeInfo: ...


class DvsPortLinkUpEvent(DvsEvent):
    @property
    def portKey(self) -> str: ...
    @property
    def runtimeInfo(self) -> vim.dvs.DistributedVirtualPort.RuntimeInfo: ...


class DvsPortReconfiguredEvent(DvsEvent):
    @property
    def portKey(self) -> List[str]: ...
    @property
    def configChanges(self) -> List[ChangesInfoEventArgument]: ...


class DvsPortRuntimeChangeEvent(DvsEvent):
    @property
    def portKey(self) -> str: ...
    @property
    def runtimeInfo(self) -> vim.dvs.DistributedVirtualPort.RuntimeInfo: ...


class DvsPortUnblockedEvent(DvsEvent):
    @property
    def portKey(self) -> str: ...
    @property
    def runtimeInfo(self) -> vim.dvs.DistributedVirtualPort.RuntimeInfo: ...
    @property
    def prevBlockState(self) -> str: ...


class DvsPortVendorSpecificStateChangeEvent(DvsEvent):
    @property
    def portKey(self) -> str: ...


class DvsReconfiguredEvent(DvsEvent):
    @property
    def configSpec(self) -> vim.DistributedVirtualSwitch.ConfigSpec: ...
    @property
    def configChanges(self) -> ChangesInfoEventArgument: ...


class DvsRenamedEvent(DvsEvent):
    @property
    def oldName(self) -> str: ...
    @property
    def newName(self) -> str: ...


class DvsRestoreEvent(DvsEvent): ...


class DvsUpgradeAvailableEvent(DvsEvent):
    @property
    def productInfo(self) -> vim.dvs.ProductSpec: ...


class DvsUpgradeInProgressEvent(DvsEvent):
    @property
    def productInfo(self) -> vim.dvs.ProductSpec: ...


class DvsUpgradeRejectedEvent(DvsEvent):
    @property
    def productInfo(self) -> vim.dvs.ProductSpec: ...


class DvsUpgradedEvent(DvsEvent):
    @property
    def productInfo(self) -> vim.dvs.ProductSpec: ...


class EnteredMaintenanceModeEvent(HostEvent): ...


class EnteredStandbyModeEvent(HostEvent): ...


class EnteringMaintenanceModeEvent(HostEvent): ...


class EnteringStandbyModeEvent(HostEvent): ...


class EntityEventArgument(EventArgument):
    @property
    def name(self) -> str: ...


class ErrorUpgradeEvent(UpgradeEvent): ...


class Event(vmodl.DynamicData):
    @property
    def key(self) -> int: ...
    @property
    def chainId(self) -> int: ...
    @property
    def createdTime(self) -> datetime: ...
    @property
    def userName(self) -> str: ...
    @property
    def datacenter(self) -> DatacenterEventArgument: ...
    @property
    def computeResource(self) -> ComputeResourceEventArgument: ...
    @property
    def host(self) -> HostEventArgument: ...
    @property
    def vm(self) -> VmEventArgument: ...
    @property
    def ds(self) -> DatastoreEventArgument: ...
    @property
    def net(self) -> NetworkEventArgument: ...
    @property
    def dvs(self) -> DvsEventArgument: ...
    @property
    def fullFormattedMessage(self) -> str: ...
    @property
    def changeTag(self) -> str: ...


    class EventSeverity(Enum):
        error = "error"
        warning = "warning"
        info = "info"
        user = "user"


class EventArgument(vmodl.DynamicData): ...


class EventDescription(vmodl.DynamicData):
    @property
    def category(self) -> List[vim.ElementDescription]: ...
    @property
    def eventInfo(self) -> List[EventDescription.EventDetail]: ...
    @property
    def enumeratedTypes(self) -> List[vim.EnumDescription]: ...


    class EventArgDesc(vmodl.DynamicData):
        @property
        def name(self) -> str: ...
        @property
        def type(self) -> str: ...
        @property
        def description(self) -> vim.ElementDescription: ...


    class EventDetail(vmodl.DynamicData):
        @property
        def key(self) -> type: ...
        @property
        def description(self) -> str: ...
        @property
        def category(self) -> str: ...
        @property
        def formatOnDatacenter(self) -> str: ...
        @property
        def formatOnComputeResource(self) -> str: ...
        @property
        def formatOnHost(self) -> str: ...
        @property
        def formatOnVm(self) -> str: ...
        @property
        def fullFormat(self) -> str: ...
        @property
        def longDescription(self) -> str: ...


    class EventCategory(Enum):
        info = "info"
        warning = "warning"
        error = "error"
        user = "user"


class EventEx(Event):
    @property
    def eventTypeId(self) -> str: ...
    @property
    def severity(self) -> str: ...
    @property
    def message(self) -> str: ...
    @property
    def arguments(self) -> List[vmodl.KeyAnyValue]: ...
    @property
    def objectId(self) -> str: ...
    @property
    def objectType(self) -> type: ...
    @property
    def objectName(self) -> str: ...
    @property
    def fault(self) -> vmodl.MethodFault: ...


class EventFilterSpec(vmodl.DynamicData):
    @property
    def entity(self) -> EventFilterSpec.ByEntity: ...
    @property
    def time(self) -> EventFilterSpec.ByTime: ...
    @property
    def userName(self) -> EventFilterSpec.ByUsername: ...
    @property
    def eventChainId(self) -> int: ...
    @property
    def alarm(self) -> vim.alarm.Alarm: ...
    @property
    def scheduledTask(self) -> vim.scheduler.ScheduledTask: ...
    @property
    def disableFullMessage(self) -> bool: ...
    @property
    def category(self) -> List[str]: ...
    @property
    def type(self) -> List[type]: ...
    @property
    def tag(self) -> List[str]: ...
    @property
    def eventTypeId(self) -> List[str]: ...
    @property
    def maxCount(self) -> int: ...


    class ByEntity(vmodl.DynamicData):
        @property
        def entity(self) -> vim.ManagedEntity: ...
        @property
        def recursion(self) -> EventFilterSpec.RecursionOption: ...


    class ByTime(vmodl.DynamicData):
        @property
        def beginTime(self) -> datetime: ...
        @property
        def endTime(self) -> datetime: ...


    class ByUsername(vmodl.DynamicData):
        @property
        def systemUser(self) -> bool: ...
        @property
        def userList(self) -> List[str]: ...


    class RecursionOption(Enum):
        self = "self"
        children = "children"
        all = "all"


class ExitMaintenanceModeEvent(HostEvent): ...


class ExitStandbyModeFailedEvent(HostEvent): ...


class ExitedStandbyModeEvent(HostEvent): ...


class ExitingStandbyModeEvent(HostEvent): ...


class ExtendedEvent(GeneralEvent):
    @property
    def eventTypeId(self) -> str: ...
    @property
    def managedObject(self) -> ManagedObject: ...
    @property
    def data(self) -> List[ExtendedEvent.Pair]: ...


    class Pair(vmodl.DynamicData):
        @property
        def key(self) -> str: ...
        @property
        def value(self) -> str: ...


class FailoverLevelRestored(ClusterEvent): ...


class FolderEventArgument(EntityEventArgument):
    @property
    def folder(self) -> vim.Folder: ...


class GeneralEvent(Event):
    @property
    def message(self) -> str: ...


class GeneralHostErrorEvent(GeneralEvent): ...


class GeneralHostInfoEvent(GeneralEvent): ...


class GeneralHostWarningEvent(GeneralEvent): ...


class GeneralUserEvent(GeneralEvent):
    @property
    def entity(self) -> ManagedEntityEventArgument: ...


class GeneralVmErrorEvent(GeneralEvent): ...


class GeneralVmInfoEvent(GeneralEvent): ...


class GeneralVmWarningEvent(GeneralEvent): ...


class GhostDvsProxySwitchDetectedEvent(HostEvent):
    @property
    def switchUuid(self) -> List[str]: ...


class GhostDvsProxySwitchRemovedEvent(HostEvent):
    @property
    def switchUuid(self) -> List[str]: ...


class GlobalMessageChangedEvent(SessionEvent):
    @property
    def message(self) -> str: ...
    @property
    def prevMessage(self) -> str: ...


class HealthStatusChangedEvent(Event):
    @property
    def componentId(self) -> str: ...
    @property
    def oldStatus(self) -> str: ...
    @property
    def newStatus(self) -> str: ...
    @property
    def componentName(self) -> str: ...
    @property
    def serviceId(self) -> str: ...


class HostAddFailedEvent(HostEvent):
    @property
    def hostname(self) -> str: ...


class HostAddedEvent(HostEvent): ...


class HostAdminDisableEvent(HostEvent): ...


class HostAdminEnableEvent(HostEvent): ...


class HostCnxFailedAccountFailedEvent(HostEvent): ...


class HostCnxFailedAlreadyManagedEvent(HostEvent):
    @property
    def serverName(self) -> str: ...


class HostCnxFailedBadCcagentEvent(HostEvent): ...


class HostCnxFailedBadUsernameEvent(HostEvent): ...


class HostCnxFailedBadVersionEvent(HostEvent): ...


class HostCnxFailedCcagentUpgradeEvent(HostEvent): ...


class HostCnxFailedEvent(HostEvent): ...


class HostCnxFailedNetworkErrorEvent(HostEvent): ...


class HostCnxFailedNoAccessEvent(HostEvent): ...


class HostCnxFailedNoConnectionEvent(HostEvent): ...


class HostCnxFailedNoLicenseEvent(HostEvent): ...


class HostCnxFailedNotFoundEvent(HostEvent): ...


class HostCnxFailedTimeoutEvent(HostEvent): ...


class HostComplianceCheckedEvent(HostEvent):
    @property
    def profile(self) -> ProfileEventArgument: ...


class HostCompliantEvent(HostEvent): ...


class HostConfigAppliedEvent(HostEvent): ...


class HostConnectedEvent(HostEvent): ...


class HostConnectionLostEvent(HostEvent): ...


class HostDasDisabledEvent(HostEvent): ...


class HostDasDisablingEvent(HostEvent): ...


class HostDasEnabledEvent(HostEvent): ...


class HostDasEnablingEvent(HostEvent): ...


class HostDasErrorEvent(HostEvent):
    @property
    def message(self) -> str: ...
    @property
    def reason(self) -> str: ...


    class HostDasErrorReason(Enum):
        configFailed = "configfailed"
        timeout = "timeout"
        communicationInitFailed = "communicationinitfailed"
        healthCheckScriptFailed = "healthcheckscriptfailed"
        agentFailed = "agentfailed"
        agentShutdown = "agentshutdown"
        isolationAddressUnpingable = "isolationaddressunpingable"
        other = "other"


class HostDasEvent(HostEvent): ...


class HostDasOkEvent(HostEvent): ...


class HostDisconnectedEvent(HostEvent):
    @property
    def reason(self) -> str: ...


class HostEnableAdminFailedEvent(HostEvent):
    @property
    def permissions(self) -> List[vim.AuthorizationManager.Permission]: ...


class HostEvent(Event): ...


class HostEventArgument(EntityEventArgument):
    @property
    def host(self) -> vim.HostSystem: ...


class HostExtraNetworksEvent(HostDasEvent):
    @property
    def ips(self) -> str: ...


class HostGetShortNameFailedEvent(HostEvent): ...


class HostInAuditModeEvent(HostEvent): ...


class HostInventoryFullEvent(LicenseEvent):
    @property
    def capacity(self) -> int: ...


class HostInventoryUnreadableEvent(Event): ...


class HostIpChangedEvent(HostEvent):
    @property
    def oldIP(self) -> str: ...
    @property
    def newIP(self) -> str: ...


class HostIpInconsistentEvent(HostEvent):
    @property
    def ipAddress(self) -> str: ...
    @property
    def ipAddress2(self) -> str: ...


class HostIpToShortNameFailedEvent(HostEvent): ...


class HostIsolationIpPingFailedEvent(HostDasEvent):
    @property
    def isolationIp(self) -> str: ...


class HostLicenseExpiredEvent(LicenseEvent): ...


class HostLocalPortCreatedEvent(DvsEvent):
    @property
    def hostLocalPort(self) -> vim.dvs.DistributedVirtualPort.HostLocalPortInfo: ...


class HostMissingNetworksEvent(HostDasEvent):
    @property
    def ips(self) -> str: ...


class HostMonitoringStateChangedEvent(ClusterEvent):
    @property
    def state(self) -> str: ...
    @property
    def prevState(self) -> str: ...


class HostNoAvailableNetworksEvent(HostDasEvent):
    @property
    def ips(self) -> str: ...


class HostNoHAEnabledPortGroupsEvent(HostDasEvent): ...


class HostNoRedundantManagementNetworkEvent(HostDasEvent): ...


class HostNonCompliantEvent(HostEvent): ...


class HostNotInClusterEvent(HostDasEvent): ...


class HostOvercommittedEvent(ClusterOvercommittedEvent): ...


class HostPrimaryAgentNotShortNameEvent(HostDasEvent):
    @property
    def primaryAgent(self) -> str: ...


class HostProfileAppliedEvent(HostEvent):
    @property
    def profile(self) -> ProfileEventArgument: ...


class HostReconnectionFailedEvent(HostEvent): ...


class HostRemovedEvent(HostEvent): ...


class HostShortNameInconsistentEvent(HostDasEvent):
    @property
    def shortName(self) -> str: ...
    @property
    def shortName2(self) -> str: ...


class HostShortNameToIpFailedEvent(HostEvent):
    @property
    def shortName(self) -> str: ...


class HostShutdownEvent(HostEvent):
    @property
    def reason(self) -> str: ...


class HostSpecificationChangedEvent(HostEvent): ...


class HostSpecificationRequireEvent(HostEvent): ...


class HostSpecificationUpdateEvent(HostEvent):
    @property
    def hostSpec(self) -> vim.profile.host.HostSpecification: ...


class HostStatusChangedEvent(ClusterStatusChangedEvent): ...


class HostSubSpecificationDeleteEvent(HostEvent):
    @property
    def subSpecName(self) -> str: ...


class HostSubSpecificationUpdateEvent(HostEvent):
    @property
    def hostSubSpec(self) -> vim.profile.host.HostSubSpecification: ...


class HostSyncFailedEvent(HostEvent):
    @property
    def reason(self) -> vmodl.MethodFault: ...


class HostUpgradeFailedEvent(HostEvent): ...


class HostUserWorldSwapNotEnabledEvent(HostEvent): ...


class HostVnicConnectedToCustomizedDVPortEvent(HostEvent):
    @property
    def vnic(self) -> VnicPortArgument: ...
    @property
    def prevPortKey(self) -> str: ...


class HostWwnChangedEvent(HostEvent):
    @property
    def oldNodeWwns(self) -> List[long]: ...
    @property
    def oldPortWwns(self) -> List[long]: ...
    @property
    def newNodeWwns(self) -> List[long]: ...
    @property
    def newPortWwns(self) -> List[long]: ...


class HostWwnConflictEvent(HostEvent):
    @property
    def conflictedVms(self) -> List[VmEventArgument]: ...
    @property
    def conflictedHosts(self) -> List[HostEventArgument]: ...
    @property
    def wwn(self) -> long: ...


class IncorrectHostInformationEvent(LicenseEvent): ...


class InfoUpgradeEvent(UpgradeEvent): ...


class InsufficientFailoverResourcesEvent(ClusterEvent): ...


class InvalidEditionEvent(LicenseEvent):
    @property
    def feature(self) -> str: ...


class LicenseEvent(Event): ...


class LicenseExpiredEvent(Event):
    @property
    def feature(self) -> vim.LicenseManager.FeatureInfo: ...


class LicenseNonComplianceEvent(LicenseEvent):
    @property
    def url(self) -> str: ...


class LicenseRestrictedEvent(LicenseEvent): ...


class LicenseServerAvailableEvent(LicenseEvent):
    @property
    def licenseServer(self) -> str: ...


class LicenseServerUnavailableEvent(LicenseEvent):
    @property
    def licenseServer(self) -> str: ...


class LocalDatastoreCreatedEvent(HostEvent):
    @property
    def datastore(self) -> DatastoreEventArgument: ...
    @property
    def datastoreUrl(self) -> str: ...


class LocalTSMEnabledEvent(HostEvent): ...


class LockerMisconfiguredEvent(Event):
    @property
    def datastore(self) -> DatastoreEventArgument: ...


class LockerReconfiguredEvent(Event):
    @property
    def oldDatastore(self) -> DatastoreEventArgument: ...
    @property
    def newDatastore(self) -> DatastoreEventArgument: ...


class ManagedEntityEventArgument(EntityEventArgument):
    @property
    def entity(self) -> vim.ManagedEntity: ...


class MigrationErrorEvent(MigrationEvent): ...


class MigrationEvent(VmEvent):
    @property
    def fault(self) -> vmodl.MethodFault: ...


class MigrationHostErrorEvent(MigrationEvent):
    @property
    def dstHost(self) -> HostEventArgument: ...


class MigrationHostWarningEvent(MigrationEvent):
    @property
    def dstHost(self) -> HostEventArgument: ...


class MigrationResourceErrorEvent(MigrationEvent):
    @property
    def dstPool(self) -> ResourcePoolEventArgument: ...
    @property
    def dstHost(self) -> HostEventArgument: ...


class MigrationResourceWarningEvent(MigrationEvent):
    @property
    def dstPool(self) -> ResourcePoolEventArgument: ...
    @property
    def dstHost(self) -> HostEventArgument: ...


class MigrationWarningEvent(MigrationEvent): ...


class MtuMatchEvent(DvsHealthStatusChangeEvent): ...


class MtuMismatchEvent(DvsHealthStatusChangeEvent): ...


class NASDatastoreCreatedEvent(HostEvent):
    @property
    def datastore(self) -> DatastoreEventArgument: ...
    @property
    def datastoreUrl(self) -> str: ...


class NetworkEventArgument(EntityEventArgument):
    @property
    def network(self) -> vim.Network: ...


class NetworkRollbackEvent(Event):
    @property
    def methodName(self) -> str: ...
    @property
    def transactionId(self) -> str: ...


class NoAccessUserEvent(SessionEvent):
    @property
    def ipAddress(self) -> str: ...


class NoDatastoresConfiguredEvent(HostEvent): ...


class NoLicenseEvent(LicenseEvent):
    @property
    def feature(self) -> vim.LicenseManager.FeatureInfo: ...


class NoMaintenanceModeDrsRecommendationForVM(VmEvent): ...


class NonVIWorkloadDetectedOnDatastoreEvent(DatastoreEvent): ...


class NotEnoughResourcesToStartVmEvent(VmEvent):
    @property
    def reason(self) -> str: ...


class OutOfSyncDvsHost(DvsEvent):
    @property
    def hostOutOfSync(self) -> List[DvsOutOfSyncHostArgument]: ...


class PermissionAddedEvent(PermissionEvent):
    @property
    def role(self) -> RoleEventArgument: ...
    @property
    def propagate(self) -> bool: ...


class PermissionEvent(AuthorizationEvent):
    @property
    def entity(self) -> ManagedEntityEventArgument: ...
    @property
    def principal(self) -> str: ...
    @property
    def group(self) -> bool: ...


class PermissionRemovedEvent(PermissionEvent): ...


class PermissionUpdatedEvent(PermissionEvent):
    @property
    def role(self) -> RoleEventArgument: ...
    @property
    def propagate(self) -> bool: ...
    @property
    def prevRole(self) -> RoleEventArgument: ...
    @property
    def prevPropagate(self) -> bool: ...


class ProfileAssociatedEvent(ProfileEvent): ...


class ProfileChangedEvent(ProfileEvent): ...


class ProfileCreatedEvent(ProfileEvent): ...


class ProfileDissociatedEvent(ProfileEvent): ...


class ProfileEvent(Event):
    @property
    def profile(self) -> ProfileEventArgument: ...


class ProfileEventArgument(EventArgument):
    @property
    def profile(self) -> vim.profile.Profile: ...
    @property
    def name(self) -> str: ...


class ProfileReferenceHostChangedEvent(ProfileEvent):
    @property
    def referenceHost(self) -> vim.HostSystem: ...
    @property
    def referenceHostName(self) -> str: ...
    @property
    def prevReferenceHostName(self) -> str: ...


class ProfileRemovedEvent(ProfileEvent): ...


class RecoveryEvent(DvsEvent):
    @property
    def hostName(self) -> str: ...
    @property
    def portKey(self) -> str: ...
    @property
    def dvsUuid(self) -> str: ...
    @property
    def vnic(self) -> str: ...


class RemoteTSMEnabledEvent(HostEvent): ...


class ResourcePoolCreatedEvent(ResourcePoolEvent):
    @property
    def parent(self) -> ResourcePoolEventArgument: ...


class ResourcePoolDestroyedEvent(ResourcePoolEvent): ...


class ResourcePoolEvent(Event):
    @property
    def resourcePool(self) -> ResourcePoolEventArgument: ...


class ResourcePoolEventArgument(EntityEventArgument):
    @property
    def resourcePool(self) -> vim.ResourcePool: ...


class ResourcePoolMovedEvent(ResourcePoolEvent):
    @property
    def oldParent(self) -> ResourcePoolEventArgument: ...
    @property
    def newParent(self) -> ResourcePoolEventArgument: ...


class ResourcePoolReconfiguredEvent(ResourcePoolEvent):
    @property
    def configChanges(self) -> ChangesInfoEventArgument: ...


class ResourceViolatedEvent(ResourcePoolEvent): ...


class RoleAddedEvent(RoleEvent):
    @property
    def privilegeList(self) -> List[str]: ...


class RoleEvent(AuthorizationEvent):
    @property
    def role(self) -> RoleEventArgument: ...


class RoleEventArgument(EventArgument):
    @property
    def roleId(self) -> int: ...
    @property
    def name(self) -> str: ...


class RoleRemovedEvent(RoleEvent): ...


class RoleUpdatedEvent(RoleEvent):
    @property
    def privilegeList(self) -> List[str]: ...
    @property
    def prevRoleName(self) -> str: ...
    @property
    def privilegesAdded(self) -> List[str]: ...
    @property
    def privilegesRemoved(self) -> List[str]: ...


class RollbackEvent(DvsEvent):
    @property
    def hostName(self) -> str: ...
    @property
    def methodName(self) -> str: ...


class ScheduledTaskCompletedEvent(ScheduledTaskEvent): ...


class ScheduledTaskCreatedEvent(ScheduledTaskEvent): ...


class ScheduledTaskEmailCompletedEvent(ScheduledTaskEvent):
    @property
    def to(self) -> str: ...


class ScheduledTaskEmailFailedEvent(ScheduledTaskEvent):
    @property
    def to(self) -> str: ...
    @property
    def reason(self) -> vmodl.MethodFault: ...


class ScheduledTaskEvent(Event):
    @property
    def scheduledTask(self) -> ScheduledTaskEventArgument: ...
    @property
    def entity(self) -> ManagedEntityEventArgument: ...


class ScheduledTaskEventArgument(EntityEventArgument):
    @property
    def scheduledTask(self) -> vim.scheduler.ScheduledTask: ...


class ScheduledTaskFailedEvent(ScheduledTaskEvent):
    @property
    def reason(self) -> vmodl.MethodFault: ...


class ScheduledTaskReconfiguredEvent(ScheduledTaskEvent):
    @property
    def configChanges(self) -> ChangesInfoEventArgument: ...


class ScheduledTaskRemovedEvent(ScheduledTaskEvent): ...


class ScheduledTaskStartedEvent(ScheduledTaskEvent): ...


class ServerLicenseExpiredEvent(LicenseEvent):
    @property
    def product(self) -> str: ...


class ServerStartedSessionEvent(SessionEvent): ...


class SessionEvent(Event): ...


class SessionTerminatedEvent(SessionEvent):
    @property
    def sessionId(self) -> str: ...
    @property
    def terminatedUsername(self) -> str: ...


class TaskEvent(Event):
    @property
    def info(self) -> vim.TaskInfo: ...


class TaskTimeoutEvent(TaskEvent): ...


class TeamingMatchEvent(DvsHealthStatusChangeEvent): ...


class TeamingMisMatchEvent(DvsHealthStatusChangeEvent): ...


class TemplateBeingUpgradedEvent(TemplateUpgradeEvent): ...


class TemplateUpgradeEvent(Event):
    @property
    def legacyTemplate(self) -> str: ...


class TemplateUpgradeFailedEvent(TemplateUpgradeEvent):
    @property
    def reason(self) -> vmodl.MethodFault: ...


class TemplateUpgradedEvent(TemplateUpgradeEvent): ...


class TimedOutHostOperationEvent(HostEvent): ...


class UnlicensedVirtualMachinesEvent(LicenseEvent):
    @property
    def unlicensed(self) -> int: ...
    @property
    def available(self) -> int: ...


class UnlicensedVirtualMachinesFoundEvent(LicenseEvent):
    @property
    def available(self) -> int: ...


class UpdatedAgentBeingRestartedEvent(HostEvent): ...


class UpgradeEvent(Event):
    @property
    def message(self) -> str: ...


class UplinkPortMtuNotSupportEvent(DvsHealthStatusChangeEvent): ...


class UplinkPortMtuSupportEvent(DvsHealthStatusChangeEvent): ...


class UplinkPortVlanTrunkedEvent(DvsHealthStatusChangeEvent): ...


class UplinkPortVlanUntrunkedEvent(DvsHealthStatusChangeEvent): ...


class UserAssignedToGroup(HostEvent):
    @property
    def userLogin(self) -> str: ...
    @property
    def group(self) -> str: ...


class UserLoginSessionEvent(SessionEvent):
    @property
    def ipAddress(self) -> str: ...
    @property
    def userAgent(self) -> str: ...
    @property
    def locale(self) -> str: ...
    @property
    def sessionId(self) -> str: ...


class UserLogoutSessionEvent(SessionEvent):
    @property
    def ipAddress(self) -> str: ...
    @property
    def userAgent(self) -> str: ...
    @property
    def callCount(self) -> long: ...
    @property
    def sessionId(self) -> str: ...
    @property
    def loginTime(self) -> datetime: ...


class UserPasswordChanged(HostEvent):
    @property
    def userLogin(self) -> str: ...


class UserUnassignedFromGroup(HostEvent):
    @property
    def userLogin(self) -> str: ...
    @property
    def group(self) -> str: ...


class UserUpgradeEvent(UpgradeEvent): ...


class VMFSDatastoreCreatedEvent(HostEvent):
    @property
    def datastore(self) -> DatastoreEventArgument: ...
    @property
    def datastoreUrl(self) -> str: ...


class VMFSDatastoreExpandedEvent(HostEvent):
    @property
    def datastore(self) -> DatastoreEventArgument: ...


class VMFSDatastoreExtendedEvent(HostEvent):
    @property
    def datastore(self) -> DatastoreEventArgument: ...


class VMotionLicenseExpiredEvent(LicenseEvent): ...


class VcAgentUninstallFailedEvent(HostEvent):
    @property
    def reason(self) -> str: ...


class VcAgentUninstalledEvent(HostEvent): ...


class VcAgentUpgradeFailedEvent(HostEvent):
    @property
    def reason(self) -> str: ...


class VcAgentUpgradedEvent(HostEvent): ...


class VimAccountPasswordChangedEvent(HostEvent): ...


class VmAcquiredMksTicketEvent(VmEvent): ...


class VmAcquiredTicketEvent(VmEvent):
    @property
    def ticketType(self) -> str: ...


class VmAutoRenameEvent(VmEvent):
    @property
    def oldName(self) -> str: ...
    @property
    def newName(self) -> str: ...


class VmBeingClonedEvent(VmCloneEvent):
    @property
    def destFolder(self) -> FolderEventArgument: ...
    @property
    def destName(self) -> str: ...
    @property
    def destHost(self) -> HostEventArgument: ...


class VmBeingClonedNoFolderEvent(VmCloneEvent):
    @property
    def destName(self) -> str: ...
    @property
    def destHost(self) -> HostEventArgument: ...


class VmBeingCreatedEvent(VmEvent):
    @property
    def configSpec(self) -> vim.vm.ConfigSpec: ...


class VmBeingDeployedEvent(VmEvent):
    @property
    def srcTemplate(self) -> VmEventArgument: ...


class VmBeingHotMigratedEvent(VmEvent):
    @property
    def destHost(self) -> HostEventArgument: ...
    @property
    def destDatacenter(self) -> DatacenterEventArgument: ...
    @property
    def destDatastore(self) -> DatastoreEventArgument: ...


class VmBeingMigratedEvent(VmEvent):
    @property
    def destHost(self) -> HostEventArgument: ...
    @property
    def destDatacenter(self) -> DatacenterEventArgument: ...
    @property
    def destDatastore(self) -> DatastoreEventArgument: ...


class VmBeingRelocatedEvent(VmRelocateSpecEvent):
    @property
    def destHost(self) -> HostEventArgument: ...
    @property
    def destDatacenter(self) -> DatacenterEventArgument: ...
    @property
    def destDatastore(self) -> DatastoreEventArgument: ...


class VmCloneEvent(VmEvent): ...


class VmCloneFailedEvent(VmCloneEvent):
    @property
    def destFolder(self) -> FolderEventArgument: ...
    @property
    def destName(self) -> str: ...
    @property
    def destHost(self) -> HostEventArgument: ...
    @property
    def reason(self) -> vmodl.MethodFault: ...


class VmClonedEvent(VmCloneEvent):
    @property
    def sourceVm(self) -> VmEventArgument: ...


class VmConfigMissingEvent(VmEvent): ...


class VmConnectedEvent(VmEvent): ...


class VmCreatedEvent(VmEvent): ...


class VmDasBeingResetEvent(VmEvent):
    @property
    def reason(self) -> str: ...


class VmDasBeingResetWithScreenshotEvent(VmDasBeingResetEvent):
    @property
    def screenshotFilePath(self) -> str: ...


class VmDasResetFailedEvent(VmEvent): ...


class VmDasUpdateErrorEvent(VmEvent): ...


class VmDasUpdateOkEvent(VmEvent): ...


class VmDateRolledBackEvent(VmEvent): ...


class VmDeployFailedEvent(VmEvent):
    @property
    def destDatastore(self) -> EntityEventArgument: ...
    @property
    def reason(self) -> vmodl.MethodFault: ...


class VmDeployedEvent(VmEvent):
    @property
    def srcTemplate(self) -> VmEventArgument: ...


class VmDisconnectedEvent(VmEvent): ...


class VmDiscoveredEvent(VmEvent): ...


class VmDiskFailedEvent(VmEvent):
    @property
    def disk(self) -> str: ...
    @property
    def reason(self) -> vmodl.MethodFault: ...


class VmEmigratingEvent(VmEvent): ...


class VmEndRecordingEvent(VmEvent): ...


class VmEndReplayingEvent(VmEvent): ...


class VmEvent(Event):
    @property
    def template(self) -> bool: ...


class VmEventArgument(EntityEventArgument):
    @property
    def vm(self) -> vim.VirtualMachine: ...


class VmFailedMigrateEvent(VmEvent):
    @property
    def destHost(self) -> HostEventArgument: ...
    @property
    def reason(self) -> vmodl.MethodFault: ...
    @property
    def destDatacenter(self) -> DatacenterEventArgument: ...
    @property
    def destDatastore(self) -> DatastoreEventArgument: ...


class VmFailedRelayoutEvent(VmEvent):
    @property
    def reason(self) -> vmodl.MethodFault: ...


class VmFailedRelayoutOnVmfs2DatastoreEvent(VmEvent): ...


class VmFailedStartingSecondaryEvent(VmEvent):
    @property
    def reason(self) -> str: ...


    class FailureReason(Enum):
        incompatibleHost = "incompatiblehost"
        loginFailed = "loginfailed"
        registerVmFailed = "registervmfailed"
        migrateFailed = "migratefailed"


class VmFailedToPowerOffEvent(VmEvent):
    @property
    def reason(self) -> vmodl.MethodFault: ...


class VmFailedToPowerOnEvent(VmEvent):
    @property
    def reason(self) -> vmodl.MethodFault: ...


class VmFailedToRebootGuestEvent(VmEvent):
    @property
    def reason(self) -> vmodl.MethodFault: ...


class VmFailedToResetEvent(VmEvent):
    @property
    def reason(self) -> vmodl.MethodFault: ...


class VmFailedToShutdownGuestEvent(VmEvent):
    @property
    def reason(self) -> vmodl.MethodFault: ...


class VmFailedToStandbyGuestEvent(VmEvent):
    @property
    def reason(self) -> vmodl.MethodFault: ...


class VmFailedToSuspendEvent(VmEvent):
    @property
    def reason(self) -> vmodl.MethodFault: ...


class VmFailedUpdatingSecondaryConfig(VmEvent): ...


class VmFailoverFailed(VmEvent):
    @property
    def reason(self) -> vmodl.MethodFault: ...


class VmFaultToleranceStateChangedEvent(VmEvent):
    @property
    def oldState(self) -> vim.VirtualMachine.FaultToleranceState: ...
    @property
    def newState(self) -> vim.VirtualMachine.FaultToleranceState: ...


class VmFaultToleranceTurnedOffEvent(VmEvent): ...


class VmFaultToleranceVmTerminatedEvent(VmEvent):
    @property
    def reason(self) -> str: ...


class VmGuestOSCrashedEvent(VmEvent): ...


class VmGuestRebootEvent(VmEvent): ...


class VmGuestShutdownEvent(VmEvent): ...


class VmGuestStandbyEvent(VmEvent): ...


class VmHealthMonitoringStateChangedEvent(ClusterEvent):
    @property
    def state(self) -> str: ...
    @property
    def prevState(self) -> str: ...


class VmInstanceUuidAssignedEvent(VmEvent):
    @property
    def instanceUuid(self) -> str: ...


class VmInstanceUuidChangedEvent(VmEvent):
    @property
    def oldInstanceUuid(self) -> str: ...
    @property
    def newInstanceUuid(self) -> str: ...


class VmInstanceUuidConflictEvent(VmEvent):
    @property
    def conflictedVm(self) -> VmEventArgument: ...
    @property
    def instanceUuid(self) -> str: ...


class VmMacAssignedEvent(VmEvent):
    @property
    def adapter(self) -> str: ...
    @property
    def mac(self) -> str: ...


class VmMacChangedEvent(VmEvent):
    @property
    def adapter(self) -> str: ...
    @property
    def oldMac(self) -> str: ...
    @property
    def newMac(self) -> str: ...


class VmMacConflictEvent(VmEvent):
    @property
    def conflictedVm(self) -> VmEventArgument: ...
    @property
    def mac(self) -> str: ...


class VmMaxFTRestartCountReached(VmEvent): ...


class VmMaxRestartCountReached(VmEvent): ...


class VmMessageErrorEvent(VmEvent):
    @property
    def message(self) -> str: ...
    @property
    def messageInfo(self) -> List[vim.vm.Message]: ...


class VmMessageEvent(VmEvent):
    @property
    def message(self) -> str: ...
    @property
    def messageInfo(self) -> List[vim.vm.Message]: ...


class VmMessageWarningEvent(VmEvent):
    @property
    def message(self) -> str: ...
    @property
    def messageInfo(self) -> List[vim.vm.Message]: ...


class VmMigratedEvent(VmEvent):
    @property
    def sourceHost(self) -> HostEventArgument: ...
    @property
    def sourceDatacenter(self) -> DatacenterEventArgument: ...
    @property
    def sourceDatastore(self) -> DatastoreEventArgument: ...


class VmNoCompatibleHostForSecondaryEvent(VmEvent): ...


class VmNoNetworkAccessEvent(VmEvent):
    @property
    def destHost(self) -> HostEventArgument: ...


class VmOrphanedEvent(VmEvent): ...


class VmPowerOffOnIsolationEvent(VmPoweredOffEvent):
    @property
    def isolatedHost(self) -> HostEventArgument: ...


class VmPoweredOffEvent(VmEvent): ...


class VmPoweredOnEvent(VmEvent): ...


class VmPoweringOnWithCustomizedDVPortEvent(VmEvent):
    @property
    def vnic(self) -> List[VnicPortArgument]: ...


class VmPrimaryFailoverEvent(VmEvent):
    @property
    def reason(self) -> str: ...


class VmReconfiguredEvent(VmEvent):
    @property
    def configSpec(self) -> vim.vm.ConfigSpec: ...
    @property
    def configChanges(self) -> ChangesInfoEventArgument: ...


class VmRegisteredEvent(VmEvent): ...


class VmRelayoutSuccessfulEvent(VmEvent): ...


class VmRelayoutUpToDateEvent(VmEvent): ...


class VmReloadFromPathEvent(VmEvent):
    @property
    def configPath(self) -> str: ...


class VmReloadFromPathFailedEvent(VmEvent):
    @property
    def configPath(self) -> str: ...


class VmRelocateFailedEvent(VmRelocateSpecEvent):
    @property
    def destHost(self) -> HostEventArgument: ...
    @property
    def reason(self) -> vmodl.MethodFault: ...
    @property
    def destDatacenter(self) -> DatacenterEventArgument: ...
    @property
    def destDatastore(self) -> DatastoreEventArgument: ...


class VmRelocateSpecEvent(VmEvent): ...


class VmRelocatedEvent(VmRelocateSpecEvent):
    @property
    def sourceHost(self) -> HostEventArgument: ...
    @property
    def sourceDatacenter(self) -> DatacenterEventArgument: ...
    @property
    def sourceDatastore(self) -> DatastoreEventArgument: ...


class VmRemoteConsoleConnectedEvent(VmEvent): ...


class VmRemoteConsoleDisconnectedEvent(VmEvent): ...


class VmRemovedEvent(VmEvent): ...


class VmRenamedEvent(VmEvent):
    @property
    def oldName(self) -> str: ...
    @property
    def newName(self) -> str: ...


class VmRequirementsExceedCurrentEVCModeEvent(VmEvent): ...


class VmResettingEvent(VmEvent): ...


class VmResourcePoolMovedEvent(VmEvent):
    @property
    def oldParent(self) -> ResourcePoolEventArgument: ...
    @property
    def newParent(self) -> ResourcePoolEventArgument: ...


class VmResourceReallocatedEvent(VmEvent):
    @property
    def configChanges(self) -> ChangesInfoEventArgument: ...


class VmRestartedOnAlternateHostEvent(VmPoweredOnEvent):
    @property
    def sourceHost(self) -> HostEventArgument: ...


class VmResumingEvent(VmEvent): ...


class VmSecondaryAddedEvent(VmEvent): ...


class VmSecondaryDisabledBySystemEvent(VmEvent):
    @property
    def reason(self) -> vmodl.MethodFault: ...


class VmSecondaryDisabledEvent(VmEvent): ...


class VmSecondaryEnabledEvent(VmEvent): ...


class VmSecondaryStartedEvent(VmEvent): ...


class VmShutdownOnIsolationEvent(VmPoweredOffEvent):
    @property
    def isolatedHost(self) -> HostEventArgument: ...
    @property
    def shutdownResult(self) -> str: ...


    class Operation(Enum):
        shutdown = "shutdown"
        poweredOff = "poweredoff"


class VmStartRecordingEvent(VmEvent): ...


class VmStartReplayingEvent(VmEvent): ...


class VmStartingEvent(VmEvent): ...


class VmStartingSecondaryEvent(VmEvent): ...


class VmStaticMacConflictEvent(VmEvent):
    @property
    def conflictedVm(self) -> VmEventArgument: ...
    @property
    def mac(self) -> str: ...


class VmStoppingEvent(VmEvent): ...


class VmSuspendedEvent(VmEvent): ...


class VmSuspendingEvent(VmEvent): ...


class VmTimedoutStartingSecondaryEvent(VmEvent):
    @property
    def timeout(self) -> long: ...


class VmUnsupportedStartingEvent(VmStartingEvent):
    @property
    def guestId(self) -> str: ...


class VmUpgradeCompleteEvent(VmEvent):
    @property
    def version(self) -> str: ...


class VmUpgradeFailedEvent(VmEvent): ...


class VmUpgradingEvent(VmEvent):
    @property
    def version(self) -> str: ...


class VmUuidAssignedEvent(VmEvent):
    @property
    def uuid(self) -> str: ...


class VmUuidChangedEvent(VmEvent):
    @property
    def oldUuid(self) -> str: ...
    @property
    def newUuid(self) -> str: ...


class VmUuidConflictEvent(VmEvent):
    @property
    def conflictedVm(self) -> VmEventArgument: ...
    @property
    def uuid(self) -> str: ...


class VmVnicPoolReservationViolationClearEvent(DvsEvent):
    @property
    def vmVnicResourcePoolKey(self) -> str: ...
    @property
    def vmVnicResourcePoolName(self) -> str: ...


class VmVnicPoolReservationViolationRaiseEvent(DvsEvent):
    @property
    def vmVnicResourcePoolKey(self) -> str: ...
    @property
    def vmVnicResourcePoolName(self) -> str: ...


class VmWwnAssignedEvent(VmEvent):
    @property
    def nodeWwns(self) -> List[long]: ...
    @property
    def portWwns(self) -> List[long]: ...


class VmWwnChangedEvent(VmEvent):
    @property
    def oldNodeWwns(self) -> List[long]: ...
    @property
    def oldPortWwns(self) -> List[long]: ...
    @property
    def newNodeWwns(self) -> List[long]: ...
    @property
    def newPortWwns(self) -> List[long]: ...


class VmWwnConflictEvent(VmEvent):
    @property
    def conflictedVms(self) -> List[VmEventArgument]: ...
    @property
    def conflictedHosts(self) -> List[HostEventArgument]: ...
    @property
    def wwn(self) -> long: ...


class VnicPortArgument(vmodl.DynamicData):
    @property
    def vnic(self) -> str: ...
    @property
    def port(self) -> vim.dvs.PortConnection: ...


class WarningUpgradeEvent(UpgradeEvent): ...


class iScsiBootFailureEvent(HostEvent): ...