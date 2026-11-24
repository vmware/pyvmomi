# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import datetime as _datetime
import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vim
import pyVmomi.vmodl
import pyVmomi.vim.cluster
import pyVmomi.vim.encryption
import pyVmomi.vim.host
import pyVmomi.vim.vm
import pyVmomi.vim.vsan



class AbortWipeDiskStatus(pyVmomi.vmodl.DynamicData):
   disk: str
   success: bool
   reason: list[pyVmomi.vmodl.LocalizableMessage] = []


class AboutInfoEx(pyVmomi.vmodl.DynamicData):
   name: _typing.Optional[str] = None
   version: _typing.Optional[str] = None
   build: _typing.Optional[str] = None
   buildType: _typing.Optional[str] = None
   apiVersion: _typing.Optional[str] = None


class AddStoragePoolDiskSpec(pyVmomi.vmodl.DynamicData):
   host: pyVmomi.vim.HostSystem
   disks: list[StoragePoolDisk] = []


class ClientClusterUnicastConfig(pyVmomi.vmodl.DynamicData):
   remoteUnicastConfig: list[ClientClusterUnicastInfo] = []


class ClientClusterUnicastInfo(pyVmomi.vmodl.DynamicData):
   clusterUuid: str
   unicastInfo: list[ClientHostUnicastInfo] = []


class ClientHostUnicastInfo(pyVmomi.vmodl.DynamicData):
   hostUuid: str
   unicastSpec: list[pyVmomi.vim.cluster.VsanUnicastAddressInfo] = []
   thumbprintList: list[pyVmomi.vim.vm.CertThumbprint] = []


class ClusterStatus(pyVmomi.vmodl.DynamicData):
   class State(pyVmomi.vmodl.DynamicData):
      class CompletionEstimate(pyVmomi.vmodl.DynamicData):
         completeTime: _typing.Optional[_datetime.datetime] = None
         percentComplete: _typing.Optional[int] = None

      state: str
      completion: _typing.Optional[CompletionEstimate] = None

   uuid: _typing.Optional[str] = None
   nodeUuid: _typing.Optional[str] = None
   health: str
   nodeState: State
   memberUuid: list[str] = []


class ComplianceDetail(pyVmomi.vmodl.DynamicData):
   objectUUID: str
   complianceStatus: str
   objectHealth: int
   violatedPolicies: list[PolicyStatus] = []


class ComplianceResult(pyVmomi.vmodl.DynamicData):
   checkTime: _datetime.datetime
   policyId: _typing.Optional[str] = None
   policyGen: _typing.Optional[int] = None
   objComplianceDetail: list[ComplianceDetail] = []

class ComplianceStatus:
   pass


class ConfigInfo(pyVmomi.vmodl.DynamicData):
   class StorageInfo(pyVmomi.vmodl.DynamicData):
      autoClaimStorage: _typing.Optional[bool] = None
      diskMapping: list[DiskMapping] = []
      diskMapInfo: list[DiskMapInfo] = []
      checksumEnabled: _typing.Optional[bool] = None

   class ClusterInfo(pyVmomi.vmodl.DynamicData):
      uuid: _typing.Optional[str] = None
      nodeUuid: _typing.Optional[str] = None

   class NetworkInfo(pyVmomi.vmodl.DynamicData):
      class PortConfig(pyVmomi.vmodl.DynamicData):
         ipConfig: _typing.Optional[IpConfig] = None
         device: str

      port: list[PortConfig] = []

   class FaultDomainInfo(pyVmomi.vmodl.DynamicData):
      name: str

   enabled: _typing.Optional[bool] = None
   hostSystem: _typing.Optional[pyVmomi.vim.HostSystem] = None
   clusterInfo: _typing.Optional[ClusterInfo] = None
   storageInfo: _typing.Optional[StorageInfo] = None
   networkInfo: _typing.Optional[NetworkInfo] = None
   faultDomainInfo: _typing.Optional[FaultDomainInfo] = None
   vsanEsaEnabled: _typing.Optional[bool] = None
   vsanCyberRecoveryEnabled: _typing.Optional[bool] = None


class ConfigInfoEx(ConfigInfo):
   encryptionInfo: _typing.Optional[EncryptionInfo] = None
   dataEfficiencyInfo: _typing.Optional[pyVmomi.vim.vsan.DataEfficiencyConfig] = None
   resyncIopsLimitInfo: _typing.Optional[pyVmomi.vim.vsan.ResyncIopsInfo] = None
   extendedConfig: _typing.Optional[pyVmomi.vim.vsan.VsanExtendedConfig] = None
   datastoreInfo: _typing.Optional[pyVmomi.vim.vsan.DatastoreConfig] = None
   unmapConfig: _typing.Optional[pyVmomi.vim.vsan.VsanUnmapConfig] = None
   witnessHostConfig: list[pyVmomi.vim.vsan.WitnessHostConfig] = []
   internalExtendedConfig: _typing.Optional[pyVmomi.vim.vsan.VsanInternalExtendedConfig] = None
   metricsConfig: _typing.Optional[pyVmomi.vim.vsan.MetricsConfig] = None
   unicastConfig: _typing.Optional[ServerClusterUnicastConfig] = None
   rdmaConfig: _typing.Optional[pyVmomi.vim.vsan.RdmaConfig] = None
   dataInTransitEncryptionInfo: _typing.Optional[DataInTransitEncryptionInfo] = None
   mode: _typing.Optional[str] = None
   serverClusterConfigs: list[RemoteVsanServerClusterConfig] = []
   snapServiceConfig: _typing.Optional[pyVmomi.vim.vsan.SnapServiceConfig] = None
   deconvergedNetConfig: _typing.Optional[pyVmomi.vim.vsan.VsanDeconvergedNetConfig] = None
   remoteDITInfos: list[DataInTransitEncryptionInfo] = []
   clientUnicastConfig: _typing.Optional[ClientClusterUnicastConfig] = None
   siteTakeoverConfig: _typing.Optional[SiteTakeoverConfig] = None
   vbossHostConfig: _typing.Optional[VbossHostConfig] = None
   autoRAIDConfig: _typing.Optional[pyVmomi.vim.vsan.AutoRAIDConfig] = None


class CreateNativeKeyProviderSpec(pyVmomi.vmodl.DynamicData):
   provider: str
   keyId: _typing.Optional[str] = None
   keyDerivationKey: _typing.Optional[str] = None
   tpmRequired: _typing.Optional[bool] = None


class DataInTransitEncryptionInfo(pyVmomi.vmodl.DynamicData):
   enabled: _typing.Optional[bool] = None
   rekeyInterval: _typing.Optional[int] = None
   transitionState: _typing.Optional[str] = None
   serverClusterUuid: _typing.Optional[str] = None
   clientClusterUuid: _typing.Optional[str] = None


class DecommissionMode(pyVmomi.vmodl.DynamicData):
   class ObjectAction(pyVmomi.VmomiSupport.Enum):
      noAction: _typing.ClassVar['ObjectAction'] = 'noAction'
      ensureObjectAccessibility: _typing.ClassVar['ObjectAction'] = 'ensureObjectAccessibility'
      evacuateAllData: _typing.ClassVar['ObjectAction'] = 'evacuateAllData'

   objectAction: str


class DeleteStoragePoolDiskSpec(pyVmomi.vmodl.DynamicData):
   diskUuids: list[str] = []
   maintenanceSpec: pyVmomi.vim.host.MaintenanceSpec


class DiskMapInfo(pyVmomi.vmodl.DynamicData):
   mapping: DiskMapping
   mounted: bool


class DiskMapInfoEx(pyVmomi.vmodl.DynamicData):
   mapping: DiskMapping
   isMounted: bool
   unlockedEncrypted: _typing.Optional[bool] = None
   isAllFlash: bool
   isDataEfficiency: _typing.Optional[bool] = None
   encryptionInfo: _typing.Optional[pyVmomi.vim.vsan.DataEncryptionConfig] = None
   dataEfficiencyConfig: _typing.Optional[pyVmomi.vim.vsan.DataEfficiencyConfig] = None
   diskgroupCapability: list[str] = []


class DiskMapResult(pyVmomi.vmodl.DynamicData):
   mapping: DiskMapping
   diskResult: list[DiskResult] = []
   error: _typing.Optional[pyVmomi.vmodl.MethodFault] = None


class DiskMapping(pyVmomi.vmodl.DynamicData):
   ssd: pyVmomi.vim.host.ScsiDisk
   nonSsd: list[pyVmomi.vim.host.ScsiDisk] = []


class DiskMappingCreationSpec(pyVmomi.vmodl.DynamicData):
   class DiskMappingCreationType(pyVmomi.VmomiSupport.Enum):
      hybrid: _typing.ClassVar['DiskMappingCreationType'] = 'hybrid'
      allFlash: _typing.ClassVar['DiskMappingCreationType'] = 'allFlash'
      vsandirect: _typing.ClassVar['DiskMappingCreationType'] = 'vsandirect'
      pmem: _typing.ClassVar['DiskMappingCreationType'] = 'pmem'
      DiskMappingCreationType_Unknown: _typing.ClassVar['DiskMappingCreationType'] = 'DiskMappingCreationType_Unknown'

   host: pyVmomi.vim.HostSystem
   cacheDisks: list[pyVmomi.vim.host.ScsiDisk] = []
   capacityDisks: list[pyVmomi.vim.host.ScsiDisk] = []
   creationType: str


class DiskResult(pyVmomi.vmodl.DynamicData):
   class State(pyVmomi.VmomiSupport.Enum):
      inUse: _typing.ClassVar['State'] = 'inUse'
      eligible: _typing.ClassVar['State'] = 'eligible'
      ineligible: _typing.ClassVar['State'] = 'ineligible'

   disk: pyVmomi.vim.host.ScsiDisk
   state: str
   vsanUuid: _typing.Optional[str] = None
   error: _typing.Optional[pyVmomi.vmodl.MethodFault] = None
   degraded: _typing.Optional[bool] = None


class DiskResultEx(DiskResult):
   vsanDirectTagged: bool
   storagePoolDiskState: _typing.Optional[str] = None
   storagePoolDiskError: _typing.Optional[pyVmomi.vmodl.MethodFault] = None
   isCapacityFlash: _typing.Optional[bool] = None


class DrsStats(pyVmomi.vmodl.DynamicData):
   host: pyVmomi.vim.HostSystem
   stats: pyVmomi.VmomiSupport.binary
   readLocalityPresented: _typing.Optional[bool] = None


class EncryptionInfo(pyVmomi.vmodl.DynamicData):
   enabled: _typing.Optional[bool] = None
   kekId: _typing.Optional[str] = None
   hostKeyId: _typing.Optional[str] = None
   kmipServers: list[pyVmomi.vim.encryption.KmipServerSpec] = []
   kmsServerCerts: list[str] = []
   clientKey: _typing.Optional[str] = None
   clientCert: _typing.Optional[str] = None
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

class EncryptionOperation:
   pass

class EncryptionTransitionState:
   pass

class HealthState:
   pass


class IpConfig(pyVmomi.vmodl.DynamicData):
   upstreamIpAddress: str
   downstreamIpAddress: str


class IpConfigEx(IpConfig):
   upstreamIpV6Address: _typing.Optional[str] = None
   downstreamIpV6Address: _typing.Optional[str] = None


class MembershipInfo(pyVmomi.vmodl.DynamicData):
   nodeUuid: str
   hostname: str

class NodeState:
   pass


class PolicyStatus(pyVmomi.vmodl.DynamicData):
   id: str
   expectedValue: str
   currentValue: str


class PortConfigEx(ConfigInfo.NetworkInfo.PortConfig):
   class TrafficType(pyVmomi.VmomiSupport.Enum):
      vsan: _typing.ClassVar['TrafficType'] = 'vsan'
      witness: _typing.ClassVar['TrafficType'] = 'witness'
      TrafficType_Unknown: _typing.ClassVar['TrafficType'] = 'TrafficType_Unknown'

   class TrafficType90(pyVmomi.VmomiSupport.Enum):
      vsanExternal: _typing.ClassVar['TrafficType90'] = 'vsanExternal'

   trafficTypes: list[str] = []


class QueryVsanDisksSpec(pyVmomi.vmodl.DynamicData):
   diskName: _typing.Optional[str] = None
   vsanDiskType: _typing.Optional[str] = None


class RemoteVsanServerClusterConfig(pyVmomi.vmodl.DynamicData):
   clusterUuid: str
   siteAffinity: _typing.Optional[SiteAffinityInfo] = None


class RuntimeStats(pyVmomi.vmodl.DynamicData):
   resyncIopsInfo: _typing.Optional[pyVmomi.vim.vsan.ResyncIopsInfo] = None
   configGeneration: _typing.Optional[pyVmomi.vim.cluster.VsanConfigGeneration] = None
   supportedClusterSize: _typing.Optional[int] = None
   repairTimerInfo: _typing.Optional[pyVmomi.vim.vsan.RepairTimerInfo] = None
   componentLimitPerCluster: _typing.Optional[int] = None
   maxWitnessClusters: _typing.Optional[int] = None


class ServerClusterUnicastConfig(pyVmomi.vmodl.DynamicData):
   remoteUnicastConfig: list[ServerClusterUnicastInfo] = []


class ServerClusterUnicastInfo(pyVmomi.vmodl.DynamicData):
   clusterUuid: str
   unicastInfo: list[pyVmomi.vim.vsan.ServerHostUnicastInfo] = []

class ServerNodeType:
   pass


class SiteAffinityInfo(pyVmomi.vmodl.DynamicData):
   name: str
   siteId: _typing.Optional[str] = None


class SiteTakeoverConfig(pyVmomi.vmodl.DynamicData):
   takeoverTimestamp: _typing.Optional[pyVmomi.VmomiSupport.long] = None

class StatsType:
   pass


class StoragePoolDisk(pyVmomi.vmodl.DynamicData):
   diskName: str
   diskType: str


class StoragePoolDiskInfo(pyVmomi.vmodl.DynamicData):
   disk: pyVmomi.vim.host.ScsiDisk
   vsanUuid: _typing.Optional[str] = None
   error: _typing.Optional[pyVmomi.vmodl.MethodFault] = None
   isMounted: _typing.Optional[bool] = None
   isEncrypted: _typing.Optional[bool] = None
   dekId: _typing.Optional[str] = None
   diskType: _typing.Optional[str] = None

class StoragePoolDiskType:
   pass


class StoragePoolInfo(pyVmomi.vmodl.DynamicData):
   storagePoolDisks: list[StoragePoolDiskInfo] = []


class TrimDiskEntry(pyVmomi.vmodl.DynamicData):
   diskName: str
   diskType: _typing.Optional[str] = None


class TrimDiskSpec(pyVmomi.vmodl.DynamicData):
   disks: list[TrimDiskEntry] = []

class TrimDiskType:
   pass


class UpdateStoragePoolDiskSpec(pyVmomi.vmodl.DynamicData):
   diskUuids: list[str] = []
   diskFormatVersion: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class VbossHostConfig(pyVmomi.vim.vsan.VbossConfig):
   pass


class VsanAssociatedObjects(pyVmomi.vmodl.DynamicData):
   spbmProfileId: str
   spbmProfileGenerationNum: int
   vsanObjects: list[str] = []


class VsanAssociatedObjectsResult(pyVmomi.vmodl.DynamicData):
   data: list[VsanAssociatedObjects] = []
   offset: int
   limit: int


class VsanComplianceQuerySpec(pyVmomi.vmodl.DynamicData):
   uuids: list[str] = []
   spbmProfileId: _typing.Optional[str] = None
   spbmProfileGenerationId: _typing.Optional[int] = None


class VsanComponentSyncState(pyVmomi.vmodl.DynamicData):
   uuid: str
   diskUuid: str
   hostUuid: str
   bytesToSync: pyVmomi.VmomiSupport.long
   recoveryETA: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   reasons: list[str] = []


class VsanDirectStorage(pyVmomi.vmodl.DynamicData):
   scsiDisks: list[VsanScsiDisk] = []
   tier: _typing.Optional[str] = None

class VsanDiskEvacReason:
   pass


class VsanDiskInfo(pyVmomi.vmodl.DynamicData):
   vsanUuid: str
   formatVersion: int


class VsanDiskManagementSystemCapability(pyVmomi.vmodl.DynamicData):
   version: str

class VsanDiskTrimOption:
   pass

class VsanDiskType:
   pass

class VsanDiskgroupCapability:
   pass


class VsanHostCapability(pyVmomi.vmodl.DynamicData):
   host: pyVmomi.vim.HostSystem
   isSupported: bool
   isLicensed: bool


class VsanManagedDisksInfo(pyVmomi.vmodl.DynamicData):
   vSANDirectDisks: list[VsanDirectStorage] = []
   vSANDiskMapInfo: list[DiskMapInfoEx] = []
   vSANPMemInfo: _typing.Optional[VsanManagedPMemInfo] = None
   storagePools: list[StoragePoolInfo] = []


class VsanManagedPMemInfo(pyVmomi.vmodl.DynamicData):
   localPMemDatastores: list[pyVmomi.vim.Datastore] = []


class VsanObjectProfileInfo(pyVmomi.vmodl.DynamicData):
   vsanObjectUuid: str
   spbmProfileId: str
   spbmProfileGenerationNum: int


class VsanObjectSyncState(pyVmomi.vmodl.DynamicData):
   uuid: str
   components: list[VsanComponentSyncState] = []


class VsanRuntimeInfo(pyVmomi.vmodl.DynamicData):
   class DiskIssueType(pyVmomi.VmomiSupport.Enum):
      nonExist: _typing.ClassVar['DiskIssueType'] = 'nonExist'
      stampMismatch: _typing.ClassVar['DiskIssueType'] = 'stampMismatch'
      unknown: _typing.ClassVar['DiskIssueType'] = 'unknown'

   class DiskIssue(pyVmomi.vmodl.DynamicData):
      diskId: str
      issue: str

   membershipList: list[MembershipInfo] = []
   diskIssues: list[DiskIssue] = []
   accessGenNo: _typing.Optional[int] = None


class VsanScsiDisk(pyVmomi.vmodl.DynamicData):
   capacity: pyVmomi.vim.host.DiskDimensions.Lba
   usedCapacity: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   devicePath: str
   ssd: _typing.Optional[bool] = None
   localDisk: _typing.Optional[bool] = None
   scsiDiskType: _typing.Optional[str] = None
   uuid: str
   operationalState: list[str] = []
   canonicalName: _typing.Optional[str] = None
   displayName: _typing.Optional[str] = None
   lunType: str
   vendor: _typing.Optional[str] = None
   model: _typing.Optional[str] = None
   mountInfo: _typing.Optional[pyVmomi.vim.host.MountInfo] = None


class VsanSyncingObjectQueryResult(pyVmomi.vmodl.DynamicData):
   totalObjectsToSync: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   totalBytesToSync: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   totalRecoveryETA: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   objects: list[VsanObjectSyncState] = []
   syncingObjectRecoveryDetails: _typing.Optional[VsanSyncingObjectRecoveryDetails] = None


class VsanSyncingObjectRecoveryDetails(pyVmomi.vmodl.DynamicData):
   activelySyncingObjectRecoveryETA: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   queuedForSyncObjectRecoveryETA: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   suspendedObjectRecoveryETA: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   activeObjectsToSync: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   queuedObjectsToSync: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   suspendedObjectsToSync: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   bytesToSyncForActiveObjects: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   bytesToSyncForQueuedObjects: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   bytesToSyncForSuspendedObjects: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class VsanWhatIfEvacDetail(pyVmomi.vmodl.DynamicData):
   success: _typing.Optional[bool] = None
   bytesToSync: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   inaccessibleObjects: list[str] = []
   incompliantObjects: list[str] = []
   extraSpaceNeeded: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   failedDueToInaccessibleObjects: _typing.Optional[bool] = None


class VsanWhatIfEvacResult(pyVmomi.vmodl.DynamicData):
   noAction: VsanWhatIfEvacDetail
   ensureAccess: VsanWhatIfEvacDetail
   evacAllData: VsanWhatIfEvacDetail

class WipeDiskEligible:
   pass

class WipeDiskState:
   pass


class WipeDiskStatus(pyVmomi.vmodl.DynamicData):
   disk: str
   eligible: str
   ineligibleReason: list[pyVmomi.vmodl.LocalizableMessage] = []
   wipeState: _typing.Optional[str] = None
   percentageCompleted: _typing.Optional[int] = None
   estimatedTime: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   wipeStartTime: _typing.Optional[_datetime.datetime] = None
   wipeCompleteTime: _typing.Optional[_datetime.datetime] = None
