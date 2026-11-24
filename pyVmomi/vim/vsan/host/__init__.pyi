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
   """
   Abort wipe disk status.
   
   Attributes:
       disk: Disk canonical name to abort.
       success: Disk wipe abort success or not.
       reason: Disk wipe abort failure reason.
           
           This property is used when failing to abort wipe on disk.
           Includes following reasons:
           Disk wipe is not in progress,
           or the disk doesn't support abort sanitize,
           or abort sanitize fails internally.
   """
   disk: str
   success: bool
   reason: list[pyVmomi.vmodl.LocalizableMessage] = []


class AboutInfoEx(pyVmomi.vmodl.DynamicData):
   """
   This data object type describes system information including the name,
   version, build type and build number.
   
   Attributes:
       name: Represents name of current product.
       version: Represents version of current product.
       build: Represents build number of current product.
       buildType: Represents build type of current product.
       apiVersion: Represents management API version for vSAN.
   """
   name: _typing.Optional[str] = None
   version: _typing.Optional[str] = None
   build: _typing.Optional[str] = None
   buildType: _typing.Optional[str] = None
   apiVersion: _typing.Optional[str] = None


class AddStoragePoolDiskSpec(pyVmomi.vmodl.DynamicData):
   """
   Specification to create/add disks to the storage pool in the vSAN host.
   
   Attributes:
       host: Target host to which the disks need to be added to.
       disks: Storage pool disk properties like diskName, diskType.
   """
   host: pyVmomi.vim.HostSystem
   disks: list[StoragePoolDisk] = []


class ClientClusterUnicastConfig(pyVmomi.vmodl.DynamicData):
   """
   Unicast configuration for a server host.
   
   It is used for remote unicast agent operations. It includes unicast
   information for a list of client clusters.
   
   Attributes:
       remoteUnicastConfig: The list of client clusters' unicast information.
   """
   remoteUnicastConfig: list[ClientClusterUnicastInfo] = []


class ClientClusterUnicastInfo(pyVmomi.vmodl.DynamicData):
   """
   Unicast information for a client cluster.
   
   It is used for remote unicast
   agent operations. It includes client cluster UUID to which server host
   connects and lists of unicast address information for all hosts
   within the client cluster.
   
   Attributes:
       clusterUuid: The client cluster UUID that server host uses to add client hosts
           as their unicast agents.
       unicastInfo: The list of client hosts' unicast information.
   """
   clusterUuid: str
   unicastInfo: list[ClientHostUnicastInfo] = []


class ClientHostUnicastInfo(pyVmomi.vmodl.DynamicData):
   """
   Unicast information of a host in client cluster.
   
   Attributes:
       hostUuid: Client host UUID.
       unicastSpec: The list of unicast information for the host in a client cluster.
       thumbprintList: A list of SSL certificate thumbprints with supported secure hashing
           algorithms.
           
           See `pyVmomi.vim.vm.CertThumbprint`
   """
   hostUuid: str
   unicastSpec: list[pyVmomi.vim.cluster.VsanUnicastAddressInfo] = []
   thumbprintList: list[pyVmomi.vim.vm.CertThumbprint] = []


class ClusterStatus(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.vim.vsan.host.ClusterStatus` data object contains a host's cluster status
   information for the VSAN service.
   
   This data object is used to represent
   read-only state whose values may change during operation.
   
   See Also: `pyVmomi.vim.host.VsanSystem.queryHostStatus`
   
   Attributes:
       uuid: VSAN service cluster UUID.
       nodeUuid: VSAN node UUID for this host.
       health: VSAN health state for this host.
       nodeState: VSAN node state for this host.
       memberUuid: List of UUIDs for VSAN nodes known to this host.
   """
   class State(pyVmomi.vmodl.DynamicData):
      """
      Data object representing the VSAN node state for a host.
      
      Attributes:
          state: VSAN node state for this host.
          completion: An estimation of the completion of a node state transition; this
              value may be populated for transitory node states.
      """
      class CompletionEstimate(pyVmomi.vmodl.DynamicData):
         """
         Estimated completion status for transitory node states.
         
         See Also: `pyVmomi.vim.vsan.host.NodeState`
         
         Attributes:
             completeTime: Estimated time of completion.
             percentComplete: Estimated percent of completion as a value in the range [0, 100].
         """
         completeTime: _typing.Optional[_datetime.datetime] = None
         percentComplete: _typing.Optional[int] = None

      state: str
      completion: _typing.Optional[ClusterStatus.State.CompletionEstimate] = None

   uuid: _typing.Optional[str] = None
   nodeUuid: _typing.Optional[str] = None
   health: str
   nodeState: ClusterStatus.State
   memberUuid: list[str] = []


class ComplianceDetail(pyVmomi.vmodl.DynamicData):
   """
   Describes the result of policy compliance checking for vSAN object.
   
   Attributes:
       objectUUID: Requirement vSAN object with which the compliance was checked.
       complianceStatus: Status of the compliance check operation.
       objectHealth: Value for object health state.
       violatedPolicies: Values for capabilities that are known to be non-compliant
           with the specified constraints.
   """
   objectUUID: str
   complianceStatus: str
   objectHealth: int
   violatedPolicies: list[PolicyStatus] = []


class ComplianceResult(pyVmomi.vmodl.DynamicData):
   """
   Describes the results of policy compliance checking for vSAN objects.
   
   Attributes:
       checkTime: Time when the compliance was checked.
       policyId: Requirement policy with which the compliance was checked.
   """
   checkTime: _datetime.datetime
   policyId: _typing.Optional[str] = None
   policyGen: _typing.Optional[int] = None
   objComplianceDetail: list[ComplianceDetail] = []

class ComplianceStatus:
   """Defines the set of status values for compliance operations."""
   pass


class ConfigInfo(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.vim.vsan.host.ConfigInfo` data object contains host-specific settings
   for the VSAN service.
   
   This data object is used both for specifying
   settings for updating the VSAN service, and as an output datatype
   when retrieving current VSAN service settings.
   
   Attributes:
       enabled: Whether the VSAN service is currently enabled on this host.
       hostSystem: The `pyVmomi.vim.HostSystem` for this host.
           
           This argument is required when this configuration is specified as
           an input to VC-level APIs. When this configuration is specified
           to a host-level direct API, this argument may be omitted.
       clusterInfo: The VSAN service cluster configuration for this host.
       storageInfo: The VSAN storage configuration for this host.
           
           VSAN storage configuration settings are independent of the
           current value of `pyVmomi.vim.vsan.host.ConfigInfo.enabled`.
       networkInfo: The VSAN network configuration for this host.
           
           VSAN network configuration settings are independent of the
           current value of `pyVmomi.vim.vsan.host.ConfigInfo.enabled`.
       faultDomainInfo: The VSAN fault domain configuration for this host.
           
           VSAN host fault domain settings are independent of the
           current value of `pyVmomi.vim.vsan.host.ConfigInfo.enabled`.
       vsanEsaEnabled: Whether the vSAN ESA is enabled on this host.
           
           This can only be
           enabled when vSAN is enabled on this host.
           
           Since: vSphere API Release 8.0.0.1
       vsanCyberRecoveryEnabled: Whether the vSAN Cyber Recovery is enabled on this host.
           
           This can only be
           enabled when vSAN ESA is enabled on this host.
           
           Since: vSphere API Release 9.1.0.0
   """
   class StorageInfo(pyVmomi.vmodl.DynamicData):
      """
      Host-local VSAN storage configuration.
      
      This data object is used
      both for specifying and retrieving storage configuration for a
      host participating in the VSAN service.
      
      Attributes:
          autoClaimStorage: Whether the VSAN service is configured to automatically claim local
              unused storage on this host.
              
              When set, the VSAN service will automatically format and use local
              disks. Side effects from any disk consumption will be reflected in
              `pyVmomi.vim.vsan.host.ConfigInfo.StorageInfo.diskMapping`.
              If this argument is specified as a host-level configuration input
              at the VC-level (see `pyVmomi.vim.cluster.ConfigInfoEx.vsanHostConfig`),
              it will override that of any cluster-level default value.
          diskMapping: List of `pyVmomi.vim.vsan.host.DiskMapping` entries in use by the VSAN service.
              
              DiskMappings to be used by the VSAN service may be manually
              specified using
              `pyVmomi.vim.host.VsanSystem.initializeDisks`.
          diskMapInfo: List of `pyVmomi.vim.vsan.host.DiskMapping` entries with runtime information from
              the perspective of this host.
          checksumEnabled: Whether checksum is enabled on all the disks in this host.
              
              If any disk is not checksum capable or 520 bps formatted,
              we will skip it.
      """
      autoClaimStorage: _typing.Optional[bool] = None
      diskMapping: list[DiskMapping] = []
      diskMapInfo: list[DiskMapInfo] = []
      checksumEnabled: _typing.Optional[bool] = None

   class ClusterInfo(pyVmomi.vmodl.DynamicData):
      """
      Host-local VSAN cluster configuration.
      
      This data object is used
      both for specifying and retrieving cluster configuration for a
      host participating in the VSAN service.
      
      Attributes:
          uuid: VSAN service cluster UUID, in the string form
              \"nnnnnnnn-nnnn-nnnn-nnnn-nnnnnnnnnnnn\", where n are hexadecimal
              digits.
              
              If provided while enabling the VSAN service, this value will be
              used for the service cluster UUID. If omitted when enabling the
              VSAN service, a suitable UUID will be generated by the platform.
              This is a read-only value while the VSAN service is enabled.
          nodeUuid: VSAN node UUID for this host.
              
              This is a read-only value which is populated upon enabling of the
              VSAN service.
      """
      uuid: _typing.Optional[str] = None
      nodeUuid: _typing.Optional[str] = None

   class NetworkInfo(pyVmomi.vmodl.DynamicData):
      """
      Host-local VSAN network configuration.
      
      This data object is used
      both for specifying and retrieving network configuration for a
      host participating in the VSAN service.
      
      Attributes:
          port: Set of PortConfig entries for use by the VSAN service, one per
              \"virtual network\" as used by VSAN.
      """
      class PortConfig(pyVmomi.vmodl.DynamicData):
         """
         A PortConfig represents a virtual network adapter and its
         configuration for use by the VSAN service.
         
         See Also: `pyVmomi.vim.host.VirtualNic`
         
         Attributes:
             ipConfig: `pyVmomi.vim.vsan.host.IpConfig` for this PortConfig.
             device: Device name which identifies the network adapter for this
                 PortConfig.
         """
         ipConfig: _typing.Optional[IpConfig] = None
         device: str

      port: list[ConfigInfo.NetworkInfo.PortConfig] = []

   class FaultDomainInfo(pyVmomi.vmodl.DynamicData):
      """
      Host-local VSAN fault domain configuration.
      
      This data object is used
      both for specifying and retrieving fault domain configuration for a
      host participating in the VSAN service.
      
      Attributes:
          name: The configured VSAN fault domain.
              
              The length of fault domain name should not exceed 256.
              Empty string indicates that the default fault domain is used.
      """
      name: str

   enabled: _typing.Optional[bool] = None
   hostSystem: _typing.Optional[pyVmomi.vim.HostSystem] = None
   clusterInfo: _typing.Optional[ConfigInfo.ClusterInfo] = None
   storageInfo: _typing.Optional[ConfigInfo.StorageInfo] = None
   networkInfo: _typing.Optional[ConfigInfo.NetworkInfo] = None
   faultDomainInfo: _typing.Optional[ConfigInfo.FaultDomainInfo] = None
   vsanEsaEnabled: _typing.Optional[bool] = None
   vsanCyberRecoveryEnabled: _typing.Optional[bool] = None


class ConfigInfoEx(ConfigInfo):
   """
   ConfigInfoEx is an extension of vim.vsan.host.ConfigInfo,
   it contains encryption configuration for vSAN encryption
   service.
   
   Attributes:
       encryptionInfo: Encryption configuration.
       dataEfficiencyInfo: Data efficiency configuration.
       resyncIopsLimitInfo: Resync IOPS limit configuration in Mbps.
           
           The value should be between
           0 and 512.
       extendedConfig: vSAN Extended configurations.
       datastoreInfo: Datastore configuration.
       unmapConfig: SCSI unmap command configuration on vSAN.
       witnessHostConfig: Witness host configuration, available only when host works
           as witness node in vSAN stretched cluster, otherwise this field
           will be omitted.
       internalExtendedConfig: vSAN host-level extended configurations.
       metricsConfig: vSAN metric configurations for all monitor clients.
       unicastConfig: Unicast configuration.
           
           It is used for remote unicast agent operations.
           The remote unicast agent need to be set because when user mounts
           remote vSAN datastore, client cluster needs to access the objects
           on remote clusters.
       rdmaConfig: The RDMA configuration for vSAN.
       dataInTransitEncryptionInfo: vSAN configuration for data-in-transit encryption.
       mode: Mode for vSAN.
       serverClusterConfigs: Server cluster configurations for HCI Mesh server clusters.
       snapServiceConfig: The Snapshot Service configuration for vSAN.
           
           Since: 8.0.0.4
       deconvergedNetConfig: De-converged network configuration for vSAN.
       remoteDITInfos: vSAN configuration for data-in-transit encryption between client and
           server cluster.
       clientUnicastConfig: Unicast configuration for server cluster members, which is used for
           remote unicast agent operations.
           
           The client unicast agent needs to be set to support remote DIT between
           client and server cluster. When the client cluster mounts a remote
           datastore, its unicast config needs to be pushed to server hosts.
       siteTakeoverConfig: The site takeover configuration for a host.
           
           Only applicable when the cluster is
           configured as stretched cluster.
       vbossHostConfig: The host level configuration of vSAN vBoss service.
       autoRAIDConfig: vSAN auto RAID configuration.
   """
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
   """
   Specifies parameters needed to create native key provider.
   
   Attributes:
       provider: Provider identifier.
           
           A unique string provided by the client.
       keyId: Key identifier for the provider.
           
           The key identifier is required to be a 128-bit UUID represented as
           a hexadecimal string in \"12345678-abcd-1234-cdef-123456789abc\" format.
           If unset, the key identifier will be generated automatically.
       keyDerivationKey: Key used to derive data encryption keys.
           
           Base64 encoded.
           If unset, the key derivation key will be generated automatically.
       tpmRequired: TPM Required or Not.
           
           When TPM is required, user won't be able to create native key provider
           on hosts without TPM.
           If unset, there's no TPM constraints on host.
   """
   provider: str
   keyId: _typing.Optional[str] = None
   keyDerivationKey: _typing.Optional[str] = None
   tpmRequired: _typing.Optional[bool] = None


class DataInTransitEncryptionInfo(pyVmomi.vmodl.DynamicData):
   """
   The configuration for data-in-transit encryption.
   
   Attributes:
       enabled: Whether data-in-transit encryption is enabled in the cluster.
       rekeyInterval: Periodical rekeying interval in minutes.
           
           Default interval is 1440, i.e. 24 hours.
           Minimal interval is 30 minutes and maximum is 10080, i.e. 7 days.
       transitionState: Transition state is used to mark intermediate stages during
           encryption configuration change for a vSAN cluster.
           
           Default to 'settled'.
       serverClusterUuid: The server cluster UUID where the remote vSAN datastores are hosted.
           
           This is used to support data in transit encryption for remote vSAN.
       clientClusterUuid: The client cluster UUID which mounts the remote vSAN datastore.
   """
   enabled: _typing.Optional[bool] = None
   rekeyInterval: _typing.Optional[int] = None
   transitionState: _typing.Optional[str] = None
   serverClusterUuid: _typing.Optional[str] = None
   clientClusterUuid: _typing.Optional[str] = None


class DecommissionMode(pyVmomi.vmodl.DynamicData):
   """
   A `pyVmomi.vim.vsan.host.DecommissionMode` defines an action to take upon decommissioning
   a host from use with the VSAN service.
   
   If the VSAN service DecommissionMode is omitted in a call to
   `pyVmomi.vim.HostSystem.enterMaintenanceMode`, the default action chosen
   will be `ensureObjectAccessibility`.
   
   See Also: `pyVmomi.vim.HostSystem.enterMaintenanceMode`, `pyVmomi.vim.host.MaintenanceSpec.vsanMode`
   
   Attributes:
       objectAction: Specifies an action to take with regard to the VSAN service upon
           putting a host into maintenance mode.
   """
   class ObjectAction(pyVmomi.VmomiSupport.Enum):
      """
      The action to take with regard to storage objects upon decommissioning
      a host from use with the VSAN service.
      
      Attributes:
          noAction: No special action should take place regarding VSAN data.
          ensureObjectAccessibility: VSAN data reconfiguration should be performed to ensure storage
              object accessibility.
          evacuateAllData: VSAN data evacuation should be performed such that all storage
              object data is removed from the host.
      """
      noAction: _typing.ClassVar['DecommissionMode.ObjectAction'] = 'noAction'
      ensureObjectAccessibility: _typing.ClassVar['DecommissionMode.ObjectAction'] = 'ensureObjectAccessibility'
      evacuateAllData: _typing.ClassVar['DecommissionMode.ObjectAction'] = 'evacuateAllData'

   objectAction: str


class DeleteStoragePoolDiskSpec(pyVmomi.vmodl.DynamicData):
   """
   Specification to delete a single or multiple disks on the vSAN cluster.
   
   The disk(s) can be specified by their uniquely identifiable disk uuid.
   """
   diskUuids: list[str] = []
   maintenanceSpec: pyVmomi.vim.host.MaintenanceSpec


class DiskMapInfo(pyVmomi.vmodl.DynamicData):
   """
   A DiskMapInfo represents a `pyVmomi.vim.vsan.host.DiskMapping` and its
   corresponding runtime information.
   
   See Also: `pyVmomi.vim.vsan.host.ConfigInfo.StorageInfo`, `pyVmomi.vim.host.VsanSystem.initializeDisks`
   
   Attributes:
       mapping: DiskMapping.
       mounted: Indicates whether the `pyVmomi.vim.vsan.host.DiskMapping` is mounted.
   """
   mapping: DiskMapping
   mounted: bool


class DiskMapInfoEx(pyVmomi.vmodl.DynamicData):
   """
   DiskMapInfoEx is used to present information of
   a Virtual disk group.
   
   It extended vim.vsan.host.DiskMapInfo,
   added fields all-flash and space efficiency settings on
   this disk group.
   
   Attributes:
       mapping: The disk structure of this vSAN disk group.
       isMounted: Whether this disk group is mounted to this host.
           
           For an unmounted
           disk group, it cannot be used for vSAN I/O on this host.
           To make unmounted disk group contribute to vSAN I/O, please
           try vim.host.VsanSystem.InitializeDisks and vim.host.VsanSystem.AddDisks.
       unlockedEncrypted: Whether encryption keys for this disk group are loaded.
           
           If vSAN encryption is on and the encryption keys are not loaded for
           the disk group, the disk group cannot be used for vSAN I/O on this host.
       isAllFlash: Whether this disk group is all flash disk group.
       isDataEfficiency: This field will be True if both vSAN deduplication and compression are
           enabled, or only compression is enabled on this disk group.
           
           Check `pyVmomi.vim.vsan.host.DiskMapInfoEx.dataEfficiencyConfig` for more
           details.
       encryptionInfo: vSAN encryption metadata for the disk group.
       dataEfficiencyConfig: The data efficiency configuration on this disk group.
           
           dedupEnabled in dataEfficiencyConfig will be set when both vSAN
           deduplication and compression are enabled.
           compressionEnabled in dataEfficiencyConfig will be set when
           compression-only is enabled.
           dedupEnabled and compressionEnabled will not be set at the same time
           (i.e. mutually-exclusive True).
           For more details refer to `pyVmomi.vim.vsan.DataEfficiencyConfig`
       diskgroupCapability: vSAN diskgroup capability.
           
           See `pyVmomi.vim.vsan.host.VsanDiskgroupCapability` for all supported values.
   """
   mapping: DiskMapping
   isMounted: bool
   unlockedEncrypted: _typing.Optional[bool] = None
   isAllFlash: bool
   isDataEfficiency: _typing.Optional[bool] = None
   encryptionInfo: _typing.Optional[pyVmomi.vim.vsan.DataEncryptionConfig] = None
   dataEfficiencyConfig: _typing.Optional[pyVmomi.vim.vsan.DataEfficiencyConfig] = None
   diskgroupCapability: list[str] = []


class DiskMapResult(pyVmomi.vmodl.DynamicData):
   """
   A DiskMapResult represents the result of an operation performed
   on the set of disks in a `pyVmomi.vim.vsan.host.DiskMapping`.
   
   See Also: `pyVmomi.vim.host.VsanSystem.initializeDisks`, `pyVmomi.vim.host.VsanSystem.update`
   
   Attributes:
       mapping: DiskMapping for this result.
       diskResult: List of results for each disk in the mapping.
       error: Error information for this result.
   """
   mapping: DiskMapping
   diskResult: list[DiskResult] = []
   error: _typing.Optional[pyVmomi.vmodl.MethodFault] = None


class DiskMapping(pyVmomi.vmodl.DynamicData):
   """
   A `pyVmomi.vim.vsan.host.DiskMapping` is a set of one SSD `pyVmomi.vim.host.ScsiDisk` backed
   by a set of one or more non-SSD `pyVmomi.vim.host.ScsiDisk`.
   
   The maximum
   allowed `pyVmomi.vim.vsan.host.DiskMapping` for a host is 5. A maximum set
   of 7 non-SSDs `pyVmomi.vim.host.ScsiDisk` can be added to the one
   SSD `pyVmomi.vim.host.ScsiDisk`.
   
   See Also: `pyVmomi.vim.vsan.host.ConfigInfo.StorageInfo`, `pyVmomi.vim.host.VsanSystem.initializeDisks`
   
   Attributes:
       ssd: SSD `pyVmomi.vim.host.ScsiDisk`.
       nonSsd: Set of non-SSD backing `pyVmomi.vim.host.ScsiDisk`.
   """
   ssd: pyVmomi.vim.host.ScsiDisk
   nonSsd: list[pyVmomi.vim.host.ScsiDisk] = []


class DiskMappingCreationSpec(pyVmomi.vmodl.DynamicData):
   """
   Specification for vSAN disk group creation.
   
   It is used for semi-automatic disk claim on specific host
   for vSAN service, both hybrid and all flash
   disk groups could be created with this specification.
   It could be used to create new disk group, and append
   new disks to existing vSAN disk group.
   It can also be used for vSAN direct datastore provision on specific
   host. For claiming vSAN direct datastore,
   `pyVmomi.vim.vsan.host.DiskMappingCreationSpec.creationType` is set to
   \"vsandirect\" and the disk(s) to be claimed are provided through
   `pyVmomi.vim.vsan.host.DiskMappingCreationSpec.capacityDisks`.
   
   Attributes:
       host: Target host to create vSAN disk group.
       cacheDisks: Disk(s) to be used as cache tier of disk group.
           
           If the specification is used to create new disk group,
           disk(s) set to this field must not be used by vSAN,
           and this field is required;
           if the specification is used to append disk(s) to
           existing disk group, this field is optional, and cannot
           accept more than one disk, and disk specified here should
           be the cache tier of existing disk group.
       capacityDisks: Disk(s) to be used as capacity tier of disk group.
           
           All disk(s)
           specified to this field, must not be used by vSAN.
           This field can also be used in vSAN direct datastore provision,
           i.e. `pyVmomi.vim.vsan.host.DiskMappingCreationSpec.creationType` set to
           \"vsandirect\". It represents all the disk(s) used to create vSAN direct
           datastores. All disk(s) specified to this field must not be used by vSAN
           or any other datastores.
       creationType: Disk group type to create.
   """
   class DiskMappingCreationType(pyVmomi.VmomiSupport.Enum):
      """
      Disk group types to create.
      
      Attributes:
          hybrid: Consumes SSD as cache tier, and HDD as capacity tier.
          allFlash: Uses SSD for both cache tier and capacity tier.
              
              vSAN optimizes the on-disk format on all flash disk group, to support more features, such as deduplication and compression, etc.
          pmem: Do not use.
      """
      hybrid: _typing.ClassVar['DiskMappingCreationSpec.DiskMappingCreationType'] = 'hybrid'
      allFlash: _typing.ClassVar['DiskMappingCreationSpec.DiskMappingCreationType'] = 'allFlash'
      vsandirect: _typing.ClassVar['DiskMappingCreationSpec.DiskMappingCreationType'] = 'vsandirect'
      pmem: _typing.ClassVar['DiskMappingCreationSpec.DiskMappingCreationType'] = 'pmem'
      DiskMappingCreationType_Unknown: _typing.ClassVar['DiskMappingCreationSpec.DiskMappingCreationType'] = 'DiskMappingCreationType_Unknown'

   host: pyVmomi.vim.HostSystem
   cacheDisks: list[pyVmomi.vim.host.ScsiDisk] = []
   capacityDisks: list[pyVmomi.vim.host.ScsiDisk] = []
   creationType: str


class DiskResult(pyVmomi.vmodl.DynamicData):
   """
   A DiskResult represents the result of VSAN configuration operation
   on a `pyVmomi.vim.host.ScsiDisk`, and its current eligibility state for use by
   the VSAN service.
   
   See Also: `pyVmomi.vim.host.VsanSystem.queryDisksForVsan`, `pyVmomi.vim.host.VsanSystem.update`, `pyVmomi.vim.vsan.host.DiskResult.State`
   
   Attributes:
       disk: Disk for this result.
       state: State of the disk for this result.
       vsanUuid: VSAN disk UUID in case this disk is a VSAN disk.
       error: Error information for this result: may be populated with additional
           information about the disk at hand, regardless of the disk's state.
       degraded: Indicates whether the disk is degraded in VSAN performance.
           
           If set, indicates the disk performance is degraded in VSAN
           If unset, it is unknown whether the disk performance is degraded in VSAN.
   """
   class State(pyVmomi.VmomiSupport.Enum):
      """
      Values used for indicating a disk's status for use by the VSAN service.
      
      See Also: `pyVmomi.vim.vsan.host.DiskResult.state`
      
      Attributes:
          inUse: Disk is currently in use by the VSAN service.
              
              A disk may be considered in use by the VSAN service regardless of
              whether the VSAN service is enabled. As long as a disk is in use
              by VSAN, it is reserved exclusively for VSAN and may not be used
              for other purposes.
          eligible: Disk is considered eligible for use by the VSAN service,
              but is not currently in use.
          ineligible: Disk is considered ineligible for use by the VSAN service,
              and is not currently in use.
      """
      inUse: _typing.ClassVar['DiskResult.State'] = 'inUse'
      eligible: _typing.ClassVar['DiskResult.State'] = 'eligible'
      ineligible: _typing.ClassVar['DiskResult.State'] = 'ineligible'

   disk: pyVmomi.vim.host.ScsiDisk
   state: str
   vsanUuid: _typing.Optional[str] = None
   error: _typing.Optional[pyVmomi.vmodl.MethodFault] = None
   degraded: _typing.Optional[bool] = None


class DiskResultEx(DiskResult):
   """
   A DiskResultEx represents the results of vSAN configuration
   operation on a `pyVmomi.vim.host.ScsiDisk`, and its current eligibility state
   for use by vSAN.
   
   Attributes:
       vsanDirectTagged: Indicates whether the disk is tagged to be claimed as vSAN Direct disk.
           
           If set to true, it indicates users prefer to use this disk to be
           claimed as vSAN Direct disk. If set to false or unset, it indicates
           users do not have such preference. Currently only eligible disks can
           be tagged as vSAN Direct. It acts as a hint to the upper management
           suites like VCF, tagging it does not automatically claim the disk
           as vSAN Direct.
       storagePoolDiskState: Indicates state of the storage pool disk.
           
           Represents if the disk is In-use/Eligible/Ineligible for storage pool.
           See `pyVmomi.vim.vsan.host.DiskResult.State`.
       storagePoolDiskError: Error information corresponding to the storagePoolDiskState.
           
           For eg:
           If storagePoolDiskState is Ineligible, storagePoolDiskError will give
           the corresponding reason for ineligiblility like 'Disk is in use by
           DiskGroup'.
           This may also be populated with additional information about the disk
           at hand.
       isCapacityFlash: Check if given disk is capacity flash or not.
           
           For eg: If setup is
           all flash setup, for capacity tier SSDs, this flag will be true.
   """
   vsanDirectTagged: bool
   storagePoolDiskState: _typing.Optional[str] = None
   storagePoolDiskError: _typing.Optional[pyVmomi.vmodl.MethodFault] = None
   isCapacityFlash: _typing.Optional[bool] = None


class DrsStats(pyVmomi.vmodl.DynamicData):
   """
   vSAN storage stats per host to support DRS integration
   
   Attributes:
       host: vSAN host entity associated to the DRS stats.
       stats: Binary value to present vSAN DRS stats in below C struct:
           typedef VmHostStat uint8; // vSAN VM read locality per host.
           
           // 1 means the host can serve read request
           // without cross site IO, and 0 means
           // either the data is inaccessible to this
           // host or the host needs cross site read
           // to serve the read request.
           struct VmStats {
           Uuid vmUuid; // VM instance UUID;
           uint32 totalSizeInKb; // Total capacity used by this VM in KB on
           // vSAN datastore;
           VmHostStat perHostValue[0]; // Weight of VM active vSAN data contributed
           // per vSAN host. The order is determined by
           // host member list specified to API
           // VsanQueryHostDrsStats, and length is
           // determined by number of vSAN member hosts;
           };
           struct Stats {
           uint64 hostCapInKb; // host capacity contributed to vSAN in KB;
           uint64 hostUsageInKb; // host usage on vSAN datastore in KB;
           uint32 numVms; // number of vSAN VMs registered on this host;
           uint32 numHosts; // number of vSAN member hosts; It is determined
           // by host member list specified to API
           // VsanQueryHostDrsStats. Any host member change
           // can be detected by vSAN VC service, and trigger
           // next stats query to capture the new change.
           VmStats perVmStats[0];// vSAN VM DRS stats, length is determined by
           // numVms; And note that size of VmStats struct
           // itself is dynamic.
           };
       readLocalityPresented: Whether object site read locality is presented in VmStats
   """
   host: pyVmomi.vim.HostSystem
   stats: pyVmomi.VmomiSupport.binary
   readLocalityPresented: _typing.Optional[bool] = None


class EncryptionInfo(pyVmomi.vmodl.DynamicData):
   """
   VMware vSAN can encrypt data on the disk.
   
   Below terminologies
   and their acronyms are used to demonstrate how the encryption works.
   DEK - Data Encryption Key. Keys that are used to encryption data on
   each disk. Plain DEK will not be persisted by vSAN for safety.
   Instead, vSAN will encrypt the DEK and store the encrypted format.
   KEK - Key Encryption Key. A vSAN cluster will maintain a KEK that is
   used to encrypt the DEKs. vSAN does not persist the KEK. It only
   persists the Id of the KEK, and retrieve plain KEK from KMS (mentioned
   below) by providing the KEK's Id.
   KMS - Key Management Server, where KEK is generated and stored, we
   support KMS from several popular vendors, such as SafeNet, Thales,
   Vormetrics, and HyTrust.
   Encryption configuration for vSAN encryption service. It contains
   encryption enablement state, KEK Id, KMS information, client certificate,
   private key, and KMS certificates.
   
   Attributes:
       enabled: Encryption enablement state.
       kekId: Unique ID for the KEK in the KMS cluster.
           
           It's returned by KMS after
           vCenter invoking key generation operation. ESX host can retrieve the key
           with this ID.
       hostKeyId: The Id of host key which is used for host core dump encryption.
           
           This
           should be generated by vCenter to call key management server and pass to
           ESXi host. ESXi host can later retrieve the key with this ID.
       kmipServers: The KMS servers where the global KEK is created and stored.
           
           Host will
           fetch KEK from the KMS cluster with given KEK ID.
       kmsServerCerts: Certificates of Key Management Servers in PEM encoding.
           
           Host will use
           these certificates to decide if a KMS should be trusted or not.
       clientKey: Client private key.
           
           Host will use this key for authentication when
           connecting to KMS.
       clientCert: Client certificate in PEM encoding.
           
           Host will use this certificate
           for authentication when connecting to KMS.
       dekGenerationId: Data Encryption Key (DEK) generation number.
       changing: Whether encryption state is currently changing to have all disk groups
           matching the state described in enabled.
       eraseDisksBeforeUse: Whether disks should be wiped when a normal disk is converted to
           encrypted disk, or a disk is claimed as encrypted disk, or a disk
           runs deep rekey.
           
           If set true, every sector on a disk will be written
           with random data. Disk wipe does significantly reduce the possibility
           of data leak and increases the attacker's cost to reveal sensitive
           data. The disadvantage of disk wipe is that it takes a long time to
           finish, so turn it on through UI or API only when necessary. If not
           set, disk won't be wiped.
       wrappedDek: Data Encryption Key (DEK) wrapped by Key Encryption Key (KEK).
       dekId: UUID of cluster wide Data Encryption Key (DEK).
       oldWrappedDek: Old Data Encryption Key (DEK) wrapped by Key Encryption Key (KEK).
       oldDekId: UUID of the old cluster wide Data Encryption Key (DEK).
       kekVerifier: Verifier of KEK.
           
           It's calculated by encrypting all zero data with KEK.
           ESX host can verify KEK correctness using this verifier.
       dekVerifier: Verifier of DEK.
           
           It's calculated by encrypting all zero data with DEK.
           ESX host can verify DEK correctness using this verifier.
       oldDekVerifier: Verifier of old DEK.
           
           It's calculated by encrypting all zero data with old DEK.
           ESX host can verify old DEK correctness using this verifier.
       iv: Initialization vector used by encryption algorithm.
           
           The vector is encoded as a string.
       syncing: Whether the cluster is syncing encryption config when it enables
           encryption or does deep rekey.
   """
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
   """The rekey operation type of vSAN2 encryption."""
   pass

class EncryptionTransitionState:
   """
   The state of host during data-in-transit encryption configuration
   change for a vSAN cluster.
   
   The final configuration whether to
   turn on or turn off encryption for the cluster is defined in
   `pyVmomi.vim.vsan.host.ConfigInfoEx.dataInTransitEncryptionInfo`.
   """
   pass

class HealthState:
   """
   A `pyVmomi.vim.vsan.host.HealthState` represents the state of a participating
   host in the VSAN service.
   
   See Also: `pyVmomi.vim.vsan.host.ClusterStatus`
   """
   pass


class IpConfig(pyVmomi.vmodl.DynamicData):
   """
   Deprecated: As of vSphere API 9.1, vSAN has been using unicast only
   configuration in all supported releases. The multicast configuration has been
   deprecated.An `pyVmomi.vim.vsan.host.IpConfig` is a pair of multicast IP addresses for use by the VSAN
   service.
   
   For VSAN there is one such IpConfig pair per \"virtual network\" as
   represented by `pyVmomi.vim.vsan.host.ConfigInfo.NetworkInfo.PortConfig`.
   
   See Also: `pyVmomi.vim.vsan.host.ConfigInfo.NetworkInfo`, `pyVmomi.vim.vsan.host.ConfigInfo.NetworkInfo.port`, `pyVmomi.vim.vsan.host.ConfigInfo.NetworkInfo.PortConfig`, `pyVmomi.vim.host.VsanSystem.update`
   
   Attributes:
       upstreamIpAddress: Agent-to-master multicast IP address.
       downstreamIpAddress: Master-to-agent multicast IP address.
   """
   upstreamIpAddress: str
   downstreamIpAddress: str


class IpConfigEx(IpConfig):
   """
   Deprecated: As of vSphere API 9.1, vSAN has been using unicast only
   configuration in all supported releases. The multicast configuration has been
   deprecated.An IpConfigEx is an extension of vim.vsan.host.IpConfig,
   it contains a pair of IPv4 multicast addresses and a pair
   of IPv6 multicast addresses, used by vSAN service.
   
   For vSAN there is one such IpConfigEx per
   \"virtual network\" as represented by
   vim.vsan.host.ConfigInfo.NetworkInfo.PortConfigEx.
   On vSAN vmknic with both IPv4 and IPv6 addresses,
   vSAN attempts communication over both IP versions.
   Setting the IPv6 related configuration values here only if
   we want to change them from their defaults.
   
   Attributes:
       upstreamIpV6Address: Agent-to-master multicast IPv6 address.
           
           If this field is not set during vSAN update,
           FF19:0:0:0:0:1:2:3 will be taken.
       downstreamIpV6Address: Master-to-agent multicast IPv6 address.
           
           If this field is not set during vSAN update,
           FF19:0:0:0:0:2:3:4 will be taken.
   """
   upstreamIpV6Address: _typing.Optional[str] = None
   downstreamIpV6Address: _typing.Optional[str] = None


class MembershipInfo(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.vim.vsan.host.MembershipInfo` data object contains VSAN cluster
   membership information for a single host, as observed from a
   given host.
   
   This data object is used to represent read-only
   state whose values may change during operation.
   
   See Also: `pyVmomi.vim.host.RuntimeInfo.vsanRuntimeInfo`
   
   Attributes:
       nodeUuid: VSAN node UUID for the host of this MembershipInfo.
       hostname: Hostname for the host of this MembershipInfo.
           
           May be the empty string \"\" if the hostname is unavailable.
   """
   nodeUuid: str
   hostname: str

class NodeState:
   """
   A `pyVmomi.vim.vsan.host.NodeState` represents the state of participation of a host
   in the VSAN service.
   
   See Also: `pyVmomi.vim.vsan.host.ClusterStatus`, `pyVmomi.vim.vsan.host.ClusterStatus.State`
   """
   pass


class PolicyStatus(pyVmomi.vmodl.DynamicData):
   """
   Provides information when compliance checking produces non-compliant
   results.
   
   Attributes:
       id: The checked policy ID.
       expectedValue: The expected policy value.
       currentValue: The current policy value.
   """
   id: str
   expectedValue: str
   currentValue: str


class PortConfigEx(ConfigInfo.NetworkInfo.PortConfig):
   """
   A PortConfigEx represents a virtual network adapter and its
   configuration for use by the vSAN service.
   
   This is an extension of vim.vsan.host.ConfigInfo.NetworkInfo.PortConfig,
   More configuration details are exposed, including traffic type,
   and IPv6 addresses.
   
   Attributes:
       trafficTypes: Type of vSAN traffic through this network adapter.
           
           If this field is not set or set empty during Virtual update,
           type 'vsan' will be taken as default.
           This field is invisible to older version client.
   """
   class TrafficType(pyVmomi.VmomiSupport.Enum):
      """
      Network transmission type of vSAN traffic through
      a virtual network adapter for 8.x and previous releases.
      
      Attributes:
          vsan: This vmknic is used for general vSAN data transmission.
              
              If no vSAN vmknic configured with 'witness' traffic type, witness data transmission will be handled by vmknic with 'vsan' traffic type.
          witness: This vmknic is dedicated for vSAN witness data transmission.
              
              For vSAN stretched cluster, this traffic type is recommended for vSAN vmknics to be used for witness transmission.
      """
      vsan: _typing.ClassVar['PortConfigEx.TrafficType'] = 'vsan'
      witness: _typing.ClassVar['PortConfigEx.TrafficType'] = 'witness'
      TrafficType_Unknown: _typing.ClassVar['PortConfigEx.TrafficType'] = 'TrafficType_Unknown'

   class TrafficType90(pyVmomi.VmomiSupport.Enum):
      """
      Network transmission type of vSAN traffic through
      a virtual network adapter for 9.0 release
      """
      vsanExternal: _typing.ClassVar['PortConfigEx.TrafficType90'] = 'vsanExternal'

   trafficTypes: list[str] = []


class QueryVsanDisksSpec(pyVmomi.vmodl.DynamicData):
   """
   Specification to filter vSAN disks by diskName, or by
   `pyVmomi.vim.vsan.host.VsanDiskType` which is diskGroup type or storagePool
   type or vSAN directDisk type.
   
   If only diskName specified, it will check ssd canonicalName in diskGroup
   type, disk canonicalName in storagePool and directDisk type. Return when
   disk name is matched in any type.
   If only vsanDiskType is specified, it will return all disks belonging to
   that diskType.
   If both diskName and vsanDiskType specified, it will find disk(ssd for
   diskGroup) under this specified disk type.
   """
   diskName: _typing.Optional[str] = None
   vsanDiskType: _typing.Optional[str] = None


class RemoteVsanServerClusterConfig(pyVmomi.vmodl.DynamicData):
   """
   Server cluster specific configuration for HCI Mesh
   
   Attributes:
       clusterUuid: The server cluster UUID which client cluster uses to mount remote vSAN
           datastores of server hosts.
       siteAffinity: The server cluster site affinity.
           
           This is a site fault domain name and
           UUID for a site in server cluster. The entries in the field is unset
           if the server is a single site cluster or the host has a
           symmetric network connectivity with both the server cluster sites.
   """
   clusterUuid: str
   siteAffinity: _typing.Optional[SiteAffinityInfo] = None


class RuntimeStats(pyVmomi.vmodl.DynamicData):
   """
   vSAN runtime stats from the perspective of the host in question.
   
   It is used to present read-only stats which may change during
   operation.
   
   Attributes:
       resyncIopsInfo: Runtime value of vSAN resync IOPS information.
           
           This field is to present
           `resyncIopsInfo`.
       configGeneration: Current config generation of the host.
       supportedClusterSize: Maximum vSAN cluster size supported by this host.
       repairTimerInfo: Repair timer information of the host.
       componentLimitPerCluster: Get shared witness per cluster component limit of the host.
       maxWitnessClusters: Get shared witness max number of clusters on a witness node.
   """
   resyncIopsInfo: _typing.Optional[pyVmomi.vim.vsan.ResyncIopsInfo] = None
   configGeneration: _typing.Optional[pyVmomi.vim.cluster.VsanConfigGeneration] = None
   supportedClusterSize: _typing.Optional[int] = None
   repairTimerInfo: _typing.Optional[pyVmomi.vim.vsan.RepairTimerInfo] = None
   componentLimitPerCluster: _typing.Optional[int] = None
   maxWitnessClusters: _typing.Optional[int] = None


class ServerClusterUnicastConfig(pyVmomi.vmodl.DynamicData):
   """
   Unicast configuration for a client host.
   
   It is used for remote unicast agent operations. It includes unicast
   information for a list of server clusters.
   
   Attributes:
       remoteUnicastConfig: The list of server clusters' unicast information.
   """
   remoteUnicastConfig: list[ServerClusterUnicastInfo] = []


class ServerClusterUnicastInfo(pyVmomi.vmodl.DynamicData):
   """
   Unicast information for a client host.
   
   It is used for remote unicast
   agent operations. It includes server cluster UUID to which client host
   connects and lists of unicast address information for all server hosts
   within the server cluster.
   
   Attributes:
       clusterUuid: The server cluster UUID that client host uses to add server hosts
           as their unicast agents.
       unicastInfo: The list of server hosts' unicast information.
   """
   clusterUuid: str
   unicastInfo: list[pyVmomi.vim.vsan.ServerHostUnicastInfo] = []

class ServerNodeType:
   """Remote server node type"""
   pass


class SiteAffinityInfo(pyVmomi.vmodl.DynamicData):
   """
   The server cluster site affinity for HCI Mesh server.
   
   Attributes:
       name: The server cluster site affinity.
           
           This is the site fault domain name
           for a site in server cluster.
       siteId: The server cluster site affinity.
           
           This is the site fault domain UUID
           generated internally for a site in server cluster.
   """
   name: str
   siteId: _typing.Optional[str] = None


class SiteTakeoverConfig(pyVmomi.vmodl.DynamicData):
   """
   The site takeover configuration for a host.
   
   Attributes:
       takeoverTimestamp: The site takeover operation timestamp.
           
           After a site has completed the takeover
           operation, all hosts in the recovered site will have a new unified takeover
           timestamp used to prevent object corruption from stale I/Os.
           A host has to be rebooted when its site takeover timestamp is older than
           the one from the recovered site. If a host newly joins the cluster,
           it will have the takeover timestamp from the recovered site automatically.
   """
   takeoverTimestamp: _typing.Optional[pyVmomi.VmomiSupport.long] = None

class StatsType:
   """
   Declaration of all supported vSAN runtime stats types.
   
   It is used
   to retrieve vSAN runtime stats through
   `pyVmomi.vim.host.VsanSystemEx.getRuntimeStats`
   """
   pass


class StoragePoolDisk(pyVmomi.vmodl.DynamicData):
   """
   Entity to represent storage pool disk identifier and type.
   
   Attributes:
       diskName: Canonical name of the disk.
       diskType: Indicates storage tier of the disk.
   """
   diskName: str
   diskType: str


class StoragePoolDiskInfo(pyVmomi.vmodl.DynamicData):
   """
   StoragePoolDiskInfo is used to present information of a disk that is
   claimed by storage pool.
   
   Attributes:
       disk: Disk for the info.
       vsanUuid: VSAN disk UUID.
       error: Error information for this disk info: may be populated with additional
           information about the disk at hand, regardless of the disk's state.
       isMounted: Indicates whether the storage pool disk is mounted.
       isEncrypted: Indicates whether encryption is enabled.
       dekId: Data Encryption Key (DEK) cluster wide uuid.
       diskType: Represents storage pool disk type.
           
           Refer to
           `pyVmomi.vim.vsan.host.StoragePoolDiskType`
   """
   disk: pyVmomi.vim.host.ScsiDisk
   vsanUuid: _typing.Optional[str] = None
   error: _typing.Optional[pyVmomi.vmodl.MethodFault] = None
   isMounted: _typing.Optional[bool] = None
   isEncrypted: _typing.Optional[bool] = None
   dekId: _typing.Optional[str] = None
   diskType: _typing.Optional[str] = None

class StoragePoolDiskType:
   """Represents type of disk in storage pool."""
   pass


class StoragePoolInfo(pyVmomi.vmodl.DynamicData):
   """
   StoragePoolInfo is used to present information of a storage pool.
   
   Attributes:
       storagePoolDisks: vSAN storage pool disks information.
   """
   storagePoolDisks: list[StoragePoolDiskInfo] = []


class TrimDiskEntry(pyVmomi.vmodl.DynamicData):
   """
   An entity to represent a disk being trimmed.
   
   Attributes:
       diskName: The identifier of this disk.
       diskType: This represents the disk type hint (optional) provided to trimming
           operation.
           
           It is used to specify erasing disk behavior when trimming fails.
           Refer `pyVmomi.vim.vsan.host.TrimDiskType`. If it is not specified, the
           behavior of \"CacheDisk\" in `pyVmomi.vim.vsan.host.TrimDiskType` will be
           followed.
   """
   diskName: str
   diskType: _typing.Optional[str] = None


class TrimDiskSpec(pyVmomi.vmodl.DynamicData):
   """
   Specification of disks in a trim operation.
   
   Attributes:
       disks: A list of TrimDiskEntry which specify disks.
   """
   disks: list[TrimDiskEntry] = []

class TrimDiskType:
   """This class represents a disk type in trimming."""
   pass


class UpdateStoragePoolDiskSpec(pyVmomi.vmodl.DynamicData):
   """Specification to update disks' metadata on the vSAN cluster."""
   diskUuids: list[str] = []
   diskFormatVersion: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class VbossHostConfig(pyVmomi.vim.vsan.VbossConfig):
   """
   The VsanVbossHostConfig defines the host side configuration properties of
   vSAN vBoss service.
   
   It inherits all common properties from
   `pyVmomi.vim.vsan.VbossConfig`.
   """
   pass


class VsanAssociatedObjects(pyVmomi.vmodl.DynamicData):
   """
   This data object type describes SPBM profile associated objects
   
   Attributes:
       spbmProfileId: UUID of SPBM profile used for the policy of the object
       spbmProfileGenerationNum: spbmProfile generation number
       vsanObjects: vSAN objects.
           
           vSAN object UUID string
   """
   spbmProfileId: str
   spbmProfileGenerationNum: int
   vsanObjects: list[str] = []


class VsanAssociatedObjectsResult(pyVmomi.vmodl.DynamicData):
   """
   This data object type describes results from query SPBM profile
   associated objects
   
   Attributes:
       data: SPBM profile associated objects.
           
           As SPBM could query with SPBM
           profile generation number not specified and there could exists
           objects applied with same SPBM profile Id but different SPBM
           profile generation, result is an array of type
           `pyVmomi.vim.vsan.host.VsanAssociatedObjects`. Each item in the
           array is one SPBM generation found in vSAN for the SPBM profile
           ID. For example, if SPBM called VsanAssociatedObjects with SPBM
           profile xxx and there exists 2 generations
           (generation number 1 and 2) in vSAN. Then returned result will
           have an array of size 2. One item is spbmProfileId='xxx' and
           spbmGenNum=1 with objects associated with it. The other item is
           spbmProfileId='xxx' and spbmGenNum=2 with objects associated with
           it.
       offset: Offset for next query to use.
           
           If there is no more object to query,
           offset will be -1.
       limit: limit for next query to use
   """
   data: list[VsanAssociatedObjects] = []
   offset: int
   limit: int


class VsanComplianceQuerySpec(pyVmomi.vmodl.DynamicData):
   """
   Specification for querying vSAN object compliance detail information.
   
   Attributes:
       uuids: vSAN object UUIDs.
       spbmProfileId: Current storage profile id for the profile used by vSAN object,
           it should be retrieved from SPBM service.
           
           If vSAN object doesn't
           use a storage profile in SPBM service, the generation id should
           be null.
       spbmProfileGenerationId: Current storage profile generation id for the profile used by vSAN
           object, it should be retrieved from SPBM service.
           
           If vSAN object
           doesn't use a storage profile in SPBM service, the generation id
           should be null. It is used to compare with the generation id of the
           profile at the time the profile was applied the to vSAN object, if
           they are not the same, it means the profile used by the vSAN object
           is out of date.
   """
   uuids: list[str] = []
   spbmProfileId: _typing.Optional[str] = None
   spbmProfileGenerationId: _typing.Optional[int] = None


class VsanComponentSyncState(pyVmomi.vmodl.DynamicData):
   """
   This data object type describes sync state for a vSAN component.
   
   Attributes:
       uuid: Represents the uuid of component.
       diskUuid: Represents the uuid of disk on which component resides.
       hostUuid: Represents the uuid of host on which component resides.
       bytesToSync: Indicates how many bytes need to be synced for this component.
       recoveryETA: The estimated time in seconds to complete recovery.
           
           This attribute will
           be not returned if no data has been synced.
       reasons: The list of reasons indicate why the component went into syncing state.
           
           The API returns full list of reasons for background. However, sometimes
           it's userful to generate an aggregate reason, in which case the following
           priorities could be used:
           - P0: \"evacuate\"
           - P1: \"dying_evacuate\"
           - P2: \"rebalance\"
           - P3: \"repair\", \"reconfigure\"
           - P4: \"stale\", \"merge_concat\"
   """
   uuid: str
   diskUuid: str
   hostUuid: str
   bytesToSync: pyVmomi.VmomiSupport.long
   recoveryETA: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   reasons: list[str] = []


class VsanDirectStorage(pyVmomi.vmodl.DynamicData):
   """
   This class represents the vSAN direct storage, which is
   the host local storage managing by vSAN though it doesn't
   contribute storage resource to vSAN datastore.
   
   Attributes:
       scsiDisks: vSAN direct SCSI disks information, which are claimed from the vSAN API
           `pyVmomi.vim.cluster.VsanVcDiskManagementSystem.initializeDiskMappings`
           with the disk creation type as vmfs.
       tier: vSAN direct storage tier.
           
           It's specified by user and different tier
           of storage has different performance characteristic, which can be
           used to support deploying workload with various performance requirement.
   """
   scsiDisks: list[VsanScsiDisk] = []
   tier: _typing.Optional[str] = None

class VsanDiskEvacReason:
   """Disk evacuation reason"""
   pass


class VsanDiskInfo(pyVmomi.vmodl.DynamicData):
   """
   A VsanDiskInfo represents the additional detailed
   information of a ScsiDisk used by VSAN,
   to map physical disk to VSAN disk.
   
   See Also: `pyVmomi.vim.host.ScsiDisk`
   
   Attributes:
       vsanUuid: Disk UUID in VSAN
       formatVersion: VSAN file system version number
   """
   vsanUuid: str
   formatVersion: int


class VsanDiskManagementSystemCapability(pyVmomi.vmodl.DynamicData):
   version: str

class VsanDiskTrimOption:
   """This class represents a list of supported vSAN disk trim options."""
   pass

class VsanDiskType:
   """vSAN disk types."""
   pass

class VsanDiskgroupCapability:
   """This class represents a list of supported vSAN diskgroup capability types."""
   pass


class VsanHostCapability(pyVmomi.vmodl.DynamicData):
   """
   vSAN feature capability of specific host.
   
   It is used to for a specific vSAN feature,
   to present whether it is supported by software and
   license.
   
   Attributes:
       host: Target host.
       isSupported: Whether specific feature is supported by the
           software of host.
       isLicensed: Whether specific feature is activated by in-use license.
   """
   host: pyVmomi.vim.HostSystem
   isSupported: bool
   isLicensed: bool


class VsanManagedDisksInfo(pyVmomi.vmodl.DynamicData):
   """
   This class includes the information of vSAN disk mapping, storage pool
   disk for vSAN datastore and the vSAN direct storages like VMFS datastores
   backing by SCSI disks.
   
   The vSAN direct storages are the host local
   storages managing by vSAN though it doesn't contribute storage resource to
   vSAN datastore. For vSAN datastore disks, either disk mapping or storage
   pool disk can be present in the result, except during host upgrade and DFC.
   
   Attributes:
       vSANDirectDisks: vSAN direct disks, which are claimed from the vSAN API
           `pyVmomi.vim.cluster.VsanVcDiskManagementSystem.initializeDiskMappings`
       vSANDiskMapInfo: vSAN disk mapping information for vSAN datastore.
       vSANPMemInfo: vSAN managed PMem information.
       storagePools: vSAN storage pool information.
   """
   vSANDirectDisks: list[VsanDirectStorage] = []
   vSANDiskMapInfo: list[DiskMapInfoEx] = []
   vSANPMemInfo: _typing.Optional[VsanManagedPMemInfo] = None
   storagePools: list[StoragePoolInfo] = []


class VsanManagedPMemInfo(pyVmomi.vmodl.DynamicData):
   """
   Deprecated: as of vSphere 9.0 APIs with no replacement.This class includes the information of vSAN managed PMem
   storage.
   
   Attributes:
       localPMemDatastores: vSAN managed local PMem datastore(s).
   """
   localPMemDatastores: list[pyVmomi.vim.Datastore] = []


class VsanObjectProfileInfo(pyVmomi.vmodl.DynamicData):
   """
   This data object type describes vSAN object and its SPBM profile
   information
   
   Attributes:
       vsanObjectUuid: vSAN object uuid
       spbmProfileId: spbmProfile ID
       spbmProfileGenerationNum: spbmProfile generation number
   """
   vsanObjectUuid: str
   spbmProfileId: str
   spbmProfileGenerationNum: int


class VsanObjectSyncState(pyVmomi.vmodl.DynamicData):
   """
   This data object type describes sync state for a vSAN object.
   
   Attributes:
       uuid: Represents the uuid of vSAN object.
       components: The list of components which are in syncing state.
   """
   uuid: str
   components: list[VsanComponentSyncState] = []


class VsanRuntimeInfo(pyVmomi.vmodl.DynamicData):
   """
   This data object contains VSAN cluster runtime information from
   the perspective of the host in question.
   
   This data object is used to represent read-only state whose values
   may change during operation.
   
   Attributes:
       membershipList: This property reports host membership information.
       diskIssues: List of disk issues detected on this host.
           
           To retrieve more information on the issues, use
           `pyVmomi.vim.host.VsanSystem.queryDisksForVsan`.
       accessGenNo: Generation number tracking object accessibility.
   """
   class DiskIssueType(pyVmomi.VmomiSupport.Enum):
      """The list of disk issues."""
      nonExist: _typing.ClassVar['VsanRuntimeInfo.DiskIssueType'] = 'nonExist'
      stampMismatch: _typing.ClassVar['VsanRuntimeInfo.DiskIssueType'] = 'stampMismatch'
      unknown: _typing.ClassVar['VsanRuntimeInfo.DiskIssueType'] = 'unknown'

   class DiskIssue(pyVmomi.vmodl.DynamicData):
      """
      Data structure of reporting a disk issue.
      
      Attributes:
          diskId: Disk uuid, @see vim.host.ScsiLun#uuid
          issue: Type of issue
      """
      diskId: str
      issue: str

   membershipList: list[MembershipInfo] = []
   diskIssues: list[VsanRuntimeInfo.DiskIssue] = []
   accessGenNo: _typing.Optional[int] = None


class VsanScsiDisk(pyVmomi.vmodl.DynamicData):
   """
   This data object type describes a SCSI disk managing by vSAN.
   
   It
   includes a part of SCSI disk information which is useful
   for vSAN like capacity, device name etc for space efficiency
   
   Attributes:
       capacity: The size of SCSI disk using the Logical Block Addressing scheme.
       usedCapacity: The used capacity in byte for this disk.
       devicePath: The device path of the ScsiDisk.
           
           This device path is a file path
           that can be opened to create partitions on the disk.
       ssd: Indicates whether the ScsiDisk is SSD backed.
           
           If unset, the information whether the ScsiDisk is SSD backed
           is unknown.
       localDisk: Indicates whether the ScsiDisk is local.
           
           If unset, the information whether the ScsiDisk is local is unknown.
       scsiDiskType: The types of disk drives.
       uuid: Universally unique identifier for the LUN used to identify ScsiLun across
           multiple servers.
       operationalState: The operational states of the LUN.
           
           When more than one item is present in the array, the first state
           should be considered the primary state. For example, a LUN may
           be \"ok\" and \"degraded\" indicating I/O is still possible to the LUN, but
           it is operating in a degraded mode.
       canonicalName: Canonical name of the SCSI logical unit.
       displayName: User configurable display name of the SCSI logical unit.
       lunType: The type of SCSI device.
           
           Must be one of the values of
           `pyVmomi.vim.host.ScsiLun.ScsiLunType`.
       vendor: The vendor of the SCSI device.
       model: The model number of the SCSI device.
       mountInfo: The mount info for this disk.
   """
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
   """
   This data object type describes results being returned from querying
   syncing vSAN objects.
   
   Attributes:
       totalObjectsToSync: Total number of vSAN objects that are syncing.
           
           It's returned only when
           summary data is needed.
       totalBytesToSync: The amount of data to be re-synced.
           
           It's returned only when summary
           data is needed.
       totalRecoveryETA: The estimated time in seconds to recover all vSAN objects of
           specified types.
           
           It's returned only when summary data is needed.
       objects: The retrieved objects.
       syncingObjectRecoveryDetails: Details returned from querying vSAN syncing objects for different sync
           status.
   """
   totalObjectsToSync: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   totalBytesToSync: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   totalRecoveryETA: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   objects: list[VsanObjectSyncState] = []
   syncingObjectRecoveryDetails: _typing.Optional[VsanSyncingObjectRecoveryDetails] = None


class VsanSyncingObjectRecoveryDetails(pyVmomi.vmodl.DynamicData):
   """
   This data object type describes details returned from querying
   vSAN syncing components for different sync status.
   
   Attributes:
       activelySyncingObjectRecoveryETA: It calculates the estimated time in seconds to recover objects
           actively syncing.
       queuedForSyncObjectRecoveryETA: The estimated time in seconds to recover objects which are in queue and sync/recovery
           has not been started for the objects.
           
           This includes time in wait queue and required
           to finish the sync.
       suspendedObjectRecoveryETA: The estimated time in seconds to recover objects which are in suspended
           state.
           
           Suspended object ETA is predicted based on the current syncing
           bandwidth and it can vary.
       activeObjectsToSync: The number of objects that are actively syncing.
       queuedObjectsToSync: The number of objects which are in queue and
           for which the sync has not been started yet.
       suspendedObjectsToSync: The number of objects which are in suspended state.
       bytesToSyncForActiveObjects: The amount of data in bytes to be synced for the objects which are
           actively syncing.
       bytesToSyncForQueuedObjects: The amount of data in bytes to be synced for the objects which are
           in queue and for which the sync has not been started yet.
       bytesToSyncForSuspendedObjects: The amount of data in bytes to be synced for the objects which are
           in suspended state.
   """
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
   """
   VsanWhatIfEvacDetail represents detail prediction result if one specified
   entity(disk group or host) is evacuated from cluster.
   
   Attributes:
       success: Indicates whether evacuation of specified entity could be done.
       bytesToSync: Indicates how many bytes need to be synced to satisfy the evacuation of
           specified entity.
       inaccessibleObjects: Indicates objects which would be inaccessible due to the evacuation of
           specified entity.
       incompliantObjects: Indicates objects which would be non-compliant due to the evacuation of
           specified entity.
       extraSpaceNeeded: Indicates how many additional storage space is needed for the evacuation
           of specified entity.
       failedDueToInaccessibleObjects: Indicates whether evacuation of specified entity would fail due to
           inaccessible objects.
   """
   success: _typing.Optional[bool] = None
   bytesToSync: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   inaccessibleObjects: list[str] = []
   incompliantObjects: list[str] = []
   extraSpaceNeeded: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   failedDueToInaccessibleObjects: _typing.Optional[bool] = None


class VsanWhatIfEvacResult(pyVmomi.vmodl.DynamicData):
   """
   A WhatIfEvacResult represents the prediction result of what would be
   affected and whether the operation could succeeded if a specified entity
   (disk group or host) is evacuated.
   
   Attributes:
       noAction: Represents the impact and prediction if user choose \"noAction\" evacuation
           mode to evacuate given diskgroup or host.
       ensureAccess: Represents the impact and prediction if user choose
           \"ensureObjectAccessibility\" evacuation mode to evacuate given diskgroup or
           host.
       evacAllData: Represents the impact and prediction if user choose \"evacuateAllData\"
           evacuation mode to evacuate given diskgroup or host.
   """
   noAction: VsanWhatIfEvacDetail
   ensureAccess: VsanWhatIfEvacDetail
   evacAllData: VsanWhatIfEvacDetail

class WipeDiskEligible:
   """Wipe disk eligible."""
   pass

class WipeDiskState:
   """Wipe disk state."""
   pass


class WipeDiskStatus(pyVmomi.vmodl.DynamicData):
   """
   Wipe disk status.
   
   Attributes:
       disk: Disk canonical name to query.
       eligible: Disk eligible for wipe or not.
       ineligibleReason: Disk wipe ineligible reason.
           
           This property is used when disk is ineligible for wipe.
           Includes following reasons:
           The disk is either in use by vSAN OSA disk group,
           or the disk is in use by vSAN ESA storage pool,
           or the disk is ineligible for use by vSAN,
           or the disk does not support sanitize,
           or the disk has wipe ongoing.
       wipeState: Disk wipe state.
           
           This property is used when disk is being wiped or has been wiped.
           It will be unset when a wiped disk is claimed again in vSAN.
       percentageCompleted: Wipe percentage completed.
           
           This property is used when disk wipe state is \"Wiping\".
       estimatedTime: Estimated time to finish in seconds.
           
           This property is used when disk wipe state is \"Wiping\".
       wipeStartTime: Wipe disk start timestamp (UTC time).
           
           This property is used when disk wipe state is set.
       wipeCompleteTime: Wipe disk complete timestamp (UTC time).
           
           This property is used when disk wipe state is \"Success\", or \"Failure\".
   """
   disk: str
   eligible: str
   ineligibleReason: list[pyVmomi.vmodl.LocalizableMessage] = []
   wipeState: _typing.Optional[str] = None
   percentageCompleted: _typing.Optional[int] = None
   estimatedTime: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   wipeStartTime: _typing.Optional[_datetime.datetime] = None
   wipeCompleteTime: _typing.Optional[_datetime.datetime] = None
