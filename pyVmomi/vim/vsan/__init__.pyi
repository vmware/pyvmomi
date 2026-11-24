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



class DirectoryServerConfig(pyVmomi.vmodl.DynamicData):
   """
   The directory server configuration which can be used to communicate and
   authenticate with a directory server.
   """
   pass


class ActiveDirectoryServerConfig(DirectoryServerConfig):
   """
   The Active Directory server configuration which can be used to communicate and
   authenticate with a Microsoft Active Directory server.
   
   Attributes:
       activeDirectoryDomainName: Microsoft Active Directory Domain name which will be used for
           authentication for Kerberos based NFS share and SMB shares.
           
           The
           active directory domain name should be of the form 'example.com'.
       username: Username that is used to connect and configure the directory service.
           
           This user is required to have sufficient privileges in provided
           Organizational Unit to:
           - Create and delete Computer Objects.
           - Read and Write ms-DS-PrincipleName.
           - Read and Write uPNSuffixes.
       password: Password for the domain user.
       organizationalUnit: Active Directory's Organizational Unit.
           
           This is where all file server
           computer objects will be created. If it is not specified while creating
           File Service Domain, by default Computers OU will be used.
           We recommend an OU must be pre-created in Active Directory and default
           Computers OU should not be used. Best way to get your OU name right is
           by following below convention:
           https://support.microsoft.com/en-in/help/909264/naming-conventions-in-active-directory-for-computers-domains-sites-and
           As best practice for security and manageability, we recommend:
           - Create a dedicated OU for vSAN file service.
           - Create a basic domain user.
           - Mark the OU managed by this domain user.
             
           Note in the case of nested OU, \"/\" can be used as separator.
       preferredADServers: Preferred AD servers which are used to do username/password validation.
           
           IP or FQDN is required for each AD server. For now, only IP
           format is supported.
   """
   activeDirectoryDomainName: _typing.Optional[str] = None
   username: _typing.Optional[str] = None
   password: _typing.Optional[str] = None
   organizationalUnit: _typing.Optional[str] = None
   preferredADServers: list[str] = []


class DatastoreConfig(pyVmomi.vmodl.DynamicData):
   """
   The datastore configuration of a vSAN cluster.
   
   Attributes:
       datastores: The list of non-default vSAN datastores.
   """
   datastores: list[DatastoreSpec] = []


class AdvancedDatastoreConfig(DatastoreConfig):
   """
   The advanced vSAN datastore configuration.
   
   This data type extendes original `pyVmomi.vim.vsan.DatastoreConfig`, which
   which provides datastore management limited to local vSAN datastores.
   With the new data type, we can not only manage local vSAN datastores,
   but also mount remote vSAN datastores hosted in server clusters.
   
   Attributes:
       remoteDatastores: The remote vSAN datastores to be mounted to target vSAN cluster, which
           are provided by other vSAN clusters.
           
           All in use remote vSAN datastores of target vSAN cluster will be unmounted
           if this field is omitted.
   """
   remoteDatastores: list[pyVmomi.vim.Datastore] = []


class AutoRAIDConfig(pyVmomi.vmodl.DynamicData):
   """
   vSAN auto RAID configuration.
   
   Attributes:
       assumeAutoManagedRAID: Whether to assume all storage policies as auto RAID.
           
           By default, it will be
           set to true for enabling ESA cluster and false for disabling ESA cluster.
   """
   assumeAutoManagedRAID: bool


class AutoRAIDInfo(pyVmomi.vmodl.DynamicData):
   """
   Failure tolerance is determined together with hostFailuresToTolerate and subFailuresToTolerate.
   
   For standard cluster, subFailuresToTolerate is unset. Failure tolerance is determined by
   hostFailuresToTolerate.
   
   hostFaiuresToTolerate
    - subFailuresToTolerate
    - Failure tolerance
   
   0
    - unset
    - 0
   
   1
    - unset
    - 1
   
   2
    - unset
    - 2
   For stretched cluster, subFailuresToTolerate determines failure tolerance in site.
   hostFailuresToTolerate determines mirroring or not between sites.
   
   hostFaiuresToTolerate
    - subFailuresToTolerate
    - Site mirroring
    - Failure tolerance in site
   
   0
    - 0
    - No
    - 0
   
   0
    - 1
    - No
    - 1
   
   0
    - 2
    - No
    - 2
   
   1
    - 0
    - Yes
    - 0
   
   1
    - 1
    - Yes
    - 1
   
   1
    - 2
    - Yes
    - 2
   
   Attributes:
       hostFailuresToTolerate: hostFailuresToTolerate value
       subFailuresToTolerate: subFailuresToTolerate value
   """
   hostFailuresToTolerate: pyVmomi.VmomiSupport.long
   subFailuresToTolerate: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class CapacityReservationInfo(pyVmomi.vmodl.DynamicData):
   """
   Specify various capacity reservation information.
   
   Specified capacity will be reserved at the cluster level.
   
   Attributes:
       hostRebuildThreshold: Controls whether the host rebuild threshold is reported to the
           Capacity View and whether vSAN reserves capacity in the cluster
           to be able to repair objects after a host failure.
           
           If hostRebuildState is set to enforced and capacitity usage goes
           beyond the host rebuild threshold, vSAN will fail to create Virtual
           Machines, Virtual Disks, Snapshots, etc. But IO from existing
           Virtual Machine will not be failed.
           - Default value: Reported
       vsanOpSpaceThreshold: Controls whether the vSAN operation space threshold is reported
           to the Capacity View and whether vSAN reserves capacity in the
           cluster to be able to perform internal operations.
           
           If vsanOpSpaceState is set to enforced and capacitity usage goes
           beyond the vSAN operation space threshold, vSAN will fail to
           create Virtual Machines, Virtual Disks, Snapshots, etc. But IO
           from existing Virtual Machine will not be failed.
           - Default value: Reported
   """
   hostRebuildThreshold: _typing.Optional[str] = None
   vsanOpSpaceThreshold: _typing.Optional[str] = None

class CapacityReservationState:
   """Capacity reservation state."""
   pass


class DatastoreSpec(pyVmomi.vmodl.DynamicData):
   """
   The configuration information of a vSAN datastore.
   
   Attributes:
       uuid: The UUID of the datastore.
       name: The user friendly name of the datastore.
   """
   uuid: str
   name: str


class ClientDatastoreConfig(DatastoreSpec):
   """
   This represents a single local vSAN datastore in the server cluster and
   the list of client clusters mounting it.
   
   This is read only and shouldn't be set by users.
   
   Attributes:
       clusters: The client clusters which mount the vSAN datastore.
   """
   clusters: list[pyVmomi.vim.ClusterComputeResource] = []


class ClientUnicastConfig(pyVmomi.vmodl.DynamicData):
   """
   Data type to present unicast configuration of client clusters.
   
   Attributes:
       unicastInfo: The list of client clusters' unicast information.
   """
   unicastInfo: list[pyVmomi.vim.vsan.host.ClientClusterUnicastInfo] = []


class ClusterConfigPrecheckItem(pyVmomi.vim.ClusterComputeResource.ValidationResultBase):
   """
   Precheck validation result for cluster configuration.
   
   This is extended from
   `pyVmomi.vim.ClusterComputeResource.ValidationResultBase`
   `pyVmomi.vim.vsan.ClusterConfigPrecheckItem.description` contains the
   description of the precheck validation.
   Once the precheck validation completes, result will be set to one of the possible
   statuses as in `pyVmomi.vim.vsan.VsanHealthStatusType`.
   If any of the precheck validation fails, the reason for the failure is
   available at `pyVmomi.vim.ClusterComputeResource.ValidationResultBase.info`
   This class is currently used by the api
   `pyVmomi.vim.cluster.VsanVcClusterConfigSystem.validateConfigSpec` to return
   results
   
   Attributes:
       status: The status of cluster precheck operation.
           
           Check `pyVmomi.vim.vsan.VsanHealthStatusType` for all possible statuses.
       description: The description of the configuration precheck.
   """
   status: str
   description: _typing.Optional[pyVmomi.vmodl.LocalizableMessage] = None


class ClusterRuntimeInfo(pyVmomi.vmodl.DynamicData):
   """
   Information related to vSAN cluster that is associated with current
   host.
   
   Attributes:
       clusterUuid: The vSAN cluster UUID.
       totalComponentsCount: The number of components for this cluster on the witness host.
       cluster: The vSAN cluster managed object.
   """
   clusterUuid: str
   totalComponentsCount: int
   cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource] = None


class CompatibilityCheckResult(pyVmomi.vmodl.DynamicData):
   """
   The compatibility check result.
   
   Attributes:
       status: The overall status of compatibility check.
           
           The possible statuses are:
           - \"green\": Compatibility check has passed
           - \"red\": Compatibility check has failed.
       message: Informative and localizable message for the compatibility check.
           
           If the check status is 'red', the message will give the deails about the
           failure.
   """
   status: str
   message: _typing.Optional[pyVmomi.vmodl.LocalizableMessage] = None


class ConfigInfoEx(pyVmomi.vim.vsan.cluster.ConfigInfo):
   """
   The extended vSAN configuration information, including cluster level vSAN
   configuration and data efficiency configuration, etc.
   
   Attributes:
       dataEfficiencyConfig: The data efficiency configuration for vSAN.
       resyncIopsLimitConfig: vSAN throttling IOPS limit configuration specification.
       iscsiConfig: vSAN iSCSI configuration.
       dataEncryptionConfig: The data encryption configuration for vSAN.
       extendedConfig: vSAN extended configurations.
       datastoreConfig: vSAN datastore configuration.
       perfsvcConfig: vSAN performance service configuration.
       unmapConfig: SCSI unmap command configuration on vSAN.
       vumConfig: vSAN build recommendation engine configuration for this vSAN cluster.
           
           Build recommendation engine would use it to generate different baselines for
           this vSAN cluster.
           See `pyVmomi.vim.vsan.VsanVumConfig`
       fileServiceConfig: vSAN file service configurations.
       metricsConfig: vSAN metrics configuration for all monitor clients
       rdmaConfig: RDMA Spec for vSAN.
       dataInTransitEncryptionConfig: Data-in-transit encryption configuration for the vSAN cluster.
       vsanHealthConfig: vSAN Health configuration.
       mode: Mode for vSAN.
       vsanPMemConfig: vSAN PMem configuration.
       vsanEsaConfigInfo: Configuration info for vSAN ESA.
       xvcDatastoreConfig: vSAN cross VC datastore configuration.
       serverClusterConfig: Server cluster configuration for HCI Mesh.
       datastoreDefaultPolicySelectionConfig: vSAN datastore default policy selection configurations.
           
           Only available for vSAN ESA
       snapServiceConfig: The configuration for vSAN Snapshot service.
           
           The Snapshot service
           configuration will require specific User role and privileges.
           TODO: Update required privileges and the implementaiton to include the
           necessary validations.
           
           Since: 8.0.0.4
       deconvergedNetConfig: De-converged network configuration for vSAN.
       siteFaultDomainConfig: Configuration of site fault domain for compute only cluster.
       vbossClusterConfig: The cluster level configuration of vSAN vBoss service.
   """
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
   """
   vSAN cyber recovery configuration information.
   
   This configuration
   defines the settings and parameters for cyber recovery operations
   within a vSAN cluster.
   The only option is enabled or not today, but in the future we
   expect more options to be added.
   
   Attributes:
       enabled: Indicates whether cyber recovery is enabled for the vSAN cluster.
   """
   enabled: bool


class DataEfficiencyCapacityState(pyVmomi.vmodl.DynamicData):
   """
   The data structure stores the capacity of data efficiency enabled host.
   
   Attributes:
       logicalCapacity: Total logical capacity in bytes.
       logicalCapacityUsed: Logical capacity used in bytes by aggregating all vSAN disks usage including
           all kinds of overhead.
       physicalCapacity: Total physical capacity in bytes.
       physicalCapacityUsed: Physical capacity used in bytes by aggregating all vSAN disks usage including
           all kinds of overhead.
       dedupMetadataSize: Size of space used for deduplication metadata in bytes.
       spaceEfficiencyMetadataSize: vSAN space efficiency metadata size in bytes.
       esaDedupSpaceSaving: Total space saving in bytes by global deduplication when storing
           regular vSAN objects on vSAN ESA.
           
           Notice it doesn't include the
           space saving from RAID efficiency as we may store the
           deduplicated data with more RAID efficient way. This is only
           valid since 9.0.
       esaCompressionSpaceSaving: Total space saving in bytes by compression when storing regular vSAN objects
           on vSAN ESA.
           
           Notice it doesn't include the space saving from RAID efficiency
           as we may store the compressed data with more RAID efficient way.
           This is only valid since 9.0.
       totalSpaceUsedWithoutOverhead: Total space used in bytes when storing regular vSAN objects on vSAN ESA after
           deduplication and compression, including space used by regular objects and
           dedup store, any other overhead including RAID will be excluded.
           
           This is only valid since 9.0.
       dedupEnabledObjectSpaceUsed: Total space used in bytes of regular vSAN objects with global
           deduplication policy applied in vSAN ESA.
           
           This space used size is calculated
           after deduplication but before compression, any other overhead including RAID
           will be excluded.
   """
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
   """
   The data efficiency configuration of a vSAN cluster.
   
   Data efficiency configurations work together as below.
   
   dedupEnabled
    - compressionEnabled
    - Details
    - State Transition
   
   False
    - False
    -
   - Disable deduplication and compression. Or
   - Disable compression only
     
    -
   - Deduplication and compression -> No data efficiency
   - Compression only -> No data efficiency
     
   None
    - 0
    -
   - Disable compression only if enabled
   - Throw exception if deduplication and compression is enabled
     
    -
   - Compression only -> No data efficiency
   
   None
    - 1
    -
   - Enable compression only
   - Throw exception if deduplication and compression is enabled.
     
    -
   - No data efficiency -> Compression only
   
   0
    - None
    -
   - Disable deduplication and compression
   - Throw exception if compression only is enabled
     
    -
   - Deduplication and compression -> No data efficiency
   
   1
    - 1
    -
   - Enable deduplcation and compression
   - Disable compression only if already enabled
   - Get `pyVmomi.vim.vsan.cluster.ConfigInfo` will return compressionEnabled flag as true
     
    -
   - No data efficiency -> Deduplication and compression
   - Compression only -> Deduplication and compression
     
   1
    - 0
    -
   - Enable deduplication and compression
   - Disable compression only if already enabled
   - Get `pyVmomi.vim.vsan.cluster.ConfigInfo` will return compressionEnabled flag as True
     
    -
   - No data efficiency -> Deduplication and compression
   - Compression only -> Deduplication and compression
     
   0
    - 1
    -
   - Enable compression only
   - Disable deduplication and compression
     
    -
   - Deduplication and compression -> Compression only
   - No data efficiency -> Compression only
     
   1
    - None
    -
   - Enable deduplication and compression
   - Disable compression only if already enabled
   - Get `pyVmomi.vim.vsan.cluster.ConfigInfo` will return compression only flag as True
     
    -
   - No data efficiency -> deduplication and compression
   - Compression only -> deduplication and compression
   
   Attributes:
       dedupEnabled: Enables data deduplication and compression on the vSAN cluster.
           
           The
           behaviour of this flag is described in the table above.
       compressionEnabled: Enables compression on the vSAN cluster.
           
           For vSAN OSA, the behaviour of this flag is the same as compressionEnabled
           in the table above.
           For vSAN ESA, compression is enabled by default since 9.1.0 release, disabling
           compression is not supported.
   """
   dedupEnabled: bool
   compressionEnabled: _typing.Optional[bool] = None


class DataEfficiencyConfigEx(DataEfficiencyConfig):
   """
   DataEfficiencyConfigEx extends `pyVmomi.vim.vsan.DataEfficiencyConfig`
   
   Attributes:
       dedupStoreUuid: The UUID of the global deduplication store that is used to store
           deduplicated data.
           
           Do not set this field when enabling global deduplication because
           this field will be generated automatically by vSAN. There is rare
           use case to put a valid global deduplication store uuid here, for
           example, when restoring configuration for the cluster from
           existing running hosts.
       dedupPaused: Pause/continue the data deduplication service.
           
           Deduplication configurations work together as below.
           
           dedupEnabled
            - dedupPaused
            - Details
            - State Transition
           
           1 or 0
            - 1
            -
           - Pause the deduplication service if already enabled, it only applies to vSAN ESA
           - Stop to enable the deduplication service if not enabled, it only applies to vSAN ESA
             
            -
           - Deduplication enabled -> Deduplication service paused
           - Deduplication not initialized -> Deduplication service paused 
             
           1 or 0
            - 0
            -
           - Continue the ESA deduplication service if already enabled, it only applies to vSAN ESA
           - Restart to enable the deduplication service if not enabled, it only applies to vSAN ESA
             
            -
           - Deduplication service paused -> Deduplication enabled
           - Deduplication service paused -> Deduplication initialization
   """
   dedupStoreUuid: _typing.Optional[str] = None
   dedupPaused: _typing.Optional[bool] = None


class DataEncryptionConfig(pyVmomi.vmodl.DynamicData):
   """
   The data encryption spec of a vSAN cluster.
   
   Attributes:
       encryptionEnabled: Is data encryption enabled on the cluster?
           Enabling encryption on a cluster will proceed to encrypt all the hosts.
           
           Progress of this can be tracked by the changing flag and the reconfigure
           task.
           Disabling encryption, will expose all previously encrypted data in the
           clear.
       kmsProviderId: The Id of the KMS cluster to use for vSAN Encryption.
           
           Keys will be created on
           and used from this KMS. This parameter is ignored if encryption is disabled.
           It must be set to a valid KMS cluster ID if encryption is enabled.
           When it is already an encrypted vSAN cluster and a different value of
           kmsProviderId is provided, it will switch to the new KMS cluster as specified
           by new kmsProviderId. A new KEK Id will also be created in the new KMS
           cluster and a shallow rekey is performed to use the new KEK.
           See `pyVmomi.vim.encryption.CryptoManagerKmip.kmipServers` and
           `pyVmomi.vim.encryption.KmipClusterInfo`
       kekId: The KEK Id of the KMS cluster to use.
           
           Do not set a key's Id for this when reconfiguring vSAN encryption,
           because such key will be created automatically from key management server.
           There is rare use case to put a valid key Id here, for example, when
           restoring configuration for the cluster from existing running hosts.
       hostKeyId: The Id of host key which is used for host core dump encryption.
           
           Do not set this value when reconfiguring vSAN encryption, because
           such key will be created automatically from key management server.
       dekGenerationId: DEK generation number of the vSAN cluster.
           
           Do not set a generation number for this when reconfiguring vSAN
           encryption because such a field will be created and managed automatically
           by vSAN.
       changing: Whether Encryption has finished enabling or disabling operation.
           
           When changing is true, then encryption has not finished enabling or
           disabling. Changing will become false once all hosts currently in
           the cluster have adapted to the current setting of encryptionEnabled.
           No guarantee can be made that all data will be encrypted
           until changing is false and encryptionEnabled is true.
           This value can be read, but should never be set by API callers
           Reconfiguring a cluster.
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
       syncing: Whether the cluster is syncing encryption config when it enables encryption
           or does deep rekey.
   """
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
   """
   The data-in-transit encryption spec of a vSAN cluster.
   
   Attributes:
       enabled: Whether data-in-transit encryption is enabled in the cluster.
       rekeyInterval: Periodical rekeying interval in minutes.
           
           Default interval is 1440, i.e. 24 hours.
           Minimal interval is 30 minutes and maximum is 10080, i.e. 7 days.
       state: Transition state is read-only property which is used to mark intermediate
           stages during data-in-transit configuration change for a vSAN cluster.
           
           Refer to `pyVmomi.vim.vsan.host.EncryptionTransitionState`
   """
   enabled: _typing.Optional[bool] = None
   rekeyInterval: _typing.Optional[int] = None
   state: _typing.Optional[str] = None


class DataProtectionHealthSystem(pyVmomi.VmomiSupport.ManagedObject):
   """
   This managed object provides access to Data Protection (DP) Health related
   configuration and query APIs, operating at the vCenter or cluster level.
   
   It can be accessed via the MOID of 'dp-health-system' through vSAN service
   at vCenter server side.
   """
   def QueryHealthSummary(self, cluster: pyVmomi.vim.ClusterComputeResource) -> pyVmomi.vim.cluster.VsanClusterHealthSummary:
      """
      Query Data Protection (DP) health data and generate health checks.
      
      It's the primary API for fetching latest DP health status.
      This API doesn't support host level call and will throw exception in that case.
      The DP health summary is pushed from the DP appliance and stored in memory by the vSAN health service.
      If the DP appliance is offline or experiences a loss of connectivity,
      the vSAN health service will be unable to provide the most current DP health data.
      However, if the vSAN health service is restarted, it will first load the
      most recent available DP health status from the historical health database.
      It will then update the health status once new data is received from the DP appliance,
      which typically occurs after a few minutes.
      
      Args:
          cluster: The target cluster.
      
      Returns:
          Returns a health summary data object, containing the current DP health status.
      
      Raises:
          pyVmomi.vim.fault.VsanFault: If any runtime error is hit.
          pyVmomi.vmodl.fault.NotSupported: If the API is called at the host level.
      """
      ...
   def QueryHistoricalHealth(self, spec: pyVmomi.vim.cluster.VsanHistoricalHealthQuerySpec) -> list[pyVmomi.vim.cluster.VsanClusterHealthSummary]:
      """
      Query Data Protection (DP) historical health information based on the query spec.
      - Query general DP historical health summary.
        If no groupId and testId specified in the query spec,
        it aggregates all the historical DP health status
        for the given time range. Then returns a general DP health summary
        with only overallHealth, test group IDs, group healths,
        test IDs and test healths.
      - Query DP health status history for a certain DP health check.
        If groupId and testId are specified, and start time doesn't
        equal to end time, the result will only contain the historical
        testHealths for the given time range of the target health check.
      - Query a snapshot detail for a certain DP health check.
        If groupId and testId are specified, and start time equals to
        end time, the result will contain a full testDetail for the certain
        timestamp of the target DP health check.
      - Query overall DP health trend during the given time range.
        If both groupId and testId are specified to \"#\" in the query spec,
        the result will contain a series of DP health summaries with
        overallHealth, healthStatusCounts and timestamp within the given time range.
      
      Args:
          spec: The query spec.
      
      Returns:
          DP health summary with historical information.
      
      Raises:
          pyVmomi.vim.fault.NotFound: A NotFound error occurs when a referenced component of a managed
              object cannot be found.
              
              The referenced component can be a data
              object type (such as a role or permission) or a primitive
              (such as a string).
              
              For example, if the missing referenced component is a data object, such as
              VirtualSwitch, the NotFound error is
              thrown. The NotFound error is also thrown if the data object is found, but the referenced name
              (for example, \"vswitch0\") is not.
          pyVmomi.vmodl.fault.NotSupported: if run directly on an ESX Server host.
          pyVmomi.vmodl.fault.InvalidArgument: Exception for invalid input arguments.
              For example, if the given time range is more than one month,
              or in case the end time is before the start time.
      """
      ...
   def GetDpClusterSilentChecks(self, cluster: pyVmomi.vim.ClusterComputeResource) -> list[str]:
      """
      Get the user configured silent data protection health check list of the cluster.
      
      This API is only supported on the cluster with data protection enabled.
      
      Args:
          cluster: The target cluster which has data protection enabled
      
      Returns:
          The list of all silent health checks testIds
      
      Raises:
          pyVmomi.vim.fault.NotFound: If the cluster is not found.
          pyVmomi.vmodl.fault.NotSupported: If run directly on an ESX Server host.
          pyVmomi.vim.fault.VsanFault: If any runtime error is hit.
      """
      ...
   def SetDpClusterSilentChecks(self, cluster: pyVmomi.vim.ClusterComputeResource, addSilentChecks: list[str], removeSilentChecks: list[str]) -> bool:
      """
      Set silent health check list of the cluster.
      
      Specify [testId/groupId] for 'addSilentChecks' to add add health
      checks to silent list.
      Specify [testId/groupId] for 'removeSilentChecks' to remove health
      checks from silent list.
      To restore the whole silent list, set 'removeSilentChecks' = ['all'].
      After the silent health check list is updated, it is recommended to
      refresh the vSAN cluster data protection health summary to get the updated result.
      The health check items in the silent list should be skipped, and labeled
      with 'skipped' status.
      Note:
      - If groupId is added to silent list, all the checks under this
        group would be silent.
      - If groupId is removed from silent list, all the checks under
        this group would back to normal.
      - If given invalid testId/groupId, it will throw exception.
      - This method will do add first and then remove. So if the given
        health check is in both add and remove list, it would NOT be
        silent in the end.
      - This API is only supported for data protection health checks.
      
      Args:
          cluster: The target data protection protected cluster
          addSilentChecks: The health checks/groups to silent.
          removeSilentChecks: The health checks/groups to restore.
      
      Returns:
          True to indicate the value being set successfully.
          No return otherwise.
      
      Raises:
          pyVmomi.vim.fault.NotFound: If the cluster is not found.
          pyVmomi.vmodl.fault.NotSupported: If run directly on an ESX Server host.
          pyVmomi.vim.fault.VsanFault: If any runtime error is hit.
      """
      ...


class MountPrecheckItem(pyVmomi.vmodl.DynamicData):
   """
   Precheck result for mounting a remote vSAN datastore.
   
   It represents the
   precheck status and reason for a specific type of precheck.
   
   Attributes:
       type: The type of precheck for mounting remote vSAN datastore.
           
           All supported types are defined in below enumerations:
           `pyVmomi.vim.vsan.MountPrecheckType`,
           `pyVmomi.vim.vsan.MountPrecheckTypeDIT`.
       description: The description of precheck for mounting remote vSAN datastore.
       status: The status of precheck for mounting remote vSAN datastore.
           
           Check `pyVmomi.vim.vsan.VsanHealthStatusType` for all possible statuses.
       reason: The reason why the precheck returns unsuccessful result.
           
           It contains the
           error/warning message of the precheck.
       ignoreMessage: The warning information when the item is in \"yellow\" status but user wants
           to ignore it and proceed forcefully.
   """
   type: str
   description: pyVmomi.vmodl.LocalizableMessage
   status: str
   reason: list[pyVmomi.vmodl.LocalizableMessage] = []
   ignoreMessage: list[pyVmomi.vmodl.LocalizableMessage] = []

class DatastoreSourcePrecheckItem(MountPrecheckItem):
   """
   The base class of result item for a Datastore Source precheck.
   
   It is inherited from `pyVmomi.vim.vsan.VsanHealthStatusType`.
   The type is also specified with one of the values about
   Datastore Source prechecks in below enumerations:
   `pyVmomi.vim.vsan.MountPrecheckType`,
   `pyVmomi.vim.vsan.MountPrecheckTypeDIT`.
   
   See Also: `pyVmomi.vim.vsan.MountPrecheckType`, `pyVmomi.vim.vsan.MountPrecheckTypeDIT`
   """
   pass


class MountPrecheckResult(pyVmomi.vmodl.DynamicData):
   """
   Result for all types of remote vSAN mounting prechecks.
   
   Attributes:
       result: A list of precheck results of supported check items.
   """
   result: list[MountPrecheckItem] = []

class DatastoreSourcePrecheckResult(MountPrecheckResult):
   """Result of all prechecks for Datastore Source configuration."""
   pass


class DefaultDatastorePolicySelectionInfo(pyVmomi.vmodl.DynamicData):
   """
   Information related to Default Datastore Policy Selection
   
   Attributes:
       enabled: Is default datastore policy selection enabled
       defaultPolicyId: auto-selected default datastore policy Id
       lastPolicySelectionTime: Last default datastore policy auto-selection timestamp (UTC time).
   """
   enabled: bool
   defaultPolicyId: _typing.Optional[str] = None
   lastPolicySelectionTime: _typing.Optional[_datetime.datetime] = None


class DiskClaimConfiguration(pyVmomi.vmodl.DynamicData):
   """
   Represents disk configuration to be claimed for vSAN ESA.
   
   User can specify the desired disk configuration which can be claimed
   by vSAN. They can specify attributes like disk name prefix, disk
   model, disk vendor, number of disks etc.,
   
   Attributes:
       diskType: Specify the vSAN ESA storage tier to which the disks should be added
           to.
           
           For eg, to add disks to single tier storage pool, specify
           'SingleTier' in the diskType attribute. Please see
           `pyVmomi.vim.vsan.host.StoragePoolDiskType` for supported vSAN ESA
           storage tiers.
       diskNamePrefix: All disks starting with prefix or matching the disk name specified
           in this attribute will be claimed.
           
           For eg, if `diskNamePrefix = naa`,
           then all disks with disks starting with prefix `naa` will be claimed.
           If `diskNamePrefix = mpx.vmhba0:C0:T4:L0`, all disks matching
           this disk name will be claimed on all hosts in the vSAN cluster.
       numberOfDisks: This attribute can be used to specify number of disks to be
           claimed on every host in the cluster.
       diskModel: This attribute can be used to specify disk model to be
           claimed on every host in the cluster.
       vendor: This attribute can be used to specify disks belonging to a
           particular vendor type to be claimed on every host in the cluster.
       diskCapacity: Specify disk capacity in MegaByte (MB).
           
           Disks of specified size will be
           claimed on all hosts in the cluster.
   """
   diskType: str
   diskNamePrefix: _typing.Optional[str] = None
   numberOfDisks: _typing.Optional[int] = None
   diskModel: _typing.Optional[str] = None
   vendor: _typing.Optional[str] = None
   diskCapacity: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class ResourceCheckTaskDetails(pyVmomi.vmodl.DynamicData):
   """
   The detailed information of a running task that is related to resource check.
   
   The task could be the resource check task itself, or the parent task if
   the resource check is launched by a parent task.
   
   Attributes:
       task: The managed object of the task.
       host: The managed object of the host on which the task is running.
       hostUuid: The vSAN UUID of the host on which the task is running.
       maintenanceSpec: The host maintenance spec specifying the data evacuation mode that
           the task is running with.
   """
   task: pyVmomi.vim.Task
   host: _typing.Optional[pyVmomi.vim.HostSystem] = None
   hostUuid: _typing.Optional[str] = None
   maintenanceSpec: _typing.Optional[pyVmomi.vim.host.MaintenanceSpec] = None


class DiskDataEvacuationResourceCheckTaskDetails(ResourceCheckTaskDetails):
   """
   The detailed information of a resource check task for disk/disk-group
   data evacuation (i.e.
   
   the resource check in which
   `pyVmomi.vim.vsan.ResourceCheckSpec.operation` is \"DiskDataEvacuation\").
   
   Attributes:
       diskUuid: If `pyVmomi.vim.vsan.ResourceCheckSpec.operation` is \"DiskDataEvacuation\",
           this will be the vSAN UUID of cache-tier disk or capacity-tier disk in
           a disk-group depending on whether the task is for a disk-group or a disk.
           
           If the task is for a disk-group, this is the vSAN UUID of the cache-tier
           disk in the disk-group.
           If the task is for a disk, this is the vSAN UUID of the corresponding
           capacity-tier disk.
       isCapacityTier: If `pyVmomi.vim.vsan.ResourceCheckSpec.operation` is \"DiskDataEvacuation\",
           this flag indicates whether the task is for a disk-group or just a disk.
           
           If the flag is true, the task is for a capacity-tier disk with vSAN UUID
           in `pyVmomi.vim.vsan.ResourceCheckTaskDetails.hostUuid`; otherwise the task
           is for a disk-group represented by its cache-tier disk with vSAN UUID in
           `pyVmomi.vim.vsan.ResourceCheckTaskDetails.hostUuid`.
           This field could be unset if the backend is not ready to decide on the
           disk tier information (e.g. disk information query takes longer due to
           underlying networking delay) or even not able to get the disk tier
           information (e.g. the host which owns the disk/disk-group gets disconnected
           or not responding).
   """
   diskUuid: _typing.Optional[str] = None
   isCapacityTier: _typing.Optional[bool] = None


class EntityResourceCheckDetails(pyVmomi.vmodl.DynamicData):
   """
   Details about the resource check result for a given entity.
   
   The result
   contains information of current and predicted usage the various
   resources, like capacity, for the entity. For example, for a host result
   contains current and predicted capacity usage and component counts.
   
   Attributes:
       name: The friendly name for this entity.
           
           This is the name specified by user when the entity is created or updated.
       uuid: The vSAN UUID of the entity.
       isNew: The flag indicates whether this is a new resource entity that is recommended
           to be added for more resources in order to make the operation succeed.
           
           For
           example, for a disk group entity the flag indicates whether this is a new
           disk group that is recommended to be added for more resources in order to
           make the operation succeed.
       capacity: The total physical capacity of the entity in bytes.
           
           For example, host
           capacity will be sum of all disk-group's capacity on the host.
           If `pyVmomi.vim.vsan.EntityResourceCheckDetails.isNew` is true,
           the currentUsage is set to 0 since this a recommendation for adding
           new resource.
       postOperationCapacity: The predicted total physical capacity of the resource entity in bytes after
           the operation is done.
           
           For example, if the resource check is for host enter
           maintenance mode operation the capacity which host was contributing will be
           removed from the fault domain's total physical capacity.
       usedCapacity: The current physical usage of the entity in bytes.
           
           If `pyVmomi.vim.vsan.EntityResourceCheckDetails.isNew` is true,
           the currentUsage is set to 0.
       postOperationUsedCapacity: The predicted physical usage of the resource entity in bytes after the
           operation is done.
           
           For example, if the resource check is for host enter
           maintenance mode operation, vSAN will simulate the disk usage after the
           given host enters maintenance mode.
           If vSAN deduplication and compression is enabled during the operation,
           vSAN simulation will not take this into consideration and thus will make
           a conservative estimation of the post-operation disk usage with data
           non-deduplicated and uncompressed.
           If vSAN deduplication and compression is disabled during the operation,
           vSAN simulation will use the average of current deduplication/compression
           rate of all disk-groups in the cluster to estimate the inflation of data
           for a rough calculation of the post-operation disk usage.
       additionalRequiredCapacity: vSAN's recommendation for additional capacity for this entity to be added
           in order to make the operation succeed.
           
           This will be sum of all child
           entitie's additionalRequiredCapacity required. For example, host's
           additional capacity will be sum of all disk-group's additional capacity
           on the host.
       maxComponents: Number of maximum vSAN components this entity can hold.
       components: Predicted number of vSAN components on this entity post operation.
   """
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


class DiskGroupResourceCheckResult(EntityResourceCheckDetails):
   """
   The vSAN disk group level resource check report.
   
   It includes the resource
   check result of all disks in the disk group. Please see
   `pyVmomi.vim.vsan.DiskResourceCheckResult` for disk resource check details.
   If `pyVmomi.vim.vsan.EntityResourceCheckDetails.isNew` is true, this is a
   new disk group suggested to be added by vSAN simulation for more resources
   to make the operation succeed. In this case,
   `pyVmomi.vim.vsan.EntityResourceCheckDetails.isNew` for all disks in this
   disk-group is also true.
   
   Attributes:
       cacheTierDisk: The detailed resource check result for the cache tier disk
           in the disk group.
       capacityTierDisks: The detailed resource check result for the capacity tier disks
           in the disk group.
   """
   cacheTierDisk: _typing.Optional[DiskResourceCheckResult] = None
   capacityTierDisks: list[DiskResourceCheckResult] = []


class DiskInfo(pyVmomi.vmodl.DynamicData):
   """
   Disk information including disk UUID, disk name and
   disk type (SSD or HDD).
   
   Attributes:
       diskUuid: Disk UUID.
       diskName: Disk name.
       isSsd: Flag if the disk is SSD.
           
           Unset if the disk type can not be determined.
   """
   diskUuid: str
   diskName: str
   isSsd: _typing.Optional[bool] = None

class DiskResourceCheckResult(EntityResourceCheckDetails):
   """
   The vSAN disk level resource check report.
   
   It includes basic disk info,
   current disk usage and the predicted disk usage after the queried
   operation is performed `pyVmomi.vim.vsan.EntityResourceCheckDetails`.
   For example, if the queried resource check is for host enter maintenance
   mode operation, vSAN will simulate the disk usage after the queried host
   enters maintenance mode. This will provide user a sense of what the disk
   usage will look like if the queried operation is carried out.
   If `pyVmomi.vim.vsan.EntityResourceCheckDetails.isNew` is true, this is a new
   disk suggested to be added by vSAN simulation for more resources to make the
   operation succeed. In this case, currentUsage will be 0 and
   postOperationUsage will show how the new disk will be used assuming the
   queried operation is done from vSAN simulation.
   If `pyVmomi.vim.vsan.EntityResourceCheckDetails.isNew` is false, this is an
   existing disk in the current cluster. postOperationUsage will give the
   usage of the disk assuming the queried operation is done from vSAN
   simulation.
   """
   pass


class DpDaemonHealth(pyVmomi.vmodl.DynamicData):
   """
   This class defines health status of the DP daemon on the host.
   
   Attributes:
       host: Host instance
       name: Daemon name.
       status: Host daemon status is running, stopped or unknown.
   """
   host: pyVmomi.vim.HostSystem
   name: str
   status: str


class EntityCompatibilityResult(pyVmomi.vmodl.DynamicData):
   """
   Represent the overall compatibility status and incompatible
   reasons of a target entity.
   
   Attributes:
       entity: Target entity, either host or cluster
       compatible: Overall compatibility status of this target.
       incompatibleReasons: A list of messages to indicate detailed information about target
           incompatibile reason.
       extendedAttributes: A list of extended attributes to present extra information of target entity.
   """
   entity: pyVmomi.vim.ManagedEntity
   compatible: bool
   incompatibleReasons: list[pyVmomi.vmodl.LocalizableMessage] = []
   extendedAttributes: list[pyVmomi.vmodl.KeyAnyValue] = []


class FaultDomainResourceCheckResult(EntityResourceCheckDetails):
   """
   The fault domain level resource check report.
   
   It includes the resource check
   result of all hosts in this fault domain. Please see
   `pyVmomi.vim.vsan.HostResourceCheckResult` for host resource check details.
   If `pyVmomi.vim.vsan.EntityResourceCheckDetails.isNew` is true, this is a
   new fault domain suggested to be added by vSAN simulation for more resources
   to make the operation succeed. In this case,
   `pyVmomi.vim.vsan.EntityResourceCheckDetails.isNew` for all hosts in this fault
   domain is also true.
   
   Attributes:
       hosts: The detailed resource check result for hosts in the fault domain.
   """
   hosts: list[HostResourceCheckResult] = []


class FileServiceConfig(pyVmomi.vmodl.DynamicData):
   """
   The file service configuration for a vSAN cluster, including
   whether file service is enabled or not, the memory and CPU configuration for
   file service backend part and virtual machine, etc.
   
   Attributes:
       enabled: Indicates whether file service is enabled in the vSAN cluster.
       fileServerMemoryMB: The reserved memory used by VDFS backend services, like server, proxy and
           sockrelay.
           
           The unit is MB. The default and minimum value is 960. This
           reconfiguration takes effect during enabling file service. That means,
           file service should be disabled firstly if it is running.
       fileServerCPUMhz: The reserved CPU used by VDFS backend services, like server, proxy and
           sockrelay.
           
           The units is MHZ. The default value is 0, which means no dedicated
           CPU resources is bound. This reconfiguration takes effect during enabling
           file service. That means, file service should be disabled first if it is
           running.
       fsvmMemoryMB: The reserved memory used by vSAN file service virtual machines.
           
           The unit is
           MB. The default and minimum values is 2048. This reconfiguration takes
           effect during enabling file service. That means, file service should be
           disabled first if it is running.
       fsvmCPU: CPU cores configured for vSAN File Service Virtual Machine(by default is 2).
           
           This reconfiguration takes effect during enabling file service. That means,
           file service should be disabled first if it is running.
       network: The network that the file service will be deployed on to provide file
           access.
           
           Please note the security setting of this network will be updated
           with forged transmit and promiscuous mode enabled.
       domains: The list of domains created.
           
           The first element of this list is
           the default domain. Leave this field empty when there is no domain to be
           configured with the file service enable process.
       fileAnalyticsEnabled: Indicates whether file analytics is enabled in the vSAN cluster.
   """
   enabled: bool
   fileServerMemoryMB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   fileServerCPUMhz: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   fsvmMemoryMB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   fsvmCPU: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   network: _typing.Optional[pyVmomi.vim.Network] = None
   domains: list[FileServiceDomainConfig] = []
   fileAnalyticsEnabled: _typing.Optional[bool] = None

class FileServiceConfigOpType:
   """Enumeration of the allowed access type."""
   pass


class FileServiceDomain(pyVmomi.vmodl.DynamicData):
   """
   VsanFileServiceDomain is the data object type reflecting the properties
   of a vSAN file service domain.
   
   This type provides the UUID of the file
   service domain, and its configuration.
   
   Attributes:
       uuid: UUID of the vSAN file service domain represented in hexadecimal string.
       config: Configuration of this vSAN file service domain, including the name,
           securityFlavor, fileServerIpConfig, etc.
           
           This property is set when the vSAN file service domain is created or
           reconfigured.
   """
   uuid: str
   config: _typing.Optional[FileServiceDomainConfig] = None


class FileServiceDomainConfig(pyVmomi.vmodl.DynamicData):
   """
   A vSAN File Service Domain is unique namespace.
   
   Network and security
   configuration can be uniquely set for this namespace. One or more file shares
   be managed with this namespace. A file service domain may be integrated with
   a Directory Service like Microsoft Active Directory, although this
   integration is not mandatory.
   Note: vSAN File Service doesn't support mix mode for IPv4 + IPv6 network, so
   it will report error if both IPv4 and IPv6 configurations are detected.
   
   Attributes:
       name: The vSAN File Service domain name should be unique within a vSAN cluster,
           Any valid unique identifier can be used as name.
           
           No white spaces and special
           characters(except _ - .) with length of the domain name limited to 80 char.
           It is not necessary to associate this domain with any Directory Service (AD
           domain).
           This field is required for domain creation.
       dnsServerAddresses: The IP address of DNS server address, which is used to resolve the hostnames
           within the DNS domain.
           
           Providing this parameter is a must for file service
           domain creation operation.
       dnsSuffixes: The list of DNS suffixes which can be resolved by the DNS servers.
           
           An
           exhaustive list of all DNS domains and subdomains from where clients can
           access the file shares must be provided. Providing this parameter is a must
           for file service domain creation operation.
       fileServerIpConfig: Define a pool of IP addresses that will be used by vSAN File Service to
           provide file access from multiple file server.
           
           Each file server will be bound
           to one of the IP configurations in the IP pool and serve the NFS requests.
           A minimum of one such address is needed, more may be required based on load
           and number of shares. To evenly spread the workload, it is recommended to
           have equal (or greater) number of IP addresses than the number of hosts in
           the cluster. All the IP address will be required to be on the same subnet.
           One primary IP must be specified for the NFS referral server. All the file
           shares on vSAN file service can be listed and accessed with this primary IP.
           When a referral is encountered, the NFS client will automatically receive the
           actual managing file server location from referral server with the primary
           IP.
           This field is required for domain creation.
       directoryServerConfig: The directory server integrated with for the domain.
           
           If Directory server
           configuration is provided NFS shares can be configured with KRB5
           authentication, otherwise only AUTH_SYS(sys or unmanaged client) configs
           are allowed.
       version: The domain config version.
           
           It is recommended to leave this field unset to let
           the domain configuration negotiated between the vCenter and ESXi.
   """
   name: _typing.Optional[str] = None
   dnsServerAddresses: list[str] = []
   dnsSuffixes: list[str] = []
   fileServerIpConfig: list[FileServiceIpConfig] = []
   directoryServerConfig: _typing.Optional[DirectoryServerConfig] = None
   version: _typing.Optional[str] = None


class FileServiceDomainQuerySpec(pyVmomi.vmodl.DynamicData):
   """
   Specification for querying vSAN file service domain information.
   
   If an empty
   specification is provided then all the file service domain information will
   be returned.
   If any field is present, then only the domain matching the field query will
   be returned from the query spec.
   
   Attributes:
       uuids: List of the vSAN file service domain UUIDs to be queried.
       names: List of vSAN file service domain names to be queried.
   """
   uuids: list[str] = []
   names: list[str] = []


class FileServiceIpConfig(pyVmomi.vim.host.IpConfig):
   """
   The vSAN File Service IP configuration that is to be bound with the file
   service instance.
   
   For IPv6 configuration part, see
   `pyVmomi.vim.host.IpConfig.IpV6AddressConfiguration`, only the first element of
   list ipV6Address will be chosen if multiple IPv6 addresses are configured.
   And only ipAddress and prefixLength fields are valid.
   
   Attributes:
       fqdn: The Full Qualified Domain name (FQDN) to be used with IP addresses for the
           vSAN File Service instance.
           
           Usually it takes the form of 'fs1.example.com'.
           Please note prior mapping of IP address and FQDN is necessary before
           configuring vSAN File Service. This may need to update your DNS records.
           The first component of FQDN is used as netbios name for file service
           instances, so it must be maximum 15 characters in length.
       isPrimary: Whether the IP address is served as the primary IP address for the file
           service.
           
           The file server running with the primary IP will serve as the NFS
           referral server which may point to the file shares served by other file
           servers in this cluster.
           Only one primary IP address is supported in one domain. Default to False.
       gateway: The default IPv4 gateway address for the file service access point.
           
           The
           gateway IP must be the same for all the file servers in this domain.
       affinityLocation: The affinity location for the file server.
           
           This option is only valid under
           the stretched cluster setup. If this field is specified, this file service
           instance will be located in the affinity site when it is available. This file
           server will failover to the other site when its
           affinity site is down but will fail back once it is available.
           If this is a non-stretched cluster, this affinity location will not take
           effect.
       ipv6Gateway: The default IPv6 gateway address for the file service access point.
           
           The
           gateway IP must be the same for all the file servers in this domain.
   """
   fqdn: _typing.Optional[str] = None
   isPrimary: _typing.Optional[bool] = None
   gateway: str
   affinityLocation: _typing.Optional[str] = None
   ipv6Gateway: _typing.Optional[str] = None

class FileServicePreflightCheckScope:
   """Enumeration of preflight check scope."""
   pass

class FileServiceVMStatus:
   """Enumeration of the allowed access type."""
   pass


class FileShare(pyVmomi.vmodl.DynamicData):
   """
   VsanFileShare is the data object type for reflecting the properties of a
   vSAN file share.
   
   This type provides the UUID of the file share, the
   underlying vSAN object mapping information and its configuration
   information.
   
   Attributes:
       uuid: UUID of the vSAN file share represented in hexadecimal string.
       config: Configuration of this vSAN file share, including the name, quota,
           permissions, etc.
           
           This property is set when the vSAN file share is created or reconfigured.
       runtime: Runtime and state information of an active vSAN file service share.
   """
   uuid: str
   config: _typing.Optional[FileShareConfig] = None
   runtime: _typing.Optional[FileShareRuntimeInfo] = None

class FileShareAccessType:
   """Enumeration of the allowed access type."""
   pass


class FileShareConfig(pyVmomi.vmodl.DynamicData):
   """
   Configurations of a file share.
   
   A file share is a root folder that
   is created in file service domain and provide file sharing access
   under the root folder. Multiple users can have remote access to those
   files using protocols like Server Message Block (SMB) or Network File
   System (NFS) protocol.
   
   Attributes:
       name: The name of the file share.
           
           Must be unique within the file service domain.
           The share name cannot exceed 80 characters, and can only contain
           alphabets (A-Z, a-z), numbers (0-9) and '-' character. Every '-' character
           must be immediately preceded and followed by a number or alphabet.
           Consecutive '-'s are not allowed. This configuration is required for file
           share creation.
           This is the visible name in the URL of the file share. For example, a
           SMB file share can be like this:  
           smb://host-address/file-share-name
       domainName: The name of the file service domain the file share belongs to.
           
           This
           configuration is required for file share creation.
       quota: The hard quota configuration at the file share level.
           
           This will be defined in
           nearest MB/GB/TB terms in integer (no space allowed between the number and
           the unit). A valid quota string could be \"10GB\", \"10G\", \"10g\", \"100m\",
           \"100M\", \"1000MB\", etc.
           This will be the hard quota for the file share. A hard quota will fail the
           write I/O right away when the write is exceeding the quota.
           To set an unlimited hard quota for the file share, set the quota value to 0.
           Note that the file share size is still limited by the vSAN datastore size.
       softQuota: The soft quota configuration at the file share level.
           
           This will be defined in
           nearest MB/GB/TB terms in integer (no space allowed between the number and
           the unit). A valid quota string could be \"10GB\", \"10G\", \"10g\", \"100m\",
           \"100M\", \"1000MB\", etc.
           This will be the soft quota for the file share. A soft quota will raise
           alerts which is detected by periodically checks. To set an unlimited soft
           quota for the file share, set the soft quota value to 0.
       labels: The labels attached to the file share.
           
           The label key cannot exceed 250 bytes, cannot be '.' or '..', and cannot
           contain '/' or non-printable characters.
           The label value cannot exceed 1024 bytes.
       storagePolicy: vSAN storage policy for all the vSAN objects that are created
           to back this file share.
           
           vSAN datastore default policy is used
           when this field is not set.
       permission: The network permissions for NFS shares.
           
           CreateFileShare: If this field is not set, then no client can access
           this file share.
           ReconfigureFileShare: If this field is set it will replace all the existing
           permissions on the file share. If it is not set, no
           changes will be done.
       protocols: File Share protocols supported on the share.
           
           Default value is [ NFSv3, NFSv4 ], if protocols is not specified or empty.
       smbOptions: The options of the SMB file share.
       nfsSecType: Security type possible values are krb5, krb5i, krb5p and sys.
           
           Only used for NFS shares. Default value is 'sys'.
           For SMB share this should remain unset.
       affinityLocation: The affinity location for the vSAN File Share.
           
           The file share can
           only be placed on the preferred fault domain or the secondary fault
           domain. If this field is set when the cluster is not a stretched
           cluster, an InvalidArgument will be thrown. To specify the
           affinityLocation, at least two file server IPs should be specified
           to serve the traffic for the preferred and secondary site, respectively.
           Refer to #{vim.vsan.VsanSiteLocationType} for the supported values. In the
           file share reconfiguration workflow, when the affinityLocation is not set, it
           means to leave the original affinityLocation unchanged. Use the
           \\#{vim.vsan.VsanSiteLocationType#None} to remove the current site affinity.
   """
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
   """Enumeration of the file share owner type."""
   pass


class FileShareNetPermission(pyVmomi.vmodl.DynamicData):
   """
   The permission settings of users based on the network information.
   
   These
   settings should include the IP information of the users, permission assigned
   and the user squash information.
   
   Attributes:
       ips: The client IP information the share user entity.
           
           Currently the following IP
           range formats will be supported:
           - Single IPv4 address, e.g., 123.23.23.123
           - The network's IP address with subnet mask, e.g., 123.23.23.0/24
           - IP address ranges specified with '-', e.g., 123.23.23.123-123.23.23.128
           - The string '*' which implies all clients
       permissions: Permissions assigned to the specified user entity.
           
           No permission will be
           assigned to this client matching the IP information if the field is not set.
       allowRoot: Whether to squash the root user or not.
           
           Only takes effect when the net
           permission for the file share is set to READ_WRITE mode.
   """
   ips: str
   permissions: _typing.Optional[str] = None
   allowRoot: _typing.Optional[bool] = None

class FileShareNfsSecType:
   """
   Enumeration of the allowed NFS share security type.
   
   This field is not applicable for SMB file share.
   Kerberos security types is based on following RFC:
   https://tools.ietf.org/html/rfc2203.
   """
   pass

class FileShareProtocol:
   """Enumeration of the allowed file share protocol."""
   pass


class FileShareQueryProperties(pyVmomi.vmodl.DynamicData):
   """
   Defines the set of share properties returned from the
   `pyVmomi.vim.vsan.VsanFileServiceSystem.queryFileShares` API.
   
   The properties
   \\#uuid, #name and
   \\#domainName are always included as they are
   the identifiers of the file share.
   
   Attributes:
       includeBasic: Basic share properties include all properties for a file share, except
           \\#labels,
           \\#usedCapacity and
           \\#vsanObjectUuids.
           
           The default value is True.
       includeUsedCapacity: Specify whether to return #usedCapacity
           property of the share.
           
           The default value is False.
       includeVsanObjectUuids: Specify whether to return #vsanObjectUuids
           property of the share.
           
           The default value is False.
       includeAllLabels: Specify whether to return #labels property of the
           share.
           
           The default value is False. If this field is True, all share labels
           will be returned.
       labelKeys: Specify the label keys to be returned.
           
           This field will be ignored if
           `pyVmomi.vim.vsan.FileShareQueryProperties.includeAllLabels` is set to True.
           If a label key does not exist in a share, the label will not be returned
           with the share. An InvalidArgument will be thrown if the number of label
           keys exceeds 5.
   """
   includeBasic: _typing.Optional[bool] = None
   includeUsedCapacity: _typing.Optional[bool] = None
   includeVsanObjectUuids: _typing.Optional[bool] = None
   includeAllLabels: _typing.Optional[bool] = None
   labelKeys: list[str] = []


class FileShareQueryResult(pyVmomi.vmodl.DynamicData):
   """
   Result for query file share operation.
   
   Attributes:
       fileShares: A list of file shares that matches query criteria.
           
           Note that the number of
           return value will be limited by offset or the limit in the query
           specification and the total number of remaining file shares.
       nextOffset: This field indicates the starting offset for the next query.
           
           If there is no
           more share to be returned, this value is None. If there are more shares after
           this result to be returned, it should be passed to next query. For more
           explanation, see `pyVmomi.vim.vsan.FileShareQuerySpec.offset`
       totalShareCount: The number of file shares created in total.
           
           This value could be used by
           client to decide if there is a need to make further calls for querying
           remaining file shares.
       maxShareCount: This field indicates the maximum number of shares that can be configured
           in the cluster.
           
           This field will only be set in a vSAN ESA cluster.
           
           Since: 8.0.0.4
   """
   fileShares: list[FileShare] = []
   nextOffset: _typing.Optional[str] = None
   totalShareCount: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   maxShareCount: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class FileShareQuerySpec(pyVmomi.vmodl.DynamicData):
   """
   Specification for querying vSAN file share information.
   
   If no information
   other than the domain name has been provided then all the share information
   under this domain will be returned.
   If any field is present, then only the shares matching the field query will
   be returned from the query spec. Due to the pagination mechanism, the file
   shares loaded through different API calls are not guaranteed to be atomic.
   
   Attributes:
       domainName: The name of the domain which the share belongs to.
           
           If not specified, the file
           shares under all the domains will be queried.
       uuids: List of the vSAN file share UUIDs to be queried.
       names: List of vSAN file share names to be queried.
       offset: All file shares are sorted in alphabetical order.
           
           The offset indicates
           the starting element of the file share name. For the query of multiple pages
           the value should be the nextOffset of the return value of the last query. For
           more explanation, see #nextOffset. If the
           offset cannot be found in the list, the next file share in alphabetical order
           will be returned as the first element.
       limit: This field sets the upper limit for the maximum number of shares to be
           returned per page.
           
           Default and maximum value for pagination limit is 64.
           If the limit is larger than the allowed pagination size or is a negative
           number, an InvalidArgument exception will be thrown.
       managedBy: The filter for the managing entity of the file share.
           
           Valid values are in the
           `pyVmomi.vim.vsan.FileShareManagingEntity` field.
       protocols: The protocol types to be queried.
       pageNumber: The page number to be returned.
           
           The page number can be used to browse the
           pages of file shares returned between different pages. The page number starts
           from 1, and defaults to 1. An InvalidArgument will be thrown if the page
           number is set to a negative number or exceeds the maximum number of pages
           to be returned.
           The shares in the pagination starts from the offset specified by the
           \\#offset parameter.
       properties: Specify the share properties to be returend.
           
           If not specified, all the
           properties will be queried and returned. It is highly recommended to include
           the needed properties only to improve the query performance.
   """
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
   """
   VsanFileShareRuntimeInfo is the data object type for a file service share's
   runtime state.
   
   Attributes:
       usedCapacity: Used capacity in byte for this share.
       hostname: The name of the host that currently owns the file share.
       address: The address of the file server serving this file share.
       vsanObjectUuids: A set of UUIDs of the underlying vSAN objects.
       accessPoints: A key-value pair indicating the access points for the file share.
           
           The key of
           an access point is the type of the protocol, and the value of the access
           point is the connection string for accessing the file share with FQDNs.
           The supported type of protocol string is NFSv4/NFSv3/SMB.
       managedBy: The managing entity of the file share.
       fileServerFQDN: The FQDN of the file server serving this file share.
           
           Note: This can be used to construct the command to manage SMB shares on MMC
           (Microsoft Management Console).
           e.g., run \"fsmgmt.msc /computer:\\<fileServerFQDN>\" on Windows client to
           manage SMB shares from MMC.
   """
   usedCapacity: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   hostname: _typing.Optional[str] = None
   address: _typing.Optional[str] = None
   vsanObjectUuids: list[str] = []
   accessPoints: list[pyVmomi.vim.KeyValue] = []
   managedBy: _typing.Optional[str] = None
   fileServerFQDN: _typing.Optional[str] = None

class FileShareSmbEncryptionType:
   """Enumeration of the SMB file share encryption type."""
   pass


class FileShareSmbOptions(pyVmomi.vmodl.DynamicData):
   """
   The protocol specific options for SMB file shares.
   
   Attributes:
       encryption: This option controls whether a remote client is allowed or required to use
           SMB encryption.
           
           Default value is 'disabled'.
       accessBasedEnumeration: This option controls whether SMB clients can list entries which they don't
           have permission to access.
           
           Default value is 'False'.
           Note: enabling this feature will slow down the listing of large directories
           for the first time.
   """
   encryption: _typing.Optional[str] = None
   accessBasedEnumeration: _typing.Optional[bool] = None


class FileShareSnapshot(pyVmomi.vmodl.DynamicData):
   """
   FileShareSnapshot is the data object type for reflecting the properties of a
   file share snapshot.
   
   This type provides the name, the creation time and the
   used capacity of the snapshot.
   
   Attributes:
       config: Configuration of this snapshot, including the share UUID it belongs to, the
           name, etc.
           
           This property is set when the snapshot is created.
       creationTime: The timestamp for creating the snapshot.
       usedCapacity: Used capacity in bytes for this snapshot.
           
           This field will be unset when the
           used capacity is under calculation
   """
   config: _typing.Optional[FileShareSnapshotConfig] = None
   creationTime: _typing.Optional[_datetime.datetime] = None
   usedCapacity: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class FileShareSnapshotConfig(pyVmomi.vmodl.DynamicData):
   """
   Configurations of a snapshot for a file share.
   
   A snapshot is for consistent
   and efficient backup of file shares.
   
   Attributes:
       shareUuid: UUID of the file share to create a snapshot.
           
           This configuration is required
           for snapshot creation.
       name: The name of the snapshot.
           
           Must be unique within the file share. The snapshot
           name cannot exceed 100 bytes. It should be a valid UTF-8 name and should not
           allow use of the following characters: '', '/', ':', '*', '?', '\"', '<',
           '>', '|', '~', '@', '^', '..' and '%'. This configuration is required for
           snapshot creation.
   """
   shareUuid: _typing.Optional[str] = None
   name: _typing.Optional[str] = None


class FileShareSnapshotQueryResult(pyVmomi.vmodl.DynamicData):
   """
   Result for snapshot querying operation.
   
   The snapshots are sorted in
   chronological order by their creation time.
   
   Attributes:
       snapshots: A list of snapshots that match the query criteria.
       totalCount: The number of snapshots created in total for the file share.
   """
   snapshots: list[FileShareSnapshot] = []
   totalCount: _typing.Optional[int] = None


class FileShareSnapshotQuerySpec(pyVmomi.vmodl.DynamicData):
   """
   Specification for querying snapshot information per share.
   
   If no
   snapshotNames has been provided, then all snapshots matching the query
   criterial will be returned.
   
   Attributes:
       shareUuid: UUID of the file share which the snapshots belong to.
       snapshotNames: A list of the snapshots to be queried.
       startTime: To query the snapshots created after the given time.
       endTime: To query the snapshots created before the given time.
       pageSize: This field sets the maximum number of snapshots to be returned per page.
           
           The
           default and the maximum value for pageSize is 32. If pageSize is larger than
           32 or is non-positive, an InvalidArgument exception will be thrown.
       pageNumber: This field is used to query the snapshots on a specified page.
           
           The default
           value for pageNumber is 1. If pageNumber is non-positive or exceeds the
           maximum number of pages to be returned, an InvalidArgument exception will be
           thrown.
   """
   shareUuid: str
   snapshotNames: list[str] = []
   startTime: _typing.Optional[_datetime.datetime] = None
   endTime: _typing.Optional[_datetime.datetime] = None
   pageSize: _typing.Optional[int] = None
   pageNumber: _typing.Optional[int] = None

class HciMeshClientOperation:
   """The operation type to update Hci Mesh client info."""
   pass


class HciMeshDatastoreSource(pyVmomi.vmodl.DynamicData):
   """
   This data type represents a Datastore Source configuration.
   
   Attributes:
       vcInfo: The information of the remote vCenter which provides the Datastore Source.
   """
   vcInfo: RemoteVcInfo


class HostResourceCheckResult(EntityResourceCheckDetails):
   """
   The host level resource check report.
   
   It includes the resource check
   result of all disk groups and/or storage pools on the host. Please see
   `pyVmomi.vim.vsan.DiskGroupResourceCheckResult` for disk group resource
   check details. Please see `pyVmomi.vim.vsan.StoragePoolResourceCheckResult`
   for storage pool resource check details.
   If `pyVmomi.vim.vsan.EntityResourceCheckDetails.isNew` is true, this is a
   new host suggested to be added by vSAN simulation for more resources to
   make the operation succeed. In this case,
   `pyVmomi.vim.vsan.EntityResourceCheckDetails.isNew` for all disk groups
   on this host is also true.
   
   Attributes:
       host: The managed object of the host.
           
           Unset if `pyVmomi.vim.vsan.EntityResourceCheckDetails.isNew` is true.
       diskGroups: The detailed resource check result for disk groups on the host.
       storagePools: The detailed resource check result for the storage pool on the host.
   """
   host: _typing.Optional[pyVmomi.vim.HostSystem] = None
   diskGroups: list[DiskGroupResourceCheckResult] = []
   storagePools: list[StoragePoolResourceCheckResult] = []


class HostSiteMaintenanceStatus(pyVmomi.vmodl.DynamicData):
   """
   This class describes the fault domain maintenance status on a target host.
   
   Attributes:
       host: Target host.
       state: The fault domain maintenance state of the host; unset if the host is not connected.
       startTime: Represents the start time of the fault domain maintenance operation that places the
           host into fault domain maintenance mode, if the host is already in fault domain maintenance
           mode; otherwise it will be left as unset.
       hostCount: If the host is in fault domain maintenance mode, this attribute represents the number
           of hosts involved in the fault domain maintenance operation that placed the host
           into maintenance mode; otherwise it will be left as unset.
       hosts: If the host is in fault domain maintenance mode, this attribute represents the
           UUIDs of hosts involved in the fault domain maintenance operation that placed
           the host into maintenance mode; otherwise it will be left as unset.
       statusUpdateTime: Represents the timestamp of the most recent fault domain maintenance status update
           which could be triggered by both vCenter and hosts.
           
           If the host was never
           in fault domain maintenance mode, it will be left as unset. Unit in nanosecond.
   """
   host: pyVmomi.vim.HostSystem
   state: _typing.Optional[str] = None
   startTime: _typing.Optional[_datetime.datetime] = None
   hostCount: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   hosts: list[str] = []
   statusUpdateTime: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class IODiagnosticsFailedCheck(pyVmomi.vmodl.DynamicData):
   """
   This data object describes the IO diagnostics failed check.
   
   Attributes:
       unsupportedType: The type of IO diagnostics failed check defined in below enumerations:
           `pyVmomi.vim.vsan.IODiagnosticsFailedCheckType`,
           `vim.vsan.IODiagnosticsFailedCheckType90`
       reason: The reason message of IO diagnostics failed check.
   """
   unsupportedType: str
   reason: pyVmomi.vmodl.LocalizableMessage

class IODiagnosticsFailedCheckType:
   """
   This list defines the types of vSAN IO diagnostics failed checks
   in 8.x and previous releases.
   """
   pass


class IODiagnosticsInstance(pyVmomi.vmodl.DynamicData):
   """
   This data object describes the diagnostics instance including the name and
   the diagnostics target and the running time range.
   
   Attributes:
       name: The instance name.
       state: The state of the instance, can be \"VsanIODiagnosticsInstanceRunning\" or
           \"VsanIODiagnosticsInstanceCompleted\".
       events: The event which makes the instance stopped, if the event is unset, it means
           the IO diagnostic operation completed without any events.
       targets: The targets that the IO diagnostics run against.
       startTime: The start time of the diagnostics.
       endTime: The end time of the diagnostics.
       recurrenceName: The name of the recurrence if the instance is triggered by a recurrence.
           
           Since: 8.0.0.4
   """
   name: str
   state: str
   events: list[IODiagnosticsInstanceEvent] = []
   targets: list[IODiagnosticsTarget] = []
   startTime: _datetime.datetime
   endTime: _datetime.datetime
   recurrenceName: _typing.Optional[str] = None


class IODiagnosticsInstanceEvent(pyVmomi.vmodl.DynamicData):
   """
   This data object describes the diagnostics instance event including the type
   of the event and the time when the event happens.
   
   Attributes:
       eventType: The type of event, for details of event, please refer to below enumerations:
           `pyVmomi.vim.vsan.IODiagnosticsInstanceEventType`,
           `vim.vsan.IODiagnosticsInstanceEventType90`
       eventTime: The time when event happens.
       eventTargets: The targets to which the event is relevant.
           
           Since: 8.0.0.4
   """
   eventType: str
   eventTime: _datetime.datetime
   eventTargets: list[IODiagnosticsTarget] = []

class IODiagnosticsInstanceEventType:
   """
   This list defines the type of event which happens in the vSAN IO
   diagnostics instance for 8.x and previous releases.
   """
   pass


class IODiagnosticsInstanceQuerySpec(pyVmomi.vmodl.DynamicData):
   """
   This data object describes the spec to query the diagnostics instances in
   the given time range.
   
   Attributes:
       targets: The targets to filter the diagnostics instances.
           
           If not
           provided, all instances in the given time range will be returned.
       startTime: The start of the time range.
       endTime: The end of the time range.
   """
   targets: list[IODiagnosticsTarget] = []
   startTime: _datetime.datetime
   endTime: _typing.Optional[_datetime.datetime] = None

class IODiagnosticsInstanceState:
   """
   This data object defines the state of vSAN IO diagnostics instance.
   
   Valid types are:
   """
   pass


class IODiagnosticsObjectLayout(pyVmomi.vmodl.DynamicData):
   """
   This data object describes the layout of the object which run diagnostics instance.
   
   Attributes:
       layout: The object layout definition.
           
           The object layout is a JSON list that has the
           components, diskgroups, domowner, domproxyowner, host uuids and the
           relationship between them. The JSON list also has the fault domain
           information of all related hosts (dom owner, dom proxy owner,and all the
           component owner hosts) of the object.
           Example: [
           {
           \"uuid\": <disk group uuid>, \"type\": \"diskgroup\", \"owner\": \"<host uuid>\"
           },
           {
           \"uuid\": <component uuid>, \"type\": \"component\", \"owner\": \"<disk group uuid>\"
           },
           {
           \"uuid\": <dom owner uuid>, \"type\": \"domowner\", \"owner\": \"<host uuid>\"
           },
           {
           \"uuid\": <dom proxy owner uuid>, \"type\": \"domproxyowner\", \"owner\": \"<host uuid>\"
           },
           {
           \"uuid\": <host uuid>, \"type\": \"faultdomain\", \"owner\": \"<fault domain uuid>\",
           \"faultDomainName\": \"<fault domain name>\"
           }
           ]
           For vSAN ESA object layout, it is a list in JSON format that has the components,
           disks, domowner, domproxyowner, host uuids and the relationship between them.
           Example: [
           {
           \"uuid\": <perf tier uuid>, \"type\": \"perftier\", \"owner\": \"<host uuid>\"
           },
           {
           \"uuid\": <capacity tier uuid>, \"type\": \"capacitytier\", \"owner\": \"<host uuid>\"
           },
           {
           \"uuid\": <component uuid>, \"type\": \"component\", \"owner\": \"<disk uuid>\"
           },
           {
           \"uuid\": <dom owner uuid>, \"type\": \"domowner\", \"owner\": \"<host uuid>\"
           },
           {
           \"uuid\": <object uuid>, \"type\": \"vsan2object\", \"owner\": \"<host uuid>\",
           \"performancelegraid\": \"<performance leg raid info>\", \"capacitylegraid\": \"<capacity leg raid info>\"
           },
           {
           \"uuid\": <dom proxy owner uuid>, \"type\": \"domproxyowner\", \"owner\": \"<host uuid>\"
           },
           {
           \"uuid\": <host uuid>, \"type\": \"faultdomain\", \"owner\": \"<fault domain uuid>\",
           \"faultDomainName\": \"<fault domain name>\"
           }
           ]
   """
   layout: str


class IODiagnosticsPrecheckResult(pyVmomi.vmodl.DynamicData):
   """
   This data object describes the IO diagnostics precheck result.
   
   Attributes:
       supported: The result to indicate whether IO diagnostics is supported.
       failedChecks: The failed checks of an IO diagnostics precheck.
   """
   supported: bool
   failedChecks: list[IODiagnosticsFailedCheck] = []


class IODiagnosticsStats(pyVmomi.vmodl.DynamicData):
   """
   This data object describes the IO diagnostics result.
   
   Attributes:
       objectsIOStats: The list of each vSAN object IO diagnostics stats.
       startTime: The start time of the diagnostics.
       endTime: The end time of the diagnostics.
   """
   objectsIOStats: list[ObjectIOStats] = []
   startTime: _datetime.datetime
   endTime: _datetime.datetime


class IODiagnosticsTarget(pyVmomi.vmodl.DynamicData):
   """
   This data object describes the spec of the target to run IO diagnostics
   against.
   
   Attributes:
       type: The type of the target to run IO diagnostics against.
       entityId: The entity id of the target to run IO diagnostics against.
           
           For virtual machine, the field is VM moRef.
       objUuids: The vSAN object uuids involved to run IO diagnostics.
           
           If not specified,
           it will list all the backing objects for the entity with the specified type
           and entityId.
   """
   type: str
   entityId: str
   objUuids: list[str] = []


class IODiagnosticsTargetStats(pyVmomi.vmodl.DynamicData):
   """
   This data object describes the IO diagnostics target result.
   
   Attributes:
       target: The vSAN object IO diagnostics target information.
       objectsIODiagnosticsStats: The IO diagnostics stats of the vSAN objects.
   """
   target: IODiagnosticsTarget
   objectsIODiagnosticsStats: list[IODiagnosticsStats] = []

class IODiagnosticsTargetType:
   """
   This data object defines the types that support vSAN IO diagnostics.
   
   Valid types are:
   """
   pass


class IOLatency(pyVmomi.vmodl.DynamicData):
   """
   This data object describes the IO latency stats for each vSAN layer.
   
   Attributes:
       latencyType: The type of latency measured.
       sourceEntityUuid: The uuid of the object which sends the IO operation.
       destEntityUuid: The uuid of the object which receives the IO operation.
       readLatencyStats: The latency stats for the read operations.
       writeLatencyStats: The latency stats for the write operations.
       detailedInfo: The detailed additional info.
           
           For \"NetworkLatency\", it has fields \"threshold\" and \"domComponentUuid\";
           For \"LsomLatency\", it has field \"domComponentUuid\";
           For \"CapacityLsomLatency\" or \"PerfLsomLatency\", it has field \"physicalDiskUuid\";
           For \"CrossSiteNetworkLatency\", it has field \"threshold\";
   """
   latencyType: str
   sourceEntityUuid: str
   destEntityUuid: str
   readLatencyStats: IOLatencyMetrics
   writeLatencyStats: IOLatencyMetrics
   detailedInfo: list[pyVmomi.vmodl.KeyAnyValue] = []


class IOLatencyMetrics(pyVmomi.vmodl.DynamicData):
   """
   This data object describes the IO latency metrics.
   
   Attributes:
       totalCount: The total IO count in the diagnostics.
       averageLatency: The average latency measured in the unit of ms.
       stddevLatency: The latency standard deviation measured in the unit of ms.
   """
   totalCount: int
   averageLatency: float
   stddevLatency: _typing.Optional[float] = None

class IOLatencyType:
   """
   This data object defines the type of the vSAN IO latency in the whole vSAN IO
   stack from DOM owner to the DOM component manager and LSOM.
   """
   pass

class LifecycleCheckOperation:
   """The lifecycle operation types required by lifecycle manager/vLCM."""
   pass

class LifecycleClusterType:
   """The lifecycle cluster types required by lifecycle manager/vLCM."""
   pass


class LifecycleConfigDetails(pyVmomi.vmodl.DynamicData):
   """
   Configuration details for a vSAN cluster required by lifecycle manager/vLCM.
   
   Attributes:
       clusterType: The vSAN cluster type.
       faultDomainsDetails: The list of fault domains for the vSAN cluster.
       witnessHostsDetails: Information about the witness hosts for stretched clusters.
   """
   clusterType: str
   faultDomainsDetails: list[LifecycleFaultDomainDetails] = []
   witnessHostsDetails: list[LifecycleWitnessDetails] = []


class LifecycleFaultDomainDetails(pyVmomi.vmodl.DynamicData):
   """
   vSAN stretched cluster fault domain details required by
   lifecycle manager/vLCM.
   
   Attributes:
       isPreferredFaultDomain: Whether this is the preferred fault domain.
       name: The fault domain name.
           
           Optional when hosts are fault domains.
       hosts: The list of hosts in the fault domain.
   """
   isPreferredFaultDomain: _typing.Optional[bool] = None
   name: _typing.Optional[str] = None
   hosts: list[pyVmomi.vim.HostSystem] = []


class LifecyclePreCheckResult(pyVmomi.vmodl.DynamicData):
   """
   Precheck result required by lifecycle manager/vLCM.
   
   The type attribute represents the type of check performed.
   The status attribute represents the result of the check:
   green) The check passed
   yellow) A non-blocking check failed. The reason attribute will contain the
   failure message
   red) A blocking check failed. The reason attribute will contain the
   failure message
   
   Attributes:
       type: The check type.
           
           Check `pyVmomi.vim.vsan.LifecyclePreCheckType` for all possible types.
       description: The description of the lifecycle check.
       status: The status of the lifecycle check: green, yellow or red.
       reason: The reason why the lifecycle check returned an unsuccessful result.
           
           It
           contains the error/warning message of the lifecycle check.
   """
   type: _typing.Optional[str] = None
   description: _typing.Optional[pyVmomi.vmodl.LocalizableMessage] = None
   status: str
   reason: _typing.Optional[pyVmomi.vmodl.LocalizableMessage] = None

class LifecyclePreCheckType:
   """The lifecycle check types required by lifecycle manager/vLCM."""
   pass


class LifecycleWitnessDetails(pyVmomi.vmodl.DynamicData):
   """
   Stretched cluster witness host details required by lifecycle manager/vLCM.
   
   Attributes:
       host: The witness host.
       isVirtualAppliance: Whether the witness host is a virtual appliance or a physical machine.
       sharedClusters: The list of clusters sharing the witness host.
           
           A list with only one cluster means the witness host is not shared.
   """
   host: pyVmomi.vim.HostSystem
   isVirtualAppliance: bool
   sharedClusters: list[pyVmomi.vim.ClusterComputeResource] = []


class MetricProfile(pyVmomi.vmodl.DynamicData):
   """
   The vSAN metrics configuration per monitor client.
   
   In pull mode, when vSAN metrics query happens, all authTokens
   configured to vSAN node will be used for authentication and
   identify the monitor client.
   
   Attributes:
       authToken: The credential used for authentication between monitor and
           vSAN metrics provider.
           
           The length of this token should not exceed 30.
   """
   authToken: str


class MetricsConfig(pyVmomi.vmodl.DynamicData):
   """
   The vSAN metrics configuration for all monitor clients.
   
   Attributes:
       profiles: The customized metric profile per monitor client.
   """
   profiles: list[MetricProfile] = []

class Mode:
   """
   Mode for the vSAN cluster.
   
   If mode is not specified, then vSAN is running
   in default vSAN mode.
   """
   pass


class MountPrecheckNetworkConnectivity(pyVmomi.vmodl.DynamicData):
   """
   The network connectivity between a client host and a server host.
   
   Attributes:
       host: The server host.
       smallPingTestSuccessPct: The small ping test success percentage between a client host and
           a server host.
       largePingTestSuccessPct: The large ping test success percentage between a client host and
           a server host.
       status: The network connectivity health status between a client host to a
           server host.
           
           Check `pyVmomi.vim.vsan.VsanHealthStatusType` for all possible statuses.
   """
   host: pyVmomi.vim.HostSystem
   smallPingTestSuccessPct: int
   largePingTestSuccessPct: int
   status: str


class MountPrecheckNetworkConnectivityDetail(pyVmomi.vmodl.DynamicData):
   """
   The network connectivity between given client host and all server hosts.
   
   Attributes:
       host: The client host.
       networkConnectivity: The network connectivity for all server hosts.
   """
   host: pyVmomi.vim.HostSystem
   networkConnectivity: list[MountPrecheckNetworkConnectivity] = []


class MountPrecheckNetworkConnectivityResult(MountPrecheckItem):
   """
   The precheck result for network connectivity between client hosts and server
   hosts.
   
   It extends from `pyVmomi.vim.vsan.MountPrecheckItem` with network
   connectivity details.
   
   Attributes:
       details: A list of `pyVmomi.vim.vsan.MountPrecheckNetworkConnectivityDetail`,
           it contains the network connectivity result for each client host
           to the server hosts it mounts to.
   """
   details: list[MountPrecheckNetworkConnectivityDetail] = []


class MountPrecheckNetworkLatency(pyVmomi.vmodl.DynamicData):
   """
   The network latency between a client host and a server host.
   
   Attributes:
       host: The server host.
       networkLatency: The network latency in microseconds between a client host to a server host.
       status: The network latency health status between a client host to a server host.
           
           Check `pyVmomi.vim.vsan.VsanHealthStatusType` for all possible statuses.
   """
   host: pyVmomi.vim.HostSystem
   networkLatency: pyVmomi.VmomiSupport.long
   status: str


class MountPrecheckNetworkLatencyDetail(pyVmomi.vmodl.DynamicData):
   """
   The network latency between given client host and all server hosts.
   
   Attributes:
       host: The client host.
       networkLatencies: The network latency for all server hosts.
   """
   host: pyVmomi.vim.HostSystem
   networkLatencies: list[MountPrecheckNetworkLatency] = []

class MountPrecheckNetworkLatencyResult(MountPrecheckItem):
   """
   The precheck result for network latency between client hosts and server
   hosts.
   
   It extends from `pyVmomi.vim.vsan.MountPrecheckItem` with network
   latency details.
   
   Attributes:
       details: A list of `pyVmomi.vim.vsan.MountPrecheckNetworkLatencyDetail`, it contains the
           network latency result for each client host to the server hosts it mounts to.
   """
   details: list[MountPrecheckNetworkLatencyDetail] = []

class MountPrecheckType:
   """
   This indicates the precheck type when mounting a remote vSAN datastore
   (for 8.x and previous releases).
   """
   pass

class MountPrecheckTypeDIT:
   """
   This indicates the precheck type when mounting a remote vSAN datastore and
   enabling remote DIT at the same time.
   """
   pass


class ObjectHealthTelemetrySummary(pyVmomi.vmodl.DynamicData):
   """
   Define the object health summary for cluster obs telemetry data collection.
   
   Attributes:
       healthyObjectCount: The number of healthy objects.
       inaccessibleObjectCount: The number of inaccessible objects.
       needRetryObjectCount: The number of need retry objects.
       pdlObjectCount: The number of pdl objects.
       clusterHostCount: The number of hosts of the current cluster.
   """
   healthyObjectCount: int
   inaccessibleObjectCount: int
   needRetryObjectCount: int
   pdlObjectCount: int
   clusterHostCount: int


class ObjectIOStats(pyVmomi.vmodl.DynamicData):
   """
   This data object describes the vSAN object IO stats.
   
   Attributes:
       backingObjectId: The backing vSAN object uuid to run IO diagnostics.
       ioLatencyStats: The IO latency stats of each layer for this vSAN object.
       objectLayout: The backing vSAN object layout.
   """
   backingObjectId: str
   ioLatencyStats: list[IOLatency] = []
   objectLayout: IODiagnosticsObjectLayout

class PerfsvcRemediateAction:
   """
   Remediate action type.
   
   When vSAN cluster remediate, vSAN will check the performance service configuration and
   performance service status. If the vSAN performance service configuration is enable but
   the vSAN performance service is not running, it will return \"enable\" to remediate vSAN
   performance service. If the vSAN performance service configuration is disable but the
   vSAN performance service is not running, it will return \"disable\" to remediate vSAN
   performance service. If the vSAN performance service configuration is enable, the vSAN
   performance service is running, but the profile of performance service is not match
   the configuration, it will return \"update_profile\" to remediate vSAN performance service.
   Others will return \"no_action\" which means no need to remediate vSAN performance service.
   Valid types are:
   """
   pass

class PrecheckDatastoreSourceOperation:
   """Related operations for PrecheckDatastoreSource."""
   pass


class ProactiveRebalanceInfo(pyVmomi.vmodl.DynamicData):
   """
   The proactive rebalance information.
   
   Proactive Rebalance is used to maintain disk balance among the vSAN
   cluster. If Proactive Rebalance is enabled, vSAN automatically
   rebalances(moves the data among disks) the vSAN cluster when a capacity
   disk fullness hits proactive rebalance threshold.
   It includes the enable state of proactive rebalance, and its threshold.
   
   Attributes:
       enabled: Whether proactive rebalance is enabled.
           
           If it is set to True, rebalance data movement will begin when following
           conditions are met within vSAN cluster,
           1\\. Current disk fullness - lowest disk fullness > proactive threshold
           2\\. Current disk fullness > mean disk fulless within cluster
           - Allowed values:
             True if proactive rebalance is enabled;
             False if proactive rebalance is disabled.
           - Default value: False
       threshold: Proactive relalance threshold.
           
           It indicates the extent of the imbalance the cluster can tolerate in
           percentage. If the disk imbalance (current disk fullness -
           lowest disk fullness) is below rebalance threshold, the proactive
           rebalance will not be triggered.
           - Allowed values: 10 to 75.
           - Default value: 30.
   """
   enabled: _typing.Optional[bool] = None
   threshold: _typing.Optional[int] = None


class RdmaConfig(pyVmomi.vmodl.DynamicData):
   """
   The RDMA Configuration for vSAN.
   
   Attributes:
       rdmaEnabled: Whether RDMA is enabled for vSAN.
   """
   rdmaEnabled: bool


class ReconfigSpec(pyVmomi.vim.SDDCBase):
   """
   The vSAN reconfiguration specification.
   
   Attributes:
       vsanClusterConfig: vSAN configuration, includes default settings for hosts.
       dataEfficiencyConfig: The data efficiency configuration for vSAN.
           
           vSAN 6.2
           accomplishes data efficiency by deduplication and compression, which will be
           enabled or disabled together.
       diskMappingSpec: vSAN disk group configuration specification.
       faultDomainsSpec: Spec for configuring the fault domains.
           
           It includes a list of
           `pyVmomi.vim.cluster.VsanFaultDomainSpec` and a `pyVmomi.vim.cluster.VsanWitnessSpec`.
           If `pyVmomi.vim.cluster.VsanWitnessSpec` is specified which indicates it a
           stretched cluster, the fault domain list needs to include exactly two fault
           domain items.
       modify: Flag to specify whether the specification (\"spec\") should be applied
           incrementally.
           
           If \"modify\" is false and the operation succeeds, then the
           configuration of the vSAN cluster matches the specification exactly;
           in this case any unset portions of the specification will result in unset or
           default portions of the configuration.
       allowReducedRedundancy: This optional parameter is applicable to certain vSAN cluster
           reconfigure operations that need to migrate data across cluster for changing
           vSAN disk format.
           
           In vSAN version 6.2, enable or disable
           deduplication and compression in a cluster is such kind of operation.
           The default value 'false' will instruct the data migration process to move
           all the storage object data in the host under processing to other hosts to
           ensure the data stays fully protected; while the value 'true' may make the
           process move less data for just ensuring storage object accessibility, and
           some objects will be kept at \"reduced redundancy\" state, i.e., at a higher
           risk in case of a hardware failure during the migration process. However,
           value 'true' is useful and even the only option when cluster does not have
           enough host or free storage to ensure the data stays fully protected during
           data migration.
           See `ensureObjectAccessibility`
           and `evacuateAllData`.
       resyncIopsLimitConfig: vSAN throttling IOPS limit configuration specification.
       iscsiSpec: vSAN iSCSI configuration.
       dataEncryptionConfig: The data encryption configuration for vSAN.
       extendedConfig: vSAN extended configurations.
       datastoreConfig: vSAN datastore configuration.
       perfsvcConfig: vSAN performance service configuration.
       unmapConfig: SCSI unmap command configuration on vSAN.
       vumConfig: vSAN build recommendation engine configuration for this vSAN cluster.
           
           Build recommendation engine would use it to generate different baselines for
           this vSAN cluster.
           See `pyVmomi.vim.vsan.VsanVumConfig`
       metricsConfig: vSAN metrics configuration for all monitor clients
       fileServiceConfig: vSAN file service configurations.
       rdmaConfig: RDMA Spec for vSAN.
       dataInTransitEncryptionConfig: vSAN configuration for data-in-transit encryption.
       mode: Mode for vSAN.
       vsanHealthConfig: vSAN Health configuration.
       vsanEsaConfig: Configurations for vSAN ESA.
       xvcDatastoreConfig: vSAN cross VC datastore configuration.
       serverClusterConfig: Server cluster configuration for HCI Mesh.
       snapServiceConfig: The configuration for vSAN Snapshot service.
           
           The Snapshot service
           configuration will require specific User role and privileges.
           TODO: Update required privileges and the implementaiton to include the
           necessary validations.
           
           Since: 8.0.0.4
       deconvergedNetConfig: De-converged network configuration for vSAN.
       vbossClusterConfig: The cluster level configuration of vSAN vBoss service.
   """
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
   """
   The basic information for communicating with a remote vCenter.
   
   It is used to connect to the remote vCenter from the local.
   
   Attributes:
       linkType: The link type about how the remote vCenter is linked.
           
           It can be optional for
           `pyVmomi.vim.cluster.VsanRemoteDatastoreSystem.updateDatastoreSource` and
           `pyVmomi.vim.cluster.VsanRemoteDatastoreSystem.destroyDatastoreSource`
           APIs.
       vcHost: The remote vCenter name (e.g.
           
           FQDN) to identify the remote vCenter.
   """
   linkType: _typing.Optional[str] = None
   vcHost: str


class RemoteVcInfoStandalone(RemoteVcInfo):
   """
   The information for communicating with a standalone remote vCenter.
   
   It is an inherit class from VsanRemoteVcInfo, with adding specific
   information for a standalone remote vCenter.
   
   Attributes:
       user: The user name for login into the standalone remote vCenter.
           
           This information won't be persisted in backend implementation.
       password: The password for login into the standalone remote vCenter.
           
           This information won't be persisted in backend implementation.
       cert: The single x509 certificate encoded in PEM format, which the remote
           vCenter is expected to have.
   """
   user: _typing.Optional[str] = None
   password: _typing.Optional[str] = None
   cert: _typing.Optional[str] = None

class RemoteVcLinkType:
   """The link type of a remote vCenter."""
   pass

class RemoteVsanNetworkTopology:
   """
   Network topology between the client and server cluster in a HCI Mesh
   configuration.
   """
   pass


class RemoteVsanSite(pyVmomi.vmodl.DynamicData):
   """
   Remote vSAN Site Information.
   
   This is used to identify a site in
   both client and server clusters involved in a HCI Mesh.
   
   Attributes:
       name: Name of the target site in a client or server cluster.
           
           For a vSAN stretched cluster the name refers to a Fault Domain name.
   """
   name: str


class RemoteVsanSiteAffinity(pyVmomi.vmodl.DynamicData):
   """
   Remote vSAN Site Affinity Information.
   
   The affinity provided
   implies the network connectivity between the coupled sites to be a
   high bandwidth/low latency link.
   
   Attributes:
       clientSite: The client site that this site affinity is applicable for.
           
           This field is unset when the client is a single site cluster.
       serverSite: The remote server site to be coupled with the client site.
           
           The server site is always a stretched cluster Fault Domain.
   """
   clientSite: _typing.Optional[RemoteVsanSite] = None
   serverSite: RemoteVsanSite


class RepairTimerInfo(pyVmomi.vmodl.DynamicData):
   """
   The repair timer information of the host.
   
   Including the longest time
   and shortest time remaining for triggering repair work for objects with
   absent components on the host, the number of the objects with absent
   components.
   
   Attributes:
       maxTimeToRepair: The longest time remaining for triggering repair work for objects with
           absent components in seconds.
       minTimeToRepair: The shortest time remaining for triggering repair work for objects with
           absent components in seconds.
       objectCount: The number of the objects with absent component that need repair.
       objectCountWithRepairTimer: The number of the objects which need repair
           and it's time since incompliance is still less than
           `pyVmomi.vim.vsan.VsanExtendedConfig.objectRepairTimer`.
   """
   maxTimeToRepair: int
   minTimeToRepair: int
   objectCount: int
   objectCountWithRepairTimer: _typing.Optional[int] = None


class ResourceCheckResult(EntityResourceCheckDetails):
   """
   The resource check result for the queried spec
   `pyVmomi.vim.vsan.ResourceCheckSpec`.
   
   Attributes:
       timestamp: The timestamp when the resource check result is generated.
           
           The timestamp
           will remain unchanged if the resource check result is cached and fetched
           in the future indicating when the resource check was performed.
       status: The overall status of resource check result if resource check has completed.
           
           The possible statuses are:
           - \"green\": Resource check passed for the queried operation.
             There is sufficient resource in vSAN cluster to perform
             the queried operation.
           - \"yellow\": Resource check passed for the queried operation, but there is
             some existing issue in the cluster, e.g., network partition.
           - \"red\": Resource check failed for the queried operation.
             If any entity is suggested to be added by resource check report
             (i.e. \"isNew\" flag is set to true), then there is not enough
             resource in current vSAN cluster for the given operation. Extra
             resource is required to make the given operation succeed.
       messages: Informative and localizable messages for the resource check.
       faultDomains: Detailed hierarchical resource check report.
           
           At the top of the hierarchy it
           is fault domain level resource check report. Please see
           `pyVmomi.vim.vsan.FaultDomainResourceCheckResult`.
           For data persistence component result, this field will be unset
           at the moment.
       dataToMove: The predicted data migration in bytes assuming the queried operation
           gets performed.
           
           For example, if the queried resource check type is
           for host enter maintenance mode operation, vSAN will simulate how many
           bytes of data will need to move during the host enter maintenance mode
           process.
           For data persistence component result, this field will always be zero
           since no data will be moved during EMM operation.
       nonCompliantObjects: The vSAN UUID of objects which are predicted to become non-compliant after
           the operation is done.
           
           For example, the object may become non-compliant if
           \"ensureObjectAccessibility\" is chosen as the data evacuation mode
           after the host enters maintenance mode.
           This field is only applicable to regular vSAN component result
           `pyVmomi.vim.vsan.ResourceCheckVsanResult` and will be unset
           in the data persistence component result
           `pyVmomi.vim.vsan.ResourceCheckDataPersistenceResult`.
           If this is in the aggregated result `pyVmomi.vim.vsan.ResourceCheckStatus.result`,
           this field has the same value as in the regular vSAN component result
           `pyVmomi.vim.vsan.ResourceCheckVsanResult`.
       inaccessibleObjects: The vSAN UUID of objects which are predicted to become inaccessible after
           the operation is done.
           
           For example, for a FTT=0 object which has only one component on the host,
           the object will become inaccessible if \"noAction\" is chosen as the data
           evacuation mode after the host enters maintenance mode.
           This field is only applicable to regular vSAN component result
           `pyVmomi.vim.vsan.ResourceCheckVsanResult` and will be unset
           in the data persistence component result
           `pyVmomi.vim.vsan.ResourceCheckDataPersistenceResult`.
           If this is in the aggregated result `pyVmomi.vim.vsan.ResourceCheckStatus.result`,
           this field has the same value as in the regular vSAN component result
           `pyVmomi.vim.vsan.ResourceCheckVsanResult`.
       capacityThreshold: Capacity threshold in percentage of total capacity.
           
           For example, if total
           used capacity is more than {VsanHealthThreshold.yellowValue}% than status
           or the entity capcity should be marked as 'yellow'.
           For data persistence component result, this field will reflect the capacity
           threshold in percentage of total capacity for vsan direct datastore.
       health: What-if vSAN cluster health summary which indicates how the related vSAN
           health check will look after queried operation is performed.
       dataToResync: The resync related to objects on the host which is currently ongoing
           (in bytes) and needs to be completed before the host can enter
           maintenance mode.
       dedupStoreHealth: The what-if dedup store health which is the worst health state of
           the affected dedup store sub objects.
   """
   class ResourceCheckDedupStoreHealthState(pyVmomi.VmomiSupport.Enum):
      """
      * The dedup store health category enumeration used in resource check.
      
      Attributes:
          Inaccessible: The dedup store is inaccessible which means the dedup store
              has inaccessible sub objects.
          Noncompliant: The dedup store is noncompliant which means the dedup store
              has no inaccessible sub objects but has noncompliant sub objects.
      """
      Inaccessible: _typing.ClassVar['ResourceCheckResult.ResourceCheckDedupStoreHealthState'] = 'Inaccessible'
      Noncompliant: _typing.ClassVar['ResourceCheckResult.ResourceCheckDedupStoreHealthState'] = 'Noncompliant'

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

class ResourceCheckComponentResult(ResourceCheckResult):
   """
   The resource check result for different components,
   e.g., regular vSAN or vSphere data persistence platform.
   
   Attributes:
       type: The type of the component resource check result that is queried.
           
           Please see `pyVmomi.vim.vsan.ResourceCheckComponentType` for possible types.
   """
   type: str

class ResourceCheckComponentType:
   """Enumeration of the types for resource check component result."""
   pass


class ResourceCheckDataPersistenceResult(ResourceCheckComponentResult):
   """
   The resource check component result for vSphere Data Persistence Platform.
   
   Attributes:
       dataToRebuild: Amount of data that will rebuild asynchronously after queried
           operation is performed.
       inaccessibleInstances: Persistent service instances that are predicted to become inaccessible
           after queried operation is performed.
           
           Instance names are constructed as follows service:namespace:instance where:
           - service: Name of the persistent service.
           - namespace: Name of the instance namespace.
           - instance: Instance name given to the respective service instance
             while creating it.
       reducedAvailabilityInstances: Persistent service instances that are predicted to have reduced availability
           after queried operation is performed.
           
           Instance names are constructed as follows service:namespace:instance where:
           - service: Name of the persistent service.
           - namespace: Name of the instance namespace.
           - instance: Instance name given to the respective service instance
             while creating it.
       rebuildInstances: Persistent service instances that will lead to rebuild on a different
           entity, these instances will have reduced availability as long as the
           data is rebuilt.
           
           The data may be rebuilt synchronously or asynchronously
           depending on the service.
           Instance names are constructed as follows service:namespace:instance where:
           - service: Name of the persistent service.
           - namespace: Name of the instance namespace.
           - instance: Instance name given to the respective service instance
             while creating it.
   """
   dataToRebuild: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   inaccessibleInstances: list[str] = []
   reducedAvailabilityInstances: list[str] = []
   rebuildInstances: list[str] = []


class ResourceCheckSpec(pyVmomi.vmodl.DynamicData):
   """
   Specification for performing a resource check or retrieving the status of
   a resource check.
   
   Attributes:
       operation: The operation for which the resource check is performed:
           - \"EnterMaintenanceMode\": The resource check for host enter maintenance
             mode operation.
           - \"DiskDataEvacuation\": The resource check for vSAN disk or disk-group
             operation which requires vSAN disk data evacuation (e.g., unmount
             a vSAN disk-group, remove a vSAN disk/disk-group, rebuild a vSAN
             disk-group, etc.).
       entities: The list of entity vSAN UUIDs against which the resource check is performed.
           
           For host enter maintenance operation, only one host vSAN UUID is supported
           at a time.
       maintenanceSpec: The host maintenance spec specifying the data evacuation mode.
       parent: Specify the task if this resource check is called from a running
           task.
   """
   operation: str
   entities: list[str] = []
   maintenanceSpec: _typing.Optional[pyVmomi.vim.host.MaintenanceSpec] = None
   parent: _typing.Optional[pyVmomi.vim.Task] = None


class ResourceCheckStatus(pyVmomi.vmodl.DynamicData):
   """
   The status of a resource check for queried operation.
   
   Attributes:
       status: The overall status of the resource check that is queried.
           
           Please see `pyVmomi.vim.vsan.ResourceCheckStatusType` for possible statuses.
       result: The result of the resource check that is queried.
           
           This field will be populated only if a resource check has completed
           successfully and recently, i.e., only when
           `pyVmomi.vim.vsan.ResourceCheckStatus.status` is \"completed\".
           For \"EnterMaintenanceMode\" operation, this will be the aggregated result
           for both regular vSAN and vSphere data persistence platform.
           For detailed result of each component, please look into
           `pyVmomi.vim.vsan.ResourceCheckStatus.componentResults`.
           For other resource check types, this will be the result for
           regular vSAN as usual. The same vSAN component result will also be in
           `pyVmomi.vim.vsan.ResourceCheckStatus.componentResults`.
       task: The details of the resource check task that was generated and returned by
           `pyVmomi.vim.vsan.VsanResourceCheckSystem.performResourceCheck`.
           
           It will be set
           only when `pyVmomi.vim.vsan.ResourceCheckStatus.status` is \"resourceCheckRunning\".
           The derived class `pyVmomi.vim.vsan.DiskDataEvacuationResourceCheckTaskDetails`
           will be used if the resource check task is for disk/disk-group data
           evacuation.
       parentTask: The details of the parent task passed in by
           `pyVmomi.vim.vsan.ResourceCheckSpec.parent`.
           
           It will be set only when the
           resource check is launched from a parent task and the state of the parent
           task is \"running\".
       componentResults: The detailed resource check result for different components.
           
           The data persistence component resource check result is only available
           when the operation is \"EnterMaintenanceMode\" at the moment. For other
           resource check types, only the regular vSAN result will be available.
   """
   status: str
   result: _typing.Optional[ResourceCheckResult] = None
   task: _typing.Optional[ResourceCheckTaskDetails] = None
   parentTask: _typing.Optional[ResourceCheckTaskDetails] = None
   componentResults: list[ResourceCheckComponentResult] = []

class ResourceCheckStatusType:
   """Enumeration of the types for resource check status."""
   pass

class ResourceCheckVsanResult(ResourceCheckComponentResult):
   """The resource check component result for regular vSAN."""
   pass


class ResyncIopsInfo(pyVmomi.vmodl.DynamicData):
   """
   The IOPS limit for resync operations.
   
   Attributes:
       resyncIops: Resync IOPS value for host
   """
   resyncIops: int


class RuntimeStatsHostMap(pyVmomi.vmodl.DynamicData):
   """
   Pair of vSAN host and its runtime stats.
   
   It is used to present a vSAN host and runtime stats associated to the
   host and returned by
   `pyVmomi.vim.cluster.VsanVcClusterConfigSystem.getRuntimeStats`.
   
   Attributes:
       host: vSAN host, from which the vSAN runtime stats comes
       stats: vSAN runtime stats from above host.
   """
   host: pyVmomi.vim.HostSystem
   stats: _typing.Optional[pyVmomi.vim.vsan.host.RuntimeStats] = None


class SSDEnduranceThresholdSpec(pyVmomi.vmodl.DynamicData):
   """
   The spec for NVMe SSD endurance threshold configuration.
   
   Attributes:
       clustername: The vSAN cluster name which is set for per cluster ssd endurance spec.
       clusternameop: The operator name which is set for cluster name comparison.
           
           Support below enum values.
           \\- equals
           \\- notEqualTo
           \\- startsWith
           \\- doesNotStartWith
           \\- endsWith
           \\- doesNotEndWith
       hostname: The host name in vSAN cluster which is set for per host ssd endurance spec.
       hostnameop: The operator name which is set for host name comparison.
           
           Support below enum values.
           \\- equals
           \\- notEqualTo
           \\- startsWith
           \\- doesNotStartWith
           \\- endsWith
           \\- doesNotEndWith
       diskname: The disk name(e.g.
           
           t10.NVMe____Dell_Express_Flash_NVMe_P4510_1TB_SFF)
           in vSAN cluster which is set for per disk ssd endurance spec.
           The disk name can be queried through command 'vdq -i' on ESXi
       disknameop: The operator name which is set for disk name comparison.
           
           Support below enum values.
           \\- equals
           \\- notEqualTo
           \\- startsWith
           \\- doesNotStartWith
           \\- endsWith
           \\- doesNotEndWith
       diskvendorname: The name of disk vendor in vSAN cluster which is set for per disk ssd endurance spec.
           
           The vendor name of disk can be queried through command
           'vsish -e get /storage/scsifw/devices/<diskName>/info | grep \"vendor :\"'
       diskvendorop: The operator name which is set for disk vendor comparison.
           
           Support below enum values.
           \\- equals
           \\- notEqualTo
           \\- startsWith
           \\- doesNotStartWith
           \\- endsWith
           \\- doesNotEndWith
       ssdEndurancePtg: The warning disk endurance alarm will be triggered when the percentage is reached.
       severity: The severity of alarm rule.
           
           Support below enum values
           \\- red
           \\- yellow
   
   Since: 8.0.0.4
   """
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
   """
   Unicast information of a host in server cluster.
   
   Server cluster owns the datastore which is mounted by this host.
   
   Attributes:
       hostUuid: Server host UUID.
       nodeType: Server node type to differentiate data nodes from witness and metadata nodes.
       unicastSpec: The list of unicast information for the host in a server cluster.
       thumbprintList: A list of SSL certificate thumbprints with supported secure hashing
           algorithms.
           
           See `pyVmomi.vim.vm.CertThumbprint`
   """
   hostUuid: str
   nodeType: _typing.Optional[str] = None
   unicastSpec: list[pyVmomi.vim.cluster.VsanUnicastAddressInfo] = []
   thumbprintList: list[pyVmomi.vim.vm.CertThumbprint] = []


class SharedWitnessCompatibilityResult(pyVmomi.vmodl.DynamicData):
   """
   Data object to represent compatibility result of shared witness host.
   
   Attributes:
       witnessHostCompatibility: Represent whether given shared witness host could be attached to all
           specified ROBO clusters.
       roboClusterCompatibility: Represent whether each given ROBO cluster could support using target
           shared witness host as its witness.
   """
   witnessHostCompatibility: EntityCompatibilityResult
   roboClusterCompatibility: list[EntityCompatibilityResult] = []


class SiteMaintenanceCheckTaskDetails(ResourceCheckTaskDetails):
   """
   The detailed information of a running fault domain maintenance precheck task.
   
   Attributes:
       cluster: The managed object of the cluster on which the task is running.
       siteMaintenanceSpec: The specification of fault domain maintenance precheck task.
   """
   cluster: pyVmomi.vim.ClusterComputeResource
   siteMaintenanceSpec: SiteMaintenanceSpec


class SiteMaintenanceInfo(pyVmomi.vmodl.DynamicData):
   """
   This class provides information regarding the maintenance mode status for a
   site within a stretched cluster.
   
   Attributes:
       faultDomainName: User friendly name of the fault domain.
       state: The maintenance state of the fault domain.
       trackingTask: A task that is executing the fault domain maintenance action.
           
           This will be unset if
           there is no on-going task.
       hostStatus: Fault domain maintenance status of connected hosts in the site.
           
           If no host is
           connected, this field will be unset.
       statusUpdateTime: Represents the timestamp of the most recent fault domain maintenance status update.
           
           If the site was never in fault domain maintenance mode, it will be left as unset.
           Unit in nanosecond.
   """
   faultDomainName: str
   state: str
   trackingTask: _typing.Optional[pyVmomi.vim.Task] = None
   hostStatus: list[HostSiteMaintenanceStatus] = []
   statusUpdateTime: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class SiteMaintenancePrecheckDetail(pyVmomi.vmodl.DynamicData):
   """
   Detailed information about a precheck item for fault domain maintenance operations.
   
   Attributes:
       testName: The name of the precheck test item.
       testStatus: The result of the precheck item.
           
           Possible values are:
           - \"green\": The test passed with no issues.
           - \"yellow\": The test passed with warnings. There are non-critical issues
             that should be reviewed before proceeding.
           - \"red\": The test failed due to critical issues that must be resolved.
             
           Site Maintenance Operation Criteria:
           - When all test results are \"green\": The fault domain maintenance operation can proceed
             and is expected to complete successfully.
           - When test results include \"yellow\": The fault domain maintenance operation can proceed,
             but administrators should review the warnings and understand potential impacts.
           - When any test result is \"red\": The fault domain maintenance operation cannot proceed
             until the critical issues are resolved.
       message: Informative and localizable messages providing details about the test result.
   """
   testName: str
   testStatus: str
   message: _typing.Optional[pyVmomi.vmodl.LocalizableMessage] = None


class SiteMaintenancePrecheckStatus(pyVmomi.vmodl.DynamicData):
   """
   The status of a precheck for site maintenance operation.
   
   Attributes:
       timestamp: The timestamp indicating when the precheck was completed.
       status: The overall status of the site maintenance precheck that was queried.
           
           Please see `pyVmomi.vim.vsan.ResourceCheckStatusType` for possible statuses.
       taskDetails: The details of the precheck task that was generated
           and returned by PerformSiteMaintenancePrecheck
       resourceCheckResult: The predicted resource impact details assuming the queried operation
           is performed.
           
           This field will be populated only if a resource check
           for the queried precheck has completed successfully and recently.
   """
   timestamp: _datetime.datetime
   status: str
   taskDetails: _typing.Optional[SiteMaintenanceCheckTaskDetails] = None
   resourceCheckResult: _typing.Optional[SiteMaintenanceResourceCheckResult] = None


class SiteMaintenanceResourceCheckResult(ResourceCheckVsanResult):
   """
   The detailed information of resource check result for fault domain maintenance action.
   
   Attributes:
       vmToMigrate: List of VM Managed object IDs that will be migrated after
           the query operations are performed.
       vmToPowerOffInfo: List of VM to power off information that will be powered off after
           the query operations are performed, including the VM Managed object
           IDs and the reason for powering off.
       checkDetails: Represents the specific checks and their results for fault domain maintenance.
   """
   vmToMigrate: list[pyVmomi.VmomiSupport.ManagedObject] = []
   vmToPowerOffInfo: list[VMPowerOffInfo] = []
   checkDetails: list[SiteMaintenancePrecheckDetail] = []


class SiteMaintenanceSpec(pyVmomi.vmodl.DynamicData):
   """
   This class describes specification of a fault domain maintenance action.
   
   Attributes:
       faultDomainName: The name of the site against which the fault domain maintenance action is performed.
   """
   faultDomainName: str

class SiteMaintenanceState:
   """Defines the different fault domain maintenance states."""
   pass


class SnapServiceConfig(pyVmomi.vmodl.DynamicData):
   """
   The Snapshot service Configuration for vSAN.
   
   Attributes:
       enabled: Whether Snaphot service is enabled.
   
   Since: 8.0.0.4
   """
   enabled: bool

class SnapshotCreator:
   """
   The creator of snapshot.
   
   Since: 8.0.0.4
   """
   pass

class SnapshotType:
   """
   The type of snapshot.
   
   Since: 8.0.0.4
   """
   pass


class StoragePoolDiskResourceCheckResult(DiskResourceCheckResult):
   """
   The vSAN disk level resource check report for disks in a storage pool.
   
   It
   includes basic disk info, current disk usage and the predicted disk usage
   after the queried operation is performed
   `pyVmomi.vim.vsan.EntityResourceCheckDetails`.
   For example, if the queried resource check is for host enter maintenance
   mode operation, vSAN will simulate the disk usage after the queried host
   enters maintenance mode. This will provide user a sense of what the disk
   usage will look like if the queried operation is carried out.
   If `pyVmomi.vim.vsan.EntityResourceCheckDetails.isNew` is true, this is a new
   disk suggested to be added by vSAN simulation for more resources to make the
   operation succeed. In this case, currentUsage will be 0 and
   postOperationUsage will show how the new disk will be used assuming the
   queried operation is done from vSAN simulation.
   If `pyVmomi.vim.vsan.EntityResourceCheckDetails.isNew` is false, this is an
   existing disk in the current cluster. postOperationUsage will give the
   usage of the disk assuming the queried operation is done from vSAN
   simulation.
   
   Attributes:
       diskType: Represents storage pool disk type.
           
           Refer to
           `pyVmomi.vim.vsan.host.StoragePoolDiskType`
   """
   diskType: _typing.Optional[str] = None


class StoragePoolResourceCheckResult(EntityResourceCheckDetails):
   """
   The vSAN storage pool level resource check report.
   
   It includes the resource
   check result of all disks inside the storage pool on the host. Please see
   `pyVmomi.vim.vsan.StoragePoolDiskResourceCheckResult` for storage pool disk
   resource check details.
   
   Attributes:
       disks: The detailed resource check result for the disks in the storage pool.
   """
   disks: list[StoragePoolDiskResourceCheckResult] = []


class VMPowerOffInfo(pyVmomi.vmodl.DynamicData):
   """
   The detailed information of VMs to power off for fault domain maintenance action.
   
   Attributes:
       vmToPowerOff: List of VM Managed object IDs that will be powered off.
       reason: The reason for why the VMs need to power off.
   """
   vmToPowerOff: list[pyVmomi.VmomiSupport.ManagedObject] = []
   reason: _typing.Optional[pyVmomi.vmodl.LocalizableMessage] = None


class VbossConfig(pyVmomi.vmodl.DynamicData):
   """
   Defines some common configuration properties for
   both cluster and host layers.
   
   Attributes:
       enabled: Whether vSAN vBoss service is enabled.
   """
   enabled: bool
   configs: list[VbossObjectStoreConfig] = []


class VbossObjectStoreConfig(pyVmomi.vmodl.DynamicData):
   """
   Defines configuration properties for object store instance info on
   both cluster and host layers.
   
   Attributes:
       id: The ID of the object storeinstance.
       secretKey: The secret key of the object store instance.
           
           The secret key is used to authenticate between the object store
           service instance and vSAN datastore.
           It is a write-only field.
       volumeUuids: The list of volume UUIDs of the object store instance.
       properties: The additional properties of the object store instance.
           
           example values:
           {
           \"name\": \"object-store-name\",
           \"policy\": {
           \"id\": \"policy-id\",
           \"name\": \"policy-name\",
           \"vsanExpression\": \"((...))\"
           }
           }
   """
   id: str
   secretKey: _typing.Optional[str] = None
   volumeUuids: list[str] = []
   properties: _typing.Optional[str] = None


class VcRemoteVsanServerClusterConfig(pyVmomi.vmodl.DynamicData):
   """
   Remote vSAN server cluster configuration at a VC level.
   
   Attributes:
       serverClusters: Server cluster configurations for HCI Mesh.
   """
   serverClusters: list[VcRemoteVsanServerClusterInfo] = []


class VcRemoteVsanServerClusterInfo(pyVmomi.vmodl.DynamicData):
   """
   Remote vSAN server cluster info at a vCenter level.
   
   This contains
   additional information required for setting up a HCI Mesh configuration.
   
   Attributes:
       clusterUuid: The server cluster UUID which client cluster uses to mount remote vSAN
           datastores of server hosts.
       networkTopology: The network topology between the client and server cluster in the HCI
           Mesh configuration.
           
           It is only needed when the server cluster is a
           stretched cluster on local vCenter.
       siteAffinity: Site Affinity information between the client and server cluster.
           
           This
           is only to be provided in case of the server cluster being a stretched
           cluster with two Fault Domains. The site affinity provided implies the
           network connectivity between the coupled sites to be a high bandwidth/
           low latency link and the network connectivity between the uncoupled
           sites is assumed to be a low bandwidth high latency link. In case of a
           symmetric network connectivity between the client and server sites,
           this field can be left unset.
           A client site can only have one affinitized server site.
           A single server site can only be coupled with one client site.
           An empty list for siteAffinity will override the existing site affinity
           for the server cluster.
       ownerVc: Remote vCenter identity which owns this server cluster.
           
           This is used for
           remote vSAN across vCenter. The identity could be either FQDN or IP which
           is used to configure datastore source. This is only required during
           configuring remote data-in-transit encryption across vCenter.
           see `pyVmomi.vim.vsan.RemoteVcInfo.vcHost`
       ditConfig: Data in transit encryption config between client and server cluster
           for remote vSAN.
   """
   clusterUuid: str
   networkTopology: _typing.Optional[str] = None
   siteAffinity: list[RemoteVsanSiteAffinity] = []
   ownerVc: _typing.Optional[str] = None
   ditConfig: _typing.Optional[DataInTransitEncryptionConfig] = None


class VipConfigSpec(pyVmomi.vmodl.DynamicData):
   """
   Define virtual IP (VIP) specification.
   
   Attributes:
       enabled: Whether virtual IP (VIP) is enabled or not, disabled if it is not specified.
       v4NetworkConfig: IPv4 network configurations for Virtual IP.
           
           If provided, Virtual IP will use
           IPv4 network. At least one of v4NetworkConfig and v6NetworkConfig
           should be provided for Virtual IP enablement.
       v6NetworkConfig: IPv6 network configurations for Virtual IP.
           
           If provided, Virtual IP will use
           IPv6 network. At least one of v4NetworkConfig and v6NetworkConfig
           should be provided for Virtual IP enablement.
       vswitchConfig: The standard vSwitch configuration for Virtual IP vmkernal adapter.
           
           You can
           specify this property only if you do no specify
           `pyVmomi.vim.vsan.VipConfigSpec.distributedSwitchConfig`.
       distributedSwitchConfig: The distributed vSwitch configuration for Virtual IP vmkernal adapter.
           
           You can specify this property only if you do no specify
           `pyVmomi.vim.vsan.VipConfigSpec.vswitchConfig`.
   """
   enabled: _typing.Optional[bool] = None
   v4NetworkConfig: _typing.Optional[VipNetworkConfig] = None
   v6NetworkConfig: _typing.Optional[VipNetworkConfig] = None
   vswitchConfig: _typing.Optional[VipVswitchConfig] = None
   distributedSwitchConfig: _typing.Optional[VipDVswitchConfig] = None


class VipConfig(VipConfigSpec):
   """
   Specifies the config for Virtual IP.
   
   Attributes:
       vmknicName: The name of vmkernel adapter that is used by virtual IP.
       owner: The host with Virtual IP assigned to its vmknic by vSAN iSCSI service.
       ownerHostUuid: The uuid of host which currently holds this Virtual IP.
   """
   vmknicName: _typing.Optional[str] = None
   owner: _typing.Optional[pyVmomi.vim.HostSystem] = None
   ownerHostUuid: _typing.Optional[str] = None


class VipDVswitchConfig(pyVmomi.vmodl.DynamicData):
   """
   Define virtual IP (VIP) DvSwitch configurations.
   
   Attributes:
       portGroup: The port group moref for distributed vSwitch on which the virtual IP
           vmkernal adapter is created on.
           
           It should be set for enabling virtual
           IP. If the port group is removed after enablement, then it will be
           unset in the virtual IP query result.
       dvsUuid: The dvs uuid for distributed vSwitch on which the virtual IP
           vmkernal adapter is created on.
           
           Leave it unset for enabling
           virtual IP. It will be set for querying virtual IP configurations.
   """
   portGroup: _typing.Optional[pyVmomi.vim.dvs.DistributedVirtualPortgroup] = None
   dvsUuid: _typing.Optional[str] = None


class VipNetworkConfig(pyVmomi.vmodl.DynamicData):
   """
   Define virtual IP (VIP) network configurations for both IPv4
   and IPv6 families.
   
   Attributes:
       ipAddress: IP address for virtual IP.
       subnet: Subnet information for the virtual IP.
           
           It is network mask if this is representing IP configurations
           for IPv4 family.
           It is prefix length if this is representing IP configurations
           for IPv6 family.
       gateway: Gateway IP address for virtual IP.
           
           If not provided, it will
           use the default gateway.
   """
   ipAddress: str
   subnet: str
   gateway: _typing.Optional[str] = None


class VipVswitchConfig(pyVmomi.vmodl.DynamicData):
   """
   Define virtual IP (VIP) vSwitch configurations.
   
   Attributes:
       vswitchName: The standard vSwitch on which the Virtual IP vmkernel adapter will be created
           on.
       vlanId: The VLAN ID for the Virtual IP vmkernel adapter.
           
           Default 0 if not specified.
   """
   vswitchName: str
   vlanId: _typing.Optional[int] = None

class VsanAnalyticsEventLocationType:
   """
   Enumeration type for associating event with managed object
     
   This is a list of supported locations to associate an event.
   
   The event
   could be related to disk, hosts or cluster.
   """
   pass

class VsanAnalyticsEventSnapshotType:
   """
   Enumeration type for snapshot types
     
   This is a list of supported snapshot types.
   """
   pass

class VsanAnalyticsEventType:
   """
   Enumeration type for events currently subscribed.
   
     
   This is a list of supported supported events vSAN analytics will collect.
   """
   pass


class VsanBurnInTest(pyVmomi.vmodl.DynamicData):
   """
   Deprecated: As of vSphere API 6.7.vSAN burn in test result class.
   
   Attributes:
       testname: The burn in test name.
       workload: The burn in test workload, if has.
       duration: The burn in test duration (in seconds).
       result: The burn in test result.
   """
   testname: str
   workload: _typing.Optional[str] = None
   duration: pyVmomi.VmomiSupport.long
   result: str


class VsanBurnInTestCheckResult(pyVmomi.vmodl.DynamicData):
   """
   Deprecated: As of vSphere API 6.7.Checks that verify if all recommended vSAN burn in tests
   have been performed and passed.
   
   Attributes:
       passedTests: Passed burn in tests.
       notPerformedTests: Burn in tests with issue: There are burn in tests that have not been
           performed.
           
           It is recommended to perform all burn in tests.
       failedTests: Burn in tests with issue: There are burn in tests that have failed.
           
           It is recommended to perform and pass all burn in tests.
   """
   passedTests: list[VsanBurnInTest] = []
   notPerformedTests: list[VsanBurnInTest] = []
   failedTests: list[VsanBurnInTest] = []


class VsanCloudHealthStatus(pyVmomi.vmodl.DynamicData):
   """
   Data object containing the status of the vSAN Ready Care collection agent.
   
   Attributes:
       collectorRunning: Running status of the collector.
       lastSentTimestamp: A string timestamp of last data sent.
           
           When data was not sent, 'None' is returned.
       internetConnectivity: Status for the internet connectivity currently test connection to https://vcsa.vmware.com/
   """
   collectorRunning: _typing.Optional[bool] = None
   lastSentTimestamp: _typing.Optional[str] = None
   internetConnectivity: _typing.Optional[bool] = None


class VsanClusterBurnInTestResultList(pyVmomi.vmodl.DynamicData):
   """
   Deprecated: As of vSphere API 6.7.vSAN burn in test result store class.
   
   Attributes:
       items: List of burn in test result.
       hosts: The host manage object id list on which the burn test is executed
   """
   items: list[VsanBurnInTest] = []
   hosts: list[str] = []


class VsanCompliantDriver(pyVmomi.vmodl.DynamicData):
   """
   Information about the vSAN certified driver.
   
   Attributes:
       driverName: Name of the driver.
       driverVersion: Version of the driver.
       supportedFeatures: Supported features.
   """
   driverName: str
   driverVersion: str
   supportedFeatures: list[str] = []


class VsanCompliantFirmware(pyVmomi.vmodl.DynamicData):
   """
   Information about the HCL driver constraint for a given firmware version
   
   Attributes:
       firmwareVersion: Version of the firmware.
       compliantDrivers: Driver compliant for the firmware version.
   """
   firmwareVersion: str
   compliantDrivers: list[VsanCompliantDriver] = []


class VsanConfigBaseIssue(pyVmomi.vmodl.DynamicData):
   """Base class for all vSAN configuration issues."""
   pass


class VsanConfigCheckResult(pyVmomi.vmodl.DynamicData):
   """
   Various health checks for the misc vSAN configuration of cluster
   and its hosts, implementing both mandatory configurations and best
   practices for use in a vSAN environment.
   
   Attributes:
       vsanEnabled: True if the cluster has vSAN enabled.
       issues: Configuration issues.
   """
   vsanEnabled: bool
   issues: list[VsanConfigBaseIssue] = []


class VsanConfigNotAllDisksClaimedIssue(VsanConfigBaseIssue):
   """
   Configuration issue: There is one or more disks that are eligible
   for vSAN to use on the host.
   
   It is recommended to have all eligible
   disks on the cluster claimed by vSAN.
   
   Attributes:
       host: The host that contains eligible but not used disk(s)
       disks: The canonical name of disks that are eligible but unused by vSAN
   """
   host: pyVmomi.vim.HostSystem
   disks: list[str] = []

class VsanConfigType:
   """
   It's used to declare the vSAN configuration types that the hardware
   components like CPU, memory, disk and physical NIC is compatible with.
   """
   pass


class VsanDatastoreDefaultPolicySelectionConfig(pyVmomi.vmodl.DynamicData):
   """
   vSAN datastore default policy selection configurations
   
   Attributes:
       enabled: Flag to specify whether to allow automatically
           select default datastore policy
   """
   enabled: bool


class VsanDeconvergedNetConfig(pyVmomi.vmodl.DynamicData):
   """
   Spec for de-converged network configuration.
   
   Attributes:
       enabled: Whether de-converged network is enabled in the cluster.
           
           This property can be set only on vSAN Max clusters.
   """
   enabled: bool

class VsanDiskCompatibilityType:
   """Values indicate the vSAN storage types that the disk is compatible with."""
   pass


class VsanDiskModelInfo(pyVmomi.vmodl.DynamicData):
   """
   Information of the vSAN disk drive.
   
   Attributes:
       productId: Product ID of the disk drive.
           
           E.g., AL15SEB120N. This is the key identifier
           of the disk.
       vendor: Vendor of the disk drive.
           
           E.g., TOSHIBA
       partNumber: Part number of the disk drive.
           
           E.g., HDEBL02LPA51F. When this is present,
           it will replace the `pyVmomi.vim.vsan.VsanDiskModelInfo.productId` as the
           key identifier of the disk.
   """
   productId: str
   vendor: str
   partNumber: _typing.Optional[str] = None


class VsanDownloadItem(pyVmomi.vmodl.DynamicData):
   """
   Information of a download item
   
   Attributes:
       url: URL to the download item
       sha1sum: SHA1 sum of the download item
       formatType: An optional format identifier.
       itemId: An optional ID for this item.
   """
   url: str
   sha1sum: str
   formatType: _typing.Optional[str] = None
   itemId: _typing.Optional[str] = None


class VsanEsaConfig(pyVmomi.vmodl.DynamicData):
   """
   The configurations for the vSAN ESA.
   
   This supports storage pool.
   
   Attributes:
       storagePoolSpecs: vSAN storage pool disk specification for manual disk claim.
           
           Throws fault if vSAN ESA is not enabled or if any errors
           occur during storage pool disk claim operation.
           Refer to `pyVmomi.vim.vsan.host.AddStoragePoolDiskSpec`
       hclDiskClaimEnabled: Whether the HCLDiskClaim setting is enabled for the cluster.
           
           Set hclDiskClaimEnabled to True/False, to enable/disable HCL disk claim
           feature on vSAN ESA cluster.
           Throws fault if
           1\\. HclDiskClaim is being enabled and storagePoolSpec is being specified for manual disk claim.
           2\\. If vSAN ESA is not enabled or being enabled.
           3\\. If vSAN ESA is being disabled and hclDiskClaim setting is being enabled in the input spec.
       datastoreDefaultPolicySelectionConfig: vSAN datastore default policy selection configurations.
           
           Only available for vSAN ESA
       diskConfiguration: Attribute to specify disk configuration for vSAN ESA prescriptive
           disk claim feature.
           
           vSAN will automatically claim disks according to the prescribed
           configuration on all hosts in the cluster.
           Throws fault if
           1\\. vSAN ESA is not enabled or being disabled.
           2\\. If HCL aware disk claim configuration is enabled or being enabled.
           3\\. If storagePoolSpecs is also specified.
           4\\. Any other faults that occur while performing disk claim operation
           on the cluster.
           Refer to `pyVmomi.vim.vsan.VsanEsaDiskConfiguration`
       autoRAIDConfig: vSAN auto RAID configuration.
       deleteStoragePoolDiskSpec: vSAN storage pool disk remove specification for manual disk removal.
           
           Throws fault if vSAN ESA is not enabled or if any errors
           occur during storage pool disk removal operation.
           Refer to `pyVmomi.vim.vsan.host.DeleteStoragePoolDiskSpec`
   """
   storagePoolSpecs: list[pyVmomi.vim.vsan.host.AddStoragePoolDiskSpec] = []
   hclDiskClaimEnabled: _typing.Optional[bool] = None
   datastoreDefaultPolicySelectionConfig: _typing.Optional[VsanDatastoreDefaultPolicySelectionConfig] = None
   diskConfiguration: _typing.Optional[VsanEsaDiskConfiguration] = None
   autoRAIDConfig: _typing.Optional[AutoRAIDConfig] = None
   deleteStoragePoolDiskSpec: _typing.Optional[pyVmomi.vim.vsan.host.DeleteStoragePoolDiskSpec] = None


class VsanEsaConfigInfo(pyVmomi.vmodl.DynamicData):
   """
   The current configuration settings for vSAN ESA.
   
   Attributes:
       hclDiskClaimEnabled: Whether the HCLDiskClaim setting is enabled for the cluster.
       datastoreDefaultPolicySelectionConfig: vSAN datastore default policy selection configurations.
           
           Only available for vSAN ESA
       diskConfiguration: Lists the current vSAN ESA prescriptive disk configuration of the vSAN ESA cluster.
           
           Please see `pyVmomi.vim.vsan.VsanEsaDiskConfiguration` for available
           disk state information.
       autoRAIDConfig: vSAN auto RAID configuration.
   """
   hclDiskClaimEnabled: _typing.Optional[bool] = None
   datastoreDefaultPolicySelectionConfig: _typing.Optional[VsanDatastoreDefaultPolicySelectionConfig] = None
   diskConfiguration: _typing.Optional[VsanEsaDiskConfiguration] = None
   autoRAIDConfig: _typing.Optional[AutoRAIDConfig] = None


class VsanEsaDiskConfiguration(pyVmomi.vmodl.DynamicData):
   """
   vSAN ESA disk configuration to be claimed by vSAN ESA prescriptive
   disk claim.
   
   Attributes:
       diskClaimConfiguration: Specify one or more desired disk configuration to be claimed on vSAN
           ESA cluster by vSAN ESA prescriptive disk claim.
           
           Any existing configuration that is omitted from this specification will
           be deleted. Please specify any new configuration along with the
           existing configuration if any. Existing config can be retrieved through
           `pyVmomi.vim.cluster.VsanVcClusterConfigSystem.getConfigInfoEx`
           Refer to `pyVmomi.vim.vsan.DiskClaimConfiguration`
   """
   diskClaimConfiguration: list[DiskClaimConfiguration] = []


class VsanExtendedConfig(pyVmomi.vmodl.DynamicData):
   """
   vSAN extended configurations
   
   Attributes:
       objectRepairTimer: This configuration is to determine delay time in minutes for vSAN,
           to wait for absent component to come back before starting repair it.
           - Allowed values: 0 to 4294967295;
           - Default value: 60.
       disableSiteReadLocality: By default, site read locality is enabled for vSAN stretched
           cluster/2 nodes configuration, with this, reads to vSAN object
           only occur on the site the VirtualMachine resides on.
           
           But with
           this setting, we can disable the site read locality, which will
           force reads across all mirrors, in low latency vSAN stretched
           cluster/2 nodes configuration, this means reads would occur
           across both sites in a stretched cluster, which can most
           effectively improve the read performance.
           - Allowed values: True to disable site read locality;
             False to turn on site read locality;
           - Default value: False.
       enableCustomizedSwapObject: While create swap object for VirtualMachine, policy
           'proportionalCapacity' is overwritten by default with value 100,
           this means swap object will reserve 100% space of its size on
           vSAN datastore.
           
           This behavior can be turned off through this
           config, allow customer to fully control the policy
           'proportionalCapacity' for swap object to save swap spaces.
           After set this field to True, swap object policy set on host
           through command 'esxcli vsan policy setdefault' will be fully
           respected;
           - Allowed values: True to stop assigning 'proportionalCapacity' of
             100 for swap object to create;
             False to take the default behavior.
           - Default value: False.
       largeScaleClusterSupport: By default, vSAN cluster can only grow up to 32 nodes.
           
           But by
           setting this option, vSAN cluster is allowed to grow up to large
           scale, at maximum to 64 nodes. Please be noted, if this option
           is changed before vSAN enabled, it can be applied at host side
           immediately; but if it is changed on a vSAN cluster, all hosts
           are required to reboot to apply this change. After setting this,
           please review the vSAN health check result, which can help to
           figure out which host requires rebooting.
           - Allowed values: True to support large scale vSAN cluster, 64
             nodes for now;
             False to not support, and at maximum to 32
             nodes;
           - Default value: False.
       proactiveRebalanceInfo: Proactive Rebalance Information.
           
           Refer to `pyVmomi.vim.vsan.ProactiveRebalanceInfo`.
       capacityReservationInfo: Enforce capacity reservation Information.
           
           Refer to `pyVmomi.vim.vsan.CapacityReservationInfo`.
   """
   objectRepairTimer: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   disableSiteReadLocality: _typing.Optional[bool] = None
   enableCustomizedSwapObject: _typing.Optional[bool] = None
   largeScaleClusterSupport: _typing.Optional[bool] = None
   proactiveRebalanceInfo: _typing.Optional[ProactiveRebalanceInfo] = None
   capacityReservationInfo: _typing.Optional[CapacityReservationInfo] = None


class VsanFileServiceOvfSpec(pyVmomi.vmodl.DynamicData):
   """
   The specification of the OVF that is used to deploy file service virtual
   machines.
   
   Each of the OVF specification can be uniquely identified by
   its version number.
   
   Attributes:
       version: The release version of the vSAN file services OVF.
           
           In vCenter, it will
           keep at most one instance of the OVF for each version. Besides the
           version number, the build number will be attached in this field.
       updateTime: The update time tracks the time when this vSAN file service OVF
           is installed into the repository of the vCenter.
       task: The task tracking the vSAN file service OVF download operation.
           
           If the task
           is not present, it means that the OVF has been uploaded successfully.
   """
   version: _typing.Optional[str] = None
   updateTime: _typing.Optional[_datetime.datetime] = None
   task: _typing.Optional[pyVmomi.vim.Task] = None


class VsanFileServicePreflightCheckResult(pyVmomi.vmodl.DynamicData):
   """
   The preflight check result for enabling vSAN file services.
   
   Attributes:
       ovfInstalled: This field indicates whether the file service OVF for running vSAN file
           services has been installed on the vCenter or not.
           
           This field will show the
           highest OVF version present on this vCenter that is compatible to the
           cluster. This field will not be set if no compatible OVF version could be
           found on this vCenter.
       fsvmVersion: This field indicates current running file service OVF version used by vSAN
           file service.
           
           It will only be present if there are file service VMs running
           in this cluster without mixed version.
       lastUpgradeDate: This field indicates date file service VMs last upgraded.
       ovfMixedModeIssue: Field to indicate whether there are multiple file service VM ovf versions
           running.
           
           This field will be left empty if there is no issue regarding the mixed OVF
           version file service VMs.
       hostVersion: Field to indicate the lowest host version in this cluster.
           
           This filed will be
           left empty if there are no hosts in the cluster.
       mixedModeIssue: vSAN file service cannot be enabled when there is any host whose version is
           lower than minimum required host version in this cluster.
           
           Minimum required
           host version is 7.0.0 in vSAN OSA cluster, or 8.0.2 in vSAN ESA cluster.
           This issue will be reported if any host whose version is lower than minimum
           required host version is detected. If this field is empty, it means that
           all the hosts in the cluster meet the version requirement.
       networkPartitionIssue: Issues regarding whether there are network partitions in the cluster.
           
           This
           field will be left empty if there are no network partitions in this cluster.
       vsanDatastoreIssue: Checks whether the vSAN datastore is present to all the hosts to the cluster.
           
           If hosts without vSAN datastore will be reported in this field. This
           field will be left empty if all the host in this cluster are with vSAN
           datastore.
       domainConfigIssue: Checks whether the domain configuration is valid.
           
           Currently the check includes
           the existence of the file server IP addresses, the correctness of file server
           AD domain username and password, the network connectivity of file server domain
           configuration. This field will only be present when the domain configuration
           issue is detected.
       fileServiceVersion: This field indicates the highest file service version that the cluster can
           support.
           
           The field will be left empty if the cluster doesn't meet the
           requirement to enalbe file service.
       dvsConfigIssue: Checks whether the dvs configuration is valid.
           
           This check validates
           if the supplied network for file service is dvsPortGroup, the DSwitch
           which is hosting the port group has version equal to or older then 6.6.0.
           This field will only be present when DVS configuration issue is detected.
       domainConfigWarning: This field indicates the network connectivity between file server and gateway.
           
           Currently, it will only be present when file server could not connect to gateway.
           As it is a warning, it won't block user to proceed.
       ntpConfigWarning: Checks whether the NTP is configured in ESXi hosts.
           
           This field will only be
           present when the NTP is not configured in ESXi hosts. Without NTP configured,
           it won't block user to proceed while user might encounter failure later when
           joining Active Directory domain if time is out of sync.
       svsConfigIssue: Checks whether the standard switch configuration is valid.
       nsxConfigIssue: Checks whether the nsx configuration is valid.
   """
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
   """
   This managed object type provides the file service related configuration
   and query APIs.
   
   It can be accessed through MOID of 'vsan-cluster-file-service-system',
   through vSAN service on vCenter at cluster level, or accessed through MOID
   of 'vsan-file-service-system' on ESXi host for the detailed operation.
   """
   def DownloadFileServiceOvf(self, downloadUrl: str) -> pyVmomi.vim.Task:
      """
      Downloads a file service OVF file of the specified version from VMware
      website and install it to the OVF repository in vCenter.
      
      Args:
          downloadUrl: URL to download the vSAN file service OVF, only HTTPS URL
              is supported.
      
      Returns:
          Task for tracking the OVF installation.
      
      Raises:
          pyVmomi.vmodl.fault.InvalidArgument: Exception if the OVF of the specified version does
              not exist as specified in the source URL.
      """
      ...
   def QueryFileServiceOvfs(self) -> list[VsanFileServiceOvfSpec]:
      """
      Lists all available vSAN File Service OVF in this vCenter.
      
      Returns:
          List of the file services OVFs available in this vCenter.
      """
      ...
   def FindOvfDownloadUrl(self, cluster: pyVmomi.vim.ClusterComputeResource) -> str:
      """
      Find a compatible vSAN File Service OVF download URL for the target cluster.
      
      This API needs internet access to fetch the latest OVF download URL for the
      specified cluster.
      
      Args:
          cluster: The target cluster to download OVF files.
      
      Returns:
          The OVF download URL. Return an empty string if no proper OVF
          download URL could be found.
      """
      ...
   def PerformFileServicePreflightCheck(self, cluster: pyVmomi.vim.ClusterComputeResource, domainConfig: _typing.Optional[FileServiceDomainConfig], network: _typing.Optional[pyVmomi.vim.Network], scope: _typing.Optional[str], domainUuid: _typing.Optional[str]) -> VsanFileServicePreflightCheckResult:
      """
      Perform a preflight check on a cluster for enabling vSAN file service
      and/or for the new file service domain configuration.
      
      The preflight check items includes:
      - Basic check
        - Network partition check
        - vSAN datastore presence to each host
        - The versions of the ESXi hosts match in this cluster
        - NTP configuration check in ESXi hosts if vSAN file service
          version is 8.0 or newer
        - Domain configuration format check
        - Running OVF information check
        - If a DVS portgroup is passed as network,
          it checks if DVS version is older than 6.6
      - Advanced check
        - Checks covered in 'basic' scope
        - File server domain configuration validation in live environment
          when vSAN file service has been enabled
      
      Args:
          cluster: The target cluster to perform preflight check.
          domainConfig: The domain configuration to be validated.
              If not specified, the validation for the
              domain will be skipped.
          network: The network which will be used for fs containers
          scope: The scope that preflight check will cover. Valid inputs are
              listed in the `pyVmomi.vim.vsan.FileServicePreflightCheckScope`
              field. Defaults to \"basic\".
          domainUuid: The file service domain UUID. It is required when
              the advanced preflight check is performed on an
              existing domain. If a new file service domain is
              to be created, leave it empty.
      
      Returns:
          Preflight check result.
      """
      ...
   def CreateFileServiceDomain(self, domainConfig: FileServiceDomainConfig, cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource]) -> pyVmomi.vim.Task:
      """
      Creates a file service domain in the vSAN cluster.
      
      A vSAN file service domain is designed with the following properties:
      - A file service domain has a FQDN domain name (e.g., fs.mycompany.com)
        that client can mount.
      - It can join an Active Directory domain and use Kerberos for
        authentication and user ID mapping, or use AUTH_SYS to trust user ID
        sent from clients.
      - One more more file shares can be created in a file service domain
        and all these file shares have the same security/network properties
        of this file service domain. These file shares can be accessed from a
        certain network (e.g., VM Network).
        
      In current version, only one file service domain can be created per cluster,
      which can be initiated when the file service is enabled.
      
      Args:
          domainConfig: Domain configuration information.
          cluster: The target cluster. Ignored when called on ESXi hosts.
      
      Returns:
          A task tracking the domain creation progress.
      
      Raises:
          pyVmomi.vim.fault.InvalidState: Exception when vSAN file service is not enabled in
              this cluster.
          pyVmomi.vmodl.fault.InvalidArgument: Exception for invalid input arguments, for example,
              if the domain name already configured in the cluster.
      """
      ...
   def ReconfigureFileServiceDomain(self, domainUuid: str, domainConfig: FileServiceDomainConfig, cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource], deleteDomainConfigFields: list[str]) -> pyVmomi.vim.Task:
      """
      Updates a file service domain in the vSAN cluster.
      
      Args:
          domainUuid: The UUID of the domain to be reconfigured.
          domainConfig: New configuration of the domain. Only set the fields that
              require reconfiguration, and leave others unset.
          cluster: The target cluster. Ignored when called on ESXi hosts.
          deleteDomainConfigFields: The domain config fields to be deleted. For
              example to remove directoryServerConfig
              from the domainConfig provide
              [\"directoryServerConfig\"] here and keep the
              same unset in provided domainConfig. Do note
              removing directoryServerConfig is only
              allowed when there are no active shares.
              Here is the list of currently supported field:
              - directoryServerConfig since 7.0U1
              - directoryServerConfig.preferredADServers
                since 8.0U1 
                
              Providing any other value here will cause
              InvalidArgumentError fault.
      
      Returns:
          A task tracking the domain reconfiguration progress.
      
      Raises:
          pyVmomi.vim.fault.InvalidState: Exception when vSAN file service is not enabled in
              this cluster.
          pyVmomi.vmodl.fault.InvalidArgument: Exception for invalid input arguments, for example,
              if the domain does not exist in this cluster.
      """
      ...
   def RemoveFileServiceDomain(self, domainUuid: str, cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource]) -> pyVmomi.vim.Task:
      """
      Removes a file service domain in the vSAN cluster.
      
      A file service domain is not allowed to be removed if it still has any
      file shares.
      
      Args:
          domainUuid: The unique domain uuid that is configured in the directory
              service, for example, Active Directory (AD) from Microsoft.
          cluster: The target cluster. Ignored when called on ESXi hosts.
      
      Returns:
          A task tracking the domain remove progress.
      
      Raises:
          pyVmomi.vim.fault.InvalidState: Exception when vSAN file service is not enabled in
              this cluster, or it still has file shares.
          pyVmomi.vmodl.fault.InvalidArgument: Exception for invalid input arguments, for example,
              if the domain does not exist in this cluster.
      """
      ...
   def QueryFileServiceDomains(self, querySpec: _typing.Optional[FileServiceDomainQuerySpec], cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource]) -> list[FileServiceDomain]:
      """
      Lists all file service domains in the vSAN cluster.
      
      To list all the file service domains, leave both the uuids and names
      field empty. Otherwise the return result will be a set of file service
      domains matches the domain UUID or domain name provided in the parameters.
      If both fields are provided, only those file service domain with both
      domain name and domain UUID matched will be returned.
      
      Args:
          querySpec: The specifications of the file service domains to be
              queried.
          cluster: The target cluster. Ignored when called on ESXi hosts.
      
      Returns:
          List of all the domain information on this host.
      
      Raises:
          pyVmomi.vim.fault.InvalidState: Exception when the file service is not enabled in this
              cluster.
      """
      ...
   def CreateFileShare(self, config: FileShareConfig, cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource]) -> pyVmomi.vim.Task:
      """
      Creates a file share in this vSAN cluster.
      
      Args:
          config: The file share configuration, as specified in
              . Note that the backing vSAN object for the
              file share will be by default 1TB if the file share is thin
              provisioned. Otherwise the backing vSAN object is set to 255GB if
              quota is not set.
          cluster: The target cluster. Ignored when called on ESXi hosts.
      
      Returns:
          A task tracking the share creation progress. The UUID of the file
          share will be set to the task result field if the task succeeds.
      
      Raises:
          pyVmomi.vim.fault.InvalidState: Exception when vSAN file service is not enabled in
              this cluster.
          pyVmomi.vmodl.fault.InvalidArgument: Exception for invalid input arguments, for example,
              if the domain for this new file share does not exist
              in this cluster.
      """
      ...
   def ReconfigureFileShare(self, shareUuid: str, config: FileShareConfig, cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource], deleteLabelKeys: list[str], force: _typing.Optional[bool]) -> pyVmomi.vim.Task:
      """
      Reconfigures a file share in this vSAN cluster.
      
      All the configurations of a vSAN file share can be reconfigured through this
      API, except the file service domain.
      
      Args:
          shareUuid: The UUID of the file share to be reconfigured.
          config: The file services configuration. Only set the fields that
              require reconfiguration, and leave the others unset.
              This API will update or create the labels specified in the
              config. Labels to be deleted should be specified in the
              'deleteLabelKeys' parameter. Other labels will remain intact.
          cluster: The target cluster. Ignored when called on ESXi hosts.
          deleteLabelKeys: The keys of share labels to be deleted. If a specified
              label key does not exist in the file share, the deletion of
              this label will be ignored.
          force: The force flag is to force the reconfiguration of a vSphere
              managed file share, for example, the file share managed by Cloud
              Native Storage (CNS) service.
      
      Returns:
          A task tracking the share reconfiguring progress.
      
      Raises:
          pyVmomi.vim.fault.InvalidState: Exception when vSAN file service is not enabled in
              this cluster.
          pyVmomi.vmodl.fault.InvalidArgument: Exception for invalid input arguments, for example,
              if the file share does not exist in this cluster.
      """
      ...
   def RemoveFileShare(self, shareUuid: str, cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource], force: _typing.Optional[bool]) -> pyVmomi.vim.Task:
      """
      Removes a file share in the domain.
      
      Args:
          shareUuid: The UUID of the file share to be removed.
          cluster: The target cluster. Ignored when called on ESXi hosts.
          force: The force flag is to force the removal of a vSphere managed
              file share, for example, the file share managed by Cloud
              Native Storage (CNS) service.
      
      Returns:
          A task tracking the file share remove progress.
      
      Raises:
          pyVmomi.vim.fault.InvalidState: Exception when vSAN file service is not enabled in
              this cluster.
          pyVmomi.vmodl.fault.InvalidArgument: Exception for invalid input arguments, for example,
              if the file share does not exist in this cluster.
      """
      ...
   def QueryFileShares(self, querySpec: FileShareQuerySpec, cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource]) -> _typing.Optional[FileShareQueryResult]:
      """
      Lists all file shares in the domain.
      
      To list all the file shares in the domain, leave both the shareUuids and
      shareNames field empty. Otherwise the return result will be a set of file
      shares matches the share UUID or share name provided in the parameters. If
      both fields are provided, only those file shares with both share name and
      share UUID matched will be returned.
      Note that if none of file shares matches the querySpec, the return value is
      None.
      
      Args:
          querySpec: The specifications of the file shares to be queried.
          cluster: The target cluster. Ignored when called on ESXi hosts.
      
      Returns:
          Result of the file share query.
      
      Raises:
          pyVmomi.vim.fault.InvalidState: Exception when vSAN file service is not enabled in
              this cluster.
          pyVmomi.vmodl.fault.InvalidArgument: Exception for invalid input arguments, for example,
              if the domain does not exist in this cluster.
      """
      ...
   def UpgradeFsvm(self, cluster: pyVmomi.vim.ClusterComputeResource) -> pyVmomi.vim.Task:
      """
      Upgrade FSVM to latest ovf that is compatible with cluster's host version.
      
      A compatible OVF is expected be uploaded before calling this API.
      A preflight check will be conducted before the upgrade on the following API.
      
      Args:
          cluster: The target cluster in which FSVM deployed.
      
      Returns:
          None
      
      Raises:
          pyVmomi.vim.fault.InvalidState: Exception if the OVF of the compatible version for the
              hosts cannot be found on the corresponding vCenter
              server, or file service is not running in a valid state.
      """
      ...
   def RebalanceFileService(self, cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource]) -> pyVmomi.vim.Task:
      """
      This API is to rebalance file service in cluster.
      
      Args:
          cluster: The target cluster to do rebalance.
      
      Returns:
          the task tracking the rebalance progress.
      """
      ...
   def CreateFileShareSnapshot(self, config: FileShareSnapshotConfig, cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource]) -> pyVmomi.vim.Task:
      """
      Create a snapshot for a file share in this vSAN cluster.
      
      Args:
          config: The snapshot configuration.
          cluster: The target cluster. Ignored when called on ESXi hosts.
      
      Returns:
          A task tracking the snapshot creation progress.
      
      Raises:
          pyVmomi.vim.fault.InvalidState: Exception for invalid states, for example, if vSAN
              file service is not enabled in this cluster.
          pyVmomi.vmodl.fault.InvalidArgument: Exception for invalid input arguments, for example,
              if the file share to create a snapshot does not exist
              in this cluster.
      """
      ...
   def RemoveFileShareSnapshot(self, shareUuid: str, snapshotName: str, cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource]) -> pyVmomi.vim.Task:
      """
      Remove a snapshot of a file share in this vSAN cluster.
      
      Note: due to the limitation, it's not allowed to remove the latest snapshot
      for file service in 70U2 and an InvalidState exception will be thrown for
      this case.
      
      Args:
          shareUuid: UUID of the file share to delete the snapshots.
          snapshotName: Name of the snapshot to be deleted.
          cluster: The target cluster. Ignored when called on ESXi hosts.
      
      Returns:
          A task tracking the snapshot remove progress.
      
      Raises:
          pyVmomi.vim.fault.InvalidState: Exception for invalid states, for example, if vSAN
              file service is not enabled in this cluster.
          pyVmomi.vmodl.fault.InvalidArgument: Exception for invalid input arguments, for example,
              if the snapshot does not exist in this cluster.
      """
      ...
   def QueryFileShareSnapshots(self, querySpec: FileShareSnapshotQuerySpec, cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource]) -> _typing.Optional[FileShareSnapshotQueryResult]:
      """
      List all the snapshots that match the query spec.
      
      Args:
          querySpec: The specification of the snapshots to be queried.
          cluster: The target cluster. Ignored when called on ESXi hosts.
      
      Returns:
          Result of the snapshot query.
      
      Raises:
          pyVmomi.vim.fault.InvalidState: Exception for invalid states, for example, if vSAN
              file service is not enabled in this cluster.
          pyVmomi.vmodl.fault.InvalidArgument: Exception for invalid input arguments, for example,
              if the share does not exist in this cluster.
      """
      ...


class VsanGenericClusterBaseIssue(pyVmomi.vmodl.DynamicData):
   """Base class for all vSAN generic cluster configuration issues."""
   pass


class VsanGenericClusterBestPracticeHealth(pyVmomi.vmodl.DynamicData):
   """
   Various best practices for vSAN generic cluster configurations.
   
   Attributes:
       drsEnabled: True if DRS is enabled for this cluster.
       haEnabled: True if HA is enabled for this cluster.
       issues: Generic cluster configuration issues.
           
           For example: DRS/HA configurations, host name configurations, etc.
   """
   drsEnabled: bool
   haEnabled: bool
   issues: list[VsanGenericClusterBaseIssue] = []

class VsanHciMeshConfigLimits:
   """vSAN HCI Mesh Config limits"""
   pass


class VsanHclDeviceConstraint(pyVmomi.vmodl.DynamicData):
   """
   Information about the HCL constraint for a PCI device in the cluster/host.
   
   Attributes:
       pciId: PCI ID of a vSAN device.
       vcgLink: VCG URL for the device.
           
           In case this PCIe device is not certified by VMware
           VCG, this field will be empty.
       similarVcgLinks: VCG URLs for similar device, with the same PCI ID.
           
           Some vendors manufacture
           multiple PCIe devices with the same PCI ID, in case there're multiple devices
           of the same PCI ID certified by VMware VCG, this is the URL of those devices.
           Otherwise it will be empty.
       compliantFirmwares: vSAN compliant firmwares(and drivers) for this device.
       vcgId: Device id in the VCG portal.
       model: Model of the device.
           
           E.g., 1.2TB 10K 12Gbps SAS 2.5\"
       partner: Partner of the device.
           
           E.g., Lenovo
       partNumber: Part number of the device.
           
           E.g., HDEBL02LPA51F
       release: Certified VMware release.
   """
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
   """
   Information about the HCL constraint for a disk drive.
   
   Attributes:
       productId: Product ID of the disk drive.
           
           E.g., AL15SEB120N
       vendor: Vendor of the disk drive.
           
           E.g., TOSHIBA
       constraints: VCG HCL constraints for the disk(SAS/SATA) drive.
           
           In case the disk drive
           to query is not a SAS/SATA drive or not certified by VMware, this field
           will be empty.
       pcieConstraints: VCG HCL constraints for the PCI-e based disk drive.
           
           In case this disk
           drive is not a PCIe device or not certified by VMware, this field will
           be empty.
       partNumber: Part number of the disk drive.
           
           E.g., HDEBL02LPA51F. When it is
           present, it will replace the product id as the key identifier
           of the disk
   """
   productId: str
   vendor: str
   constraints: list[VsanHclMinFwConstraint] = []
   pcieConstraints: list[VsanHclDeviceConstraint] = []
   partNumber: _typing.Optional[str] = None


class VsanHclDriverInfo(pyVmomi.vmodl.DynamicData):
   """
   Captures a combination of driver, firmware and associated information
   recommended by the vSAN HCL.
   
   Attributes:
       driverVersion: Driver version as suggested by the HCL.
       driverLink: Where to get the driver from.
       fwVersion: The firmware version of the controller as suggested by the HCL.
       fwLinks: Where to get the firmware files from.
           
           Can be multiple files belonging to
           the same firmware, or separate firmwares for different parts of the system.
           Required to be unique file format types.
       toolsLinks: Any additional tools that should be installed alongside the driver.
           
           May include
           tools required for firmware patching.
       eula: EULA provided by this item.
           
           Note, in case of a VIB, this is empty, as for Firmware,
           it is the EULA provided by the vendor.
       driverType: The type of this specific driver listed on HCL.
           
           Supported drivers type are inbox and async.
       driverName: Driver name as suggested by the HCL.
       diskModes: The disk mode supported by this driver and firmware as suggested by the HCL.
           
           E.g., ['All-Flash', 'Hybrid'].
       supportedFeatures: Features supported by this driver and firmware pair as suggested by the HCL.
           
           E.g., ['RoCE v2']
   """
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
   """
   Information about a Minimum Firmware HCL constraint.
   
   Attributes:
       vcgId: Device id in the VCG portal.
       vcgLink: Device VCG portal URL.
       model: Model of the device.
           
           E.g., 1.2TB 10K 12Gbps SAS 2.5\"
       partner: Partner of the device.
           
           E.g., Lenovo
       partNumber: Part number of the device.
           
           E.g., HDEBL02LPA51F
       release: Certified VMware release.
       firmware: Certified firmware(Minimum).
   """
   vcgId: int
   vcgLink: str
   model: str
   partner: str
   partNumber: _typing.Optional[str] = None
   release: str
   firmware: str


class VsanHclQuerySpec(pyVmomi.vmodl.DynamicData):
   """
   vSAN HCL query specification which defines the validation target and scope.
   
   Attributes:
       includeOnlyVsanControllers: True to only include controllers used by vSAN.
           
           False will include all controllers in host. The default is True.
       cluster: The cluster to be validated.
           
           If it's specified, the result for
           all hosts within the same cluster will be returned. If both cluster and
           hosts are provided, only the result of provided hosts will be returned.
       hosts: The hosts to be validated.
           
           Instead of returning the result of whole cluster,
           it's supported to check against a list of hosts.
       vsanStoragePoolEligibleDisksOnly: True indicates only the disks which are eligible for use by vSAN storage
           pool will be returned.
           
           The default is False.
   """
   includeOnlyVsanControllers: _typing.Optional[bool] = None
   cluster: _typing.Optional[pyVmomi.vim.ComputeResource] = None
   hosts: list[pyVmomi.vim.HostSystem] = []
   vsanStoragePoolEligibleDisksOnly: _typing.Optional[bool] = None


class VsanHclReleaseConstraint(pyVmomi.vmodl.DynamicData):
   """
   Information about the device HCL constraints for a particular release.
   
   Attributes:
       cluster: The vSAN cluster.
       release: Target vSphere release.
       hostDevices: Host devices.
       constraints: PCI Device HCL constraints.
   """
   cluster: pyVmomi.vim.ClusterComputeResource
   release: str
   hostDevices: list[VsanHostDeviceInfo] = []
   constraints: list[VsanHclDeviceConstraint] = []


class VsanHealthConfigSpec(pyVmomi.vmodl.DynamicData):
   """
   The spec for all vSAN health configurations.
   
   Attributes:
       healthCheckThresholdSpec: The spec defining the thresholds for all of the supported targets.
           
           For the full list of all the supported targets, see:
           `pyVmomi.vim.vsan.VsanHealthThresholdTarget`
       historicalHealthConfig: vSAN historical health configuration.
   """
   healthCheckThresholdSpec: list[VsanHealthThreshold] = []
   historicalHealthConfig: _typing.Optional[VsanHistoricalHealthConfig] = None


class VsanHealthCustomizationSpec(pyVmomi.vmodl.DynamicData):
   """
   The spec for vSAN health general configuration.
   
   Attributes:
       ssdEnduranceSpec: The spec for NVMe SSD endurance threshold configuration.
   
   Since: 8.0.0.4
   """
   ssdEnduranceSpec: list[SSDEnduranceThresholdSpec] = []

class VsanHealthPerspective:
   """
   The total amount of health checks is split into multiple different
   perspectives.
   
   This list defines sets labels for sets of health checks
   in 8.x and previous releases.
   """
   pass

class VsanHealthPerspective90:
   """
   This list defines sets labels of multiple different perspectives
   for sets of health checks in 9.0 release.
   """
   pass

class VsanHealthStatusType:
   """
   Defines health status states applicable to various vSAN system entities.
   
   An entity in vSAN health system can have one of the following state.
   Each state represent the health status of entity in terms of vSAN health
   perspective.
   Each system can define its notion of each health status. For example, status
   'red' for capacity means cluster is running very close to datastore full but
   status 'red' for for an object mean it is already 'inaccessible'.
   """
   pass


class VsanHealthThreshold(pyVmomi.vmodl.DynamicData):
   """
   Define threshold values for the health status VsanHealthStatusType.red and
   VsanHealthStatusType.yellow for the given vSAN entity.
   
   Each vSAN entity is independent to define the threshold values as per the
   requirement.
   Like a capacity system can have threshold in form of percentage of total
   capacity. Other systems, for example, congestion system can have threshold
   value as fixed numbers.
   
   Attributes:
       yellowValue: Entity beyond this threshold will be marked as VsanHealthStatusType.yellow.
       redValue: Entity beyond this threshold will be marked as VsanHealthStatusType.red.
       target: This optional attribute is used as the target for the thresholds.
           
           The
           definition of the targets: `pyVmomi.vim.vsan.VsanHealthThresholdTarget`
       enabled: As each target will have its own switch for threshold customization,
           this field is used to tell if the threshold takes effect.
           
           If not given,
           the default value is False.
   """
   yellowValue: pyVmomi.VmomiSupport.long
   redValue: pyVmomi.VmomiSupport.long
   target: _typing.Optional[str] = None
   enabled: _typing.Optional[bool] = None

class VsanHealthThresholdTarget:
   """
   The vSAN threshold target type.
   
   it is used in
   `pyVmomi.vim.vsan.VsanHealthThreshold`, to indicate the thresholds are applied
   on which target. A target could be a part of one health check, or just one
   entire health check.
   For below targets, a valid threshold should be a percentage, e.g., an
   integer value which is in range [0, 100].
   """
   pass


class VsanHistoricalHealthConfig(pyVmomi.vmodl.DynamicData):
   """
   vSAN historical health configuration
   
   Attributes:
       enabled: vSAN historical health enablement state
   """
   enabled: bool


class VsanHostDeviceInfo(pyVmomi.vmodl.DynamicData):
   """
   Information of the vSAN devices on a host.
   
   Attributes:
       hostname: Host name to which this information references.
       devices: The basic information of the devices used by vSAN.
   """
   hostname: str
   devices: list[pyVmomi.vim.host.VsanBasicDeviceInfo] = []


class VsanHostVdsSystem(pyVmomi.VmomiSupport.ManagedObject):
   """
   vSAN optimized methods for assisting VDS related operations, especially
   migrations from VSS to VDS.
   
   In every ESXi host there is a singleton instance of this class
   with the Managed Object ID of 'ha-vsan-host-vds-system'.
   """
   def VsanMigrateVmsToVds(self, vmConfigSpecs: list[VsanVmVdsMigrationSpec], vdsUuid: str, timeoutSec: pyVmomi.VmomiSupport.long, revert: _typing.Optional[bool]) -> str:
      """
      Make all the VMs on the host to adopt the VDS network.
      
      Args:
          vmConfigSpecs: VMs to be migrated via associated specs
          vdsUuid: UUID of the VDS that is being migrated to.
          timeoutSec: Time in seconds. See above for timeout behavior.
      
      Returns:
          A unique identifier referring to this operation
      
      Raises:
          pyVmomi.vim.fault.NotFound: Task not found
          pyVmomi.vim.fault.VsanFault: Any unexpected runtime error.
      """
      ...
   def VsanCompleteMigrateVmsToVds(self, jobId: str, newState: str) -> None:
      """
      Mark the jobID with \"rollback\" or \"done\" flag.
      
      If it is \"done\", the migration
      is considered completed. But if it is marked with \"rollback\", all the change
      made by previous call of \"VsanMigrateVmsToVds\" to the network will be rolled
      back.
      
      Args:
          jobId: Unique identifier returned by VsanMigrateVmsToVds()
          newState: Indicates if the migration is considered completed or
              should be rolled back.
      
      Returns:
          NULL
      
      Raises:
          pyVmomi.vim.fault.NotFound: Task not found
          pyVmomi.vim.fault.VsanFault: Any unexpected runtime error.
      """
      ...


class VsanHwToVcgInfoMappingSpec(pyVmomi.vmodl.DynamicData):
   """
   This class defines the mappings from the hardware indentifiers to the vSAN
   VCG entries under one entity.
   
   An entity can be one vSAN cluster, one host,
   one controller or one NVMe disk. If the entity is a cluster or a host, it
   means applying to all the corresponding hardware devices under the cluster or
   the host.
   For example: if the entity is a host, and the host has 2 NVMe disks who have
   the same hardware identifier, then it means that the 2 NVMe disks are assumed
   to be the same device and be mapping to the same vSAN VCG entry.
   
   Attributes:
       entity: The MOID string of the entity.
       vsanHwToVcgInfoMappings: Refer to (@link vim.host.VsanHwToVcgInfoMapping).
   """
   entity: str
   vsanHwToVcgInfoMappings: list[pyVmomi.vim.host.VsanHwToVcgInfoMapping] = []


class VsanIOTripAnalyzerConfig(pyVmomi.vmodl.DynamicData):
   """
   The spec for vSAN IO trip analyzer configuration.
   
   Attributes:
       recurrences: The spec defining the recurrence settings for all entities
           to be diagnosed by IO trip analyzer.
           
           Currently it only supports diagnosing for one entity.
           If not specified, it will remove the current recurrence settings.
   """
   recurrences: list[VsanIOTripAnalyzerRecurrence] = []


class VsanIOTripAnalyzerRecurrence(pyVmomi.vmodl.DynamicData):
   """
   The spec for vSAN IO trip analyzer scheduler recurrence settings.
   
   Attributes:
       name: The unique name for this recurrence setting.
           
           If not given, it will generate the name automatically.
       targets: The target entity list to run the IO trip analyzer diagnosis.
           
           Currently it supports only one entity to be given.
       startTime: The start time for the IO trip analyzer recurrence.
       endTime: The end time for the IO trip analyzer recurrence.
           
           If not set, the recurrence will not end.
       duration: The diagnostic duration for each IO trip analyzer occurence.
           
           The unit is second.
       interval: The time interval between two IO trip analyzer tasks.
           
           If the value is set to 0, it means it is one-time IO trip analyzer
           scheduling, no recurrence needed. Unit is second.
       status: The recurrence status.
           
             
           If the status is set as enabled, the scheduler with this recurrence setting
           is up and running. Diagnostic tasks will be triggered based on the setting.
           If the status is set as disabled, the scheduler with this recurrence setting
           is not runninig. No diagnostic task will be triggered.
   """
   name: _typing.Optional[str] = None
   targets: list[IODiagnosticsTarget] = []
   startTime: _datetime.datetime
   endTime: _typing.Optional[_datetime.datetime] = None
   duration: pyVmomi.VmomiSupport.long
   interval: pyVmomi.VmomiSupport.long
   status: str

class VsanIOTripAnalyzerRecurrenceStatus:
   """The vSAN IO trip analyzer scheduler recurrence status type."""
   pass


class VsanInternalExtendedConfig(pyVmomi.vmodl.DynamicData):
   """
   vSAN internal extended configurations
   This contains vSAN host level extended configurations that can be
   configured for hosts internally by vCente server.
   
   Unlike
   `pyVmomi.vim.vsan.VsanExtendedConfig`, this is not part of vSAN
   cluster reconfiguration spec `pyVmomi.vim.vsan.ConfigInfoEx` and it
   is not meant to be set by users.
   
   Attributes:
       vcMaxDiskVersion: This configuration is the highest disk version that vCenter server
           can understand and manage.
           
           vCenter server passes this configuration
           to ESXi hosts so that ESXi hosts will not choose a higher disk
           version that vCenter server cannot understand when creating a disk
           group. The default value on ESXi host is 0 when it is unset, meaning
           that the host is not managed by any vCenter server. Note that older
           vCenter server before v6.7 update 3 won't know this value hence will
           not set it.
       stretchedClient: This configuration indicates if the host works in stretched compute
           only cluster.
           
           This configuration only serves ESX reconfiguration purpose, but
           not returned via get API.
   """
   vcMaxDiskVersion: _typing.Optional[int] = None
   stretchedClient: _typing.Optional[bool] = None


class VsanNetworkConfigBaseIssue(pyVmomi.vmodl.DynamicData):
   """Base class for all vSAN network configuration issues."""
   pass


class VsanNetworkConfigBestPracticeHealth(pyVmomi.vmodl.DynamicData):
   """
   Various health checks for the configuration of a clusters network,
   implementing not requirements but best practices for use in a vSAN
   environment.
   
   Attributes:
       vdsPresent: True if the cluster has a Virtual Distributed Switch present.
           
           It is
           enough for at least one host to be a member of a VDS for this to
           report True. See other checks for further configuration checks.
           To use a VDS is a best practice for vSAN.
       issues: Configuration issues.
   """
   vdsPresent: bool
   issues: list[VsanNetworkConfigBaseIssue] = []


class VsanNetworkConfigPnicSpeedInconsistencyIssue(VsanNetworkConfigBaseIssue):
   """
   Configuration issue: vSAN is using a vmknic on a vSwitch
   which has inconsistent physical NIC speeds.
   
   It is recommended to
   only use physical NICs of same speed on a given vSwitch backing
   vSAN. Note that physical NIC redundancy is a best practice,
   not a functional/support requirement.
   
   Attributes:
       host: The Host on which the vmknic exists
       vswitchName: Standard virtual switch name, in case of VMware Standard Switch (VSS).
       vds: The Virtual Distributed Switch, if in-use.
       speedsMb: Bit rates (speed) of the links, in Mbit/s.
           
           This list only contains each
           present speed once. Links without any speed indication (e.g. links that
           are down) are not considered in the list. As there is an issue, there
           must be at least two members in this list.
   """
   host: pyVmomi.vim.HostSystem
   vswitchName: _typing.Optional[str] = None
   vds: _typing.Optional[pyVmomi.vim.DistributedVirtualSwitch] = None
   speedsMb: list[pyVmomi.VmomiSupport.long] = []


class VsanNetworkConfigPortgroupWithNoRedundancyIssue(VsanNetworkConfigBaseIssue):
   """
   Configuration issue: vSAN is using a vmknic on a portgroup
   which doesn't have any physical NIC redundancy.
   
   This means in case
   of a physical NIC failure vSAN would not be able to use the
   vmknic any more to communicate with the remaining cluster. There are
   two possible causes for this issue: a) The virtual switch itself
   may lack physical NIC redundancy (also tracked as a separated health
   issue) or b) the NIC teaming policy of the portgroup is not configured
   for redundancy. Note that physical NIC redundancy is a best practice,
   not a functional/support requirement.
   
   Attributes:
       host: The Host on which the vmknic exists
       portgroupName: Portgroup name, in case of VMware Standard Switch (VSS).
       vds: The Virtual Distributed Switch, if in-use.
       pg: Portgroup, either VSS or VDS.
       numPnics: Number of configured physical NICs.
   """
   host: pyVmomi.vim.HostSystem
   portgroupName: _typing.Optional[str] = None
   vds: _typing.Optional[pyVmomi.vim.DistributedVirtualSwitch] = None
   pg: _typing.Optional[pyVmomi.vim.Network] = None
   numPnics: pyVmomi.VmomiSupport.long


class VsanNetworkConfigVdsScopeIssue(VsanNetworkConfigBaseIssue):
   """
   Configuration issue: A cluster uses a Virtual Distributed Switch (VDS)
   that covers parts but not all cluster hosts.
   
   It is recommended to have
   all hosts in a cluster connected to the same VDS for centralized
   configuration management.
   
   Attributes:
       vds: The Virtual Distributed Switch.
       memberHosts: Hosts which are members of the VDS.
       nonMemberHosts: Hosts which are not members of the VDS.
   """
   vds: pyVmomi.vim.DistributedVirtualSwitch
   memberHosts: list[pyVmomi.vim.HostSystem] = []
   nonMemberHosts: list[pyVmomi.vim.HostSystem] = []


class VsanNetworkConfigVsanNotOnVdsIssue(VsanNetworkConfigBaseIssue):
   """
   Configuration issue: vSAN is using a vmknic which is not
   on a vDS.
   
   This is a best practice, not a functional/support
   requirement.
   
   Attributes:
       host: The Host on which the vmknic exists
       vmknic: vmknic device name.
   """
   host: pyVmomi.vim.HostSystem
   vmknic: str


class VsanNetworkConfigVswitchWithNoRedundancyIssue(VsanNetworkConfigBaseIssue):
   """
   Configuration issue: vSAN is using a vmknic on a vSwitch
   which doesn't have any physical NIC redundancy.
   
   This means in case
   of a physical NIC failure vSAN would not be able to use the
   vmknic any more to communicate with the remaining cluster. Note
   that physical NIC redundancy is a best practice, not a functional/support
   requirement.
   
   Attributes:
       host: The Host on which the vmknic exists
       vswitchName: Standard virtual switch name, in case of VMware Standard Switch (VSS).
       vds: The Virtual Distributed Switch, if in-use.
       numPnics: Number of configured physical NICs.
   """
   host: pyVmomi.vim.HostSystem
   vswitchName: _typing.Optional[str] = None
   vds: _typing.Optional[pyVmomi.vim.DistributedVirtualSwitch] = None
   numPnics: pyVmomi.VmomiSupport.long


class VsanNetworkVMotionVmknicNotFountIssue(VsanNetworkConfigBaseIssue):
   """
   Configuration issue: Host has no vMotion vmknic configured.
   
   Attributes:
       hostWithoutVmotionVmknic: Hosts on which no vMotion vmknic is found.
   """
   hostWithoutVmotionVmknic: pyVmomi.vim.HostSystem


class VsanObjSnapParams(pyVmomi.vmodl.DynamicData):
   """
   The information for creating vSAN snapshot.
   
   Attributes:
       uuid: The UUID of vSAN object.
           
           Its format is like
           \"e3d10064-ae3c-9323-568d-b02628350470\"
       creator: It indicates snapshots created by the specified creator.
       snapshotType: Type of the snapshot.
       cookie: A cookie that is provided when creating the snapshot, which is in UUID
           format, like \"e3d10064-ae3c-9323-568d-b02628350470\".
           
           If such a data is provided in snapshot creation, it must also be provided
           when deleting the snapshot.
       immutableTag: An immutable tag that is provided when creating immutable snapshot on vSAN
           ESA, which should be used together with cookie.
   
   Since: 8.0.0.4
   """
   uuid: str
   creator: _typing.Optional[str] = None
   snapshotType: _typing.Optional[str] = None
   cookie: _typing.Optional[str] = None
   immutableTag: _typing.Optional[str] = None


class VsanObjectDetail(pyVmomi.vmodl.DynamicData):
   """
   The information related to vSAN object.
   
   Attributes:
       uuid: vSAN object uuid.
           
           Its format is like 'e3d10064-ae3c-9323-568d-b02628350470'.
       objectPath: Vmdk descriptor file that points to the object running point.
           
           It is a full
           path in the format like
           \"/vmfs/volume/vsan:522116b0018397a0-faf6eef653793842/2e661d64-20a3-afb9-80f6-e4434ba16432/foo.vmdk\"
           It is set when the field includeDescriptorPath of
           `pyVmomi.vim.vsan.VsanSnapshotQuerySpec` is True.
       snapshots: A list of snapshots information of vSAN object.
   
   Since: 8.0.0.4
   """
   uuid: str
   objectPath: _typing.Optional[str] = None
   snapshots: list[VsanSnapshotDetail] = []


class VsanObjectManager(pyVmomi.VmomiSupport.ManagedObject):
   """
   This managed type provides access to VsanObjectManager related APIs.
   
   It provides vSAN object oriented operations. So far there is only ESA
   object snapshot operations supported by this sub-system.
   On both vCenter and ESXi, there is a singleton instance of this class
   with the Managed Object ID of `pyVmomi.vim.vsan.VsanObjectManager`.
   
   Since: 8.0.0.4
   """
   pass


class VsanObjectSnapshotId(pyVmomi.vmodl.DynamicData):
   """
   The IDs related to vSAN snapshots of an object.
   
   Attributes:
       uuid: The uuid of vSAN object.
           
           Its format is like
           \"e3d10064-ae3c-9323-568d-b02628350470\"
       snapshotId: A native snapshot ID on the zDOM object, it is an integer starting from 1.
       cookie: A cookie that is provided when creating the snapshot, which is in UUID
           format, like \"e3d10064-ae3c-9323-568d-b02628350470\".
           
           If such a data is provided in snapshot creation, it must also be provided
           when deleting the snapshot.
   
   Since: 8.0.0.4
   """
   uuid: str
   snapshotId: int
   cookie: _typing.Optional[str] = None


class VsanPMemConfig(pyVmomi.vmodl.DynamicData):
   """
   Configuration for vSAN PMem.
   
   Attributes:
       enabled: Whether vSAN PMem is enabled.
   """
   enabled: bool


class VsanPerfsvcHealthResult(pyVmomi.vmodl.DynamicData):
   """
   This class encapsulates the vSAN performance service health test result
   
   Attributes:
       statsObjectInfo: This is vSAN stats object information.
       statsObjectConsistent: This is vSAN stats object consistency check value.
       statsObjectPolicyConsistent: This is vSAN stats object policy consistency check value.
       datastoreCompatible: This value indicate that if the vSAN datastore is compatible with the configuration policy.
       enoughFreeSpace: This value indicate that if the vSAN datastore has enough free space to enable vsan
           performance service.
       remediateAction: vSAN performance service remediation action.
       hostResults: This is list of hosts' performance service information.
       verboseModeStatus: This value indicate that if the vSAN performance service verbose mode is
           enable or not.
   """
   statsObjectInfo: _typing.Optional[pyVmomi.vim.cluster.VsanObjectInformation] = None
   statsObjectConsistent: _typing.Optional[bool] = None
   statsObjectPolicyConsistent: _typing.Optional[bool] = None
   datastoreCompatible: _typing.Optional[bool] = None
   enoughFreeSpace: _typing.Optional[bool] = None
   remediateAction: _typing.Optional[str] = None
   hostResults: list[pyVmomi.vim.cluster.VsanPerfNodeInformation] = []
   verboseModeStatus: _typing.Optional[bool] = None


class VsanPolicyManager(pyVmomi.VmomiSupport.ManagedObject):
   """This managed object provides access to VsanPolicyManager related API's."""
   pass

class VsanPolicyRegulationCheckOpEnum:
   """vSAN policy regulation check operators."""
   pass


class VsanPrepareVsanForVcsaSpec(pyVmomi.vmodl.DynamicData):
   """
   All configuration parameters for preparing vSAN on a host
   where VCSA will be deployed
   
   Attributes:
       vsanDiskMappingCreationSpec: If set, vCSA Deployer will claim those disks as vSAN disk groups, and a vSAN
           datastore will be created.
           
           By passing in this spec, it implies the host will be contributing disk storage
           to a vSAN cluster, therefore vSAN will be automatically enabled on the host,
           if it's not yet enabled.
       vsanDataEfficiencyConfig: The data efficiency config for vSAN.
       taskId: Unique identifier of the task this progress report is for.
       vsanDataEncryptionConfig: The data encryption config that will be used to bootstrap single node
           vSAN cluster, this config contains the fields as below:
           enabled:
           True if encryption should be enabled.
           
           kmipServers:
           Array of `pyVmomi.vim.encryption.KmipServerSpec`
           For AWS, KMS server address is AWS KMS key ARN starting with \"arn:aws\"
           kmsServerCerts:
           Certificates of Key Management Servers in PEM encoding. Host will
           use these certificates to decide if a KMS should be trusted or not.
           clientKey:
           Client private key. Host will use this key for authentication when
           connecting to KMS.
           clientCert:
           Client certificate in PEM encoding. Host will use this certificate
           for authentication when connecting to KMS.
           Three kms types(KMIP, AWS, NKP) are supported for now.
           And each KMS type requires different fields as below:
           
           KMS type
            - Required fields
           
           KMIP
            -
           - enabled
           - kmipServers
           - kmsServerCerts
           - clientKey
           - clientCert
             
           AWS
            -
           - enabled
           - kmipServers
           - kmsServerCerts
             
           NKP
            -
           - enabled
       vsanAddStoragePoolDiskSpec: If set, vCSA Deployer will claim those disks as vSAN ESA storage pool, and a
           vSAN ESA datastore will be created.
           
           By passing in this spec, it implies the host will be contributing disk storage
           to a vSAN ESA cluster, therefore vSAN ESA will be automatically enabled on the
           host, if it's not yet enabled.
           Note: This paramemter cannot be used together with
           `pyVmomi.vim.vsan.VsanPrepareVsanForVcsaSpec.vsanDiskMappingCreationSpec`
       createNativeKeyProviderSpec: Specification used to create native key provider on host.
   """
   vsanDiskMappingCreationSpec: _typing.Optional[pyVmomi.vim.vsan.host.DiskMappingCreationSpec] = None
   vsanDataEfficiencyConfig: _typing.Optional[DataEfficiencyConfig] = None
   taskId: _typing.Optional[str] = None
   vsanDataEncryptionConfig: _typing.Optional[pyVmomi.vim.vsan.host.EncryptionInfo] = None
   vsanAddStoragePoolDiskSpec: _typing.Optional[pyVmomi.vim.vsan.host.AddStoragePoolDiskSpec] = None
   createNativeKeyProviderSpec: _typing.Optional[pyVmomi.vim.vsan.host.CreateNativeKeyProviderSpec] = None


class VsanResourceCheckSystem(pyVmomi.VmomiSupport.ManagedObject):
   """
   This managed object type provides interfaces to perform resource check
   and query for various operations, e.g.
   
   host enter maintenance mode,
   disk upgrade.
   It can be accessed through MOID of 'vsan-cluster-resource-check-system',
   via vSAN service on vCenter at cluster level, or accessed through MOID
   of 'vsan-resource-check-system' on ESXi host.
   """
   def PerformResourceCheck(self, resourceCheckSpec: ResourceCheckSpec, cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource]) -> pyVmomi.vim.Task:
      """
      Perform a resource check for given spec.
      
      Given the operation type and parameter(s) for the operation, the resource
      check will run a point-in-time simulation based on the cluster state at
      the time of the resource check request. It will check whether current vSAN
      cluster has enough resource or any issue to perform the operation.
      For example, given the host enter maintenance mode operation, the host
      vSAN UUID and data evacuation mode, it will check whether there is enough
      fault domains, disk capacity, etc. or any inaccessible object which can
      prevent the host from entering maintenance mode.
      Only one resource check should be run in a vSAN cluster at a time.
      
      Args:
          resourceCheckSpec: The specification of the resource check.
          cluster: The cluster to run the resource check.
      
      Returns:
          A task to monitor resource check progress. Results can be obtained
          with the API `pyVmomi.vim.vsan.VsanResourceCheckSystem.getResourceCheckStatus`
          after the resource check finishes.
      
      Raises:
          pyVmomi.vim.fault.InvalidState: Exception when it is not qualified to run the resource
              check. For example, for host enter maintenance mode
              operation, if the given host is already in maintenance
              mode.
          pyVmomi.vmodl.fault.InvalidArgument: Exception when the given operation is not
              supported, some parameter is missing or incorrect
              in the spec. For example, for host enter
              maintenance mode operation, host vSAN UUID or
              maintenanceSpec is not provided, or data evacuation
              mode is not supported.
          pyVmomi.vim.fault.VsanFault: If any error happens during the resource check.
          pyVmomi.vim.fault.NotFound: Exception when the given entity in the spec cannot be
              found.
          pyVmomi.vmodl.fault.NotSupported: if run directly on an ESX Server host.
      """
      ...
   def GetResourceCheckStatus(self, resourceCheckSpec: _typing.Optional[ResourceCheckSpec], cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource]) -> ResourceCheckStatus:
      """
      Retrieve the status of the latest resource check.
      
      If a resource check task is running, its status will be returned.
      Otherwise the status of the last resource check will be returned.
      
      Args:
          resourceCheckSpec: The specification of the resource check to be queried.
              If it is not specified, `pyVmomi.vim.vsan.ResourceCheckStatus`
              will still be returned with `pyVmomi.vim.vsan.ResourceCheckStatus.task`
              and/or `pyVmomi.vim.vsan.ResourceCheckStatus.parentTask` information
              if such task is running in the specified cluster. However,
              `pyVmomi.vim.vsan.ResourceCheckStatus.result` will not be populated in this case.
          cluster: The cluster to fetch the resource check status.
      
      Returns:
          The status of the specified resource check. The resource check may
          have not started yet, or be currently running, or have completed
          already.
          If a resource check has completed successfully, detailed resource
          check result will also be included.
      
      Raises:
          pyVmomi.vmodl.fault.InvalidArgument: Exception when the given operation is not
              supported, some parameter is missing or incorrect
              in the spec. For example, for host enter
              maintenance mode operation, host vSAN UUID or
              maintenanceSpec is not provided, or data evacuation
              mode is not supported.
          pyVmomi.vim.fault.VsanFault: If any error happens when retrieving
              the resource check status.
      """
      ...
   def PerformResourceCheckOnHost(self, resourceCheckSpec: ResourceCheckSpec) -> pyVmomi.vim.Task:
      """
      Raises:
          pyVmomi.vim.fault.VsanFault: Base exception class for VSAN-specific faults raised for host
              or cluster operations.
      """
      ...
   def CancelResourceCheckOnHost(self) -> bool: ...

class VsanServiceStatus:
   """Defines the status of vSAN service."""
   pass

class VsanSiteLocationType:
   """Defines vSAN site location type."""
   pass


class VsanSiteMaintenanceSystem(pyVmomi.VmomiSupport.ManagedObject):
   """
   This managed object type provides the vSAN fault domain maintenance operations.
   
   Fault
   domain maintenance is a vSAN specific operation that allows all hosts within a fault domain
   to enter maintenance mode while ensuring object consistency. This managed
   object provides the functionalities to run precheck, enter maintenance mode
   and exit maintenance mode.
   It can be accessed through MOID of 'vsan-cluster-site-maintenance-system',
   through vSAN service on vCenter at cluster level.
   """
   def EnterSiteMaintenanceMode(self, faultDomainName: str, cluster: pyVmomi.vim.ClusterComputeResource) -> pyVmomi.vim.Task:
      """
      Put all hosts in a fault domain into maintenance mode.
      
      This operation puts the hosts on this fault domain into the maintenance mode, and
      guarantees the consistencies for all objects within this fault domain. A precheck
      will be performed as part of this fault domain maintenance workflow. Upon success,
      all VMs in this fault domain will be powered off or migrated to the other fault domain.
      
      Args:
          faultDomainName: The fault domain name to enter maintenance mode.
          cluster: The cluster containing the fault domain to enter maintenance mode.
      
      Returns:
          the task tracking the enter fault domain maintenance workflow.
      
      Raises:
          pyVmomi.vim.fault.VsanFault: If any runtime error is hit.
      """
      ...
   def ExitSiteMaintenanceMode(self, faultDomainName: str, cluster: pyVmomi.vim.ClusterComputeResource) -> pyVmomi.vim.Task:
      """
      Exit the fault domain maintenance mode.
      
      This operation exits the maintenance mode for all hosts in the specified
      fault domain. The objects will start the data resync during the host exit maintenance
      workflow. When the exit maintenance mode operation is successful, users
      can enable the intended workloads.
      
      Args:
          faultDomainName: The fault domain name to exit maintenance mode.
          cluster: The cluster containing the fault domain to exit maintenance mode.
      
      Returns:
          the task tracking the exit fault domain maintenance mode workflow.
      
      Raises:
          pyVmomi.vim.fault.VsanFault: If any runtime error is hit.
      """
      ...
   def PerformSiteMaintenancePrecheck(self, cluster: pyVmomi.vim.ClusterComputeResource, spec: SiteMaintenanceSpec) -> pyVmomi.vim.Task:
      """
      Initiates a precheck to determine if the target fault domain can enter maintenance mode.
      
      The precheck performs a health check and a \"what-if\" query to assess the impact
      on cluster resources (objects, VMs) once the proposed maintenance action is executed.
      Only one precheck should run in a vSAN cluster at a time.
      
      Args:
          cluster: The cluster on which to run the precheck.
          spec: The specification of the queried fault domain maintenance action.
      
      Raises:
          pyVmomi.vim.fault.VsanFault: Base exception class for VSAN-specific faults raised for host
              or cluster operations.
          pyVmomi.vmodl.fault.InvalidArgument: An InvalidArgument exception is thrown if the
              set of arguments passed to the function is not
              specified correctly.
          pyVmomi.vmodl.fault.ManagedObjectNotFound: If the cluster cannot be found.
      """
      ...
   def GetSiteMaintenancePrecheckStatus(self, cluster: pyVmomi.vim.ClusterComputeResource, faultDomainName: str) -> SiteMaintenancePrecheckStatus:
      """
      Retrieves the result of the latest fault domain maintenance check.
      
      If a precheck task is running, its status will be returned.
      Otherwise the status of the last fault domain maintenance precheck
      will be returned.
      
      Args:
          cluster: The specified cluster to query.
          faultDomainName: The fault domain to query.
      
      Raises:
          pyVmomi.vim.fault.VsanFault: Base exception class for VSAN-specific faults raised for host
              or cluster operations.
          pyVmomi.vmodl.fault.InvalidArgument: An InvalidArgument exception is thrown if the
              set of arguments passed to the function is not
              specified correctly.
          pyVmomi.vmodl.fault.ManagedObjectNotFound: If the cluster cannot be found.
      """
      ...
   def QueryClusterSiteMaintenanceState(self, cluster: pyVmomi.vim.ClusterComputeResource) -> list[SiteMaintenanceInfo]:
      """
      Query the maintenance state of all fault domains in the specified cluster.
      
      Args:
          cluster: The target cluster to query.
      
      Returns:
          A list of SiteMaintenanceInfo objects, each representing the
          maintenance state of a fault domain in the target cluster. If the target
          cluster is not a stretched cluster, an empty list is returned.
      
      Raises:
          pyVmomi.vim.fault.VsanFault: If any unexpected runtime fault occurs.
      """
      ...

class VsanSnapHealthType:
   """
   It's used to declare the health types of the received stats from the
   vSAN SnapService Appliance.
   """
   pass

class VsanSnapStatsExpirationType:
   """
   It's used to declare the expiration types of the received stats from the
   vSAN SnapService Appliance.
   """
   pass

class VsanSnapVmMembershipChangeStatus:
   """It's used to declare the virtual machine membership change status."""
   pass


class VsanSnapshotDetail(pyVmomi.vmodl.DynamicData):
   """
   The information related to vSAN snapshot.
   
   Attributes:
       snapshotId: vSAN ESA Snapshot ID, such as 1.
       snapshotType: Type of the snapshot.
       snapshotPath: Vmdk descriptor file path of the snapshot.
           
           It is a full
           path in the format like
           \"/vmfs/volume/vsan:522116b0018397a0-faf6eef653793842/2e661d64-20a3-afb9-80f6-e4434ba16432/foo-001.vmdk\"
           It is set when the field includeDescriptorPath of
           `pyVmomi.vim.vsan.VsanSnapshotQuerySpec` is True.
       snapshotTagsInfo: The tag information related to a snapshot on vSAN ESA, requested through
           the snapshotTagMask in `pyVmomi.vim.vsan.VsanSnapshotQuerySpec`.
           
           The key part is the snapshot tag type string. Currently only one tag type
           \"immutable_tag\" is supported.
           The value part is the value string of snapshot tag.
   
   Since: 8.0.0.4
   """
   snapshotId: int
   snapshotType: str
   snapshotPath: _typing.Optional[str] = None
   snapshotTagsInfo: list[pyVmomi.vim.KeyValue] = []


class VsanSnapshotQueryResult(pyVmomi.vmodl.DynamicData):
   """
   A VsanSnapshotQueryResult represents the results of a vSAN snapshot query
   operation.
   
   Attributes:
       objects: A list of queried objects with snapshots information.
   
   Since: 8.0.0.4
   """
   objects: list[VsanObjectDetail] = []


class VsanSnapshotQuerySpec(pyVmomi.vmodl.DynamicData):
   """
   Specification for querying snapshots information.
   
   Attributes:
       datastoreUuid: The vSAN datatore container ID.
           
           This can be found in
           `pyVmomi.vim.Datastore.Info.containerId`, such as
           \"522116b0018397a0-faf6eef653793842\"
       objectUuids: A list of object uuids to query snapshots.
           
           Object uuid is in the format like
           \"e3d10064-ae3c-9323-568d-b02628350470\".
       snapshotType: If set, snapshots of the specified type will be returned.
       creator: If set, snapshots created by the specified creator will be returned.
       includeDescriptorPath: If set to True, the vmdk descriptor file path will be returned.
       snapshotTagMask: The bitmap mask that indicates which snapshot tags are queried.
           
           Each bit represents a snapshot tag type, a value of 1 means the
           corresponding tag type should be included in the query.
           Current only one tag type is supported.
           \\- Bit 0 (The Least Significant Bit): Immutable tag.
           \\- Bit 1 and above: reserved for future use.
           If the queried tag type doesn't exist on the snapshot, it will not be
           returned in `pyVmomi.vim.vsan.VsanSnapshotDetail`.
   
   Since: 8.0.0.4
   """
   datastoreUuid: str
   objectUuids: list[str] = []
   snapshotType: _typing.Optional[str] = None
   creator: _typing.Optional[str] = None
   includeDescriptorPath: _typing.Optional[bool] = None
   snapshotTagMask: _typing.Optional[int] = None


class VsanSpaceEfficiencyMetadataSize(pyVmomi.vmodl.DynamicData):
   """
   This class holds the space efficiency metadata size in bytes.
   
   Attributes:
       dedupMetadataSize: Metadata size for deduplication in bytes.
       compressionMetadataSize: Metadata size for compression in bytes.
   """
   dedupMetadataSize: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   compressionMetadataSize: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class VsanSpaceEfficiencyRatio(pyVmomi.vmodl.DynamicData):
   """
   This class holds the vSAN space efficiency ratio.
   
   Attributes:
       overallRatio: The cluster level space efficiency ratio.
           
           For vSAN ESA, it will exclude all the system overhead.
       compressionRatio: The cluster level space efficiency ratio for compression.
           
           This attribute specifically quantifies the space efficiency
           achieved through compression, without considering other
           efficiency features.
           It is only exposed when compression is enabled within the
           cluster state.
           Compression Ratio = Space Usage Before Compression /
           Space Usage After Compression
       dedupRatio: The cluster level space efficiency ratio for compression.
           
           This attribute specifically quantifies the space efficiency
           achieved through deduplication, without considering other
           efficiency features.
           It is only exposed when deduplication is enabled within the
           cluster state.
           Deduplication Ratio = Space Usage Before Deduplication /
           Space Usage After Deduplication
       dedupEnabledRatio: The storage space reduction ratio by vSAN ESA global deduplication.
           
           Unlike dedupRatio, this ratio only measures the objects that are
           eligible for global deduplication.
       thinProvisionRatio: The storage space reduction ratio for thin provisioning in cluster.
           
           It measures the efficiency gained by allocating storage on-demand
           rather than reserving the full provisioned size up front.
           It is calculated by total thin provisioning space / used space.
       snapshotSavingRatio: The storage space reduction ratio by snapshots saving in cluster.
           
           It is calculated by fully inflated snapshot capacity /
           actual written snapshot capacity in bytes.
   
   Since: 8.0.0.4
   """
   overallRatio: _typing.Optional[float] = None
   compressionRatio: _typing.Optional[float] = None
   dedupRatio: _typing.Optional[float] = None
   dedupEnabledRatio: _typing.Optional[float] = None
   thinProvisionRatio: _typing.Optional[float] = None
   snapshotSavingRatio: _typing.Optional[float] = None

class VsanSyncReason:
   """The reasons why a vSAN component went into syncing state."""
   pass

class VsanSyncStatus:
   """
   The status of syncing vSAN component.
   
   Components which need recovery
   can be in one of the three status.
   """
   pass


class VsanUnmapConfig(pyVmomi.vmodl.DynamicData):
   """
   The configuration to support SCSI unmap command on vSAN datastore.
   
   Attributes:
       enable: Whether SCSI unmap command is supported on vSAN datastore.
           
           If this setting is switched from disabled to enabled, for any unmap
           request to vSAN datastore from powered on VMs will take effect and succeed
           immediately;
           And if it is switched from enabled to disabled dynamically, running VMs
           reside on this vSAN datastore won't know this change until VM rebooting
           happen. vSAN will fail any unmap request, and the failure will be handled
           by guest OS gracefully.
   """
   enable: bool


class VsanUpdateItem(pyVmomi.vmodl.DynamicData):
   """
   Information about an item (firmware, VIB) to be installed/updated.
   
   Attributes:
       host: Host for which this information is in reference to.
       type: Type of the item.
       name: Name of the item.
           
           In case of a VIB a description that includes the unique
           VIB name. In case of firmware, a description of firmware and device.
       version: Version provided by this item.
           
           Note, in case of a VIB, this may not be the
           VIB version, but rather the version of what the VIB contains, e.g. the version
           of the driver or CIM provider, which may not match exactly the version of
           the VIB.
       existingVersion: Existing version on the host, if any.
       present: If not present, it needs to be downloaded from the Internet, or uploaded to the
           Update Manager.
           
           See respective APIs.
       vibSpec: In case of VIB type, the spec for the VIB.
       vibType: Type of the Vib.
       firmwareSpec: In case of vmhba firmware type, the spec for the firmware.
       downloadInfo: Information about how to download the item.
       eula: EULA provided by this item.
           
           Note, in case of a VIB, this is empty, as for firmware,
           it is the EULA provided by the vendor.
       adapter: The device name of adapter whose vendor tool or driver/firmware to be
           installed or updated by the update item
       key: Unique key to identify the an update item.
       impact: Impact after the update item is applied.
       firmwareUnknown: Set to true when firmware is unknown.
           
           When it's true, it means associated firmware mgmt tool is missing,
           which has to be installed first.
   """
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
   """Lists the impact on the node after applying update item."""
   pass

class VsanUpdateItemType:
   """Type of VsanUpdateItem."""
   pass


class VsanValidationItem(pyVmomi.vim.ClusterComputeResource.ValidationResultBase):
   """
   The base type of validation result item for various vSAN validating or
   precheck operations.
   
   It is essentially a localizable message list in
   `pyVmomi.vim.ClusterComputeResource.ValidationResultBase.info`.
   """
   pass


class VsanVcPostDeployConfigSpec(pyVmomi.vmodl.DynamicData):
   """
   All configuration parameters for a vCenter to be applied post deploy.
   
   Attributes:
       dcName: Name of the datacenter to be created.
           
           Default: \"Datacenter\"
       clusterName: Name of the cluster to be created.
           
           Default: \"VSANCluster\"
       firstHost: Connection information about the host on which this task runs.
           
           It will be the first host to be added to vCenter, so vCenter adopts the
           settings of this host for VSAN.
       hostsToAdd: List of `pyVmomi.vim.host.ConnectSpec` objects, one for each host that should be
           connected to vCenter and added to the cluster.
       vsanDataEfficiencyConfig: The data efficiency config for vSAN.
       vsanLicenseKey: vSAN License key to apply to the cluster.
           
           If not specified, license is not
           changed. If specified, current license is overwritten.
       hostLicenseKey: ESX License key to apply to all hosts.
           
           If not specified, license is not
           changed. If specified, current license is overwritten for hosts with
           version lower than 9.0, otherwise, the key is ignored, as host license
           key is not supported since 9.0.
       taskId: Unique identifier of the task this progress report is for.
       vsanDataEncryptionConfig: The data encryption config that was used to bootstrap single node
           vSAN cluster when calling ESXi host API
           `pyVmomi.vim.host.VsanVcsaDeployerSystem.prepareVsanForVcsa`
       createNativeKeyProviderSpec: Specification used to create native key provider.
       vsanClusterMode: Advanced Mode configuration for vSAN(Optional).
           
           When this parameter is not present, a vSAN OSA/ESA cluster will be
           created based on the vSAN datastore type on the first host.
           When this parmeter is present, the new vSAN cluster will be configured into
           the specified mode. The currently accepted value for the parameter is
           vim.vsan.Mode.Mode_Storage. Any mode other than this is not supported.
           
           Since: 8.0.0.4
       deconvergedNetConfig: De-converged network configuration for vSAN.
   """
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
   """
   Spec for configuring target witness hosts and target clusters in the
   vSAN VC stretched Clusters system.
   
   Attributes:
       witnessHost: The witness host to be added into vSAN cluster.
           
           This host cannot be a
           part of target cluster.
       clusters: The list of clusters to be converted to stretched or to replace witness.
       witnessDiskMappings: Disk mapping configuration of target witness host.
       witnessStoragePoolSpecs: Storage pool configuration of target witness host.
           
           This parameter cannot
           be set together with witnessDiskMappings param.
   """
   witnessHost: pyVmomi.vim.HostSystem
   clusters: list[pyVmomi.vim.cluster.VsanStretchedClusterConfig] = []
   witnessDiskMappings: list[pyVmomi.vim.vsan.host.DiskMapping] = []
   witnessStoragePoolSpecs: list[pyVmomi.vim.vsan.host.AddStoragePoolDiskSpec] = []

class VsanVcsaDeploymentPhase:
   """Phase of deployment."""
   pass


class VsanVcsaDeploymentProgress(pyVmomi.vmodl.DynamicData):
   """
   Detailed progress information for a running or recently completed VCSA
   deployment job.
   
   Attributes:
       phase: The overall deploy is divided into multiple phases, e.g.
           
           validation,
           vsanbootstrap, vcsadeploy, vcconfig, etc.
       progressPct: Overall progress of the job in percent.
       message: Status message about current operation of the background job.
       success: Set if the job completed successfully.
           
           If it is not set, it is either still
           running or failed. See error property.
       error: Set if the job aborted with failure.
           
           If it is not set, it is either still
           running or succeeded. See success property.
       updateCounter: Any time the progress changes this counter is incremented.
           
           This way a client
           can determine if the progress has changed when retrieving the progress at
           different points in time. Never negative.
       taskId: Unique identifier of the task this progress report is for.
       vm: Virtual Machine that was created.
   """
   phase: str
   progressPct: pyVmomi.VmomiSupport.long
   message: str
   success: bool
   error: _typing.Optional[pyVmomi.vmodl.MethodFault] = None
   updateCounter: pyVmomi.VmomiSupport.long
   taskId: _typing.Optional[str] = None
   vm: _typing.Optional[pyVmomi.vim.VirtualMachine] = None


class VsanVdsMigrationPlan(pyVmomi.vmodl.DynamicData):
   """
   Migration plan from VSS to VDS.
   
   Captures all aspects of the migration,
   i.e., the overall VDS specs, all portgroup specs and translations,
   as well as which consumers (pnics, vmknic and VM vNICs) are going to
   be migrated to their equivalent VDS portgroups. All migration plans
   always keep all settings for all consumers intact as part of the
   migration. If any issues occurred and how they were resolved is
   tracked within the plan.
   
   Attributes:
       vdsSpec: VDS creation spec.
           
           Contains information about host members, and their
           pNICs.
       pgs: Migration specs for all portgroups.
           
           All policies are preserved for the
           consumers of these portgroups.
       inaccessibleVms: A list of inaccessible or orphaned VMs which are blocking the migration.
       infraVms: This is includes any infra VM which was explicitly provided by the user
           as well as possibly an auto-detected vCenter.
           
           vCenter is auto-detected by
           comparing the IP of vCenter to the IP of VMs on the VSS, and if a match is
           found the VM is added to the list. Note that dependent VMs like an
           external VC DB, a DHCP or DNS server, or similar infrastructure VMs
           will not be auto-detected.
   """
   vdsSpec: pyVmomi.vim.DistributedVirtualSwitch.CreateSpec
   pgs: list[VsanVdsPgMigrationSpec] = []
   inaccessibleVms: list[pyVmomi.vim.VirtualMachine] = []
   infraVms: list[pyVmomi.vim.VirtualMachine] = []


class VsanVdsPgMigrationHostInfo(pyVmomi.vmodl.DynamicData):
   """
   Detailed migration information for an individual host and the consumers of the
   portgroup on this host.
   
   Attributes:
       host: Host reference of the host that is being migrated.
       hostname: Hostname of the host that is being migrated.
       vmknicDevices: List of vmknic device names which are current consumer of the
           VSS portgroup that will be migrated.
       vmVnics: List of VMs and their vNics which are current consumer of the
           VSS portgroup that will be migrated.
   """
   host: pyVmomi.vim.HostSystem
   hostname: str
   vmknicDevices: list[str] = []
   vmVnics: list[VsanVdsPgMigrationVmInfo] = []


class VsanVdsPgMigrationSpec(pyVmomi.vmodl.DynamicData):
   """
   Migration spec for a VSS portgroup to VDS.
   
   Preserves all existing
   settings for its consumers.
   Note in case of collisions there will be multiple portgroup migration specs
   for a single VSS portgroup name. See 'collisionRename' field.
   
   Attributes:
       vssPgName: The original name of the VSS portgroup that is being migrated.
           
           The settings
           of the hosts tracked in the 'hosts' field are the ones that are migrated.
           Note in case of collisions there will be multiple portgroup migration specs
           for a single VSS portgroup name. See 'collisionRename' field.
       dvPgName: The name of the DV portgroup that is being created/migrated to.
       vdsPgSetting: The VDS portgroup configuration of the portgroup to be created.
       vdsPgType: Type of portgroup to be created.
       hosts: Detailed migration information for each host and the consumers of the
           portgroup on this host.
       collisionRename: If true, the hosts tracked in this pg migration spec have a different portgroup
           setting spec than other hosts.
           
           In order to not change any settings as part of
           the migration, the conflict is resolved by creating this additional DVPortgroup
           under a renamed name (e.g. VssName-2).
   """
   vssPgName: str
   dvPgName: str
   vdsPgSetting: pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch.VmwarePortConfigPolicy
   vdsPgType: str
   hosts: list[VsanVdsPgMigrationHostInfo] = []
   collisionRename: bool


class VsanVdsPgMigrationVmInfo(pyVmomi.vmodl.DynamicData):
   """
   Detailed migration information about VMs and their vNICs that are
   being migrated from a VSS portgroup to VDS.
   
   Attributes:
       vm: Virtual Machine that has (some of) its vNICs migrated.
       vnicLabel: Human readable label of the vNICs that need to be migrated.
   """
   vm: pyVmomi.vim.VirtualMachine
   vnicLabel: list[str] = []


class VsanVdsSystem(pyVmomi.VmomiSupport.ManagedObject):
   """
   vSAN optimized methods for performing VDS related operations, especially
   migrations from VSS to VDS.
   
   In every vCenter server there is a singleton instance of this class
   with the Managed Object ID of 'vsan-vds-system'.
   """
   def VsanVdsGetMigrationPlan(self, cluster: pyVmomi.vim.ComputeResource, vswitchName: _typing.Optional[str], vdsName: _typing.Optional[str], vmnicDevices: list[str], infraVm: list[pyVmomi.vim.VirtualMachine], vds: _typing.Optional[pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch], hosts: list[pyVmomi.vim.HostSystem]) -> VsanVdsMigrationPlan:
      """
      Computes a migration plan to convert the VSS instances per host in
      the cluster to a newly created VDS.
      
      The VDS preserves all settings
      of the VSS, and all consumers (vmknics, VM vNICs, pNICs) are
      considered as part of the migration. The VSS vSwitch and portgroup
      instances across the hosts are matched to each other by common name.
      It is expected that hosts have a uniform configuration, and issues
      will be raised in the migration plan if deviations are found. Any
      deviations will still be carried over, but may require renaming of
      portgroups and additional VDS portgroups to resolve the conflicts.
      The migration plan is defined to be safe, i.e., the effective data
      path for all impacted VMs, vmknics and so on are going to be
      using the same settings as before the migration. The only change
      will be in any additional pNICs added as part of the migration.  
      Note: This API can also be used to create a new VDS without any
      portgroups, but with the physical NICs attached, and with good
      settings for vSAN, by simply passing the vswitchName as NULL.
      
      Args:
          cluster: Hosts of this cluster will be migrated to the new VDS
          vswitchName: Name of the original VSS vSwitch
          vdsName: Name of the new VDS. Only required for the creation of
              a new VDS
          vmnicDevices: Physical NICs that are currently unused to be
              attached to the new vDS.
          infraVm: Infrastructure VMs that will be handled specially
              during migration.
          vds: The VDS which the hosts are connected to. Set this parameter
              when existing VDS can be leveraged.
          hosts: hosts in the cluster to be migrated to the VDS. Leave this
              field empty if all the hosts in the cluster needs to be
              migrated.
      
      Returns:
          Detailed migration plan.
      
      Raises:
          pyVmomi.vim.fault.NotFound: when specified cluster doesn't exist.
          pyVmomi.vim.fault.VsanFault: Any unexpected runtime error.
          pyVmomi.vmodl.fault.InvalidArgument: When hosts with invalid or inconsistent
              configuration are found.
      """
      ...
   def VsanVdsMigrateVss(self, cluster: pyVmomi.vim.ComputeResource, migrationPlan: _typing.Optional[VsanVdsMigrationPlan], vswitchName: _typing.Optional[str], vdsName: _typing.Optional[str], vmnicDevices: list[str], infraVm: list[pyVmomi.vim.VirtualMachine], vds: _typing.Optional[pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch], hosts: list[pyVmomi.vim.HostSystem]) -> pyVmomi.vim.Task:
      """
      Perform a migration to convert the VSS instances per host in
      the cluster to a newly created VDS.
      
      The VDS preserves all settings
      of the VSS, and all consumers (vmknics, VM vNICs, pNICs) are
      considered as part of the migration. The VSS vSwitch and portgroup
      instances across the hosts are matched to each other by common name.
      It is expected that hosts have a uniform configuration, and issues
      will be raised in the migration plan if deviations are found. Any
      deviations will still be carried over, but may require renaming of
      portgroups and additional VDS portgroups to resolve the conflicts.
      The migration plan is defined to be safe, i.e., the effective data
      path for all impacted VMs, vmknics and so on are going to be
      using the same settings as before the migration. The only change
      will be in any additional pNICs added as part of the migration.  
      Note: This API can also be used to create a new VDS without any
      portgroups, but with the physical NICs attached, and with good
      settings for vSAN, by simply passing the vswitchName as NULL.  
      If a migration plan is passed in, the API makes sure that no
      changes have happened and that the migration plan is still
      current. This can be used to make sure that the migration plan
      that the user reviewed doesn't deviate from the actual migration
      performed.  
      If there are any inaccessible or orphaned VMs found the migration
      will not be performed. This is a safety measure as such VMs may
      loose their networking.  
      If there are any inaccessible hosts in the cluster the migration
      will fail.  
      The migration will fail if there is any infraVm on ESX with
      version prior to 6.5.0d, due to the missing of API support on the
      hosts.  
      A minimal version of 6.0 is required for all hosts to be migrated
      for the NetIOC setup task. Also the VDS version will be 6.0.0 if
      there is any 6.0 host to be migrated, otherwise 6.5.0.
      
      This API by default requires DVSwitch.Create and DVSwitch.Modify on
      RootFolder, and System.Read on cluster. Host.Inventory.EditCluster
      on hosts is required if hosts parameter is provided.
      
      Args:
          cluster: Hosts of this cluster will be migrated to the new VDS
          migrationPlan: Detailed migration plan
          vswitchName: Name of the original VSS vswitch
          vdsName: Name of the new VDS. Only required for the creation of
              a new VDS
          vmnicDevices: Physical NICs that are currently unused to be
              attached to the new VDS.
          infraVm: Infrastructure VMs that will be handled specially
              during migration.
          vds: The VDS which the hosts are connected to. Set this parameter
              when existing VDS can be leveraged.
          hosts: hosts in the cluster to be migrated to the VDS. Leave this
              field empty if all the hosts in the cluster needs to be
              migrated.
      
      Returns:
          The task associated with the migration
      
      Raises:
          pyVmomi.vim.fault.NotFound: when specified cluster doesn't exist.
          pyVmomi.vim.fault.VsanFault: Any unexpected runtime error.
          pyVmomi.vmodl.fault.InvalidArgument: When hosts with invalid or inconsistent
              configuration are found.
      """
      ...
   def VsanVssMigrateVds(self, cluster: _typing.Optional[pyVmomi.vim.ComputeResource], hosts: list[pyVmomi.vim.HostSystem], vds: pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch, vswitchName: _typing.Optional[str], vmnicDevices: list[str], infraVm: list[pyVmomi.vim.VirtualMachine]) -> pyVmomi.vim.Task:
      """
      Perform a migration to convert the VDS instance in the cluster to a newly
      created VSS on each host.
      
      The VSS preserves all settings of the VDS, and
      all consumers (vmknics, VM vNICs, pNICs) are considered as part of the
      migration. The VSS vSwitch and portgroup instances on the VDS are matched
      to each other by common name. It is expected that hosts have a uniform
      configuration. The VDS will be deleted if no hosts and virtual machines
      are connected to this VDS after the migration completes.
      If there are any inaccessible or orphaned VMs found, the migration
      will not be performed. This is a safety measure as such VMs may
      lose their networking. If there are any inaccessible hosts in the cluster
      the migration will fail as well.
      
      This API requires DVSwitch.Delete and DVSwitch.Modify on vds, extra
      privilege check might be needed depends on what is being migrated.
      - Host.Inventory.EditCluster on cluster if hosts of the specified cluster to be migrated to the VDS
      - Host.Inventory.EditCluster on all the hosts specified in hosts parameter
      
      Args:
          cluster: Hosts of this cluster will be migrated from the specified
              VDS to the new VSS.
          hosts: Individual hosts to be migrated from the VDS to the VSS.
          vds: The VDS which the hosts in the cluster are connected to.
          vswitchName: Name of the new VSS to be migrated to.
          vmnicDevices: Physical NICs that are currently unused to be
              attached to the new VSS.
          infraVm: Infrastructure VMs that will be handled specially
              during migration.
      
      Returns:
          The task associated with the migration
      
      Raises:
          pyVmomi.vim.fault.NotFound: when specified cluster doesn't exist.
          pyVmomi.vim.fault.VsanFault: Any unexpected runtime error.
      """
      ...
   def RollbackVdsToVss(self, task: pyVmomi.vim.Task) -> bool:
      """
      Rollback the change committed by the
      `pyVmomi.vim.vsan.VsanVdsSystem.vsanVdsMigrateVss`
      
      Args:
          task: The task associated with the change committed by
              the VsanVdsMigrateVss
      
      Returns:
          Always return True
      
      Raises:
          pyVmomi.vim.fault.NotFound: Task not found
          pyVmomi.vim.fault.VsanFault: Any unexpected runtime error.
      """
      ...


class VsanVibInstallPreflightStatus(pyVmomi.vmodl.DynamicData):
   """
   Preflight check status.
   
   Various pieces of information useful to the user
   before performing a VIB install.
   
   Attributes:
       manualVmotionRequired: True if DRS is not configured/enabled in a way that would automatically move VMs
           when performing EnterMaintenanceMode_Task().
           
           In such cases vSAN will issue the
           EnterMaintenanceMode_Task() call, but users need to assist in vMotion of any VMs
           on that host, either by using DRS manual recommendation application, or by fully
           manual vMotion.
       rollingRequired: True if there are powered on VMs on the cluster which prevent a all-at-once
           install of VIBs across the cluster.
           
           Only relevant when the VIBs that need to
           installed require maintenance mode.
   """
   manualVmotionRequired: bool
   rollingRequired: bool


class VsanVibScanResult(pyVmomi.vmodl.DynamicData):
   """
   Information about a VIB based on a scan of a host.
   
   Attributes:
       host: Host for which this information is in reference to.
       vibName: Name of the VIB which uniquely identifies it among other VIBs in the host.
       vibVersion: Version provided by this VIB.
       existingVersion: Existing version on the host, if any.
       maintenanceModeRequired: True if install of this VIB will require maintenance mode.
       rebootRequired: True if install of this VIB will require a host reboot.
       meetsSystemReq: True if system requirements are met.
       pkgDepsMetByHost: True if this vibs dependency is satisfied by the host vibs.
   """
   host: pyVmomi.vim.HostSystem
   vibName: str
   vibVersion: str
   existingVersion: _typing.Optional[str] = None
   maintenanceModeRequired: bool
   rebootRequired: bool
   meetsSystemReq: bool
   pkgDepsMetByHost: bool


class VsanVibSpec(pyVmomi.vmodl.DynamicData):
   """
   Contains information about a VIB to be installed or scanned.
   
   Attributes:
       host: Host onto which this VIB should be installed.
       metaUrl: URL to the metadata.zip file for this VIB.
           
           If not provided, it is not possible
           to determine most of the VIB properties before installing it.
       metaSha1Sum: SHA1 sum of the metadata file.
           
           Must be provided if metaUrl field is provided.
       vibUrl: URL to the .vib file for this VIB.
       vibSha1Sum: SHA1 sum of the VIB file.
   """
   host: pyVmomi.vim.HostSystem
   metaUrl: _typing.Optional[str] = None
   metaSha1Sum: _typing.Optional[str] = None
   vibUrl: str
   vibSha1Sum: str

class VsanVibType:
   """Type of VsanVibSpec."""
   pass


class VsanVmVdsMigrationSpec(pyVmomi.vmodl.DynamicData):
   """
   Class provides a config spec for a single VM that migrates this VM
   to a VDS.
   
   Attributes:
       vmInstanceUuid: Instance UUID of the VM to be migrated to VDS.
       vnics: vNIC migration specs.
   """
   vmInstanceUuid: str
   vnics: list[VsanVnicVdsMigrationSpec] = []


class VsanVnicVdsMigrationSpec(pyVmomi.vmodl.DynamicData):
   """
   Class provides a config spec for a single Virtual NIC of a VM that
   migrates this vNIC to a VDS.
   
   Attributes:
       key: Device key, unique among all virtual devices of a VM.
       vdsBacking: Backing that put the vNIC onto VDS.
   """
   key: int
   vdsBacking: pyVmomi.vim.vm.device.VirtualDevice.BackingInfo


class VsanVumConfig(pyVmomi.vmodl.DynamicData):
   """
   The configuration to support vSAN VUM options.
   
   Attributes:
       baselinePreferenceType: Baseline preference policy for current vSAN cluster.
           
           See `pyVmomi.vim.cluster.VsanBaselinePreferenceType` for all supported value.
   """
   baselinePreferenceType: str


class WitnessHostConfig(pyVmomi.vmodl.DynamicData):
   """
   vSAN extended configuration for witness host, to present
   vSAN stretched cluster configuration on this witness host.
   
   Attributes:
       subClusterUuid: The UUID of vSAN cluster with which this witness host is associated.
       preferredFaultDomainName: The preferred fault domain configured on this witness host.
   """
   subClusterUuid: str
   preferredFaultDomainName: str
   metadataMode: _typing.Optional[bool] = None


class XVCClientInfo(pyVmomi.vmodl.DynamicData):
   """
   Client cluster info from remote VC
   
   Attributes:
       cluster: The client cluster which mounts the vSAN datastore across VC.
       clusterName: The client cluster name which mounts the vSAN datastore across VC.
       vsanFormatVersion: The client cluster vSAN format version.
           
           This is stored at server side
           for vSAN version compatibility check.
       ownerVc: Remote VC address which owns this client cluster
       vcUuid: Remote VC uuid which owns this client cluster
       clusterUuid: The client cluster uuid which mounts the vSAN datastore across VC.
   """
   cluster: pyVmomi.vim.ClusterComputeResource
   clusterName: str
   vsanFormatVersion: str
   ownerVc: str
   vcUuid: _typing.Optional[str] = None
   clusterUuid: _typing.Optional[str] = None


class XVCDatastoreConfig(pyVmomi.vmodl.DynamicData):
   """
   vSAN cross VC datastore configuration.
   
   Attributes:
       xvcDatastores: vSAN cross datastore information list.
   """
   xvcDatastores: list[XVCDatastoreInfo] = []


class XVCDatastoreInfo(pyVmomi.vmodl.DynamicData):
   """
   Cross VC datastore information
   
   Attributes:
       datastore: The remote datastore to be mounted across VC.
       ownerVc: Remote VC address which owns this remote datastore
   """
   datastore: pyVmomi.vim.Datastore
   ownerVc: str


class XvcClientConfig(DatastoreSpec):
   """
   This represents a single local vSAN datastore in the server cluster and
   the list of cross VC client clusters mounting it.
   
   This is read only and shouldn't be set by users.
   
   Attributes:
       xvcClusters: The client clusters which mount the vSAN datastore across VC.
   """
   xvcClusters: list[XVCClientInfo] = []


class XvcClientInfoSpec(pyVmomi.vmodl.DynamicData):
   """
   The spec to present the client cluster's mount request
   
   Attributes:
       clientVc: Client VC name which owns this client cluster
       vcUuid: The uuid of the client vCenter
       vcVersion: The API version of the client vCenter
       cluster: The client cluster which requests to mount specified the vSAN datastores.
       clusterName: The client cluster name which requests to mount specified the vSAN
           datastores.
       clusterUuid: The uuid of the client cluster
       vsanFormatVersion: The client cluster vSAN format version.
           
           This is passed to server side
           for vSAN version compatibility check.
       minVsanFormatVersion: Minimum required cluster vSAN format version.
           
           This is passed to server side
           for vSAN version compatibility check.
       datastore: The server datastores requested to mount across VC
       unicastInfo: The client cluster's unicast info.
           
           It is used for supporting XVC DIT.
           The remote unicast agent needs to be set because when user mounts
           remote vSAN datastore, server cluster needs to do authentication
           on client host when remote DIT is enabled.
       saGeneration: The generation ID for service account lifecycle management.
   """
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
   """
   A condition on an object model property.
   
   Matches all objects that
   have a property that satisfies the condition.
   
   Attributes:
       property: Name of the property.
       operator: The operator to use for comparison of the property value.
           
           Must be one of XvcQueryCriteriaOperator.
       comparableValue: The value against which to compare the property value.
       comparableList: The list against which to compare the property values.
       ignoreCase: Whether to treat lower and upper cases of the same letter as if they
           were the same character.
   """
   property: str
   operator: _typing.Optional[str] = None
   comparableValue: _typing.Optional[object] = None
   comparableList: _typing.Optional[pyVmomi.vmodl.DynamicArray] = None
   ignoreCase: _typing.Optional[bool] = None

class XvcQueryCriteriaOperator:
   """
   Defines the possible operators to use when comparing the values of
   individual property.
   """
   pass


class XvcQueryFilter(pyVmomi.vmodl.DynamicData):
   """
   A set of conditions on the object model properties that
   together defines the criteria for filtering/matching the
   resources whose data to retrieve.
   
   Attributes:
       criterias: A list of conditions on the object model properties that could together
           define the criteria for filtering/matching the objects whose data to
           retrieve.
       operator: The logical operator which defines how the conditions should be combined
           to filter a given object.
   """
   criterias: list[XvcQueryCriteria] = []
   operator: _typing.Optional[str] = None

class XvcQueryFilterOperator:
   """Defines operator types for query filter."""
   pass


class XvcQueryPropertyValue(pyVmomi.vmodl.DynamicData):
   """Value of a certain property."""
   value: _typing.Optional[object] = None


class XvcQueryResultSet(pyVmomi.vmodl.DynamicData):
   """
   This data type describes the info of the objects returned from Query API.
   
   It is a dictionary like structure. The 'properties' list defines all
   keys of the returned information. The 'resultItems' list contains all
   returned objects' information. The properties' values of each object are
   listed in VsanXvcResultItem. The mapping between keys and values is by the
   index of the lists.
   
   Attributes:
       properties: The names of properties returned for each object item in
           the result set.
       resultItems: The list of result items.
           
           Each item corresponds to a particular
           object that satisfies the query conditions.
       totalCount: The total number of objects that match the query.
   """
   properties: list[str] = []
   resultItems: list[XvcResultItem] = []
   totalCount: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class XvcQuerySpec(pyVmomi.vmodl.DynamicData):
   """
   A query which encapsulates a request for specific object model.
   
   It supports filtering the object model's data to return by
   conditions on target object model's properties. Also, it allows
   for paging the final result set.
   
   Attributes:
       objectModel: Supported object models:
           - providerVcenter: The vCenters which the queried vCenter has configured as
             Datastore Sources.
           - clientVcenter: The vCenters which have added the queried vCenter as
             Datastore Source.
           - datastore: The vSAN local datastores on all provider vCenters and
             the local vCenter which are allowed to be mounted.
           - clientCluster: The clusters which mount the datastores on the queried
             vCenter.
           - serverCluster: The clusters which provide vSAN datastores on the
             queried vCenter.
       properties: Specifies the object model properties to be included in the
           result set for the query.
           
           For providerVcenter, each properties are illustrated below:
           - name: The vCenter's name (align with the Datastore Source configuration
             or specified remote vCenter information).
           - uuid: The vCenter's uuid.
           - version: The vCenter's API version.
           - linkType: The vCenter's link type. See .
           - totalCapacity: The total capacity of the datastores which can be mounted
             on the vCenter.
           - usedCapacity: The used capacity of the datastores which can be mounted
             on the vCenter
           - status: The communication status of the vCenter. When the vCenter can be
             communicated, the status code is 'OK'. When there is issue for communication,
             the status is in format of 'code{info}', as below:
             
             code: VsanSslVerifyCertFault, info: The expected certificate of the
             vCenter. This is the string of single x509 certificate encoded in PEM format.
             Caller needs to explicitly specify the certificate in passed parameter of
             `pyVmomi.vim.vsan.RemoteVcInfoStandalone` and retry the related APIs.
             
             code: NotAuthenticated, info: Some detailed information about
             unauthentication.
             
             code: ERROR, info: The exception type of the error, with some detailed
             error information. Representing a generic error.
           - clientVcenter: The queried vCenter which configures the providerVcenter
             as a Datastore Source. This is for differentiating multiple queried vCenters
             which configures the same providerVcenter.
             
           For clientVcenter, each properties are illustrated below:
           - name: The vCenter's name.
           - uuid: The vCenter's uuid.
           - providerVcenter: The queried vCenter which the clientVcenter configures
             as a Datastore Source. This is for differentiating multiple queried vCenters
             which has the same clientVcenter.
             
           For datastore, each properties are illustrated below:
           - name: The datastore's name.
           - moId: The datastore's moId.
           - providerVcenter: The name (align with the Datastore Source configuration
             or specified remote vCenter information) of the vCenter which provides the
             datastore.
           - serverGuid: The uuid of the providerVcenter.
           - datacenter: The name of the datacenter which provides the datastore.
           - clusterName: The name of the cluster which provides the datastore.
           - clusterMoId: The moId of the cluster which provides the datastore.
           - totalCapacity: The total capacity of the datastore.
           - usedCapacity: The used capacity of the datastore.
           - vmCount: The count the VMs which are provisioned in the datastore.
           - aliasOf: The alias property of the datastore.
           - containerId: The containerId property of the datastore.
           - clusterType: The cluster type(OSA/ESA) which provides the datastore.
           - clusterVmCount: The count of cluster VMs which are provisioned in the
             datastore.
           - vsanhcimeshdit: The status of capability vsanhcimeshdit for the
             datastore's server cluster.
           - effectiveTotalCapacity: The effective total capacity of the
             datastore.
           - effectiveUsedCapacity: The effective used capacity of the
             datastore.
             
           For clientCluster, each properties are illustrated below:
           - name: The name of the cluster.
           - moId: The moId of the cluster.
           - uuid: The uuid of the cluster.
           - vcenter: The name of the vCenter which provides the cluster.
           - serverGuid: The uuid of the vCenter which provides the cluster.
           - providerVcenter: The name (align with the Datastore Source configuration
             or specified remote vCenter information) of the vCenter which has
             datastore(s) mounted by the client.
           - datastores: The moIds list of the datastores on the providerVcenter
             which are mounted by the client cluster
             
           For serverCluster, each properties are illustrated below:
           - name: The name of the cluster.
           - providerVcenter: The name (align with the Datastore Source
             configuration or specified remote vCenter information) of the
             vCenter which provides the cluster.
           - moId: The moId of the cluster.
           - serverGuid: The uuid of the vCenter which provides the cluster.
           - uuid: The uuid of the cluster.
           - types: The types indicators list of the server cluster which
             provides the datastore. It can be the combination of the following
             values:
           - OSA: The cluster is a vSAN OSA cluster.
           - ESA: The cluster is a vSAN ESA cluster.
           - Max: The cluster is a vSAN Max cluster. A vSAN Max cluster is also
             a special kind of vSAN ESA cluster.
           - Stretched: The cluster is a vSAN OSA cluster.
             Multiple values could be combined to reflect the accurate cluster type,
             Some valid combinations are below:
           - OSA,Stretched: The cluster is a vSAN OSA Stretched cluster.
           - ESA, Stretched: The cluster is a vSAN ESA Stretched cluster.
           - ESA, Max: The cluster is a vSAN Max cluster, while a vSAN Max
             cluster must also be a vSAN ESA cluster.
           - ESA, Max, Stretched: The cluster is a vSAN Max Stretched
             cluster.
           - faultDomains: The fault domain info configured for the cluster.
             It is a list of fault domain name.
           - preferredFdName: The preferred fault domain name of the cluster.
       filter: Restricts (filters) the set of resources to be returned for the query.
       offset: The offset into the result set.
           
           Must be non-negative number.
           If unset, defaults to 0.
       limit: The maximum number of result items to return.
           
           If used, the value should
           be a non-negative integer.
       returnTotalCount: Indicates whether the total number of objects that matched the query
           should be computed and returned.
           
           This is meaningful only in cases where
           the number of objects that match the query could be more than the limit
           of the result items to be returned. If unset, defaults to false.
   """
   objectModel: _typing.Optional[str] = None
   properties: list[str] = []
   filter: _typing.Optional[XvcQueryFilter] = None
   offset: _typing.Optional[int] = None
   limit: _typing.Optional[int] = None
   returnTotalCount: _typing.Optional[bool] = None


class XvcResultItem(pyVmomi.vmodl.DynamicData):
   """
   Result item of a single object, which contains multiple properties
   in a list.
   
   Attributes:
       propertyValues: Values of queried properties in a list.
   """
   propertyValues: list[XvcQueryPropertyValue] = []

class clusterPowerState:
   """Defines the high level cluster power state.."""
   pass
