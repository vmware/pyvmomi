# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from . import cluster as cluster
from . import host as host
from . import upgradesystem as upgradesystem

import datetime as _datetime
import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vim
import pyVmomi.vmodl
import pyVmomi.vim.cluster
import pyVmomi.vim.dvs
import pyVmomi.vim.encryption
import pyVmomi.vim.host
import pyVmomi.vim.vm
import pyVmomi.vim.vm.device
import pyVmomi.vim.vsan.cluster
import pyVmomi.vim.vsan.host



class ActiveDirectoryServerConfig(DirectoryServerConfig):
   activeDirectoryDomainName: _typing.Optional[str] = None
   username: _typing.Optional[str] = None
   password: _typing.Optional[str] = None
   organizationalUnit: _typing.Optional[str] = None
   preferredADServers: list[str] = []


class AdvancedDatastoreConfig(DatastoreConfig):
   remoteDatastores: list[pyVmomi.vim.Datastore] = []


class AutoRAIDConfig(pyVmomi.vmodl.DynamicData):
   assumeAutoManagedRAID: bool


class AutoRAIDInfo(pyVmomi.vmodl.DynamicData):
   hostFailuresToTolerate: pyVmomi.VmomiSupport.long
   subFailuresToTolerate: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class CapacityReservationInfo(pyVmomi.vmodl.DynamicData):
   hostRebuildThreshold: _typing.Optional[str] = None
   vsanOpSpaceThreshold: _typing.Optional[str] = None

class CapacityReservationState:
   pass


class ClientDatastoreConfig(DatastoreSpec):
   clusters: list[pyVmomi.vim.ClusterComputeResource] = []


class ClientUnicastConfig(pyVmomi.vmodl.DynamicData):
   unicastInfo: list[pyVmomi.vim.vsan.host.ClientClusterUnicastInfo] = []


class ClusterConfigPrecheckItem(pyVmomi.vim.ClusterComputeResource.ValidationResultBase):
   status: str
   description: _typing.Optional[pyVmomi.vmodl.LocalizableMessage] = None


class ClusterRuntimeInfo(pyVmomi.vmodl.DynamicData):
   clusterUuid: str
   totalComponentsCount: int
   cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource] = None


class CompatibilityCheckResult(pyVmomi.vmodl.DynamicData):
   status: str
   message: _typing.Optional[pyVmomi.vmodl.LocalizableMessage] = None


class ConfigInfoEx(pyVmomi.vim.vsan.cluster.ConfigInfo):
   dataEfficiencyConfig: _typing.Optional[DataEfficiencyConfig] = None
   resyncIopsLimitConfig: _typing.Optional[ResyncIopsInfo] = None
   iscsiConfig: _typing.Optional[pyVmomi.vim.cluster.VsanIscsiTargetServiceConfig] = None
   dataEncryptionConfig: _typing.Optional[DataEncryptionConfig] = None
   extendedConfig: _typing.Optional[VsanExtendedConfig] = None
   datastoreConfig: _typing.Optional[DatastoreConfig] = None
   perfsvcConfig: _typing.Optional[pyVmomi.vim.cluster.VsanPerfsvcConfig] = None
   unmapConfig: _typing.Optional[VsanUnmapConfig] = None
   vumConfig: _typing.Optional[VsanVumConfig] = None
   fileServiceConfig: _typing.Optional[FileServiceConfig] = None
   metricsConfig: _typing.Optional[MetricsConfig] = None
   rdmaConfig: _typing.Optional[RdmaConfig] = None
   dataInTransitEncryptionConfig: _typing.Optional[DataInTransitEncryptionConfig] = None
   vsanHealthConfig: _typing.Optional[VsanHealthConfigSpec] = None
   mode: _typing.Optional[str] = None
   vsanPMemConfig: _typing.Optional[VsanPMemConfig] = None
   vsanEsaConfigInfo: _typing.Optional[VsanEsaConfigInfo] = None
   xvcDatastoreConfig: _typing.Optional[XVCDatastoreConfig] = None
   serverClusterConfig: _typing.Optional[VcRemoteVsanServerClusterConfig] = None
   datastoreDefaultPolicySelectionConfig: _typing.Optional[VsanDatastoreDefaultPolicySelectionConfig] = None
   snapServiceConfig: _typing.Optional[SnapServiceConfig] = None
   deconvergedNetConfig: _typing.Optional[VsanDeconvergedNetConfig] = None
   siteFaultDomainConfig: _typing.Optional[pyVmomi.vim.cluster.SiteFaultDomainConfig] = None
   vbossClusterConfig: _typing.Optional[pyVmomi.vim.vsan.cluster.VbossClusterConfig] = None


class CyberRecoveryConfig(pyVmomi.vmodl.DynamicData):
   enabled: bool


class DataEfficiencyCapacityState(pyVmomi.vmodl.DynamicData):
   logicalCapacity: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   logicalCapacityUsed: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   physicalCapacity: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   physicalCapacityUsed: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   dedupMetadataSize: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   spaceEfficiencyMetadataSize: _typing.Optional[VsanSpaceEfficiencyMetadataSize] = None
   esaDedupSpaceSaving: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   esaCompressionSpaceSaving: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   totalSpaceUsedWithoutOverhead: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   dedupEnabledObjectSpaceUsed: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class DataEfficiencyConfig(pyVmomi.vmodl.DynamicData):
   dedupEnabled: bool
   compressionEnabled: _typing.Optional[bool] = None


class DataEfficiencyConfigEx(DataEfficiencyConfig):
   dedupStoreUuid: _typing.Optional[str] = None
   dedupPaused: _typing.Optional[bool] = None


class DataEncryptionConfig(pyVmomi.vmodl.DynamicData):
   encryptionEnabled: bool
   kmsProviderId: _typing.Optional[pyVmomi.vim.encryption.KeyProviderId] = None
   kekId: _typing.Optional[str] = None
   hostKeyId: _typing.Optional[str] = None
   dekGenerationId: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   changing: _typing.Optional[bool] = None
   eraseDisksBeforeUse: _typing.Optional[bool] = None
   wrappedDek: _typing.Optional[str] = None
   dekId: _typing.Optional[str] = None
   oldWrappedDek: _typing.Optional[str] = None
   oldDekId: _typing.Optional[str] = None
   kekVerifier: _typing.Optional[str] = None
   dekVerifier: _typing.Optional[str] = None
   oldDekVerifier: _typing.Optional[str] = None
   iv: _typing.Optional[str] = None
   syncing: _typing.Optional[bool] = None


class DataInTransitEncryptionConfig(pyVmomi.vmodl.DynamicData):
   enabled: _typing.Optional[bool] = None
   rekeyInterval: _typing.Optional[int] = None
   state: _typing.Optional[str] = None


class DataProtectionHealthSystem(pyVmomi.VmomiSupport.ManagedObject):
   def QueryHealthSummary(self, cluster: pyVmomi.vim.ClusterComputeResource) -> pyVmomi.vim.cluster.VsanClusterHealthSummary: ...
   def QueryHistoricalHealth(self, spec: pyVmomi.vim.cluster.VsanHistoricalHealthQuerySpec) -> list[pyVmomi.vim.cluster.VsanClusterHealthSummary]: ...
   def GetDpClusterSilentChecks(self, cluster: pyVmomi.vim.ClusterComputeResource) -> list[str]: ...
   def SetDpClusterSilentChecks(self, cluster: pyVmomi.vim.ClusterComputeResource, addSilentChecks: list[str], removeSilentChecks: list[str]) -> bool: ...


class DatastoreConfig(pyVmomi.vmodl.DynamicData):
   datastores: list[DatastoreSpec] = []

class DatastoreSourcePrecheckItem(MountPrecheckItem):
   pass

class DatastoreSourcePrecheckResult(MountPrecheckResult):
   pass


class DatastoreSpec(pyVmomi.vmodl.DynamicData):
   uuid: str
   name: str


class DefaultDatastorePolicySelectionInfo(pyVmomi.vmodl.DynamicData):
   enabled: bool
   defaultPolicyId: _typing.Optional[str] = None
   lastPolicySelectionTime: _typing.Optional[_datetime.datetime] = None


class DirectoryServerConfig(pyVmomi.vmodl.DynamicData):
   pass


class DiskClaimConfiguration(pyVmomi.vmodl.DynamicData):
   diskType: str
   diskNamePrefix: _typing.Optional[str] = None
   numberOfDisks: _typing.Optional[int] = None
   diskModel: _typing.Optional[str] = None
   vendor: _typing.Optional[str] = None
   diskCapacity: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class DiskDataEvacuationResourceCheckTaskDetails(ResourceCheckTaskDetails):
   diskUuid: _typing.Optional[str] = None
   isCapacityTier: _typing.Optional[bool] = None


class DiskGroupResourceCheckResult(EntityResourceCheckDetails):
   cacheTierDisk: _typing.Optional[DiskResourceCheckResult] = None
   capacityTierDisks: list[DiskResourceCheckResult] = []


class DiskInfo(pyVmomi.vmodl.DynamicData):
   diskUuid: str
   diskName: str
   isSsd: _typing.Optional[bool] = None

class DiskResourceCheckResult(EntityResourceCheckDetails):
   pass


class DpDaemonHealth(pyVmomi.vmodl.DynamicData):
   host: pyVmomi.vim.HostSystem
   name: str
   status: str


class EntityCompatibilityResult(pyVmomi.vmodl.DynamicData):
   entity: pyVmomi.vim.ManagedEntity
   compatible: bool
   incompatibleReasons: list[pyVmomi.vmodl.LocalizableMessage] = []
   extendedAttributes: list[pyVmomi.vmodl.KeyAnyValue] = []


class EntityResourceCheckDetails(pyVmomi.vmodl.DynamicData):
   name: _typing.Optional[str] = None
   uuid: _typing.Optional[str] = None
   isNew: _typing.Optional[bool] = None
   capacity: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   postOperationCapacity: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   usedCapacity: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   postOperationUsedCapacity: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   additionalRequiredCapacity: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   maxComponents: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   components: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class FaultDomainResourceCheckResult(EntityResourceCheckDetails):
   hosts: list[HostResourceCheckResult] = []


class FileServiceConfig(pyVmomi.vmodl.DynamicData):
   enabled: bool
   fileServerMemoryMB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   fileServerCPUMhz: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   fsvmMemoryMB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   fsvmCPU: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   network: _typing.Optional[pyVmomi.vim.Network] = None
   domains: list[FileServiceDomainConfig] = []
   fileAnalyticsEnabled: _typing.Optional[bool] = None

class FileServiceConfigOpType:
   pass


class FileServiceDomain(pyVmomi.vmodl.DynamicData):
   uuid: str
   config: _typing.Optional[FileServiceDomainConfig] = None


class FileServiceDomainConfig(pyVmomi.vmodl.DynamicData):
   name: _typing.Optional[str] = None
   dnsServerAddresses: list[str] = []
   dnsSuffixes: list[str] = []
   fileServerIpConfig: list[FileServiceIpConfig] = []
   directoryServerConfig: _typing.Optional[DirectoryServerConfig] = None
   version: _typing.Optional[str] = None


class FileServiceDomainQuerySpec(pyVmomi.vmodl.DynamicData):
   uuids: list[str] = []
   names: list[str] = []


class FileServiceIpConfig(pyVmomi.vim.host.IpConfig):
   fqdn: _typing.Optional[str] = None
   isPrimary: _typing.Optional[bool] = None
   gateway: str
   affinityLocation: _typing.Optional[str] = None
   ipv6Gateway: _typing.Optional[str] = None

class FileServicePreflightCheckScope:
   pass

class FileServiceVMStatus:
   pass


class FileShare(pyVmomi.vmodl.DynamicData):
   uuid: str
   config: _typing.Optional[FileShareConfig] = None
   runtime: _typing.Optional[FileShareRuntimeInfo] = None

class FileShareAccessType:
   pass


class FileShareConfig(pyVmomi.vmodl.DynamicData):
   name: _typing.Optional[str] = None
   domainName: _typing.Optional[str] = None
   quota: _typing.Optional[str] = None
   softQuota: _typing.Optional[str] = None
   labels: list[pyVmomi.vim.KeyValue] = []
   storagePolicy: _typing.Optional[pyVmomi.vim.vm.ProfileSpec] = None
   permission: list[FileShareNetPermission] = []
   protocols: list[str] = []
   smbOptions: _typing.Optional[FileShareSmbOptions] = None
   nfsSecType: _typing.Optional[str] = None
   affinityLocation: _typing.Optional[str] = None

class FileShareManagingEntity:
   pass


class FileShareNetPermission(pyVmomi.vmodl.DynamicData):
   ips: str
   permissions: _typing.Optional[str] = None
   allowRoot: _typing.Optional[bool] = None

class FileShareNfsSecType:
   pass

class FileShareProtocol:
   pass


class FileShareQueryProperties(pyVmomi.vmodl.DynamicData):
   includeBasic: _typing.Optional[bool] = None
   includeUsedCapacity: _typing.Optional[bool] = None
   includeVsanObjectUuids: _typing.Optional[bool] = None
   includeAllLabels: _typing.Optional[bool] = None
   labelKeys: list[str] = []


class FileShareQueryResult(pyVmomi.vmodl.DynamicData):
   fileShares: list[FileShare] = []
   nextOffset: _typing.Optional[str] = None
   totalShareCount: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   maxShareCount: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class FileShareQuerySpec(pyVmomi.vmodl.DynamicData):
   domainName: _typing.Optional[str] = None
   uuids: list[str] = []
   names: list[str] = []
   offset: _typing.Optional[str] = None
   limit: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   managedBy: list[str] = []
   protocols: list[str] = []
   pageNumber: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   properties: _typing.Optional[FileShareQueryProperties] = None


class FileShareRuntimeInfo(pyVmomi.vmodl.DynamicData):
   usedCapacity: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   hostname: _typing.Optional[str] = None
   address: _typing.Optional[str] = None
   vsanObjectUuids: list[str] = []
   accessPoints: list[pyVmomi.vim.KeyValue] = []
   managedBy: _typing.Optional[str] = None
   fileServerFQDN: _typing.Optional[str] = None

class FileShareSmbEncryptionType:
   pass


class FileShareSmbOptions(pyVmomi.vmodl.DynamicData):
   encryption: _typing.Optional[str] = None
   accessBasedEnumeration: _typing.Optional[bool] = None


class FileShareSnapshot(pyVmomi.vmodl.DynamicData):
   config: _typing.Optional[FileShareSnapshotConfig] = None
   creationTime: _typing.Optional[_datetime.datetime] = None
   usedCapacity: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class FileShareSnapshotConfig(pyVmomi.vmodl.DynamicData):
   shareUuid: _typing.Optional[str] = None
   name: _typing.Optional[str] = None


class FileShareSnapshotQueryResult(pyVmomi.vmodl.DynamicData):
   snapshots: list[FileShareSnapshot] = []
   totalCount: _typing.Optional[int] = None


class FileShareSnapshotQuerySpec(pyVmomi.vmodl.DynamicData):
   shareUuid: str
   snapshotNames: list[str] = []
   startTime: _typing.Optional[_datetime.datetime] = None
   endTime: _typing.Optional[_datetime.datetime] = None
   pageSize: _typing.Optional[int] = None
   pageNumber: _typing.Optional[int] = None

class HciMeshClientOperation:
   pass


class HciMeshDatastoreSource(pyVmomi.vmodl.DynamicData):
   vcInfo: RemoteVcInfo


class HostResourceCheckResult(EntityResourceCheckDetails):
   host: _typing.Optional[pyVmomi.vim.HostSystem] = None
   diskGroups: list[DiskGroupResourceCheckResult] = []
   storagePools: list[StoragePoolResourceCheckResult] = []


class HostSiteMaintenanceStatus(pyVmomi.vmodl.DynamicData):
   host: pyVmomi.vim.HostSystem
   state: _typing.Optional[str] = None
   startTime: _typing.Optional[_datetime.datetime] = None
   hostCount: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   hosts: list[str] = []
   statusUpdateTime: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class IODiagnosticsFailedCheck(pyVmomi.vmodl.DynamicData):
   unsupportedType: str
   reason: pyVmomi.vmodl.LocalizableMessage

class IODiagnosticsFailedCheckType:
   pass


class IODiagnosticsInstance(pyVmomi.vmodl.DynamicData):
   name: str
   state: str
   events: list[IODiagnosticsInstanceEvent] = []
   targets: list[IODiagnosticsTarget] = []
   startTime: _datetime.datetime
   endTime: _datetime.datetime
   recurrenceName: _typing.Optional[str] = None


class IODiagnosticsInstanceEvent(pyVmomi.vmodl.DynamicData):
   eventType: str
   eventTime: _datetime.datetime
   eventTargets: list[IODiagnosticsTarget] = []

class IODiagnosticsInstanceEventType:
   pass


class IODiagnosticsInstanceQuerySpec(pyVmomi.vmodl.DynamicData):
   targets: list[IODiagnosticsTarget] = []
   startTime: _datetime.datetime
   endTime: _typing.Optional[_datetime.datetime] = None

class IODiagnosticsInstanceState:
   pass


class IODiagnosticsObjectLayout(pyVmomi.vmodl.DynamicData):
   layout: str


class IODiagnosticsPrecheckResult(pyVmomi.vmodl.DynamicData):
   supported: bool
   failedChecks: list[IODiagnosticsFailedCheck] = []


class IODiagnosticsStats(pyVmomi.vmodl.DynamicData):
   objectsIOStats: list[ObjectIOStats] = []
   startTime: _datetime.datetime
   endTime: _datetime.datetime


class IODiagnosticsTarget(pyVmomi.vmodl.DynamicData):
   type: str
   entityId: str
   objUuids: list[str] = []


class IODiagnosticsTargetStats(pyVmomi.vmodl.DynamicData):
   target: IODiagnosticsTarget
   objectsIODiagnosticsStats: list[IODiagnosticsStats] = []

class IODiagnosticsTargetType:
   pass


class IOLatency(pyVmomi.vmodl.DynamicData):
   latencyType: str
   sourceEntityUuid: str
   destEntityUuid: str
   readLatencyStats: IOLatencyMetrics
   writeLatencyStats: IOLatencyMetrics
   detailedInfo: list[pyVmomi.vmodl.KeyAnyValue] = []


class IOLatencyMetrics(pyVmomi.vmodl.DynamicData):
   totalCount: int
   averageLatency: float
   stddevLatency: _typing.Optional[float] = None

class IOLatencyType:
   pass

class LifecycleCheckOperation:
   pass

class LifecycleClusterType:
   pass


class LifecycleConfigDetails(pyVmomi.vmodl.DynamicData):
   clusterType: str
   faultDomainsDetails: list[LifecycleFaultDomainDetails] = []
   witnessHostsDetails: list[LifecycleWitnessDetails] = []


class LifecycleFaultDomainDetails(pyVmomi.vmodl.DynamicData):
   isPreferredFaultDomain: _typing.Optional[bool] = None
   name: _typing.Optional[str] = None
   hosts: list[pyVmomi.vim.HostSystem] = []


class LifecyclePreCheckResult(pyVmomi.vmodl.DynamicData):
   type: _typing.Optional[str] = None
   description: _typing.Optional[pyVmomi.vmodl.LocalizableMessage] = None
   status: str
   reason: _typing.Optional[pyVmomi.vmodl.LocalizableMessage] = None

class LifecyclePreCheckType:
   pass


class LifecycleWitnessDetails(pyVmomi.vmodl.DynamicData):
   host: pyVmomi.vim.HostSystem
   isVirtualAppliance: bool
   sharedClusters: list[pyVmomi.vim.ClusterComputeResource] = []


class MetricProfile(pyVmomi.vmodl.DynamicData):
   authToken: str


class MetricsConfig(pyVmomi.vmodl.DynamicData):
   profiles: list[MetricProfile] = []

class Mode:
   pass


class MountPrecheckItem(pyVmomi.vmodl.DynamicData):
   type: str
   description: pyVmomi.vmodl.LocalizableMessage
   status: str
   reason: list[pyVmomi.vmodl.LocalizableMessage] = []
   ignoreMessage: list[pyVmomi.vmodl.LocalizableMessage] = []


class MountPrecheckNetworkConnectivity(pyVmomi.vmodl.DynamicData):
   host: pyVmomi.vim.HostSystem
   smallPingTestSuccessPct: int
   largePingTestSuccessPct: int
   status: str


class MountPrecheckNetworkConnectivityDetail(pyVmomi.vmodl.DynamicData):
   host: pyVmomi.vim.HostSystem
   networkConnectivity: list[MountPrecheckNetworkConnectivity] = []


class MountPrecheckNetworkConnectivityResult(MountPrecheckItem):
   details: list[MountPrecheckNetworkConnectivityDetail] = []


class MountPrecheckNetworkLatency(pyVmomi.vmodl.DynamicData):
   host: pyVmomi.vim.HostSystem
   networkLatency: pyVmomi.VmomiSupport.long
   status: str


class MountPrecheckNetworkLatencyDetail(pyVmomi.vmodl.DynamicData):
   host: pyVmomi.vim.HostSystem
   networkLatencies: list[MountPrecheckNetworkLatency] = []

class MountPrecheckNetworkLatencyResult(MountPrecheckItem):
   details: list[MountPrecheckNetworkLatencyDetail] = []


class MountPrecheckResult(pyVmomi.vmodl.DynamicData):
   result: list[MountPrecheckItem] = []

class MountPrecheckType:
   pass

class MountPrecheckTypeDIT:
   pass


class ObjectHealthTelemetrySummary(pyVmomi.vmodl.DynamicData):
   healthyObjectCount: int
   inaccessibleObjectCount: int
   needRetryObjectCount: int
   pdlObjectCount: int
   clusterHostCount: int


class ObjectIOStats(pyVmomi.vmodl.DynamicData):
   backingObjectId: str
   ioLatencyStats: list[IOLatency] = []
   objectLayout: IODiagnosticsObjectLayout

class PerfsvcRemediateAction:
   pass

class PrecheckDatastoreSourceOperation:
   pass


class ProactiveRebalanceInfo(pyVmomi.vmodl.DynamicData):
   enabled: _typing.Optional[bool] = None
   threshold: _typing.Optional[int] = None


class RdmaConfig(pyVmomi.vmodl.DynamicData):
   rdmaEnabled: bool


class ReconfigSpec(pyVmomi.vim.SDDCBase):
   vsanClusterConfig: _typing.Optional[pyVmomi.vim.vsan.cluster.ConfigInfo] = None
   dataEfficiencyConfig: _typing.Optional[DataEfficiencyConfig] = None
   diskMappingSpec: _typing.Optional[pyVmomi.vim.cluster.VsanDiskMappingsConfigSpec] = None
   faultDomainsSpec: _typing.Optional[pyVmomi.vim.cluster.VsanFaultDomainsConfigSpec] = None
   modify: bool
   allowReducedRedundancy: _typing.Optional[bool] = None
   resyncIopsLimitConfig: _typing.Optional[ResyncIopsInfo] = None
   iscsiSpec: _typing.Optional[pyVmomi.vim.cluster.VsanIscsiTargetServiceSpec] = None
   dataEncryptionConfig: _typing.Optional[DataEncryptionConfig] = None
   extendedConfig: _typing.Optional[VsanExtendedConfig] = None
   datastoreConfig: _typing.Optional[DatastoreConfig] = None
   perfsvcConfig: _typing.Optional[pyVmomi.vim.cluster.VsanPerfsvcConfig] = None
   unmapConfig: _typing.Optional[VsanUnmapConfig] = None
   vumConfig: _typing.Optional[VsanVumConfig] = None
   metricsConfig: _typing.Optional[MetricsConfig] = None
   fileServiceConfig: _typing.Optional[FileServiceConfig] = None
   rdmaConfig: _typing.Optional[RdmaConfig] = None
   dataInTransitEncryptionConfig: _typing.Optional[DataInTransitEncryptionConfig] = None
   mode: _typing.Optional[str] = None
   vsanHealthConfig: _typing.Optional[VsanHealthConfigSpec] = None
   vsanEsaConfig: _typing.Optional[VsanEsaConfig] = None
   xvcDatastoreConfig: _typing.Optional[XVCDatastoreConfig] = None
   serverClusterConfig: _typing.Optional[VcRemoteVsanServerClusterConfig] = None
   snapServiceConfig: _typing.Optional[SnapServiceConfig] = None
   deconvergedNetConfig: _typing.Optional[VsanDeconvergedNetConfig] = None
   vbossClusterConfig: _typing.Optional[pyVmomi.vim.vsan.cluster.VbossClusterConfig] = None


class RemoteVcInfo(pyVmomi.vmodl.DynamicData):
   linkType: _typing.Optional[str] = None
   vcHost: str


class RemoteVcInfoStandalone(RemoteVcInfo):
   user: _typing.Optional[str] = None
   password: _typing.Optional[str] = None
   cert: _typing.Optional[str] = None

class RemoteVcLinkType:
   pass

class RemoteVsanNetworkTopology:
   pass


class RemoteVsanSite(pyVmomi.vmodl.DynamicData):
   name: str


class RemoteVsanSiteAffinity(pyVmomi.vmodl.DynamicData):
   clientSite: _typing.Optional[RemoteVsanSite] = None
   serverSite: RemoteVsanSite


class RepairTimerInfo(pyVmomi.vmodl.DynamicData):
   maxTimeToRepair: int
   minTimeToRepair: int
   objectCount: int
   objectCountWithRepairTimer: _typing.Optional[int] = None

class ResourceCheckComponentResult(ResourceCheckResult):
   type: str

class ResourceCheckComponentType:
   pass


class ResourceCheckDataPersistenceResult(ResourceCheckComponentResult):
   dataToRebuild: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   inaccessibleInstances: list[str] = []
   reducedAvailabilityInstances: list[str] = []
   rebuildInstances: list[str] = []


class ResourceCheckResult(EntityResourceCheckDetails):
   class ResourceCheckDedupStoreHealthState(pyVmomi.VmomiSupport.Enum):
      Inaccessible: _typing.ClassVar['ResourceCheckDedupStoreHealthState'] = 'Inaccessible'
      Noncompliant: _typing.ClassVar['ResourceCheckDedupStoreHealthState'] = 'Noncompliant'

   timestamp: _datetime.datetime
   status: str
   messages: list[pyVmomi.vmodl.LocalizableMessage] = []
   faultDomains: list[FaultDomainResourceCheckResult] = []
   dataToMove: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   nonCompliantObjects: list[str] = []
   inaccessibleObjects: list[str] = []
   capacityThreshold: _typing.Optional[VsanHealthThreshold] = None
   health: _typing.Optional[pyVmomi.vim.cluster.VsanClusterHealthSummary] = None
   dataToResync: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   dedupStoreHealth: _typing.Optional[str] = None


class ResourceCheckSpec(pyVmomi.vmodl.DynamicData):
   operation: str
   entities: list[str] = []
   maintenanceSpec: _typing.Optional[pyVmomi.vim.host.MaintenanceSpec] = None
   parent: _typing.Optional[pyVmomi.vim.Task] = None


class ResourceCheckStatus(pyVmomi.vmodl.DynamicData):
   status: str
   result: _typing.Optional[ResourceCheckResult] = None
   task: _typing.Optional[ResourceCheckTaskDetails] = None
   parentTask: _typing.Optional[ResourceCheckTaskDetails] = None
   componentResults: list[ResourceCheckComponentResult] = []

class ResourceCheckStatusType:
   pass


class ResourceCheckTaskDetails(pyVmomi.vmodl.DynamicData):
   task: pyVmomi.vim.Task
   host: _typing.Optional[pyVmomi.vim.HostSystem] = None
   hostUuid: _typing.Optional[str] = None
   maintenanceSpec: _typing.Optional[pyVmomi.vim.host.MaintenanceSpec] = None

class ResourceCheckVsanResult(ResourceCheckComponentResult):
   pass


class ResyncIopsInfo(pyVmomi.vmodl.DynamicData):
   resyncIops: int


class RuntimeStatsHostMap(pyVmomi.vmodl.DynamicData):
   host: pyVmomi.vim.HostSystem
   stats: _typing.Optional[pyVmomi.vim.vsan.host.RuntimeStats] = None


class SSDEnduranceThresholdSpec(pyVmomi.vmodl.DynamicData):
   clustername: str
   clusternameop: _typing.Optional[str] = None
   hostname: _typing.Optional[str] = None
   hostnameop: _typing.Optional[str] = None
   diskname: _typing.Optional[str] = None
   disknameop: _typing.Optional[str] = None
   diskvendorname: _typing.Optional[str] = None
   diskvendorop: _typing.Optional[str] = None
   ssdEndurancePtg: float
   severity: str


class ServerHostUnicastInfo(pyVmomi.vmodl.DynamicData):
   hostUuid: str
   nodeType: _typing.Optional[str] = None
   unicastSpec: list[pyVmomi.vim.cluster.VsanUnicastAddressInfo] = []
   thumbprintList: list[pyVmomi.vim.vm.CertThumbprint] = []


class SharedWitnessCompatibilityResult(pyVmomi.vmodl.DynamicData):
   witnessHostCompatibility: EntityCompatibilityResult
   roboClusterCompatibility: list[EntityCompatibilityResult] = []


class SiteMaintenanceCheckTaskDetails(ResourceCheckTaskDetails):
   cluster: pyVmomi.vim.ClusterComputeResource
   siteMaintenanceSpec: SiteMaintenanceSpec


class SiteMaintenanceInfo(pyVmomi.vmodl.DynamicData):
   faultDomainName: str
   state: str
   trackingTask: _typing.Optional[pyVmomi.vim.Task] = None
   hostStatus: list[HostSiteMaintenanceStatus] = []
   statusUpdateTime: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class SiteMaintenancePrecheckDetail(pyVmomi.vmodl.DynamicData):
   testName: str
   testStatus: str
   message: _typing.Optional[pyVmomi.vmodl.LocalizableMessage] = None


class SiteMaintenancePrecheckStatus(pyVmomi.vmodl.DynamicData):
   timestamp: _datetime.datetime
   status: str
   taskDetails: _typing.Optional[SiteMaintenanceCheckTaskDetails] = None
   resourceCheckResult: _typing.Optional[SiteMaintenanceResourceCheckResult] = None


class SiteMaintenanceResourceCheckResult(ResourceCheckVsanResult):
   vmToMigrate: list[pyVmomi.VmomiSupport.ManagedObject] = []
   vmToPowerOffInfo: list[VMPowerOffInfo] = []
   checkDetails: list[SiteMaintenancePrecheckDetail] = []


class SiteMaintenanceSpec(pyVmomi.vmodl.DynamicData):
   faultDomainName: str

class SiteMaintenanceState:
   pass


class SnapServiceConfig(pyVmomi.vmodl.DynamicData):
   enabled: bool

class SnapshotCreator:
   pass

class SnapshotType:
   pass


class StoragePoolDiskResourceCheckResult(DiskResourceCheckResult):
   diskType: _typing.Optional[str] = None


class StoragePoolResourceCheckResult(EntityResourceCheckDetails):
   disks: list[StoragePoolDiskResourceCheckResult] = []


class VMPowerOffInfo(pyVmomi.vmodl.DynamicData):
   vmToPowerOff: list[pyVmomi.VmomiSupport.ManagedObject] = []
   reason: _typing.Optional[pyVmomi.vmodl.LocalizableMessage] = None


class VbossConfig(pyVmomi.vmodl.DynamicData):
   enabled: bool
   configs: list[VbossObjectStoreConfig] = []


class VbossObjectStoreConfig(pyVmomi.vmodl.DynamicData):
   id: str
   secretKey: _typing.Optional[str] = None
   volumeUuids: list[str] = []
   properties: _typing.Optional[str] = None


class VcRemoteVsanServerClusterConfig(pyVmomi.vmodl.DynamicData):
   serverClusters: list[VcRemoteVsanServerClusterInfo] = []


class VcRemoteVsanServerClusterInfo(pyVmomi.vmodl.DynamicData):
   clusterUuid: str
   networkTopology: _typing.Optional[str] = None
   siteAffinity: list[RemoteVsanSiteAffinity] = []
   ownerVc: _typing.Optional[str] = None
   ditConfig: _typing.Optional[DataInTransitEncryptionConfig] = None


class VipConfig(VipConfigSpec):
   vmknicName: _typing.Optional[str] = None
   owner: _typing.Optional[pyVmomi.vim.HostSystem] = None
   ownerHostUuid: _typing.Optional[str] = None


class VipConfigSpec(pyVmomi.vmodl.DynamicData):
   enabled: _typing.Optional[bool] = None
   v4NetworkConfig: _typing.Optional[VipNetworkConfig] = None
   v6NetworkConfig: _typing.Optional[VipNetworkConfig] = None
   vswitchConfig: _typing.Optional[VipVswitchConfig] = None
   distributedSwitchConfig: _typing.Optional[VipDVswitchConfig] = None


class VipDVswitchConfig(pyVmomi.vmodl.DynamicData):
   portGroup: _typing.Optional[pyVmomi.vim.dvs.DistributedVirtualPortgroup] = None
   dvsUuid: _typing.Optional[str] = None


class VipNetworkConfig(pyVmomi.vmodl.DynamicData):
   ipAddress: str
   subnet: str
   gateway: _typing.Optional[str] = None


class VipVswitchConfig(pyVmomi.vmodl.DynamicData):
   vswitchName: str
   vlanId: _typing.Optional[int] = None

class VsanAnalyticsEventLocationType:
   pass

class VsanAnalyticsEventSnapshotType:
   pass

class VsanAnalyticsEventType:
   pass


class VsanBurnInTest(pyVmomi.vmodl.DynamicData):
   testname: str
   workload: _typing.Optional[str] = None
   duration: pyVmomi.VmomiSupport.long
   result: str


class VsanBurnInTestCheckResult(pyVmomi.vmodl.DynamicData):
   passedTests: list[VsanBurnInTest] = []
   notPerformedTests: list[VsanBurnInTest] = []
   failedTests: list[VsanBurnInTest] = []


class VsanCloudHealthStatus(pyVmomi.vmodl.DynamicData):
   collectorRunning: _typing.Optional[bool] = None
   lastSentTimestamp: _typing.Optional[str] = None
   internetConnectivity: _typing.Optional[bool] = None


class VsanClusterBurnInTestResultList(pyVmomi.vmodl.DynamicData):
   items: list[VsanBurnInTest] = []
   hosts: list[str] = []


class VsanCompliantDriver(pyVmomi.vmodl.DynamicData):
   driverName: str
   driverVersion: str
   supportedFeatures: list[str] = []


class VsanCompliantFirmware(pyVmomi.vmodl.DynamicData):
   firmwareVersion: str
   compliantDrivers: list[VsanCompliantDriver] = []


class VsanConfigBaseIssue(pyVmomi.vmodl.DynamicData):
   pass


class VsanConfigCheckResult(pyVmomi.vmodl.DynamicData):
   vsanEnabled: bool
   issues: list[VsanConfigBaseIssue] = []


class VsanConfigNotAllDisksClaimedIssue(VsanConfigBaseIssue):
   host: pyVmomi.vim.HostSystem
   disks: list[str] = []

class VsanConfigType:
   pass


class VsanDatastoreDefaultPolicySelectionConfig(pyVmomi.vmodl.DynamicData):
   enabled: bool


class VsanDeconvergedNetConfig(pyVmomi.vmodl.DynamicData):
   enabled: bool

class VsanDiskCompatibilityType:
   pass


class VsanDiskModelInfo(pyVmomi.vmodl.DynamicData):
   productId: str
   vendor: str
   partNumber: _typing.Optional[str] = None


class VsanDownloadItem(pyVmomi.vmodl.DynamicData):
   url: str
   sha1sum: str
   formatType: _typing.Optional[str] = None
   itemId: _typing.Optional[str] = None


class VsanEsaConfig(pyVmomi.vmodl.DynamicData):
   storagePoolSpecs: list[pyVmomi.vim.vsan.host.AddStoragePoolDiskSpec] = []
   hclDiskClaimEnabled: _typing.Optional[bool] = None
   datastoreDefaultPolicySelectionConfig: _typing.Optional[VsanDatastoreDefaultPolicySelectionConfig] = None
   diskConfiguration: _typing.Optional[VsanEsaDiskConfiguration] = None
   autoRAIDConfig: _typing.Optional[AutoRAIDConfig] = None
   deleteStoragePoolDiskSpec: _typing.Optional[pyVmomi.vim.vsan.host.DeleteStoragePoolDiskSpec] = None


class VsanEsaConfigInfo(pyVmomi.vmodl.DynamicData):
   hclDiskClaimEnabled: _typing.Optional[bool] = None
   datastoreDefaultPolicySelectionConfig: _typing.Optional[VsanDatastoreDefaultPolicySelectionConfig] = None
   diskConfiguration: _typing.Optional[VsanEsaDiskConfiguration] = None
   autoRAIDConfig: _typing.Optional[AutoRAIDConfig] = None


class VsanEsaDiskConfiguration(pyVmomi.vmodl.DynamicData):
   diskClaimConfiguration: list[DiskClaimConfiguration] = []


class VsanExtendedConfig(pyVmomi.vmodl.DynamicData):
   objectRepairTimer: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   disableSiteReadLocality: _typing.Optional[bool] = None
   enableCustomizedSwapObject: _typing.Optional[bool] = None
   largeScaleClusterSupport: _typing.Optional[bool] = None
   proactiveRebalanceInfo: _typing.Optional[ProactiveRebalanceInfo] = None
   capacityReservationInfo: _typing.Optional[CapacityReservationInfo] = None


class VsanFileServiceOvfSpec(pyVmomi.vmodl.DynamicData):
   version: _typing.Optional[str] = None
   updateTime: _typing.Optional[_datetime.datetime] = None
   task: _typing.Optional[pyVmomi.vim.Task] = None


class VsanFileServicePreflightCheckResult(pyVmomi.vmodl.DynamicData):
   ovfInstalled: _typing.Optional[str] = None
   fsvmVersion: _typing.Optional[str] = None
   lastUpgradeDate: _typing.Optional[_datetime.datetime] = None
   ovfMixedModeIssue: _typing.Optional[str] = None
   hostVersion: _typing.Optional[str] = None
   mixedModeIssue: _typing.Optional[str] = None
   networkPartitionIssue: _typing.Optional[str] = None
   vsanDatastoreIssue: _typing.Optional[str] = None
   domainConfigIssue: _typing.Optional[str] = None
   fileServiceVersion: _typing.Optional[str] = None
   dvsConfigIssue: _typing.Optional[str] = None
   domainConfigWarning: _typing.Optional[str] = None
   ntpConfigWarning: _typing.Optional[str] = None
   svsConfigIssue: _typing.Optional[str] = None
   nsxConfigIssue: _typing.Optional[str] = None


class VsanFileServiceSystem(pyVmomi.VmomiSupport.ManagedObject):
   def DownloadFileServiceOvf(self, downloadUrl: str) -> pyVmomi.vim.Task: ...
   def QueryFileServiceOvfs(self) -> list[VsanFileServiceOvfSpec]: ...
   def FindOvfDownloadUrl(self, cluster: pyVmomi.vim.ClusterComputeResource) -> str: ...
   def PerformFileServicePreflightCheck(self, cluster: pyVmomi.vim.ClusterComputeResource, domainConfig: _typing.Optional[FileServiceDomainConfig], network: _typing.Optional[pyVmomi.vim.Network], scope: _typing.Optional[str], domainUuid: _typing.Optional[str]) -> VsanFileServicePreflightCheckResult: ...
   def CreateFileServiceDomain(self, domainConfig: FileServiceDomainConfig, cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource]) -> pyVmomi.vim.Task: ...
   def ReconfigureFileServiceDomain(self, domainUuid: str, domainConfig: FileServiceDomainConfig, cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource], deleteDomainConfigFields: list[str]) -> pyVmomi.vim.Task: ...
   def RemoveFileServiceDomain(self, domainUuid: str, cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource]) -> pyVmomi.vim.Task: ...
   def QueryFileServiceDomains(self, querySpec: _typing.Optional[FileServiceDomainQuerySpec], cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource]) -> list[FileServiceDomain]: ...
   def CreateFileShare(self, config: FileShareConfig, cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource]) -> pyVmomi.vim.Task: ...
   def ReconfigureFileShare(self, shareUuid: str, config: FileShareConfig, cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource], deleteLabelKeys: list[str], force: _typing.Optional[bool]) -> pyVmomi.vim.Task: ...
   def RemoveFileShare(self, shareUuid: str, cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource], force: _typing.Optional[bool]) -> pyVmomi.vim.Task: ...
   def QueryFileShares(self, querySpec: FileShareQuerySpec, cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource]) -> _typing.Optional[FileShareQueryResult]: ...
   def UpgradeFsvm(self, cluster: pyVmomi.vim.ClusterComputeResource) -> pyVmomi.vim.Task: ...
   def RebalanceFileService(self, cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource]) -> pyVmomi.vim.Task: ...
   def CreateFileShareSnapshot(self, config: FileShareSnapshotConfig, cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource]) -> pyVmomi.vim.Task: ...
   def RemoveFileShareSnapshot(self, shareUuid: str, snapshotName: str, cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource]) -> pyVmomi.vim.Task: ...
   def QueryFileShareSnapshots(self, querySpec: FileShareSnapshotQuerySpec, cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource]) -> _typing.Optional[FileShareSnapshotQueryResult]: ...


class VsanGenericClusterBaseIssue(pyVmomi.vmodl.DynamicData):
   pass


class VsanGenericClusterBestPracticeHealth(pyVmomi.vmodl.DynamicData):
   drsEnabled: bool
   haEnabled: bool
   issues: list[VsanGenericClusterBaseIssue] = []

class VsanHciMeshConfigLimits:
   pass


class VsanHclDeviceConstraint(pyVmomi.vmodl.DynamicData):
   pciId: str
   vcgLink: _typing.Optional[str] = None
   similarVcgLinks: list[str] = []
   compliantFirmwares: list[VsanCompliantFirmware] = []
   vcgId: _typing.Optional[int] = None
   model: _typing.Optional[str] = None
   partner: _typing.Optional[str] = None
   partNumber: _typing.Optional[str] = None
   release: _typing.Optional[str] = None


class VsanHclDiskConstraint(pyVmomi.vmodl.DynamicData):
   productId: str
   vendor: str
   constraints: list[VsanHclMinFwConstraint] = []
   pcieConstraints: list[VsanHclDeviceConstraint] = []
   partNumber: _typing.Optional[str] = None


class VsanHclDriverInfo(pyVmomi.vmodl.DynamicData):
   driverVersion: _typing.Optional[str] = None
   driverLink: _typing.Optional[VsanDownloadItem] = None
   fwVersion: _typing.Optional[str] = None
   fwLinks: list[VsanDownloadItem] = []
   toolsLinks: list[VsanDownloadItem] = []
   eula: _typing.Optional[str] = None
   driverType: _typing.Optional[str] = None
   driverName: _typing.Optional[str] = None
   diskModes: list[str] = []
   supportedFeatures: list[str] = []


class VsanHclMinFwConstraint(pyVmomi.vmodl.DynamicData):
   vcgId: int
   vcgLink: str
   model: str
   partner: str
   partNumber: _typing.Optional[str] = None
   release: str
   firmware: str


class VsanHclQuerySpec(pyVmomi.vmodl.DynamicData):
   includeOnlyVsanControllers: _typing.Optional[bool] = None
   cluster: _typing.Optional[pyVmomi.vim.ComputeResource] = None
   hosts: list[pyVmomi.vim.HostSystem] = []
   vsanStoragePoolEligibleDisksOnly: _typing.Optional[bool] = None


class VsanHclReleaseConstraint(pyVmomi.vmodl.DynamicData):
   cluster: pyVmomi.vim.ClusterComputeResource
   release: str
   hostDevices: list[VsanHostDeviceInfo] = []
   constraints: list[VsanHclDeviceConstraint] = []


class VsanHealthConfigSpec(pyVmomi.vmodl.DynamicData):
   healthCheckThresholdSpec: list[VsanHealthThreshold] = []
   historicalHealthConfig: _typing.Optional[VsanHistoricalHealthConfig] = None


class VsanHealthCustomizationSpec(pyVmomi.vmodl.DynamicData):
   ssdEnduranceSpec: list[SSDEnduranceThresholdSpec] = []

class VsanHealthPerspective:
   pass

class VsanHealthPerspective90:
   pass

class VsanHealthStatusType:
   pass


class VsanHealthThreshold(pyVmomi.vmodl.DynamicData):
   yellowValue: pyVmomi.VmomiSupport.long
   redValue: pyVmomi.VmomiSupport.long
   target: _typing.Optional[str] = None
   enabled: _typing.Optional[bool] = None

class VsanHealthThresholdTarget:
   pass


class VsanHistoricalHealthConfig(pyVmomi.vmodl.DynamicData):
   enabled: bool


class VsanHostDeviceInfo(pyVmomi.vmodl.DynamicData):
   hostname: str
   devices: list[pyVmomi.vim.host.VsanBasicDeviceInfo] = []


class VsanHostVdsSystem(pyVmomi.VmomiSupport.ManagedObject):
   def VsanMigrateVmsToVds(self, vmConfigSpecs: list[VsanVmVdsMigrationSpec], vdsUuid: str, timeoutSec: pyVmomi.VmomiSupport.long, revert: _typing.Optional[bool]) -> str: ...
   def VsanCompleteMigrateVmsToVds(self, jobId: str, newState: str) -> None: ...


class VsanHwToVcgInfoMappingSpec(pyVmomi.vmodl.DynamicData):
   entity: str
   vsanHwToVcgInfoMappings: list[pyVmomi.vim.host.VsanHwToVcgInfoMapping] = []


class VsanIOTripAnalyzerConfig(pyVmomi.vmodl.DynamicData):
   recurrences: list[VsanIOTripAnalyzerRecurrence] = []


class VsanIOTripAnalyzerRecurrence(pyVmomi.vmodl.DynamicData):
   name: _typing.Optional[str] = None
   targets: list[IODiagnosticsTarget] = []
   startTime: _datetime.datetime
   endTime: _typing.Optional[_datetime.datetime] = None
   duration: pyVmomi.VmomiSupport.long
   interval: pyVmomi.VmomiSupport.long
   status: str

class VsanIOTripAnalyzerRecurrenceStatus:
   pass


class VsanInternalExtendedConfig(pyVmomi.vmodl.DynamicData):
   vcMaxDiskVersion: _typing.Optional[int] = None
   stretchedClient: _typing.Optional[bool] = None


class VsanNetworkConfigBaseIssue(pyVmomi.vmodl.DynamicData):
   pass


class VsanNetworkConfigBestPracticeHealth(pyVmomi.vmodl.DynamicData):
   vdsPresent: bool
   issues: list[VsanNetworkConfigBaseIssue] = []


class VsanNetworkConfigPnicSpeedInconsistencyIssue(VsanNetworkConfigBaseIssue):
   host: pyVmomi.vim.HostSystem
   vswitchName: _typing.Optional[str] = None
   vds: _typing.Optional[pyVmomi.vim.DistributedVirtualSwitch] = None
   speedsMb: list[pyVmomi.VmomiSupport.long] = []


class VsanNetworkConfigPortgroupWithNoRedundancyIssue(VsanNetworkConfigBaseIssue):
   host: pyVmomi.vim.HostSystem
   portgroupName: _typing.Optional[str] = None
   vds: _typing.Optional[pyVmomi.vim.DistributedVirtualSwitch] = None
   pg: _typing.Optional[pyVmomi.vim.Network] = None
   numPnics: pyVmomi.VmomiSupport.long


class VsanNetworkConfigVdsScopeIssue(VsanNetworkConfigBaseIssue):
   vds: pyVmomi.vim.DistributedVirtualSwitch
   memberHosts: list[pyVmomi.vim.HostSystem] = []
   nonMemberHosts: list[pyVmomi.vim.HostSystem] = []


class VsanNetworkConfigVsanNotOnVdsIssue(VsanNetworkConfigBaseIssue):
   host: pyVmomi.vim.HostSystem
   vmknic: str


class VsanNetworkConfigVswitchWithNoRedundancyIssue(VsanNetworkConfigBaseIssue):
   host: pyVmomi.vim.HostSystem
   vswitchName: _typing.Optional[str] = None
   vds: _typing.Optional[pyVmomi.vim.DistributedVirtualSwitch] = None
   numPnics: pyVmomi.VmomiSupport.long


class VsanNetworkVMotionVmknicNotFountIssue(VsanNetworkConfigBaseIssue):
   hostWithoutVmotionVmknic: pyVmomi.vim.HostSystem


class VsanObjSnapParams(pyVmomi.vmodl.DynamicData):
   uuid: str
   creator: _typing.Optional[str] = None
   snapshotType: _typing.Optional[str] = None
   cookie: _typing.Optional[str] = None
   immutableTag: _typing.Optional[str] = None


class VsanObjectDetail(pyVmomi.vmodl.DynamicData):
   uuid: str
   objectPath: _typing.Optional[str] = None
   snapshots: list[VsanSnapshotDetail] = []


class VsanObjectManager(pyVmomi.VmomiSupport.ManagedObject):
   pass


class VsanObjectSnapshotId(pyVmomi.vmodl.DynamicData):
   uuid: str
   snapshotId: int
   cookie: _typing.Optional[str] = None


class VsanPMemConfig(pyVmomi.vmodl.DynamicData):
   enabled: bool


class VsanPerfsvcHealthResult(pyVmomi.vmodl.DynamicData):
   statsObjectInfo: _typing.Optional[pyVmomi.vim.cluster.VsanObjectInformation] = None
   statsObjectConsistent: _typing.Optional[bool] = None
   statsObjectPolicyConsistent: _typing.Optional[bool] = None
   datastoreCompatible: _typing.Optional[bool] = None
   enoughFreeSpace: _typing.Optional[bool] = None
   remediateAction: _typing.Optional[str] = None
   hostResults: list[pyVmomi.vim.cluster.VsanPerfNodeInformation] = []
   verboseModeStatus: _typing.Optional[bool] = None


class VsanPolicyManager(pyVmomi.VmomiSupport.ManagedObject):
   pass

class VsanPolicyRegulationCheckOpEnum:
   pass


class VsanPrepareVsanForVcsaSpec(pyVmomi.vmodl.DynamicData):
   vsanDiskMappingCreationSpec: _typing.Optional[pyVmomi.vim.vsan.host.DiskMappingCreationSpec] = None
   vsanDataEfficiencyConfig: _typing.Optional[DataEfficiencyConfig] = None
   taskId: _typing.Optional[str] = None
   vsanDataEncryptionConfig: _typing.Optional[pyVmomi.vim.vsan.host.EncryptionInfo] = None
   vsanAddStoragePoolDiskSpec: _typing.Optional[pyVmomi.vim.vsan.host.AddStoragePoolDiskSpec] = None
   createNativeKeyProviderSpec: _typing.Optional[pyVmomi.vim.vsan.host.CreateNativeKeyProviderSpec] = None


class VsanResourceCheckSystem(pyVmomi.VmomiSupport.ManagedObject):
   def PerformResourceCheck(self, resourceCheckSpec: ResourceCheckSpec, cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource]) -> pyVmomi.vim.Task: ...
   def GetResourceCheckStatus(self, resourceCheckSpec: _typing.Optional[ResourceCheckSpec], cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource]) -> ResourceCheckStatus: ...
   def PerformResourceCheckOnHost(self, resourceCheckSpec: ResourceCheckSpec) -> pyVmomi.vim.Task: ...
   def CancelResourceCheckOnHost(self) -> bool: ...

class VsanServiceStatus:
   pass

class VsanSiteLocationType:
   pass


class VsanSiteMaintenanceSystem(pyVmomi.VmomiSupport.ManagedObject):
   def EnterSiteMaintenanceMode(self, faultDomainName: str, cluster: pyVmomi.vim.ClusterComputeResource) -> pyVmomi.vim.Task: ...
   def ExitSiteMaintenanceMode(self, faultDomainName: str, cluster: pyVmomi.vim.ClusterComputeResource) -> pyVmomi.vim.Task: ...
   def PerformSiteMaintenancePrecheck(self, cluster: pyVmomi.vim.ClusterComputeResource, spec: SiteMaintenanceSpec) -> pyVmomi.vim.Task: ...
   def GetSiteMaintenancePrecheckStatus(self, cluster: pyVmomi.vim.ClusterComputeResource, faultDomainName: str) -> SiteMaintenancePrecheckStatus: ...
   def QueryClusterSiteMaintenanceState(self, cluster: pyVmomi.vim.ClusterComputeResource) -> list[SiteMaintenanceInfo]: ...

class VsanSnapHealthType:
   pass

class VsanSnapStatsExpirationType:
   pass

class VsanSnapVmMembershipChangeStatus:
   pass


class VsanSnapshotDetail(pyVmomi.vmodl.DynamicData):
   snapshotId: int
   snapshotType: str
   snapshotPath: _typing.Optional[str] = None
   snapshotTagsInfo: list[pyVmomi.vim.KeyValue] = []


class VsanSnapshotQueryResult(pyVmomi.vmodl.DynamicData):
   objects: list[VsanObjectDetail] = []


class VsanSnapshotQuerySpec(pyVmomi.vmodl.DynamicData):
   datastoreUuid: str
   objectUuids: list[str] = []
   snapshotType: _typing.Optional[str] = None
   creator: _typing.Optional[str] = None
   includeDescriptorPath: _typing.Optional[bool] = None
   snapshotTagMask: _typing.Optional[int] = None


class VsanSpaceEfficiencyMetadataSize(pyVmomi.vmodl.DynamicData):
   dedupMetadataSize: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   compressionMetadataSize: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class VsanSpaceEfficiencyRatio(pyVmomi.vmodl.DynamicData):
   overallRatio: _typing.Optional[float] = None
   compressionRatio: _typing.Optional[float] = None
   dedupRatio: _typing.Optional[float] = None
   dedupEnabledRatio: _typing.Optional[float] = None
   thinProvisionRatio: _typing.Optional[float] = None
   snapshotSavingRatio: _typing.Optional[float] = None

class VsanSyncReason:
   pass

class VsanSyncStatus:
   pass


class VsanUnmapConfig(pyVmomi.vmodl.DynamicData):
   enable: bool


class VsanUpdateItem(pyVmomi.vmodl.DynamicData):
   host: pyVmomi.vim.HostSystem
   type: str
   name: str
   version: str
   existingVersion: _typing.Optional[str] = None
   present: bool
   vibSpec: list[VsanVibSpec] = []
   vibType: _typing.Optional[str] = None
   firmwareSpec: _typing.Optional[pyVmomi.vim.host.VsanHclFirmwareUpdateSpec] = None
   downloadInfo: list[VsanDownloadItem] = []
   eula: _typing.Optional[str] = None
   adapter: _typing.Optional[str] = None
   key: _typing.Optional[str] = None
   impact: _typing.Optional[str] = None
   firmwareUnknown: _typing.Optional[bool] = None

class VsanUpdateItemImpactType:
   pass

class VsanUpdateItemType:
   pass


class VsanValidationItem(pyVmomi.vim.ClusterComputeResource.ValidationResultBase):
   pass


class VsanVcPostDeployConfigSpec(pyVmomi.vmodl.DynamicData):
   dcName: _typing.Optional[str] = None
   clusterName: _typing.Optional[str] = None
   firstHost: _typing.Optional[pyVmomi.vim.host.ConnectSpec] = None
   hostsToAdd: list[pyVmomi.vim.host.ConnectSpec] = []
   vsanDataEfficiencyConfig: _typing.Optional[DataEfficiencyConfig] = None
   vsanLicenseKey: _typing.Optional[str] = None
   hostLicenseKey: _typing.Optional[str] = None
   taskId: _typing.Optional[str] = None
   vsanDataEncryptionConfig: _typing.Optional[pyVmomi.vim.vsan.host.EncryptionInfo] = None
   createNativeKeyProviderSpec: _typing.Optional[pyVmomi.vim.vsan.host.CreateNativeKeyProviderSpec] = None
   vsanClusterMode: _typing.Optional[str] = None
   deconvergedNetConfig: _typing.Optional[VsanDeconvergedNetConfig] = None


class VsanVcStretchedClusterConfigSpec(pyVmomi.vmodl.DynamicData):
   witnessHost: pyVmomi.vim.HostSystem
   clusters: list[pyVmomi.vim.cluster.VsanStretchedClusterConfig] = []
   witnessDiskMappings: list[pyVmomi.vim.vsan.host.DiskMapping] = []
   witnessStoragePoolSpecs: list[pyVmomi.vim.vsan.host.AddStoragePoolDiskSpec] = []

class VsanVcsaDeploymentPhase:
   pass


class VsanVcsaDeploymentProgress(pyVmomi.vmodl.DynamicData):
   phase: str
   progressPct: pyVmomi.VmomiSupport.long
   message: str
   success: bool
   error: _typing.Optional[pyVmomi.vmodl.MethodFault] = None
   updateCounter: pyVmomi.VmomiSupport.long
   taskId: _typing.Optional[str] = None
   vm: _typing.Optional[pyVmomi.vim.VirtualMachine] = None


class VsanVdsMigrationPlan(pyVmomi.vmodl.DynamicData):
   vdsSpec: pyVmomi.vim.DistributedVirtualSwitch.CreateSpec
   pgs: list[VsanVdsPgMigrationSpec] = []
   inaccessibleVms: list[pyVmomi.vim.VirtualMachine] = []
   infraVms: list[pyVmomi.vim.VirtualMachine] = []


class VsanVdsPgMigrationHostInfo(pyVmomi.vmodl.DynamicData):
   host: pyVmomi.vim.HostSystem
   hostname: str
   vmknicDevices: list[str] = []
   vmVnics: list[VsanVdsPgMigrationVmInfo] = []


class VsanVdsPgMigrationSpec(pyVmomi.vmodl.DynamicData):
   vssPgName: str
   dvPgName: str
   vdsPgSetting: pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch.VmwarePortConfigPolicy
   vdsPgType: str
   hosts: list[VsanVdsPgMigrationHostInfo] = []
   collisionRename: bool


class VsanVdsPgMigrationVmInfo(pyVmomi.vmodl.DynamicData):
   vm: pyVmomi.vim.VirtualMachine
   vnicLabel: list[str] = []


class VsanVdsSystem(pyVmomi.VmomiSupport.ManagedObject):
   def VsanVdsGetMigrationPlan(self, cluster: pyVmomi.vim.ComputeResource, vswitchName: _typing.Optional[str], vdsName: _typing.Optional[str], vmnicDevices: list[str], infraVm: list[pyVmomi.vim.VirtualMachine], vds: _typing.Optional[pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch], hosts: list[pyVmomi.vim.HostSystem]) -> VsanVdsMigrationPlan: ...
   def VsanVdsMigrateVss(self, cluster: pyVmomi.vim.ComputeResource, migrationPlan: _typing.Optional[VsanVdsMigrationPlan], vswitchName: _typing.Optional[str], vdsName: _typing.Optional[str], vmnicDevices: list[str], infraVm: list[pyVmomi.vim.VirtualMachine], vds: _typing.Optional[pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch], hosts: list[pyVmomi.vim.HostSystem]) -> pyVmomi.vim.Task: ...
   def VsanVssMigrateVds(self, cluster: _typing.Optional[pyVmomi.vim.ComputeResource], hosts: list[pyVmomi.vim.HostSystem], vds: pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch, vswitchName: _typing.Optional[str], vmnicDevices: list[str], infraVm: list[pyVmomi.vim.VirtualMachine]) -> pyVmomi.vim.Task: ...
   def RollbackVdsToVss(self, task: pyVmomi.vim.Task) -> bool: ...


class VsanVibInstallPreflightStatus(pyVmomi.vmodl.DynamicData):
   manualVmotionRequired: bool
   rollingRequired: bool


class VsanVibScanResult(pyVmomi.vmodl.DynamicData):
   host: pyVmomi.vim.HostSystem
   vibName: str
   vibVersion: str
   existingVersion: _typing.Optional[str] = None
   maintenanceModeRequired: bool
   rebootRequired: bool
   meetsSystemReq: bool
   pkgDepsMetByHost: bool


class VsanVibSpec(pyVmomi.vmodl.DynamicData):
   host: pyVmomi.vim.HostSystem
   metaUrl: _typing.Optional[str] = None
   metaSha1Sum: _typing.Optional[str] = None
   vibUrl: str
   vibSha1Sum: str

class VsanVibType:
   pass


class VsanVmVdsMigrationSpec(pyVmomi.vmodl.DynamicData):
   vmInstanceUuid: str
   vnics: list[VsanVnicVdsMigrationSpec] = []


class VsanVnicVdsMigrationSpec(pyVmomi.vmodl.DynamicData):
   key: int
   vdsBacking: pyVmomi.vim.vm.device.VirtualDevice.BackingInfo


class VsanVumConfig(pyVmomi.vmodl.DynamicData):
   baselinePreferenceType: str


class WitnessHostConfig(pyVmomi.vmodl.DynamicData):
   subClusterUuid: str
   preferredFaultDomainName: str
   metadataMode: _typing.Optional[bool] = None


class XVCClientInfo(pyVmomi.vmodl.DynamicData):
   cluster: pyVmomi.vim.ClusterComputeResource
   clusterName: str
   vsanFormatVersion: str
   ownerVc: str
   vcUuid: _typing.Optional[str] = None
   clusterUuid: _typing.Optional[str] = None


class XVCDatastoreConfig(pyVmomi.vmodl.DynamicData):
   xvcDatastores: list[XVCDatastoreInfo] = []


class XVCDatastoreInfo(pyVmomi.vmodl.DynamicData):
   datastore: pyVmomi.vim.Datastore
   ownerVc: str


class XvcClientConfig(DatastoreSpec):
   xvcClusters: list[XVCClientInfo] = []


class XvcClientInfoSpec(pyVmomi.vmodl.DynamicData):
   clientVc: str
   vcUuid: _typing.Optional[str] = None
   vcVersion: _typing.Optional[str] = None
   cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource] = None
   clusterName: _typing.Optional[str] = None
   clusterUuid: _typing.Optional[str] = None
   vsanFormatVersion: _typing.Optional[str] = None
   minVsanFormatVersion: _typing.Optional[str] = None
   datastore: list[pyVmomi.vim.Datastore] = []
   unicastInfo: _typing.Optional[pyVmomi.vim.vsan.host.ClientClusterUnicastInfo] = None
   saGeneration: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class XvcQueryCriteria(pyVmomi.vmodl.DynamicData):
   property: str
   operator: _typing.Optional[str] = None
   comparableValue: _typing.Optional[object] = None
   comparableList: _typing.Optional[pyVmomi.vmodl.DynamicArray] = None
   ignoreCase: _typing.Optional[bool] = None

class XvcQueryCriteriaOperator:
   pass


class XvcQueryFilter(pyVmomi.vmodl.DynamicData):
   criterias: list[XvcQueryCriteria] = []
   operator: _typing.Optional[str] = None

class XvcQueryFilterOperator:
   pass


class XvcQueryPropertyValue(pyVmomi.vmodl.DynamicData):
   value: _typing.Optional[object] = None


class XvcQueryResultSet(pyVmomi.vmodl.DynamicData):
   properties: list[str] = []
   resultItems: list[XvcResultItem] = []
   totalCount: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class XvcQuerySpec(pyVmomi.vmodl.DynamicData):
   objectModel: _typing.Optional[str] = None
   properties: list[str] = []
   filter: _typing.Optional[XvcQueryFilter] = None
   offset: _typing.Optional[int] = None
   limit: _typing.Optional[int] = None
   returnTotalCount: _typing.Optional[bool] = None


class XvcResultItem(pyVmomi.vmodl.DynamicData):
   propertyValues: list[XvcQueryPropertyValue] = []

class clusterPowerState:
   pass
