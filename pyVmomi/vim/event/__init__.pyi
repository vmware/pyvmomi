from typing import List, Literal
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
    @spec.setter
    def spec(self, value: vim.host.LocalAccountManager.AccountSpecification):
        self._spec = value
    @property
    def group(self) -> bool: ...
    @group.setter
    def group(self, value: bool):
        self._group = value


class AccountRemovedEvent(HostEvent):
    @property
    def account(self) -> str: ...
    @account.setter
    def account(self, value: str):
        self._account = value
    @property
    def group(self) -> bool: ...
    @group.setter
    def group(self, value: bool):
        self._group = value


class AccountUpdatedEvent(HostEvent):
    @property
    def spec(self) -> vim.host.LocalAccountManager.AccountSpecification: ...
    @spec.setter
    def spec(self, value: vim.host.LocalAccountManager.AccountSpecification):
        self._spec = value
    @property
    def group(self) -> bool: ...
    @group.setter
    def group(self, value: bool):
        self._group = value
    @property
    def prevDescription(self) -> str: ...
    @prevDescription.setter
    def prevDescription(self, value: str):
        self._prevDescription = value


class AdminPasswordNotChangedEvent(HostEvent): ...


class AlarmAcknowledgedEvent(AlarmEvent):
    @property
    def source(self) -> ManagedEntityEventArgument: ...
    @source.setter
    def source(self, value: ManagedEntityEventArgument):
        self._source = value
    @property
    def entity(self) -> ManagedEntityEventArgument: ...
    @entity.setter
    def entity(self, value: ManagedEntityEventArgument):
        self._entity = value


class AlarmActionTriggeredEvent(AlarmEvent):
    @property
    def source(self) -> ManagedEntityEventArgument: ...
    @source.setter
    def source(self, value: ManagedEntityEventArgument):
        self._source = value
    @property
    def entity(self) -> ManagedEntityEventArgument: ...
    @entity.setter
    def entity(self, value: ManagedEntityEventArgument):
        self._entity = value


class AlarmClearedEvent(AlarmEvent):
    @property
    def source(self) -> ManagedEntityEventArgument: ...
    @source.setter
    def source(self, value: ManagedEntityEventArgument):
        self._source = value
    @property
    def entity(self) -> ManagedEntityEventArgument: ...
    @entity.setter
    def entity(self, value: ManagedEntityEventArgument):
        self._entity = value
    # "from" is available at runtime but excluded from the type hints to pass static code checks.
    # @property
    # def from(self) -> str: ...
    # @from.setter
    # def from(self, value: str):
        # self._from = value


class AlarmCreatedEvent(AlarmEvent):
    @property
    def entity(self) -> ManagedEntityEventArgument: ...
    @entity.setter
    def entity(self, value: ManagedEntityEventArgument):
        self._entity = value


class AlarmEmailCompletedEvent(AlarmEvent):
    @property
    def entity(self) -> ManagedEntityEventArgument: ...
    @entity.setter
    def entity(self, value: ManagedEntityEventArgument):
        self._entity = value
    @property
    def to(self) -> str: ...
    @to.setter
    def to(self, value: str):
        self._to = value


class AlarmEmailFailedEvent(AlarmEvent):
    @property
    def entity(self) -> ManagedEntityEventArgument: ...
    @entity.setter
    def entity(self, value: ManagedEntityEventArgument):
        self._entity = value
    @property
    def to(self) -> str: ...
    @to.setter
    def to(self, value: str):
        self._to = value
    @property
    def reason(self) -> vmodl.MethodFault: ...
    @reason.setter
    def reason(self, value: vmodl.MethodFault):
        self._reason = value


class AlarmEvent(Event):
    @property
    def alarm(self) -> AlarmEventArgument: ...
    @alarm.setter
    def alarm(self, value: AlarmEventArgument):
        self._alarm = value


class AlarmEventArgument(EntityEventArgument):
    @property
    def alarm(self) -> vim.alarm.Alarm: ...
    @alarm.setter
    def alarm(self, value: vim.alarm.Alarm):
        self._alarm = value


class AlarmReconfiguredEvent(AlarmEvent):
    @property
    def entity(self) -> ManagedEntityEventArgument: ...
    @entity.setter
    def entity(self, value: ManagedEntityEventArgument):
        self._entity = value
    @property
    def configChanges(self) -> ChangesInfoEventArgument: ...
    @configChanges.setter
    def configChanges(self, value: ChangesInfoEventArgument):
        self._configChanges = value


class AlarmRemovedEvent(AlarmEvent):
    @property
    def entity(self) -> ManagedEntityEventArgument: ...
    @entity.setter
    def entity(self, value: ManagedEntityEventArgument):
        self._entity = value


class AlarmScriptCompleteEvent(AlarmEvent):
    @property
    def entity(self) -> ManagedEntityEventArgument: ...
    @entity.setter
    def entity(self, value: ManagedEntityEventArgument):
        self._entity = value
    @property
    def script(self) -> str: ...
    @script.setter
    def script(self, value: str):
        self._script = value


class AlarmScriptFailedEvent(AlarmEvent):
    @property
    def entity(self) -> ManagedEntityEventArgument: ...
    @entity.setter
    def entity(self, value: ManagedEntityEventArgument):
        self._entity = value
    @property
    def script(self) -> str: ...
    @script.setter
    def script(self, value: str):
        self._script = value
    @property
    def reason(self) -> vmodl.MethodFault: ...
    @reason.setter
    def reason(self, value: vmodl.MethodFault):
        self._reason = value


class AlarmSnmpCompletedEvent(AlarmEvent):
    @property
    def entity(self) -> ManagedEntityEventArgument: ...
    @entity.setter
    def entity(self, value: ManagedEntityEventArgument):
        self._entity = value


class AlarmSnmpFailedEvent(AlarmEvent):
    @property
    def entity(self) -> ManagedEntityEventArgument: ...
    @entity.setter
    def entity(self, value: ManagedEntityEventArgument):
        self._entity = value
    @property
    def reason(self) -> vmodl.MethodFault: ...
    @reason.setter
    def reason(self, value: vmodl.MethodFault):
        self._reason = value


class AlarmStatusChangedEvent(AlarmEvent):
    @property
    def source(self) -> ManagedEntityEventArgument: ...
    @source.setter
    def source(self, value: ManagedEntityEventArgument):
        self._source = value
    @property
    def entity(self) -> ManagedEntityEventArgument: ...
    @entity.setter
    def entity(self, value: ManagedEntityEventArgument):
        self._entity = value
    # "from" is available at runtime but excluded from the type hints to pass static code checks.
    # @property
    # def from(self) -> str: ...
    # @from.setter
    # def from(self, value: str):
        # self._from = value
    @property
    def to(self) -> str: ...
    @to.setter
    def to(self, value: str):
        self._to = value


class AllVirtualMachinesLicensedEvent(LicenseEvent): ...


class AlreadyAuthenticatedSessionEvent(SessionEvent): ...


class AuthorizationEvent(Event): ...


class BadUsernameSessionEvent(SessionEvent):
    @property
    def ipAddress(self) -> str: ...
    @ipAddress.setter
    def ipAddress(self, value: str):
        self._ipAddress = value


class CanceledHostOperationEvent(HostEvent): ...


class ChangesInfoEventArgument(vmodl.DynamicData):
    @property
    def modified(self) -> str: ...
    @modified.setter
    def modified(self, value: str):
        self._modified = value
    @property
    def added(self) -> str: ...
    @added.setter
    def added(self, value: str):
        self._added = value
    @property
    def deleted(self) -> str: ...
    @deleted.setter
    def deleted(self, value: str):
        self._deleted = value


class ClusterComplianceCheckedEvent(ClusterEvent):
    @property
    def profile(self) -> ProfileEventArgument: ...
    @profile.setter
    def profile(self, value: ProfileEventArgument):
        self._profile = value


class ClusterCreatedEvent(ClusterEvent):
    @property
    def parent(self) -> FolderEventArgument: ...
    @parent.setter
    def parent(self, value: FolderEventArgument):
        self._parent = value


class ClusterDestroyedEvent(ClusterEvent): ...


class ClusterEvent(Event): ...


class ClusterOvercommittedEvent(ClusterEvent): ...


class ClusterReconfiguredEvent(ClusterEvent):
    @property
    def configChanges(self) -> ChangesInfoEventArgument: ...
    @configChanges.setter
    def configChanges(self, value: ChangesInfoEventArgument):
        self._configChanges = value


class ClusterStatusChangedEvent(ClusterEvent):
    @property
    def oldStatus(self) -> str: ...
    @oldStatus.setter
    def oldStatus(self, value: str):
        self._oldStatus = value
    @property
    def newStatus(self) -> str: ...
    @newStatus.setter
    def newStatus(self, value: str):
        self._newStatus = value


class ComputeResourceEventArgument(EntityEventArgument):
    @property
    def computeResource(self) -> vim.ComputeResource: ...
    @computeResource.setter
    def computeResource(self, value: vim.ComputeResource):
        self._computeResource = value


class CustomFieldDefAddedEvent(CustomFieldDefEvent): ...


class CustomFieldDefEvent(CustomFieldEvent):
    @property
    def fieldKey(self) -> int: ...
    @fieldKey.setter
    def fieldKey(self, value: int):
        self._fieldKey = value
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value


class CustomFieldDefRemovedEvent(CustomFieldDefEvent): ...


class CustomFieldDefRenamedEvent(CustomFieldDefEvent):
    @property
    def newName(self) -> str: ...
    @newName.setter
    def newName(self, value: str):
        self._newName = value


class CustomFieldEvent(Event): ...


class CustomFieldValueChangedEvent(CustomFieldEvent):
    @property
    def entity(self) -> ManagedEntityEventArgument: ...
    @entity.setter
    def entity(self, value: ManagedEntityEventArgument):
        self._entity = value
    @property
    def fieldKey(self) -> int: ...
    @fieldKey.setter
    def fieldKey(self, value: int):
        self._fieldKey = value
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def value(self) -> str: ...
    @value.setter
    def value(self, value: str):
        self._value = value
    @property
    def prevState(self) -> str: ...
    @prevState.setter
    def prevState(self, value: str):
        self._prevState = value


class CustomizationEvent(VmEvent):
    @property
    def logLocation(self) -> str: ...
    @logLocation.setter
    def logLocation(self, value: str):
        self._logLocation = value


class CustomizationFailed(CustomizationEvent):
    @property
    def reason(self) -> str: ...
    @reason.setter
    def reason(self, value: str):
        self._reason = value


    class ReasonCode(Enum):
        userDefinedScriptDisabled = "userDefinedScriptDisabled"
        customizationDisabled = "customizationDisabled"
        rawDataIsNotSupported = "rawDataIsNotSupported"
        wrongMetadataFormat = "wrongMetadataFormat"


class CustomizationLinuxIdentityFailed(CustomizationFailed): ...


class CustomizationNetworkSetupFailed(CustomizationFailed): ...


class CustomizationStartedEvent(CustomizationEvent): ...


class CustomizationSucceeded(CustomizationEvent): ...


class CustomizationSysprepFailed(CustomizationFailed):
    @property
    def sysprepVersion(self) -> str: ...
    @sysprepVersion.setter
    def sysprepVersion(self, value: str):
        self._sysprepVersion = value
    @property
    def systemVersion(self) -> str: ...
    @systemVersion.setter
    def systemVersion(self, value: str):
        self._systemVersion = value


class CustomizationUnknownFailure(CustomizationFailed): ...


class DVPortgroupCreatedEvent(DVPortgroupEvent): ...


class DVPortgroupDestroyedEvent(DVPortgroupEvent): ...


class DVPortgroupEvent(Event): ...


class DVPortgroupReconfiguredEvent(DVPortgroupEvent):
    @property
    def configSpec(self) -> vim.dvs.DistributedVirtualPortgroup.ConfigSpec: ...
    @configSpec.setter
    def configSpec(self, value: vim.dvs.DistributedVirtualPortgroup.ConfigSpec):
        self._configSpec = value
    @property
    def configChanges(self) -> ChangesInfoEventArgument: ...
    @configChanges.setter
    def configChanges(self, value: ChangesInfoEventArgument):
        self._configChanges = value


class DVPortgroupRenamedEvent(DVPortgroupEvent):
    @property
    def oldName(self) -> str: ...
    @oldName.setter
    def oldName(self, value: str):
        self._oldName = value
    @property
    def newName(self) -> str: ...
    @newName.setter
    def newName(self, value: str):
        self._newName = value


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
    @failedHost.setter
    def failedHost(self, value: HostEventArgument):
        self._failedHost = value


class DasHostIsolatedEvent(ClusterEvent):
    @property
    def isolatedHost(self) -> HostEventArgument: ...
    @isolatedHost.setter
    def isolatedHost(self, value: HostEventArgument):
        self._isolatedHost = value


class DatacenterCreatedEvent(DatacenterEvent):
    @property
    def parent(self) -> FolderEventArgument: ...
    @parent.setter
    def parent(self, value: FolderEventArgument):
        self._parent = value


class DatacenterEvent(Event): ...


class DatacenterEventArgument(EntityEventArgument):
    @property
    def datacenter(self) -> vim.Datacenter: ...
    @datacenter.setter
    def datacenter(self, value: vim.Datacenter):
        self._datacenter = value


class DatacenterRenamedEvent(DatacenterEvent):
    @property
    def oldName(self) -> str: ...
    @oldName.setter
    def oldName(self, value: str):
        self._oldName = value
    @property
    def newName(self) -> str: ...
    @newName.setter
    def newName(self, value: str):
        self._newName = value


class DatastoreCapacityIncreasedEvent(DatastoreEvent):
    @property
    def oldCapacity(self) -> long: ...
    @oldCapacity.setter
    def oldCapacity(self, value: long):
        self._oldCapacity = value
    @property
    def newCapacity(self) -> long: ...
    @newCapacity.setter
    def newCapacity(self, value: long):
        self._newCapacity = value


class DatastoreDestroyedEvent(DatastoreEvent): ...


class DatastoreDiscoveredEvent(HostEvent):
    @property
    def datastore(self) -> DatastoreEventArgument: ...
    @datastore.setter
    def datastore(self, value: DatastoreEventArgument):
        self._datastore = value


class DatastoreDuplicatedEvent(DatastoreEvent): ...


class DatastoreEvent(Event):
    @property
    def datastore(self) -> DatastoreEventArgument: ...
    @datastore.setter
    def datastore(self, value: DatastoreEventArgument):
        self._datastore = value


class DatastoreEventArgument(EntityEventArgument):
    @property
    def datastore(self) -> vim.Datastore: ...
    @datastore.setter
    def datastore(self, value: vim.Datastore):
        self._datastore = value


class DatastoreFileCopiedEvent(DatastoreFileEvent):
    @property
    def sourceDatastore(self) -> DatastoreEventArgument: ...
    @sourceDatastore.setter
    def sourceDatastore(self, value: DatastoreEventArgument):
        self._sourceDatastore = value
    @property
    def sourceFile(self) -> str: ...
    @sourceFile.setter
    def sourceFile(self, value: str):
        self._sourceFile = value


class DatastoreFileDeletedEvent(DatastoreFileEvent): ...


class DatastoreFileEvent(DatastoreEvent):
    @property
    def targetFile(self) -> str: ...
    @targetFile.setter
    def targetFile(self, value: str):
        self._targetFile = value
    @property
    def sourceOfOperation(self) -> str: ...
    @sourceOfOperation.setter
    def sourceOfOperation(self, value: str):
        self._sourceOfOperation = value
    @property
    def succeeded(self) -> bool: ...
    @succeeded.setter
    def succeeded(self, value: bool):
        self._succeeded = value


class DatastoreFileMovedEvent(DatastoreFileEvent):
    @property
    def sourceDatastore(self) -> DatastoreEventArgument: ...
    @sourceDatastore.setter
    def sourceDatastore(self, value: DatastoreEventArgument):
        self._sourceDatastore = value
    @property
    def sourceFile(self) -> str: ...
    @sourceFile.setter
    def sourceFile(self, value: str):
        self._sourceFile = value


class DatastoreIORMReconfiguredEvent(DatastoreEvent): ...


class DatastorePrincipalConfigured(HostEvent):
    @property
    def datastorePrincipal(self) -> str: ...
    @datastorePrincipal.setter
    def datastorePrincipal(self, value: str):
        self._datastorePrincipal = value


class DatastoreRemovedOnHostEvent(HostEvent):
    @property
    def datastore(self) -> DatastoreEventArgument: ...
    @datastore.setter
    def datastore(self, value: DatastoreEventArgument):
        self._datastore = value


class DatastoreRenamedEvent(DatastoreEvent):
    @property
    def oldName(self) -> str: ...
    @oldName.setter
    def oldName(self, value: str):
        self._oldName = value
    @property
    def newName(self) -> str: ...
    @newName.setter
    def newName(self, value: str):
        self._newName = value


class DatastoreRenamedOnHostEvent(HostEvent):
    @property
    def oldName(self) -> str: ...
    @oldName.setter
    def oldName(self, value: str):
        self._oldName = value
    @property
    def newName(self) -> str: ...
    @newName.setter
    def newName(self, value: str):
        self._newName = value


class DrsDisabledEvent(ClusterEvent): ...


class DrsEnabledEvent(ClusterEvent):
    @property
    def behavior(self) -> str: ...
    @behavior.setter
    def behavior(self, value: str):
        self._behavior = value


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
    @reason.setter
    def reason(self, value: vmodl.MethodFault):
        self._reason = value


class DrsResourceConfigureSyncedEvent(HostEvent): ...


class DrsRuleComplianceEvent(VmEvent): ...


class DrsRuleViolationEvent(VmEvent): ...


class DrsSoftRuleViolationEvent(VmEvent): ...


class DrsVmMigratedEvent(VmMigratedEvent): ...


class DrsVmPoweredOnEvent(VmPoweredOnEvent): ...


class DuplicateIpDetectedEvent(HostEvent):
    @property
    def duplicateIP(self) -> str: ...
    @duplicateIP.setter
    def duplicateIP(self, value: str):
        self._duplicateIP = value
    @property
    def macAddress(self) -> str: ...
    @macAddress.setter
    def macAddress(self, value: str):
        self._macAddress = value


class DvpgImportEvent(DVPortgroupEvent):
    @property
    def importType(self) -> str: ...
    @importType.setter
    def importType(self, value: str):
        self._importType = value


class DvpgRestoreEvent(DVPortgroupEvent): ...


class DvsCreatedEvent(DvsEvent):
    @property
    def parent(self) -> FolderEventArgument: ...
    @parent.setter
    def parent(self, value: FolderEventArgument):
        self._parent = value


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
    @dvs.setter
    def dvs(self, value: vim.DistributedVirtualSwitch):
        self._dvs = value


class DvsHealthStatusChangeEvent(HostEvent):
    @property
    def switchUuid(self) -> str: ...
    @switchUuid.setter
    def switchUuid(self, value: str):
        self._switchUuid = value
    @property
    def healthResult(self) -> vim.dvs.HostMember.HealthCheckResult: ...
    @healthResult.setter
    def healthResult(self, value: vim.dvs.HostMember.HealthCheckResult):
        self._healthResult = value


class DvsHostBackInSyncEvent(DvsEvent):
    @property
    def hostBackInSync(self) -> HostEventArgument: ...
    @hostBackInSync.setter
    def hostBackInSync(self, value: HostEventArgument):
        self._hostBackInSync = value


class DvsHostJoinedEvent(DvsEvent):
    @property
    def hostJoined(self) -> HostEventArgument: ...
    @hostJoined.setter
    def hostJoined(self, value: HostEventArgument):
        self._hostJoined = value


class DvsHostLeftEvent(DvsEvent):
    @property
    def hostLeft(self) -> HostEventArgument: ...
    @hostLeft.setter
    def hostLeft(self, value: HostEventArgument):
        self._hostLeft = value


class DvsHostStatusUpdated(DvsEvent):
    @property
    def hostMember(self) -> HostEventArgument: ...
    @hostMember.setter
    def hostMember(self, value: HostEventArgument):
        self._hostMember = value
    @property
    def oldStatus(self) -> str: ...
    @oldStatus.setter
    def oldStatus(self, value: str):
        self._oldStatus = value
    @property
    def newStatus(self) -> str: ...
    @newStatus.setter
    def newStatus(self, value: str):
        self._newStatus = value
    @property
    def oldStatusDetail(self) -> str: ...
    @oldStatusDetail.setter
    def oldStatusDetail(self, value: str):
        self._oldStatusDetail = value
    @property
    def newStatusDetail(self) -> str: ...
    @newStatusDetail.setter
    def newStatusDetail(self, value: str):
        self._newStatusDetail = value


class DvsHostWentOutOfSyncEvent(DvsEvent):
    @property
    def hostOutOfSync(self) -> DvsOutOfSyncHostArgument: ...
    @hostOutOfSync.setter
    def hostOutOfSync(self, value: DvsOutOfSyncHostArgument):
        self._hostOutOfSync = value


class DvsImportEvent(DvsEvent):
    @property
    def importType(self) -> str: ...
    @importType.setter
    def importType(self, value: str):
        self._importType = value


class DvsMergedEvent(DvsEvent):
    @property
    def sourceDvs(self) -> DvsEventArgument: ...
    @sourceDvs.setter
    def sourceDvs(self, value: DvsEventArgument):
        self._sourceDvs = value
    @property
    def destinationDvs(self) -> DvsEventArgument: ...
    @destinationDvs.setter
    def destinationDvs(self, value: DvsEventArgument):
        self._destinationDvs = value


class DvsOutOfSyncHostArgument(vmodl.DynamicData):
    @property
    def outOfSyncHost(self) -> HostEventArgument: ...
    @outOfSyncHost.setter
    def outOfSyncHost(self, value: HostEventArgument):
        self._outOfSyncHost = value
    @property
    def configParamters(self) -> List[str]: ...
    @configParamters.setter
    def configParamters(self, value: List[str]):
        self._configParamters = value


class DvsPortBlockedEvent(DvsEvent):
    @property
    def portKey(self) -> str: ...
    @portKey.setter
    def portKey(self, value: str):
        self._portKey = value
    @property
    def statusDetail(self) -> str: ...
    @statusDetail.setter
    def statusDetail(self, value: str):
        self._statusDetail = value
    @property
    def runtimeInfo(self) -> vim.dvs.DistributedVirtualPort.RuntimeInfo: ...
    @runtimeInfo.setter
    def runtimeInfo(self, value: vim.dvs.DistributedVirtualPort.RuntimeInfo):
        self._runtimeInfo = value
    @property
    def prevBlockState(self) -> str: ...
    @prevBlockState.setter
    def prevBlockState(self, value: str):
        self._prevBlockState = value


class DvsPortConnectedEvent(DvsEvent):
    @property
    def portKey(self) -> str: ...
    @portKey.setter
    def portKey(self, value: str):
        self._portKey = value
    @property
    def connectee(self) -> vim.dvs.PortConnectee: ...
    @connectee.setter
    def connectee(self, value: vim.dvs.PortConnectee):
        self._connectee = value


class DvsPortCreatedEvent(DvsEvent):
    @property
    def portKey(self) -> List[str]: ...
    @portKey.setter
    def portKey(self, value: List[str]):
        self._portKey = value


class DvsPortDeletedEvent(DvsEvent):
    @property
    def portKey(self) -> List[str]: ...
    @portKey.setter
    def portKey(self, value: List[str]):
        self._portKey = value


class DvsPortDisconnectedEvent(DvsEvent):
    @property
    def portKey(self) -> str: ...
    @portKey.setter
    def portKey(self, value: str):
        self._portKey = value
    @property
    def connectee(self) -> vim.dvs.PortConnectee: ...
    @connectee.setter
    def connectee(self, value: vim.dvs.PortConnectee):
        self._connectee = value


class DvsPortEnteredPassthruEvent(DvsEvent):
    @property
    def portKey(self) -> str: ...
    @portKey.setter
    def portKey(self, value: str):
        self._portKey = value
    @property
    def runtimeInfo(self) -> vim.dvs.DistributedVirtualPort.RuntimeInfo: ...
    @runtimeInfo.setter
    def runtimeInfo(self, value: vim.dvs.DistributedVirtualPort.RuntimeInfo):
        self._runtimeInfo = value


class DvsPortExitedPassthruEvent(DvsEvent):
    @property
    def portKey(self) -> str: ...
    @portKey.setter
    def portKey(self, value: str):
        self._portKey = value
    @property
    def runtimeInfo(self) -> vim.dvs.DistributedVirtualPort.RuntimeInfo: ...
    @runtimeInfo.setter
    def runtimeInfo(self, value: vim.dvs.DistributedVirtualPort.RuntimeInfo):
        self._runtimeInfo = value


class DvsPortJoinPortgroupEvent(DvsEvent):
    @property
    def portKey(self) -> str: ...
    @portKey.setter
    def portKey(self, value: str):
        self._portKey = value
    @property
    def portgroupKey(self) -> str: ...
    @portgroupKey.setter
    def portgroupKey(self, value: str):
        self._portgroupKey = value
    @property
    def portgroupName(self) -> str: ...
    @portgroupName.setter
    def portgroupName(self, value: str):
        self._portgroupName = value


class DvsPortLeavePortgroupEvent(DvsEvent):
    @property
    def portKey(self) -> str: ...
    @portKey.setter
    def portKey(self, value: str):
        self._portKey = value
    @property
    def portgroupKey(self) -> str: ...
    @portgroupKey.setter
    def portgroupKey(self, value: str):
        self._portgroupKey = value
    @property
    def portgroupName(self) -> str: ...
    @portgroupName.setter
    def portgroupName(self, value: str):
        self._portgroupName = value


class DvsPortLinkDownEvent(DvsEvent):
    @property
    def portKey(self) -> str: ...
    @portKey.setter
    def portKey(self, value: str):
        self._portKey = value
    @property
    def runtimeInfo(self) -> vim.dvs.DistributedVirtualPort.RuntimeInfo: ...
    @runtimeInfo.setter
    def runtimeInfo(self, value: vim.dvs.DistributedVirtualPort.RuntimeInfo):
        self._runtimeInfo = value


class DvsPortLinkUpEvent(DvsEvent):
    @property
    def portKey(self) -> str: ...
    @portKey.setter
    def portKey(self, value: str):
        self._portKey = value
    @property
    def runtimeInfo(self) -> vim.dvs.DistributedVirtualPort.RuntimeInfo: ...
    @runtimeInfo.setter
    def runtimeInfo(self, value: vim.dvs.DistributedVirtualPort.RuntimeInfo):
        self._runtimeInfo = value


class DvsPortReconfiguredEvent(DvsEvent):
    @property
    def portKey(self) -> List[str]: ...
    @portKey.setter
    def portKey(self, value: List[str]):
        self._portKey = value
    @property
    def configChanges(self) -> List[ChangesInfoEventArgument]: ...
    @configChanges.setter
    def configChanges(self, value: List[ChangesInfoEventArgument]):
        self._configChanges = value


class DvsPortRuntimeChangeEvent(DvsEvent):
    @property
    def portKey(self) -> str: ...
    @portKey.setter
    def portKey(self, value: str):
        self._portKey = value
    @property
    def runtimeInfo(self) -> vim.dvs.DistributedVirtualPort.RuntimeInfo: ...
    @runtimeInfo.setter
    def runtimeInfo(self, value: vim.dvs.DistributedVirtualPort.RuntimeInfo):
        self._runtimeInfo = value


class DvsPortUnblockedEvent(DvsEvent):
    @property
    def portKey(self) -> str: ...
    @portKey.setter
    def portKey(self, value: str):
        self._portKey = value
    @property
    def runtimeInfo(self) -> vim.dvs.DistributedVirtualPort.RuntimeInfo: ...
    @runtimeInfo.setter
    def runtimeInfo(self, value: vim.dvs.DistributedVirtualPort.RuntimeInfo):
        self._runtimeInfo = value
    @property
    def prevBlockState(self) -> str: ...
    @prevBlockState.setter
    def prevBlockState(self, value: str):
        self._prevBlockState = value


class DvsPortVendorSpecificStateChangeEvent(DvsEvent):
    @property
    def portKey(self) -> str: ...
    @portKey.setter
    def portKey(self, value: str):
        self._portKey = value


class DvsReconfiguredEvent(DvsEvent):
    @property
    def configSpec(self) -> vim.DistributedVirtualSwitch.ConfigSpec: ...
    @configSpec.setter
    def configSpec(self, value: vim.DistributedVirtualSwitch.ConfigSpec):
        self._configSpec = value
    @property
    def configChanges(self) -> ChangesInfoEventArgument: ...
    @configChanges.setter
    def configChanges(self, value: ChangesInfoEventArgument):
        self._configChanges = value


class DvsRenamedEvent(DvsEvent):
    @property
    def oldName(self) -> str: ...
    @oldName.setter
    def oldName(self, value: str):
        self._oldName = value
    @property
    def newName(self) -> str: ...
    @newName.setter
    def newName(self, value: str):
        self._newName = value


class DvsRestoreEvent(DvsEvent): ...


class DvsUpgradeAvailableEvent(DvsEvent):
    @property
    def productInfo(self) -> vim.dvs.ProductSpec: ...
    @productInfo.setter
    def productInfo(self, value: vim.dvs.ProductSpec):
        self._productInfo = value


class DvsUpgradeInProgressEvent(DvsEvent):
    @property
    def productInfo(self) -> vim.dvs.ProductSpec: ...
    @productInfo.setter
    def productInfo(self, value: vim.dvs.ProductSpec):
        self._productInfo = value


class DvsUpgradeRejectedEvent(DvsEvent):
    @property
    def productInfo(self) -> vim.dvs.ProductSpec: ...
    @productInfo.setter
    def productInfo(self, value: vim.dvs.ProductSpec):
        self._productInfo = value


class DvsUpgradedEvent(DvsEvent):
    @property
    def productInfo(self) -> vim.dvs.ProductSpec: ...
    @productInfo.setter
    def productInfo(self, value: vim.dvs.ProductSpec):
        self._productInfo = value


class EnteredMaintenanceModeEvent(HostEvent): ...


class EnteredStandbyModeEvent(HostEvent): ...


class EnteringMaintenanceModeEvent(HostEvent): ...


class EnteringStandbyModeEvent(HostEvent): ...


class EntityEventArgument(EventArgument):
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value


class ErrorUpgradeEvent(UpgradeEvent): ...


class Event(vmodl.DynamicData):
    @property
    def key(self) -> int: ...
    @key.setter
    def key(self, value: int):
        self._key = value
    @property
    def chainId(self) -> int: ...
    @chainId.setter
    def chainId(self, value: int):
        self._chainId = value
    @property
    def createdTime(self) -> datetime: ...
    @createdTime.setter
    def createdTime(self, value: datetime):
        self._createdTime = value
    @property
    def userName(self) -> str: ...
    @userName.setter
    def userName(self, value: str):
        self._userName = value
    @property
    def datacenter(self) -> DatacenterEventArgument: ...
    @datacenter.setter
    def datacenter(self, value: DatacenterEventArgument):
        self._datacenter = value
    @property
    def computeResource(self) -> ComputeResourceEventArgument: ...
    @computeResource.setter
    def computeResource(self, value: ComputeResourceEventArgument):
        self._computeResource = value
    @property
    def host(self) -> HostEventArgument: ...
    @host.setter
    def host(self, value: HostEventArgument):
        self._host = value
    @property
    def vm(self) -> VmEventArgument: ...
    @vm.setter
    def vm(self, value: VmEventArgument):
        self._vm = value
    @property
    def ds(self) -> DatastoreEventArgument: ...
    @ds.setter
    def ds(self, value: DatastoreEventArgument):
        self._ds = value
    @property
    def net(self) -> NetworkEventArgument: ...
    @net.setter
    def net(self, value: NetworkEventArgument):
        self._net = value
    @property
    def dvs(self) -> DvsEventArgument: ...
    @dvs.setter
    def dvs(self, value: DvsEventArgument):
        self._dvs = value
    @property
    def fullFormattedMessage(self) -> str: ...
    @fullFormattedMessage.setter
    def fullFormattedMessage(self, value: str):
        self._fullFormattedMessage = value
    @property
    def changeTag(self) -> str: ...
    @changeTag.setter
    def changeTag(self, value: str):
        self._changeTag = value


    class EventSeverity(Enum):
        error = "error"
        warning = "warning"
        info = "info"
        user = "user"


class EventArgument(vmodl.DynamicData): ...


class EventDescription(vmodl.DynamicData):
    @property
    def category(self) -> List[vim.ElementDescription]: ...
    @category.setter
    def category(self, value: List[vim.ElementDescription]):
        self._category = value
    @property
    def eventInfo(self) -> List[EventDescription.EventDetail]: ...
    @eventInfo.setter
    def eventInfo(self, value: List[EventDescription.EventDetail]):
        self._eventInfo = value
    @property
    def enumeratedTypes(self) -> List[vim.EnumDescription]: ...
    @enumeratedTypes.setter
    def enumeratedTypes(self, value: List[vim.EnumDescription]):
        self._enumeratedTypes = value


    class EventArgDesc(vmodl.DynamicData):
        @property
        def name(self) -> str: ...
        @name.setter
        def name(self, value: str):
            self._name = value
        @property
        def type(self) -> str: ...
        @type.setter
        def type(self, value: str):
            self._type = value
        @property
        def description(self) -> vim.ElementDescription: ...
        @description.setter
        def description(self, value: vim.ElementDescription):
            self._description = value


    class EventDetail(vmodl.DynamicData):
        @property
        def key(self) -> type: ...
        @key.setter
        def key(self, value: type):
            self._key = value
        @property
        def description(self) -> str: ...
        @description.setter
        def description(self, value: str):
            self._description = value
        @property
        def category(self) -> str: ...
        @category.setter
        def category(self, value: str):
            self._category = value
        @property
        def formatOnDatacenter(self) -> str: ...
        @formatOnDatacenter.setter
        def formatOnDatacenter(self, value: str):
            self._formatOnDatacenter = value
        @property
        def formatOnComputeResource(self) -> str: ...
        @formatOnComputeResource.setter
        def formatOnComputeResource(self, value: str):
            self._formatOnComputeResource = value
        @property
        def formatOnHost(self) -> str: ...
        @formatOnHost.setter
        def formatOnHost(self, value: str):
            self._formatOnHost = value
        @property
        def formatOnVm(self) -> str: ...
        @formatOnVm.setter
        def formatOnVm(self, value: str):
            self._formatOnVm = value
        @property
        def fullFormat(self) -> str: ...
        @fullFormat.setter
        def fullFormat(self, value: str):
            self._fullFormat = value
        @property
        def longDescription(self) -> str: ...
        @longDescription.setter
        def longDescription(self, value: str):
            self._longDescription = value


    class EventCategory(Enum):
        info = "info"
        warning = "warning"
        error = "error"
        user = "user"


class EventEx(Event):
    @property
    def eventTypeId(self) -> str: ...
    @eventTypeId.setter
    def eventTypeId(self, value: str):
        self._eventTypeId = value
    @property
    def severity(self) -> str: ...
    @severity.setter
    def severity(self, value: str):
        self._severity = value
    @property
    def message(self) -> str: ...
    @message.setter
    def message(self, value: str):
        self._message = value
    @property
    def arguments(self) -> List[vmodl.KeyAnyValue]: ...
    @arguments.setter
    def arguments(self, value: List[vmodl.KeyAnyValue]):
        self._arguments = value
    @property
    def objectId(self) -> str: ...
    @objectId.setter
    def objectId(self, value: str):
        self._objectId = value
    @property
    def objectType(self) -> type: ...
    @objectType.setter
    def objectType(self, value: type):
        self._objectType = value
    @property
    def objectName(self) -> str: ...
    @objectName.setter
    def objectName(self, value: str):
        self._objectName = value
    @property
    def fault(self) -> vmodl.MethodFault: ...
    @fault.setter
    def fault(self, value: vmodl.MethodFault):
        self._fault = value


class EventFilterSpec(vmodl.DynamicData):
    @property
    def entity(self) -> EventFilterSpec.ByEntity: ...
    @entity.setter
    def entity(self, value: EventFilterSpec.ByEntity):
        self._entity = value
    @property
    def time(self) -> EventFilterSpec.ByTime: ...
    @time.setter
    def time(self, value: EventFilterSpec.ByTime):
        self._time = value
    @property
    def userName(self) -> EventFilterSpec.ByUsername: ...
    @userName.setter
    def userName(self, value: EventFilterSpec.ByUsername):
        self._userName = value
    @property
    def eventChainId(self) -> int: ...
    @eventChainId.setter
    def eventChainId(self, value: int):
        self._eventChainId = value
    @property
    def alarm(self) -> vim.alarm.Alarm: ...
    @alarm.setter
    def alarm(self, value: vim.alarm.Alarm):
        self._alarm = value
    @property
    def scheduledTask(self) -> vim.scheduler.ScheduledTask: ...
    @scheduledTask.setter
    def scheduledTask(self, value: vim.scheduler.ScheduledTask):
        self._scheduledTask = value
    @property
    def disableFullMessage(self) -> bool: ...
    @disableFullMessage.setter
    def disableFullMessage(self, value: bool):
        self._disableFullMessage = value
    @property
    def category(self) -> List[str]: ...
    @category.setter
    def category(self, value: List[str]):
        self._category = value
    @property
    def type(self) -> List[type]: ...
    @type.setter
    def type(self, value: List[type]):
        self._type = value
    @property
    def tag(self) -> List[str]: ...
    @tag.setter
    def tag(self, value: List[str]):
        self._tag = value
    @property
    def eventTypeId(self) -> List[str]: ...
    @eventTypeId.setter
    def eventTypeId(self, value: List[str]):
        self._eventTypeId = value
    @property
    def maxCount(self) -> int: ...
    @maxCount.setter
    def maxCount(self, value: int):
        self._maxCount = value


    class ByEntity(vmodl.DynamicData):
        @property
        def entity(self) -> vim.ManagedEntity: ...
        @entity.setter
        def entity(self, value: vim.ManagedEntity):
            self._entity = value
        @property
        def recursion(self) -> EventFilterSpec.RecursionOption | Literal['self', 'children', 'all']: ...
        @recursion.setter
        def recursion(self, value: EventFilterSpec.RecursionOption | Literal['self', 'children', 'all']):
            self._recursion = value


    class ByTime(vmodl.DynamicData):
        @property
        def beginTime(self) -> datetime: ...
        @beginTime.setter
        def beginTime(self, value: datetime):
            self._beginTime = value
        @property
        def endTime(self) -> datetime: ...
        @endTime.setter
        def endTime(self, value: datetime):
            self._endTime = value


    class ByUsername(vmodl.DynamicData):
        @property
        def systemUser(self) -> bool: ...
        @systemUser.setter
        def systemUser(self, value: bool):
            self._systemUser = value
        @property
        def userList(self) -> List[str]: ...
        @userList.setter
        def userList(self, value: List[str]):
            self._userList = value


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
    @eventTypeId.setter
    def eventTypeId(self, value: str):
        self._eventTypeId = value
    @property
    def managedObject(self) -> ManagedObject: ...
    @managedObject.setter
    def managedObject(self, value: ManagedObject):
        self._managedObject = value
    @property
    def data(self) -> List[ExtendedEvent.Pair]: ...
    @data.setter
    def data(self, value: List[ExtendedEvent.Pair]):
        self._data = value


    class Pair(vmodl.DynamicData):
        @property
        def key(self) -> str: ...
        @key.setter
        def key(self, value: str):
            self._key = value
        @property
        def value(self) -> str: ...
        @value.setter
        def value(self, value: str):
            self._value = value


class FailoverLevelRestored(ClusterEvent): ...


class FolderEventArgument(EntityEventArgument):
    @property
    def folder(self) -> vim.Folder: ...
    @folder.setter
    def folder(self, value: vim.Folder):
        self._folder = value


class GeneralEvent(Event):
    @property
    def message(self) -> str: ...
    @message.setter
    def message(self, value: str):
        self._message = value


class GeneralHostErrorEvent(GeneralEvent): ...


class GeneralHostInfoEvent(GeneralEvent): ...


class GeneralHostWarningEvent(GeneralEvent): ...


class GeneralUserEvent(GeneralEvent):
    @property
    def entity(self) -> ManagedEntityEventArgument: ...
    @entity.setter
    def entity(self, value: ManagedEntityEventArgument):
        self._entity = value


class GeneralVmErrorEvent(GeneralEvent): ...


class GeneralVmInfoEvent(GeneralEvent): ...


class GeneralVmWarningEvent(GeneralEvent): ...


class GhostDvsProxySwitchDetectedEvent(HostEvent):
    @property
    def switchUuid(self) -> List[str]: ...
    @switchUuid.setter
    def switchUuid(self, value: List[str]):
        self._switchUuid = value


class GhostDvsProxySwitchRemovedEvent(HostEvent):
    @property
    def switchUuid(self) -> List[str]: ...
    @switchUuid.setter
    def switchUuid(self, value: List[str]):
        self._switchUuid = value


class GlobalMessageChangedEvent(SessionEvent):
    @property
    def message(self) -> str: ...
    @message.setter
    def message(self, value: str):
        self._message = value
    @property
    def prevMessage(self) -> str: ...
    @prevMessage.setter
    def prevMessage(self, value: str):
        self._prevMessage = value


class HealthStatusChangedEvent(Event):
    @property
    def componentId(self) -> str: ...
    @componentId.setter
    def componentId(self, value: str):
        self._componentId = value
    @property
    def oldStatus(self) -> str: ...
    @oldStatus.setter
    def oldStatus(self, value: str):
        self._oldStatus = value
    @property
    def newStatus(self) -> str: ...
    @newStatus.setter
    def newStatus(self, value: str):
        self._newStatus = value
    @property
    def componentName(self) -> str: ...
    @componentName.setter
    def componentName(self, value: str):
        self._componentName = value
    @property
    def serviceId(self) -> str: ...
    @serviceId.setter
    def serviceId(self, value: str):
        self._serviceId = value


class HostAddFailedEvent(HostEvent):
    @property
    def hostname(self) -> str: ...
    @hostname.setter
    def hostname(self, value: str):
        self._hostname = value


class HostAddedEvent(HostEvent): ...


class HostAdminDisableEvent(HostEvent): ...


class HostAdminEnableEvent(HostEvent): ...


class HostCnxFailedAccountFailedEvent(HostEvent): ...


class HostCnxFailedAlreadyManagedEvent(HostEvent):
    @property
    def serverName(self) -> str: ...
    @serverName.setter
    def serverName(self, value: str):
        self._serverName = value


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
    @profile.setter
    def profile(self, value: ProfileEventArgument):
        self._profile = value


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
    @message.setter
    def message(self, value: str):
        self._message = value
    @property
    def reason(self) -> str: ...
    @reason.setter
    def reason(self, value: str):
        self._reason = value


    class HostDasErrorReason(Enum):
        configFailed = "configFailed"
        timeout = "timeout"
        communicationInitFailed = "communicationInitFailed"
        healthCheckScriptFailed = "healthCheckScriptFailed"
        agentFailed = "agentFailed"
        agentShutdown = "agentShutdown"
        isolationAddressUnpingable = "isolationAddressUnpingable"
        other = "other"


class HostDasEvent(HostEvent): ...


class HostDasOkEvent(HostEvent): ...


class HostDisconnectedEvent(HostEvent):
    @property
    def reason(self) -> str: ...
    @reason.setter
    def reason(self, value: str):
        self._reason = value


class HostEnableAdminFailedEvent(HostEvent):
    @property
    def permissions(self) -> List[vim.AuthorizationManager.Permission]: ...
    @permissions.setter
    def permissions(self, value: List[vim.AuthorizationManager.Permission]):
        self._permissions = value


class HostEvent(Event): ...


class HostEventArgument(EntityEventArgument):
    @property
    def host(self) -> vim.HostSystem: ...
    @host.setter
    def host(self, value: vim.HostSystem):
        self._host = value


class HostExtraNetworksEvent(HostDasEvent):
    @property
    def ips(self) -> str: ...
    @ips.setter
    def ips(self, value: str):
        self._ips = value


class HostGetShortNameFailedEvent(HostEvent): ...


class HostInAuditModeEvent(HostEvent): ...


class HostInventoryFullEvent(LicenseEvent):
    @property
    def capacity(self) -> int: ...
    @capacity.setter
    def capacity(self, value: int):
        self._capacity = value


class HostInventoryUnreadableEvent(Event): ...


class HostIpChangedEvent(HostEvent):
    @property
    def oldIP(self) -> str: ...
    @oldIP.setter
    def oldIP(self, value: str):
        self._oldIP = value
    @property
    def newIP(self) -> str: ...
    @newIP.setter
    def newIP(self, value: str):
        self._newIP = value


class HostIpInconsistentEvent(HostEvent):
    @property
    def ipAddress(self) -> str: ...
    @ipAddress.setter
    def ipAddress(self, value: str):
        self._ipAddress = value
    @property
    def ipAddress2(self) -> str: ...
    @ipAddress2.setter
    def ipAddress2(self, value: str):
        self._ipAddress2 = value


class HostIpToShortNameFailedEvent(HostEvent): ...


class HostIsolationIpPingFailedEvent(HostDasEvent):
    @property
    def isolationIp(self) -> str: ...
    @isolationIp.setter
    def isolationIp(self, value: str):
        self._isolationIp = value


class HostLicenseExpiredEvent(LicenseEvent): ...


class HostLocalPortCreatedEvent(DvsEvent):
    @property
    def hostLocalPort(self) -> vim.dvs.DistributedVirtualPort.HostLocalPortInfo: ...
    @hostLocalPort.setter
    def hostLocalPort(self, value: vim.dvs.DistributedVirtualPort.HostLocalPortInfo):
        self._hostLocalPort = value


class HostMissingNetworksEvent(HostDasEvent):
    @property
    def ips(self) -> str: ...
    @ips.setter
    def ips(self, value: str):
        self._ips = value


class HostMonitoringStateChangedEvent(ClusterEvent):
    @property
    def state(self) -> str: ...
    @state.setter
    def state(self, value: str):
        self._state = value
    @property
    def prevState(self) -> str: ...
    @prevState.setter
    def prevState(self, value: str):
        self._prevState = value


class HostNoAvailableNetworksEvent(HostDasEvent):
    @property
    def ips(self) -> str: ...
    @ips.setter
    def ips(self, value: str):
        self._ips = value


class HostNoHAEnabledPortGroupsEvent(HostDasEvent): ...


class HostNoRedundantManagementNetworkEvent(HostDasEvent): ...


class HostNonCompliantEvent(HostEvent): ...


class HostNotInClusterEvent(HostDasEvent): ...


class HostOvercommittedEvent(ClusterOvercommittedEvent): ...


class HostPrimaryAgentNotShortNameEvent(HostDasEvent):
    @property
    def primaryAgent(self) -> str: ...
    @primaryAgent.setter
    def primaryAgent(self, value: str):
        self._primaryAgent = value


class HostProfileAppliedEvent(HostEvent):
    @property
    def profile(self) -> ProfileEventArgument: ...
    @profile.setter
    def profile(self, value: ProfileEventArgument):
        self._profile = value


class HostReconnectionFailedEvent(HostEvent): ...


class HostRemovedEvent(HostEvent): ...


class HostShortNameInconsistentEvent(HostDasEvent):
    @property
    def shortName(self) -> str: ...
    @shortName.setter
    def shortName(self, value: str):
        self._shortName = value
    @property
    def shortName2(self) -> str: ...
    @shortName2.setter
    def shortName2(self, value: str):
        self._shortName2 = value


class HostShortNameToIpFailedEvent(HostEvent):
    @property
    def shortName(self) -> str: ...
    @shortName.setter
    def shortName(self, value: str):
        self._shortName = value


class HostShutdownEvent(HostEvent):
    @property
    def reason(self) -> str: ...
    @reason.setter
    def reason(self, value: str):
        self._reason = value


class HostSpecificationChangedEvent(HostEvent): ...


class HostSpecificationRequireEvent(HostEvent): ...


class HostSpecificationUpdateEvent(HostEvent):
    @property
    def hostSpec(self) -> vim.profile.host.HostSpecification: ...
    @hostSpec.setter
    def hostSpec(self, value: vim.profile.host.HostSpecification):
        self._hostSpec = value


class HostStatusChangedEvent(ClusterStatusChangedEvent): ...


class HostSubSpecificationDeleteEvent(HostEvent):
    @property
    def subSpecName(self) -> str: ...
    @subSpecName.setter
    def subSpecName(self, value: str):
        self._subSpecName = value


class HostSubSpecificationUpdateEvent(HostEvent):
    @property
    def hostSubSpec(self) -> vim.profile.host.HostSubSpecification: ...
    @hostSubSpec.setter
    def hostSubSpec(self, value: vim.profile.host.HostSubSpecification):
        self._hostSubSpec = value


class HostSyncFailedEvent(HostEvent):
    @property
    def reason(self) -> vmodl.MethodFault: ...
    @reason.setter
    def reason(self, value: vmodl.MethodFault):
        self._reason = value


class HostUpgradeFailedEvent(HostEvent): ...


class HostUserWorldSwapNotEnabledEvent(HostEvent): ...


class HostVnicConnectedToCustomizedDVPortEvent(HostEvent):
    @property
    def vnic(self) -> VnicPortArgument: ...
    @vnic.setter
    def vnic(self, value: VnicPortArgument):
        self._vnic = value
    @property
    def prevPortKey(self) -> str: ...
    @prevPortKey.setter
    def prevPortKey(self, value: str):
        self._prevPortKey = value


class HostWwnChangedEvent(HostEvent):
    @property
    def oldNodeWwns(self) -> List[long]: ...
    @oldNodeWwns.setter
    def oldNodeWwns(self, value: List[long]):
        self._oldNodeWwns = value
    @property
    def oldPortWwns(self) -> List[long]: ...
    @oldPortWwns.setter
    def oldPortWwns(self, value: List[long]):
        self._oldPortWwns = value
    @property
    def newNodeWwns(self) -> List[long]: ...
    @newNodeWwns.setter
    def newNodeWwns(self, value: List[long]):
        self._newNodeWwns = value
    @property
    def newPortWwns(self) -> List[long]: ...
    @newPortWwns.setter
    def newPortWwns(self, value: List[long]):
        self._newPortWwns = value


class HostWwnConflictEvent(HostEvent):
    @property
    def conflictedVms(self) -> List[VmEventArgument]: ...
    @conflictedVms.setter
    def conflictedVms(self, value: List[VmEventArgument]):
        self._conflictedVms = value
    @property
    def conflictedHosts(self) -> List[HostEventArgument]: ...
    @conflictedHosts.setter
    def conflictedHosts(self, value: List[HostEventArgument]):
        self._conflictedHosts = value
    @property
    def wwn(self) -> long: ...
    @wwn.setter
    def wwn(self, value: long):
        self._wwn = value


class IncorrectHostInformationEvent(LicenseEvent): ...


class InfoUpgradeEvent(UpgradeEvent): ...


class InsufficientFailoverResourcesEvent(ClusterEvent): ...


class InvalidEditionEvent(LicenseEvent):
    @property
    def feature(self) -> str: ...
    @feature.setter
    def feature(self, value: str):
        self._feature = value


class LicenseEvent(Event): ...


class LicenseExpiredEvent(Event):
    @property
    def feature(self) -> vim.LicenseManager.FeatureInfo: ...
    @feature.setter
    def feature(self, value: vim.LicenseManager.FeatureInfo):
        self._feature = value


class LicenseNonComplianceEvent(LicenseEvent):
    @property
    def url(self) -> str: ...
    @url.setter
    def url(self, value: str):
        self._url = value


class LicenseRestrictedEvent(LicenseEvent): ...


class LicenseServerAvailableEvent(LicenseEvent):
    @property
    def licenseServer(self) -> str: ...
    @licenseServer.setter
    def licenseServer(self, value: str):
        self._licenseServer = value


class LicenseServerUnavailableEvent(LicenseEvent):
    @property
    def licenseServer(self) -> str: ...
    @licenseServer.setter
    def licenseServer(self, value: str):
        self._licenseServer = value


class LocalDatastoreCreatedEvent(HostEvent):
    @property
    def datastore(self) -> DatastoreEventArgument: ...
    @datastore.setter
    def datastore(self, value: DatastoreEventArgument):
        self._datastore = value
    @property
    def datastoreUrl(self) -> str: ...
    @datastoreUrl.setter
    def datastoreUrl(self, value: str):
        self._datastoreUrl = value


class LocalTSMEnabledEvent(HostEvent): ...


class LockerMisconfiguredEvent(Event):
    @property
    def datastore(self) -> DatastoreEventArgument: ...
    @datastore.setter
    def datastore(self, value: DatastoreEventArgument):
        self._datastore = value


class LockerReconfiguredEvent(Event):
    @property
    def oldDatastore(self) -> DatastoreEventArgument: ...
    @oldDatastore.setter
    def oldDatastore(self, value: DatastoreEventArgument):
        self._oldDatastore = value
    @property
    def newDatastore(self) -> DatastoreEventArgument: ...
    @newDatastore.setter
    def newDatastore(self, value: DatastoreEventArgument):
        self._newDatastore = value


class ManagedEntityEventArgument(EntityEventArgument):
    @property
    def entity(self) -> vim.ManagedEntity: ...
    @entity.setter
    def entity(self, value: vim.ManagedEntity):
        self._entity = value


class MigrationErrorEvent(MigrationEvent): ...


class MigrationEvent(VmEvent):
    @property
    def fault(self) -> vmodl.MethodFault: ...
    @fault.setter
    def fault(self, value: vmodl.MethodFault):
        self._fault = value


class MigrationHostErrorEvent(MigrationEvent):
    @property
    def dstHost(self) -> HostEventArgument: ...
    @dstHost.setter
    def dstHost(self, value: HostEventArgument):
        self._dstHost = value


class MigrationHostWarningEvent(MigrationEvent):
    @property
    def dstHost(self) -> HostEventArgument: ...
    @dstHost.setter
    def dstHost(self, value: HostEventArgument):
        self._dstHost = value


class MigrationResourceErrorEvent(MigrationEvent):
    @property
    def dstPool(self) -> ResourcePoolEventArgument: ...
    @dstPool.setter
    def dstPool(self, value: ResourcePoolEventArgument):
        self._dstPool = value
    @property
    def dstHost(self) -> HostEventArgument: ...
    @dstHost.setter
    def dstHost(self, value: HostEventArgument):
        self._dstHost = value


class MigrationResourceWarningEvent(MigrationEvent):
    @property
    def dstPool(self) -> ResourcePoolEventArgument: ...
    @dstPool.setter
    def dstPool(self, value: ResourcePoolEventArgument):
        self._dstPool = value
    @property
    def dstHost(self) -> HostEventArgument: ...
    @dstHost.setter
    def dstHost(self, value: HostEventArgument):
        self._dstHost = value


class MigrationWarningEvent(MigrationEvent): ...


class MtuMatchEvent(DvsHealthStatusChangeEvent): ...


class MtuMismatchEvent(DvsHealthStatusChangeEvent): ...


class NASDatastoreCreatedEvent(HostEvent):
    @property
    def datastore(self) -> DatastoreEventArgument: ...
    @datastore.setter
    def datastore(self, value: DatastoreEventArgument):
        self._datastore = value
    @property
    def datastoreUrl(self) -> str: ...
    @datastoreUrl.setter
    def datastoreUrl(self, value: str):
        self._datastoreUrl = value


class NetworkEventArgument(EntityEventArgument):
    @property
    def network(self) -> vim.Network: ...
    @network.setter
    def network(self, value: vim.Network):
        self._network = value


class NetworkRollbackEvent(Event):
    @property
    def methodName(self) -> str: ...
    @methodName.setter
    def methodName(self, value: str):
        self._methodName = value
    @property
    def transactionId(self) -> str: ...
    @transactionId.setter
    def transactionId(self, value: str):
        self._transactionId = value


class NoAccessUserEvent(SessionEvent):
    @property
    def ipAddress(self) -> str: ...
    @ipAddress.setter
    def ipAddress(self, value: str):
        self._ipAddress = value


class NoDatastoresConfiguredEvent(HostEvent): ...


class NoLicenseEvent(LicenseEvent):
    @property
    def feature(self) -> vim.LicenseManager.FeatureInfo: ...
    @feature.setter
    def feature(self, value: vim.LicenseManager.FeatureInfo):
        self._feature = value


class NoMaintenanceModeDrsRecommendationForVM(VmEvent): ...


class NonVIWorkloadDetectedOnDatastoreEvent(DatastoreEvent): ...


class NotEnoughResourcesToStartVmEvent(VmEvent):
    @property
    def reason(self) -> str: ...
    @reason.setter
    def reason(self, value: str):
        self._reason = value


class OutOfSyncDvsHost(DvsEvent):
    @property
    def hostOutOfSync(self) -> List[DvsOutOfSyncHostArgument]: ...
    @hostOutOfSync.setter
    def hostOutOfSync(self, value: List[DvsOutOfSyncHostArgument]):
        self._hostOutOfSync = value


class PermissionAddedEvent(PermissionEvent):
    @property
    def role(self) -> RoleEventArgument: ...
    @role.setter
    def role(self, value: RoleEventArgument):
        self._role = value
    @property
    def propagate(self) -> bool: ...
    @propagate.setter
    def propagate(self, value: bool):
        self._propagate = value


class PermissionEvent(AuthorizationEvent):
    @property
    def entity(self) -> ManagedEntityEventArgument: ...
    @entity.setter
    def entity(self, value: ManagedEntityEventArgument):
        self._entity = value
    @property
    def principal(self) -> str: ...
    @principal.setter
    def principal(self, value: str):
        self._principal = value
    @property
    def group(self) -> bool: ...
    @group.setter
    def group(self, value: bool):
        self._group = value


class PermissionRemovedEvent(PermissionEvent): ...


class PermissionUpdatedEvent(PermissionEvent):
    @property
    def role(self) -> RoleEventArgument: ...
    @role.setter
    def role(self, value: RoleEventArgument):
        self._role = value
    @property
    def propagate(self) -> bool: ...
    @propagate.setter
    def propagate(self, value: bool):
        self._propagate = value
    @property
    def prevRole(self) -> RoleEventArgument: ...
    @prevRole.setter
    def prevRole(self, value: RoleEventArgument):
        self._prevRole = value
    @property
    def prevPropagate(self) -> bool: ...
    @prevPropagate.setter
    def prevPropagate(self, value: bool):
        self._prevPropagate = value


class ProfileAssociatedEvent(ProfileEvent): ...


class ProfileChangedEvent(ProfileEvent): ...


class ProfileCreatedEvent(ProfileEvent): ...


class ProfileDissociatedEvent(ProfileEvent): ...


class ProfileEvent(Event):
    @property
    def profile(self) -> ProfileEventArgument: ...
    @profile.setter
    def profile(self, value: ProfileEventArgument):
        self._profile = value


class ProfileEventArgument(EventArgument):
    @property
    def profile(self) -> vim.profile.Profile: ...
    @profile.setter
    def profile(self, value: vim.profile.Profile):
        self._profile = value
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value


class ProfileReferenceHostChangedEvent(ProfileEvent):
    @property
    def referenceHost(self) -> vim.HostSystem: ...
    @referenceHost.setter
    def referenceHost(self, value: vim.HostSystem):
        self._referenceHost = value
    @property
    def referenceHostName(self) -> str: ...
    @referenceHostName.setter
    def referenceHostName(self, value: str):
        self._referenceHostName = value
    @property
    def prevReferenceHostName(self) -> str: ...
    @prevReferenceHostName.setter
    def prevReferenceHostName(self, value: str):
        self._prevReferenceHostName = value


class ProfileRemovedEvent(ProfileEvent): ...


class RecoveryEvent(DvsEvent):
    @property
    def hostName(self) -> str: ...
    @hostName.setter
    def hostName(self, value: str):
        self._hostName = value
    @property
    def portKey(self) -> str: ...
    @portKey.setter
    def portKey(self, value: str):
        self._portKey = value
    @property
    def dvsUuid(self) -> str: ...
    @dvsUuid.setter
    def dvsUuid(self, value: str):
        self._dvsUuid = value
    @property
    def vnic(self) -> str: ...
    @vnic.setter
    def vnic(self, value: str):
        self._vnic = value


class RemoteTSMEnabledEvent(HostEvent): ...


class ResourcePoolCreatedEvent(ResourcePoolEvent):
    @property
    def parent(self) -> ResourcePoolEventArgument: ...
    @parent.setter
    def parent(self, value: ResourcePoolEventArgument):
        self._parent = value


class ResourcePoolDestroyedEvent(ResourcePoolEvent): ...


class ResourcePoolEvent(Event):
    @property
    def resourcePool(self) -> ResourcePoolEventArgument: ...
    @resourcePool.setter
    def resourcePool(self, value: ResourcePoolEventArgument):
        self._resourcePool = value


class ResourcePoolEventArgument(EntityEventArgument):
    @property
    def resourcePool(self) -> vim.ResourcePool: ...
    @resourcePool.setter
    def resourcePool(self, value: vim.ResourcePool):
        self._resourcePool = value


class ResourcePoolMovedEvent(ResourcePoolEvent):
    @property
    def oldParent(self) -> ResourcePoolEventArgument: ...
    @oldParent.setter
    def oldParent(self, value: ResourcePoolEventArgument):
        self._oldParent = value
    @property
    def newParent(self) -> ResourcePoolEventArgument: ...
    @newParent.setter
    def newParent(self, value: ResourcePoolEventArgument):
        self._newParent = value


class ResourcePoolReconfiguredEvent(ResourcePoolEvent):
    @property
    def configChanges(self) -> ChangesInfoEventArgument: ...
    @configChanges.setter
    def configChanges(self, value: ChangesInfoEventArgument):
        self._configChanges = value


class ResourceViolatedEvent(ResourcePoolEvent): ...


class RoleAddedEvent(RoleEvent):
    @property
    def privilegeList(self) -> List[str]: ...
    @privilegeList.setter
    def privilegeList(self, value: List[str]):
        self._privilegeList = value


class RoleEvent(AuthorizationEvent):
    @property
    def role(self) -> RoleEventArgument: ...
    @role.setter
    def role(self, value: RoleEventArgument):
        self._role = value


class RoleEventArgument(EventArgument):
    @property
    def roleId(self) -> int: ...
    @roleId.setter
    def roleId(self, value: int):
        self._roleId = value
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value


class RoleRemovedEvent(RoleEvent): ...


class RoleUpdatedEvent(RoleEvent):
    @property
    def privilegeList(self) -> List[str]: ...
    @privilegeList.setter
    def privilegeList(self, value: List[str]):
        self._privilegeList = value
    @property
    def prevRoleName(self) -> str: ...
    @prevRoleName.setter
    def prevRoleName(self, value: str):
        self._prevRoleName = value
    @property
    def privilegesAdded(self) -> List[str]: ...
    @privilegesAdded.setter
    def privilegesAdded(self, value: List[str]):
        self._privilegesAdded = value
    @property
    def privilegesRemoved(self) -> List[str]: ...
    @privilegesRemoved.setter
    def privilegesRemoved(self, value: List[str]):
        self._privilegesRemoved = value


class RollbackEvent(DvsEvent):
    @property
    def hostName(self) -> str: ...
    @hostName.setter
    def hostName(self, value: str):
        self._hostName = value
    @property
    def methodName(self) -> str: ...
    @methodName.setter
    def methodName(self, value: str):
        self._methodName = value


class ScheduledTaskCompletedEvent(ScheduledTaskEvent): ...


class ScheduledTaskCreatedEvent(ScheduledTaskEvent): ...


class ScheduledTaskEmailCompletedEvent(ScheduledTaskEvent):
    @property
    def to(self) -> str: ...
    @to.setter
    def to(self, value: str):
        self._to = value


class ScheduledTaskEmailFailedEvent(ScheduledTaskEvent):
    @property
    def to(self) -> str: ...
    @to.setter
    def to(self, value: str):
        self._to = value
    @property
    def reason(self) -> vmodl.MethodFault: ...
    @reason.setter
    def reason(self, value: vmodl.MethodFault):
        self._reason = value


class ScheduledTaskEvent(Event):
    @property
    def scheduledTask(self) -> ScheduledTaskEventArgument: ...
    @scheduledTask.setter
    def scheduledTask(self, value: ScheduledTaskEventArgument):
        self._scheduledTask = value
    @property
    def entity(self) -> ManagedEntityEventArgument: ...
    @entity.setter
    def entity(self, value: ManagedEntityEventArgument):
        self._entity = value


class ScheduledTaskEventArgument(EntityEventArgument):
    @property
    def scheduledTask(self) -> vim.scheduler.ScheduledTask: ...
    @scheduledTask.setter
    def scheduledTask(self, value: vim.scheduler.ScheduledTask):
        self._scheduledTask = value


class ScheduledTaskFailedEvent(ScheduledTaskEvent):
    @property
    def reason(self) -> vmodl.MethodFault: ...
    @reason.setter
    def reason(self, value: vmodl.MethodFault):
        self._reason = value


class ScheduledTaskReconfiguredEvent(ScheduledTaskEvent):
    @property
    def configChanges(self) -> ChangesInfoEventArgument: ...
    @configChanges.setter
    def configChanges(self, value: ChangesInfoEventArgument):
        self._configChanges = value


class ScheduledTaskRemovedEvent(ScheduledTaskEvent): ...


class ScheduledTaskStartedEvent(ScheduledTaskEvent): ...


class ServerLicenseExpiredEvent(LicenseEvent):
    @property
    def product(self) -> str: ...
    @product.setter
    def product(self, value: str):
        self._product = value


class ServerStartedSessionEvent(SessionEvent): ...


class SessionEvent(Event): ...


class SessionTerminatedEvent(SessionEvent):
    @property
    def sessionId(self) -> str: ...
    @sessionId.setter
    def sessionId(self, value: str):
        self._sessionId = value
    @property
    def terminatedUsername(self) -> str: ...
    @terminatedUsername.setter
    def terminatedUsername(self, value: str):
        self._terminatedUsername = value


class TaskEvent(Event):
    @property
    def info(self) -> vim.TaskInfo: ...
    @info.setter
    def info(self, value: vim.TaskInfo):
        self._info = value


class TaskTimeoutEvent(TaskEvent): ...


class TeamingMatchEvent(DvsHealthStatusChangeEvent): ...


class TeamingMisMatchEvent(DvsHealthStatusChangeEvent): ...


class TemplateBeingUpgradedEvent(TemplateUpgradeEvent): ...


class TemplateUpgradeEvent(Event):
    @property
    def legacyTemplate(self) -> str: ...
    @legacyTemplate.setter
    def legacyTemplate(self, value: str):
        self._legacyTemplate = value


class TemplateUpgradeFailedEvent(TemplateUpgradeEvent):
    @property
    def reason(self) -> vmodl.MethodFault: ...
    @reason.setter
    def reason(self, value: vmodl.MethodFault):
        self._reason = value


class TemplateUpgradedEvent(TemplateUpgradeEvent): ...


class TimedOutHostOperationEvent(HostEvent): ...


class UnlicensedVirtualMachinesEvent(LicenseEvent):
    @property
    def unlicensed(self) -> int: ...
    @unlicensed.setter
    def unlicensed(self, value: int):
        self._unlicensed = value
    @property
    def available(self) -> int: ...
    @available.setter
    def available(self, value: int):
        self._available = value


class UnlicensedVirtualMachinesFoundEvent(LicenseEvent):
    @property
    def available(self) -> int: ...
    @available.setter
    def available(self, value: int):
        self._available = value


class UpdatedAgentBeingRestartedEvent(HostEvent): ...


class UpgradeEvent(Event):
    @property
    def message(self) -> str: ...
    @message.setter
    def message(self, value: str):
        self._message = value


class UplinkPortMtuNotSupportEvent(DvsHealthStatusChangeEvent): ...


class UplinkPortMtuSupportEvent(DvsHealthStatusChangeEvent): ...


class UplinkPortVlanTrunkedEvent(DvsHealthStatusChangeEvent): ...


class UplinkPortVlanUntrunkedEvent(DvsHealthStatusChangeEvent): ...


class UserAssignedToGroup(HostEvent):
    @property
    def userLogin(self) -> str: ...
    @userLogin.setter
    def userLogin(self, value: str):
        self._userLogin = value
    @property
    def group(self) -> str: ...
    @group.setter
    def group(self, value: str):
        self._group = value


class UserLoginSessionEvent(SessionEvent):
    @property
    def ipAddress(self) -> str: ...
    @ipAddress.setter
    def ipAddress(self, value: str):
        self._ipAddress = value
    @property
    def userAgent(self) -> str: ...
    @userAgent.setter
    def userAgent(self, value: str):
        self._userAgent = value
    @property
    def locale(self) -> str: ...
    @locale.setter
    def locale(self, value: str):
        self._locale = value
    @property
    def sessionId(self) -> str: ...
    @sessionId.setter
    def sessionId(self, value: str):
        self._sessionId = value


class UserLogoutSessionEvent(SessionEvent):
    @property
    def ipAddress(self) -> str: ...
    @ipAddress.setter
    def ipAddress(self, value: str):
        self._ipAddress = value
    @property
    def userAgent(self) -> str: ...
    @userAgent.setter
    def userAgent(self, value: str):
        self._userAgent = value
    @property
    def callCount(self) -> long: ...
    @callCount.setter
    def callCount(self, value: long):
        self._callCount = value
    @property
    def sessionId(self) -> str: ...
    @sessionId.setter
    def sessionId(self, value: str):
        self._sessionId = value
    @property
    def loginTime(self) -> datetime: ...
    @loginTime.setter
    def loginTime(self, value: datetime):
        self._loginTime = value


class UserPasswordChanged(HostEvent):
    @property
    def userLogin(self) -> str: ...
    @userLogin.setter
    def userLogin(self, value: str):
        self._userLogin = value


class UserUnassignedFromGroup(HostEvent):
    @property
    def userLogin(self) -> str: ...
    @userLogin.setter
    def userLogin(self, value: str):
        self._userLogin = value
    @property
    def group(self) -> str: ...
    @group.setter
    def group(self, value: str):
        self._group = value


class UserUpgradeEvent(UpgradeEvent): ...


class VMFSDatastoreCreatedEvent(HostEvent):
    @property
    def datastore(self) -> DatastoreEventArgument: ...
    @datastore.setter
    def datastore(self, value: DatastoreEventArgument):
        self._datastore = value
    @property
    def datastoreUrl(self) -> str: ...
    @datastoreUrl.setter
    def datastoreUrl(self, value: str):
        self._datastoreUrl = value


class VMFSDatastoreExpandedEvent(HostEvent):
    @property
    def datastore(self) -> DatastoreEventArgument: ...
    @datastore.setter
    def datastore(self, value: DatastoreEventArgument):
        self._datastore = value


class VMFSDatastoreExtendedEvent(HostEvent):
    @property
    def datastore(self) -> DatastoreEventArgument: ...
    @datastore.setter
    def datastore(self, value: DatastoreEventArgument):
        self._datastore = value


class VMotionLicenseExpiredEvent(LicenseEvent): ...


class VcAgentUninstallFailedEvent(HostEvent):
    @property
    def reason(self) -> str: ...
    @reason.setter
    def reason(self, value: str):
        self._reason = value


class VcAgentUninstalledEvent(HostEvent): ...


class VcAgentUpgradeFailedEvent(HostEvent):
    @property
    def reason(self) -> str: ...
    @reason.setter
    def reason(self, value: str):
        self._reason = value


class VcAgentUpgradedEvent(HostEvent): ...


class VimAccountPasswordChangedEvent(HostEvent): ...


class VmAcquiredMksTicketEvent(VmEvent): ...


class VmAcquiredTicketEvent(VmEvent):
    @property
    def ticketType(self) -> str: ...
    @ticketType.setter
    def ticketType(self, value: str):
        self._ticketType = value


class VmAutoRenameEvent(VmEvent):
    @property
    def oldName(self) -> str: ...
    @oldName.setter
    def oldName(self, value: str):
        self._oldName = value
    @property
    def newName(self) -> str: ...
    @newName.setter
    def newName(self, value: str):
        self._newName = value


class VmBeingClonedEvent(VmCloneEvent):
    @property
    def destFolder(self) -> FolderEventArgument: ...
    @destFolder.setter
    def destFolder(self, value: FolderEventArgument):
        self._destFolder = value
    @property
    def destName(self) -> str: ...
    @destName.setter
    def destName(self, value: str):
        self._destName = value
    @property
    def destHost(self) -> HostEventArgument: ...
    @destHost.setter
    def destHost(self, value: HostEventArgument):
        self._destHost = value


class VmBeingClonedNoFolderEvent(VmCloneEvent):
    @property
    def destName(self) -> str: ...
    @destName.setter
    def destName(self, value: str):
        self._destName = value
    @property
    def destHost(self) -> HostEventArgument: ...
    @destHost.setter
    def destHost(self, value: HostEventArgument):
        self._destHost = value


class VmBeingCreatedEvent(VmEvent):
    @property
    def configSpec(self) -> vim.vm.ConfigSpec: ...
    @configSpec.setter
    def configSpec(self, value: vim.vm.ConfigSpec):
        self._configSpec = value


class VmBeingDeployedEvent(VmEvent):
    @property
    def srcTemplate(self) -> VmEventArgument: ...
    @srcTemplate.setter
    def srcTemplate(self, value: VmEventArgument):
        self._srcTemplate = value


class VmBeingHotMigratedEvent(VmEvent):
    @property
    def destHost(self) -> HostEventArgument: ...
    @destHost.setter
    def destHost(self, value: HostEventArgument):
        self._destHost = value
    @property
    def destDatacenter(self) -> DatacenterEventArgument: ...
    @destDatacenter.setter
    def destDatacenter(self, value: DatacenterEventArgument):
        self._destDatacenter = value
    @property
    def destDatastore(self) -> DatastoreEventArgument: ...
    @destDatastore.setter
    def destDatastore(self, value: DatastoreEventArgument):
        self._destDatastore = value


class VmBeingMigratedEvent(VmEvent):
    @property
    def destHost(self) -> HostEventArgument: ...
    @destHost.setter
    def destHost(self, value: HostEventArgument):
        self._destHost = value
    @property
    def destDatacenter(self) -> DatacenterEventArgument: ...
    @destDatacenter.setter
    def destDatacenter(self, value: DatacenterEventArgument):
        self._destDatacenter = value
    @property
    def destDatastore(self) -> DatastoreEventArgument: ...
    @destDatastore.setter
    def destDatastore(self, value: DatastoreEventArgument):
        self._destDatastore = value


class VmBeingRelocatedEvent(VmRelocateSpecEvent):
    @property
    def destHost(self) -> HostEventArgument: ...
    @destHost.setter
    def destHost(self, value: HostEventArgument):
        self._destHost = value
    @property
    def destDatacenter(self) -> DatacenterEventArgument: ...
    @destDatacenter.setter
    def destDatacenter(self, value: DatacenterEventArgument):
        self._destDatacenter = value
    @property
    def destDatastore(self) -> DatastoreEventArgument: ...
    @destDatastore.setter
    def destDatastore(self, value: DatastoreEventArgument):
        self._destDatastore = value


class VmCloneEvent(VmEvent): ...


class VmCloneFailedEvent(VmCloneEvent):
    @property
    def destFolder(self) -> FolderEventArgument: ...
    @destFolder.setter
    def destFolder(self, value: FolderEventArgument):
        self._destFolder = value
    @property
    def destName(self) -> str: ...
    @destName.setter
    def destName(self, value: str):
        self._destName = value
    @property
    def destHost(self) -> HostEventArgument: ...
    @destHost.setter
    def destHost(self, value: HostEventArgument):
        self._destHost = value
    @property
    def reason(self) -> vmodl.MethodFault: ...
    @reason.setter
    def reason(self, value: vmodl.MethodFault):
        self._reason = value


class VmClonedEvent(VmCloneEvent):
    @property
    def sourceVm(self) -> VmEventArgument: ...
    @sourceVm.setter
    def sourceVm(self, value: VmEventArgument):
        self._sourceVm = value


class VmConfigMissingEvent(VmEvent): ...


class VmConnectedEvent(VmEvent): ...


class VmCreatedEvent(VmEvent): ...


class VmDasBeingResetEvent(VmEvent):
    @property
    def reason(self) -> str: ...
    @reason.setter
    def reason(self, value: str):
        self._reason = value


class VmDasBeingResetWithScreenshotEvent(VmDasBeingResetEvent):
    @property
    def screenshotFilePath(self) -> str: ...
    @screenshotFilePath.setter
    def screenshotFilePath(self, value: str):
        self._screenshotFilePath = value


class VmDasResetFailedEvent(VmEvent): ...


class VmDasUpdateErrorEvent(VmEvent): ...


class VmDasUpdateOkEvent(VmEvent): ...


class VmDateRolledBackEvent(VmEvent): ...


class VmDeployFailedEvent(VmEvent):
    @property
    def destDatastore(self) -> EntityEventArgument: ...
    @destDatastore.setter
    def destDatastore(self, value: EntityEventArgument):
        self._destDatastore = value
    @property
    def reason(self) -> vmodl.MethodFault: ...
    @reason.setter
    def reason(self, value: vmodl.MethodFault):
        self._reason = value


class VmDeployedEvent(VmEvent):
    @property
    def srcTemplate(self) -> VmEventArgument: ...
    @srcTemplate.setter
    def srcTemplate(self, value: VmEventArgument):
        self._srcTemplate = value


class VmDisconnectedEvent(VmEvent): ...


class VmDiscoveredEvent(VmEvent): ...


class VmDiskFailedEvent(VmEvent):
    @property
    def disk(self) -> str: ...
    @disk.setter
    def disk(self, value: str):
        self._disk = value
    @property
    def reason(self) -> vmodl.MethodFault: ...
    @reason.setter
    def reason(self, value: vmodl.MethodFault):
        self._reason = value


class VmEmigratingEvent(VmEvent): ...


class VmEndRecordingEvent(VmEvent): ...


class VmEndReplayingEvent(VmEvent): ...


class VmEvent(Event):
    @property
    def template(self) -> bool: ...
    @template.setter
    def template(self, value: bool):
        self._template = value


class VmEventArgument(EntityEventArgument):
    @property
    def vm(self) -> vim.VirtualMachine: ...
    @vm.setter
    def vm(self, value: vim.VirtualMachine):
        self._vm = value


class VmFailedMigrateEvent(VmEvent):
    @property
    def destHost(self) -> HostEventArgument: ...
    @destHost.setter
    def destHost(self, value: HostEventArgument):
        self._destHost = value
    @property
    def reason(self) -> vmodl.MethodFault: ...
    @reason.setter
    def reason(self, value: vmodl.MethodFault):
        self._reason = value
    @property
    def destDatacenter(self) -> DatacenterEventArgument: ...
    @destDatacenter.setter
    def destDatacenter(self, value: DatacenterEventArgument):
        self._destDatacenter = value
    @property
    def destDatastore(self) -> DatastoreEventArgument: ...
    @destDatastore.setter
    def destDatastore(self, value: DatastoreEventArgument):
        self._destDatastore = value


class VmFailedRelayoutEvent(VmEvent):
    @property
    def reason(self) -> vmodl.MethodFault: ...
    @reason.setter
    def reason(self, value: vmodl.MethodFault):
        self._reason = value


class VmFailedRelayoutOnVmfs2DatastoreEvent(VmEvent): ...


class VmFailedStartingSecondaryEvent(VmEvent):
    @property
    def reason(self) -> str: ...
    @reason.setter
    def reason(self, value: str):
        self._reason = value


    class FailureReason(Enum):
        incompatibleHost = "incompatibleHost"
        loginFailed = "loginFailed"
        registerVmFailed = "registerVmFailed"
        migrateFailed = "migrateFailed"


class VmFailedToPowerOffEvent(VmEvent):
    @property
    def reason(self) -> vmodl.MethodFault: ...
    @reason.setter
    def reason(self, value: vmodl.MethodFault):
        self._reason = value


class VmFailedToPowerOnEvent(VmEvent):
    @property
    def reason(self) -> vmodl.MethodFault: ...
    @reason.setter
    def reason(self, value: vmodl.MethodFault):
        self._reason = value


class VmFailedToRebootGuestEvent(VmEvent):
    @property
    def reason(self) -> vmodl.MethodFault: ...
    @reason.setter
    def reason(self, value: vmodl.MethodFault):
        self._reason = value


class VmFailedToResetEvent(VmEvent):
    @property
    def reason(self) -> vmodl.MethodFault: ...
    @reason.setter
    def reason(self, value: vmodl.MethodFault):
        self._reason = value


class VmFailedToShutdownGuestEvent(VmEvent):
    @property
    def reason(self) -> vmodl.MethodFault: ...
    @reason.setter
    def reason(self, value: vmodl.MethodFault):
        self._reason = value


class VmFailedToStandbyGuestEvent(VmEvent):
    @property
    def reason(self) -> vmodl.MethodFault: ...
    @reason.setter
    def reason(self, value: vmodl.MethodFault):
        self._reason = value


class VmFailedToSuspendEvent(VmEvent):
    @property
    def reason(self) -> vmodl.MethodFault: ...
    @reason.setter
    def reason(self, value: vmodl.MethodFault):
        self._reason = value


class VmFailedUpdatingSecondaryConfig(VmEvent): ...


class VmFailoverFailed(VmEvent):
    @property
    def reason(self) -> vmodl.MethodFault: ...
    @reason.setter
    def reason(self, value: vmodl.MethodFault):
        self._reason = value


class VmFaultToleranceStateChangedEvent(VmEvent):
    @property
    def oldState(self) -> vim.VirtualMachine.FaultToleranceState | Literal['notConfigured', 'disabled', 'enabled', 'needSecondary', 'starting', 'running']: ...
    @oldState.setter
    def oldState(self, value: vim.VirtualMachine.FaultToleranceState | Literal['notConfigured', 'disabled', 'enabled', 'needSecondary', 'starting', 'running']):
        self._oldState = value
    @property
    def newState(self) -> vim.VirtualMachine.FaultToleranceState | Literal['notConfigured', 'disabled', 'enabled', 'needSecondary', 'starting', 'running']: ...
    @newState.setter
    def newState(self, value: vim.VirtualMachine.FaultToleranceState | Literal['notConfigured', 'disabled', 'enabled', 'needSecondary', 'starting', 'running']):
        self._newState = value


class VmFaultToleranceTurnedOffEvent(VmEvent): ...


class VmFaultToleranceVmTerminatedEvent(VmEvent):
    @property
    def reason(self) -> str: ...
    @reason.setter
    def reason(self, value: str):
        self._reason = value


class VmGuestOSCrashedEvent(VmEvent): ...


class VmGuestRebootEvent(VmEvent): ...


class VmGuestShutdownEvent(VmEvent): ...


class VmGuestStandbyEvent(VmEvent): ...


class VmHealthMonitoringStateChangedEvent(ClusterEvent):
    @property
    def state(self) -> str: ...
    @state.setter
    def state(self, value: str):
        self._state = value
    @property
    def prevState(self) -> str: ...
    @prevState.setter
    def prevState(self, value: str):
        self._prevState = value


class VmInstanceUuidAssignedEvent(VmEvent):
    @property
    def instanceUuid(self) -> str: ...
    @instanceUuid.setter
    def instanceUuid(self, value: str):
        self._instanceUuid = value


class VmInstanceUuidChangedEvent(VmEvent):
    @property
    def oldInstanceUuid(self) -> str: ...
    @oldInstanceUuid.setter
    def oldInstanceUuid(self, value: str):
        self._oldInstanceUuid = value
    @property
    def newInstanceUuid(self) -> str: ...
    @newInstanceUuid.setter
    def newInstanceUuid(self, value: str):
        self._newInstanceUuid = value


class VmInstanceUuidConflictEvent(VmEvent):
    @property
    def conflictedVm(self) -> VmEventArgument: ...
    @conflictedVm.setter
    def conflictedVm(self, value: VmEventArgument):
        self._conflictedVm = value
    @property
    def instanceUuid(self) -> str: ...
    @instanceUuid.setter
    def instanceUuid(self, value: str):
        self._instanceUuid = value


class VmMacAssignedEvent(VmEvent):
    @property
    def adapter(self) -> str: ...
    @adapter.setter
    def adapter(self, value: str):
        self._adapter = value
    @property
    def mac(self) -> str: ...
    @mac.setter
    def mac(self, value: str):
        self._mac = value


class VmMacChangedEvent(VmEvent):
    @property
    def adapter(self) -> str: ...
    @adapter.setter
    def adapter(self, value: str):
        self._adapter = value
    @property
    def oldMac(self) -> str: ...
    @oldMac.setter
    def oldMac(self, value: str):
        self._oldMac = value
    @property
    def newMac(self) -> str: ...
    @newMac.setter
    def newMac(self, value: str):
        self._newMac = value


class VmMacConflictEvent(VmEvent):
    @property
    def conflictedVm(self) -> VmEventArgument: ...
    @conflictedVm.setter
    def conflictedVm(self, value: VmEventArgument):
        self._conflictedVm = value
    @property
    def mac(self) -> str: ...
    @mac.setter
    def mac(self, value: str):
        self._mac = value


class VmMaxFTRestartCountReached(VmEvent): ...


class VmMaxRestartCountReached(VmEvent): ...


class VmMessageErrorEvent(VmEvent):
    @property
    def message(self) -> str: ...
    @message.setter
    def message(self, value: str):
        self._message = value
    @property
    def messageInfo(self) -> List[vim.vm.Message]: ...
    @messageInfo.setter
    def messageInfo(self, value: List[vim.vm.Message]):
        self._messageInfo = value


class VmMessageEvent(VmEvent):
    @property
    def message(self) -> str: ...
    @message.setter
    def message(self, value: str):
        self._message = value
    @property
    def messageInfo(self) -> List[vim.vm.Message]: ...
    @messageInfo.setter
    def messageInfo(self, value: List[vim.vm.Message]):
        self._messageInfo = value


class VmMessageWarningEvent(VmEvent):
    @property
    def message(self) -> str: ...
    @message.setter
    def message(self, value: str):
        self._message = value
    @property
    def messageInfo(self) -> List[vim.vm.Message]: ...
    @messageInfo.setter
    def messageInfo(self, value: List[vim.vm.Message]):
        self._messageInfo = value


class VmMigratedEvent(VmEvent):
    @property
    def sourceHost(self) -> HostEventArgument: ...
    @sourceHost.setter
    def sourceHost(self, value: HostEventArgument):
        self._sourceHost = value
    @property
    def sourceDatacenter(self) -> DatacenterEventArgument: ...
    @sourceDatacenter.setter
    def sourceDatacenter(self, value: DatacenterEventArgument):
        self._sourceDatacenter = value
    @property
    def sourceDatastore(self) -> DatastoreEventArgument: ...
    @sourceDatastore.setter
    def sourceDatastore(self, value: DatastoreEventArgument):
        self._sourceDatastore = value


class VmNoCompatibleHostForSecondaryEvent(VmEvent): ...


class VmNoNetworkAccessEvent(VmEvent):
    @property
    def destHost(self) -> HostEventArgument: ...
    @destHost.setter
    def destHost(self, value: HostEventArgument):
        self._destHost = value


class VmOrphanedEvent(VmEvent): ...


class VmPowerOffOnIsolationEvent(VmPoweredOffEvent):
    @property
    def isolatedHost(self) -> HostEventArgument: ...
    @isolatedHost.setter
    def isolatedHost(self, value: HostEventArgument):
        self._isolatedHost = value


class VmPoweredOffEvent(VmEvent): ...


class VmPoweredOnEvent(VmEvent): ...


class VmPoweringOnWithCustomizedDVPortEvent(VmEvent):
    @property
    def vnic(self) -> List[VnicPortArgument]: ...
    @vnic.setter
    def vnic(self, value: List[VnicPortArgument]):
        self._vnic = value


class VmPrimaryFailoverEvent(VmEvent):
    @property
    def reason(self) -> str: ...
    @reason.setter
    def reason(self, value: str):
        self._reason = value


class VmReconfiguredEvent(VmEvent):
    @property
    def configSpec(self) -> vim.vm.ConfigSpec: ...
    @configSpec.setter
    def configSpec(self, value: vim.vm.ConfigSpec):
        self._configSpec = value
    @property
    def configChanges(self) -> ChangesInfoEventArgument: ...
    @configChanges.setter
    def configChanges(self, value: ChangesInfoEventArgument):
        self._configChanges = value


class VmRegisteredEvent(VmEvent): ...


class VmRelayoutSuccessfulEvent(VmEvent): ...


class VmRelayoutUpToDateEvent(VmEvent): ...


class VmReloadFromPathEvent(VmEvent):
    @property
    def configPath(self) -> str: ...
    @configPath.setter
    def configPath(self, value: str):
        self._configPath = value


class VmReloadFromPathFailedEvent(VmEvent):
    @property
    def configPath(self) -> str: ...
    @configPath.setter
    def configPath(self, value: str):
        self._configPath = value


class VmRelocateFailedEvent(VmRelocateSpecEvent):
    @property
    def destHost(self) -> HostEventArgument: ...
    @destHost.setter
    def destHost(self, value: HostEventArgument):
        self._destHost = value
    @property
    def reason(self) -> vmodl.MethodFault: ...
    @reason.setter
    def reason(self, value: vmodl.MethodFault):
        self._reason = value
    @property
    def destDatacenter(self) -> DatacenterEventArgument: ...
    @destDatacenter.setter
    def destDatacenter(self, value: DatacenterEventArgument):
        self._destDatacenter = value
    @property
    def destDatastore(self) -> DatastoreEventArgument: ...
    @destDatastore.setter
    def destDatastore(self, value: DatastoreEventArgument):
        self._destDatastore = value


class VmRelocateSpecEvent(VmEvent): ...


class VmRelocatedEvent(VmRelocateSpecEvent):
    @property
    def sourceHost(self) -> HostEventArgument: ...
    @sourceHost.setter
    def sourceHost(self, value: HostEventArgument):
        self._sourceHost = value
    @property
    def sourceDatacenter(self) -> DatacenterEventArgument: ...
    @sourceDatacenter.setter
    def sourceDatacenter(self, value: DatacenterEventArgument):
        self._sourceDatacenter = value
    @property
    def sourceDatastore(self) -> DatastoreEventArgument: ...
    @sourceDatastore.setter
    def sourceDatastore(self, value: DatastoreEventArgument):
        self._sourceDatastore = value


class VmRemoteConsoleConnectedEvent(VmEvent): ...


class VmRemoteConsoleDisconnectedEvent(VmEvent): ...


class VmRemovedEvent(VmEvent): ...


class VmRenamedEvent(VmEvent):
    @property
    def oldName(self) -> str: ...
    @oldName.setter
    def oldName(self, value: str):
        self._oldName = value
    @property
    def newName(self) -> str: ...
    @newName.setter
    def newName(self, value: str):
        self._newName = value


class VmRequirementsExceedCurrentEVCModeEvent(VmEvent): ...


class VmResettingEvent(VmEvent): ...


class VmResourcePoolMovedEvent(VmEvent):
    @property
    def oldParent(self) -> ResourcePoolEventArgument: ...
    @oldParent.setter
    def oldParent(self, value: ResourcePoolEventArgument):
        self._oldParent = value
    @property
    def newParent(self) -> ResourcePoolEventArgument: ...
    @newParent.setter
    def newParent(self, value: ResourcePoolEventArgument):
        self._newParent = value


class VmResourceReallocatedEvent(VmEvent):
    @property
    def configChanges(self) -> ChangesInfoEventArgument: ...
    @configChanges.setter
    def configChanges(self, value: ChangesInfoEventArgument):
        self._configChanges = value


class VmRestartedOnAlternateHostEvent(VmPoweredOnEvent):
    @property
    def sourceHost(self) -> HostEventArgument: ...
    @sourceHost.setter
    def sourceHost(self, value: HostEventArgument):
        self._sourceHost = value


class VmResumingEvent(VmEvent): ...


class VmSecondaryAddedEvent(VmEvent): ...


class VmSecondaryDisabledBySystemEvent(VmEvent):
    @property
    def reason(self) -> vmodl.MethodFault: ...
    @reason.setter
    def reason(self, value: vmodl.MethodFault):
        self._reason = value


class VmSecondaryDisabledEvent(VmEvent): ...


class VmSecondaryEnabledEvent(VmEvent): ...


class VmSecondaryStartedEvent(VmEvent): ...


class VmShutdownOnIsolationEvent(VmPoweredOffEvent):
    @property
    def isolatedHost(self) -> HostEventArgument: ...
    @isolatedHost.setter
    def isolatedHost(self, value: HostEventArgument):
        self._isolatedHost = value
    @property
    def shutdownResult(self) -> str: ...
    @shutdownResult.setter
    def shutdownResult(self, value: str):
        self._shutdownResult = value


    class Operation(Enum):
        shutdown = "shutdown"
        poweredOff = "poweredOff"


class VmStartRecordingEvent(VmEvent): ...


class VmStartReplayingEvent(VmEvent): ...


class VmStartingEvent(VmEvent): ...


class VmStartingSecondaryEvent(VmEvent): ...


class VmStaticMacConflictEvent(VmEvent):
    @property
    def conflictedVm(self) -> VmEventArgument: ...
    @conflictedVm.setter
    def conflictedVm(self, value: VmEventArgument):
        self._conflictedVm = value
    @property
    def mac(self) -> str: ...
    @mac.setter
    def mac(self, value: str):
        self._mac = value


class VmStoppingEvent(VmEvent): ...


class VmSuspendedEvent(VmEvent): ...


class VmSuspendingEvent(VmEvent): ...


class VmTimedoutStartingSecondaryEvent(VmEvent):
    @property
    def timeout(self) -> long: ...
    @timeout.setter
    def timeout(self, value: long):
        self._timeout = value


class VmUnsupportedStartingEvent(VmStartingEvent):
    @property
    def guestId(self) -> str: ...
    @guestId.setter
    def guestId(self, value: str):
        self._guestId = value


class VmUpgradeCompleteEvent(VmEvent):
    @property
    def version(self) -> str: ...
    @version.setter
    def version(self, value: str):
        self._version = value


class VmUpgradeFailedEvent(VmEvent): ...


class VmUpgradingEvent(VmEvent):
    @property
    def version(self) -> str: ...
    @version.setter
    def version(self, value: str):
        self._version = value


class VmUuidAssignedEvent(VmEvent):
    @property
    def uuid(self) -> str: ...
    @uuid.setter
    def uuid(self, value: str):
        self._uuid = value


class VmUuidChangedEvent(VmEvent):
    @property
    def oldUuid(self) -> str: ...
    @oldUuid.setter
    def oldUuid(self, value: str):
        self._oldUuid = value
    @property
    def newUuid(self) -> str: ...
    @newUuid.setter
    def newUuid(self, value: str):
        self._newUuid = value


class VmUuidConflictEvent(VmEvent):
    @property
    def conflictedVm(self) -> VmEventArgument: ...
    @conflictedVm.setter
    def conflictedVm(self, value: VmEventArgument):
        self._conflictedVm = value
    @property
    def uuid(self) -> str: ...
    @uuid.setter
    def uuid(self, value: str):
        self._uuid = value


class VmVnicPoolReservationViolationClearEvent(DvsEvent):
    @property
    def vmVnicResourcePoolKey(self) -> str: ...
    @vmVnicResourcePoolKey.setter
    def vmVnicResourcePoolKey(self, value: str):
        self._vmVnicResourcePoolKey = value
    @property
    def vmVnicResourcePoolName(self) -> str: ...
    @vmVnicResourcePoolName.setter
    def vmVnicResourcePoolName(self, value: str):
        self._vmVnicResourcePoolName = value


class VmVnicPoolReservationViolationRaiseEvent(DvsEvent):
    @property
    def vmVnicResourcePoolKey(self) -> str: ...
    @vmVnicResourcePoolKey.setter
    def vmVnicResourcePoolKey(self, value: str):
        self._vmVnicResourcePoolKey = value
    @property
    def vmVnicResourcePoolName(self) -> str: ...
    @vmVnicResourcePoolName.setter
    def vmVnicResourcePoolName(self, value: str):
        self._vmVnicResourcePoolName = value


class VmWwnAssignedEvent(VmEvent):
    @property
    def nodeWwns(self) -> List[long]: ...
    @nodeWwns.setter
    def nodeWwns(self, value: List[long]):
        self._nodeWwns = value
    @property
    def portWwns(self) -> List[long]: ...
    @portWwns.setter
    def portWwns(self, value: List[long]):
        self._portWwns = value


class VmWwnChangedEvent(VmEvent):
    @property
    def oldNodeWwns(self) -> List[long]: ...
    @oldNodeWwns.setter
    def oldNodeWwns(self, value: List[long]):
        self._oldNodeWwns = value
    @property
    def oldPortWwns(self) -> List[long]: ...
    @oldPortWwns.setter
    def oldPortWwns(self, value: List[long]):
        self._oldPortWwns = value
    @property
    def newNodeWwns(self) -> List[long]: ...
    @newNodeWwns.setter
    def newNodeWwns(self, value: List[long]):
        self._newNodeWwns = value
    @property
    def newPortWwns(self) -> List[long]: ...
    @newPortWwns.setter
    def newPortWwns(self, value: List[long]):
        self._newPortWwns = value


class VmWwnConflictEvent(VmEvent):
    @property
    def conflictedVms(self) -> List[VmEventArgument]: ...
    @conflictedVms.setter
    def conflictedVms(self, value: List[VmEventArgument]):
        self._conflictedVms = value
    @property
    def conflictedHosts(self) -> List[HostEventArgument]: ...
    @conflictedHosts.setter
    def conflictedHosts(self, value: List[HostEventArgument]):
        self._conflictedHosts = value
    @property
    def wwn(self) -> long: ...
    @wwn.setter
    def wwn(self, value: long):
        self._wwn = value


class VnicPortArgument(vmodl.DynamicData):
    @property
    def vnic(self) -> str: ...
    @vnic.setter
    def vnic(self, value: str):
        self._vnic = value
    @property
    def port(self) -> vim.dvs.PortConnection: ...
    @port.setter
    def port(self, value: vim.dvs.PortConnection):
        self._port = value


class WarningUpgradeEvent(UpgradeEvent): ...


class iScsiBootFailureEvent(HostEvent): ...