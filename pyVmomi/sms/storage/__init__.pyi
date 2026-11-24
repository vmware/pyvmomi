# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from . import replication as replication

import datetime as _datetime
import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vim
import pyVmomi.vmodl
import pyVmomi.sms.provider
import pyVmomi.vim.host
import pyVmomi.vim.vm.replication


class AlarmStatus:
   """Enumeration of the supported Alarm Status values"""
   pass

class AlarmType:
   pass


class BackingConfig(pyVmomi.vmodl.DynamicData):
   """
   This data object represents SDRS related data associated with block device or file system.
   
   Attributes:
       thinProvisionBackingIdentifier: Identifier for the backing pool for thin provisioning
       deduplicationBackingIdentifier: Identifier for the backing pool for deduplication
       autoTieringEnabled: Flag to indicate whether auto-tiering optimizations are active
       deduplicationEfficiency: Aggregate indication of space savings efficiency in the shared
           deduplication pool.
           
           The value is between 0 and 100, higher values
           indicating better efficiency.
       performanceOptimizationInterval: Frequency in seconds at which interval auto-tiering optimizations
           are applied.
           
           A value of 0 indicates continuous optimization.
   """
   thinProvisionBackingIdentifier: _typing.Optional[str] = None
   deduplicationBackingIdentifier: _typing.Optional[str] = None
   autoTieringEnabled: _typing.Optional[bool] = None
   deduplicationEfficiency: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   performanceOptimizationInterval: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class BackingStoragePool(pyVmomi.vmodl.DynamicData):
   """
   This data object represents the backing storage pool information of block device or file system.
   
   Attributes:
       uuid: Unique identifier
       capacityInMB: Upper bound of the available capacity in the backing storage pool.
       usedSpaceInMB: Aggregate used space in the backing storage pool.
   """
   class BackingStoragePoolType(pyVmomi.VmomiSupport.Enum):
      """List of possible BackingStoragePool types"""
      thinProvisioningPool: _typing.ClassVar['BackingStoragePool.BackingStoragePoolType'] = 'thinProvisioningPool'
      deduplicationPool: _typing.ClassVar['BackingStoragePool.BackingStoragePoolType'] = 'deduplicationPool'
      thinAndDeduplicationCombinedPool: _typing.ClassVar['BackingStoragePool.BackingStoragePoolType'] = 'thinAndDeduplicationCombinedPool'

   uuid: str
   type: str
   capacityInMB: pyVmomi.VmomiSupport.long
   usedSpaceInMB: pyVmomi.VmomiSupport.long


class DatastoreBackingPoolMapping(pyVmomi.vmodl.DynamicData):
   """
   This data object represents the result of queryDatastoreBackingPoolMapping API.
   
   More than one datastore can map to the same set of BackingStoragePool.
   """
   datastore: list[pyVmomi.vim.Datastore] = []
   backingStoragePool: list[BackingStoragePool] = []


class DatastorePair(pyVmomi.vmodl.DynamicData):
   """Deprecated: As of SMS API 5.0Datastore pair that is returned as a result of queryDrsMigrationCapabilityForPerformanceEx API."""
   datastore1: pyVmomi.vim.Datastore
   datastore2: pyVmomi.vim.Datastore


class DrsMigrationCapabilityResult(pyVmomi.vmodl.DynamicData):
   """Deprecated: As of SMS API 5.0This data object represents the result of queryDrsMigrationCapabilityForPerformanceEx API."""
   recommendedDatastorePair: list[DatastorePair] = []
   nonRecommendedDatastorePair: list[DatastorePair] = []

class EntityType:
   """Enumeration of the supported Entity Type values."""
   pass


class FaultDomainProviderMapping(pyVmomi.vmodl.DynamicData):
   """
   This mapping will be set in InactiveProvider fault to notify clients
   the current active provider for the specified fault domains.
   
   Attributes:
       activeProvider: Active provider managing the fault domains
       faultDomainId: Fault domains being managed by the provider
   """
   activeProvider: pyVmomi.sms.provider.Provider
   faultDomainId: list[pyVmomi.vim.vm.replication.FaultDomainId] = []


class StoragePort(pyVmomi.vmodl.DynamicData):
   """
   This data object represents the storage port.
   
   Attributes:
       uuid: Unique identifier
       type: Storage Port Type
       alternateName: Other identifiers which can help identify storage port
   """
   uuid: str
   type: str
   alternateName: list[str] = []

class FcStoragePort(StoragePort):
   """
   This data object represents the FC storage port.
   
   Attributes:
       portWwn: World Wide Name for the Port
       nodeWwn: World Wide Name for the Node
   """
   portWwn: str
   nodeWwn: str

class FcoeStoragePort(StoragePort):
   """
   This data object represents the FCoE storage port.
   
   Attributes:
       portWwn: World Wide Name for the Port
       nodeWwn: World Wide Name for the Node
   """
   portWwn: str
   nodeWwn: str


class FileSystemInfo(pyVmomi.vmodl.DynamicData):
   """
   This data object represents information about the storage
   file-system.
   
   Attributes:
       fileServerName: Server Name
       fileSystemPath: File Path
       ipAddress: IP address
   """
   fileServerName: str
   fileSystemPath: str
   ipAddress: _typing.Optional[str] = None

class IscsiStoragePort(StoragePort):
   """
   This data object represents the iSCSI storage port.
   
   Attributes:
       identifier: IQN or EQI identifier
   """
   identifier: str


class LunHbaAssociation(pyVmomi.vmodl.DynamicData):
   """
   This data object represents the lun, HBA association
   for synchronous replication.
   """
   canonicalName: str
   hba: list[pyVmomi.vim.host.HostBusAdapter] = []


class NameValuePair(pyVmomi.vmodl.DynamicData):
   """
   This data object represents a name value pair.
   
   Attributes:
       parameterName: Name of the parameter
       parameterValue: Value of the parameter
   """
   parameterName: str
   parameterValue: str


class StorageAlarm(pyVmomi.vmodl.DynamicData):
   """
   This data object represents the storage alarm.
   
   Attributes:
       alarmId: Monotonically increasing sequence number which
           VP will maintain.
       alarmType: The type of Alarm.
           
           Must be one of the string values from
           `pyVmomi.sms.storage.AlarmType`
           Note that for VMODL VP implementation this field must be populated with one
           of the values from `vasa.data.notification.AlarmType`
       containerId: Container identifier
       objectId: The unique identifier of the object impacted by the Alarm.
           
           From VASA version 3 onwards, a non-null `pyVmomi.sms.storage.StorageAlarm.alarmObject`
           will override this member.
           This field is made optional from VASA3. Either this or
           `pyVmomi.sms.storage.StorageAlarm.alarmObject` must be set.
       objectType: The type of object impacted by the Alarm.
           
           Must be one of the string values
           from `pyVmomi.sms.storage.EntityType`
           Note that for VMODL VP implementation this field must be populated with one
           of the values from `vasa.data.notification.EntityType`
       status: Current status of the object.
           
           Must be one of the string values from
           `pyVmomi.sms.storage.AlarmStatus`
       alarmTimeStamp: Time-stamp when the alarm occurred in VP context
       messageId: Pre-defined message for system-defined event
       parameterList: List of parameters (name/value) to be passed as input for message
       alarmObject: The ID of the object on which the alarm is raised; this is an object,
           since ID's may not always be strings.
           
           vSphere will first use
           `pyVmomi.sms.storage.StorageAlarm.alarmObject` if set, and if not uses `pyVmomi.sms.storage.StorageAlarm.objectId`.
   """
   alarmId: pyVmomi.VmomiSupport.long
   alarmType: str
   containerId: _typing.Optional[str] = None
   objectId: _typing.Optional[str] = None
   objectType: str
   status: str
   alarmTimeStamp: _datetime.datetime
   messageId: str
   parameterList: list[NameValuePair] = []
   alarmObject: _typing.Optional[object] = None


class StorageArray(pyVmomi.vmodl.DynamicData):
   """
   This data object represents the storage array.
   
   Attributes:
       name: Name
       uuid: Unique identifier
       vendorId: Storage array Vendor Id
       modelId: Model Id
       firmware: Storage array firmware
       alternateName: List of alternate storage array names
       supportedBlockInterface: Supported block-device interfaces
       supportedFileSystemInterface: Supported file-system interfaces
       supportedProfile: List of supported profiles
       priority: Priority level of the provider for the given array within the session context.
           
           SMS will use this value to pick a provider among the ones that are registered
           with SMS and manage this array. Once the provider is chosen, SMS will communicate
           with it to get the data related to this array.
           Valid range: 0 to 255.
       discoverySvc: Required for NVMe-oF arrays and optional otherwise.
           
           Transport information to address the array's discovery service.
   """
   class BlockDeviceInterface(pyVmomi.VmomiSupport.Enum):
      """List of possible block device interfaces"""
      fc: _typing.ClassVar['StorageArray.BlockDeviceInterface'] = 'fc'
      iscsi: _typing.ClassVar['StorageArray.BlockDeviceInterface'] = 'iscsi'
      fcoe: _typing.ClassVar['StorageArray.BlockDeviceInterface'] = 'fcoe'
      otherBlock: _typing.ClassVar['StorageArray.BlockDeviceInterface'] = 'otherBlock'

   class FileSystemInterface(pyVmomi.VmomiSupport.Enum):
      """List of possible file system interfaces"""
      nfs: _typing.ClassVar['StorageArray.FileSystemInterface'] = 'nfs'
      otherFileSystem: _typing.ClassVar['StorageArray.FileSystemInterface'] = 'otherFileSystem'

   class VasaProfile(pyVmomi.VmomiSupport.Enum):
      """
      List of possible VASA profiles supported by Storage Array
      
      Attributes:
          blockDevice: Block device profile
          fileSystem: File system profile
          capability: Storage capability profile
          policy: Policy profile
          object: Object based storage profile
          statistics: IO Statistics profile
          storageDrsBlockDevice: Storage DRS specific block device profile
          storageDrsFileSystem: Storage DRS specific file system profile
      """
      blockDevice: _typing.ClassVar['StorageArray.VasaProfile'] = 'blockDevice'
      fileSystem: _typing.ClassVar['StorageArray.VasaProfile'] = 'fileSystem'
      capability: _typing.ClassVar['StorageArray.VasaProfile'] = 'capability'
      policy: _typing.ClassVar['StorageArray.VasaProfile'] = 'policy'
      object: _typing.ClassVar['StorageArray.VasaProfile'] = 'object'
      statistics: _typing.ClassVar['StorageArray.VasaProfile'] = 'statistics'
      storageDrsBlockDevice: _typing.ClassVar['StorageArray.VasaProfile'] = 'storageDrsBlockDevice'
      storageDrsFileSystem: _typing.ClassVar['StorageArray.VasaProfile'] = 'storageDrsFileSystem'

   name: str
   uuid: str
   vendorId: str
   modelId: str
   firmware: _typing.Optional[str] = None
   alternateName: list[str] = []
   supportedBlockInterface: list[str] = []
   supportedFileSystemInterface: list[str] = []
   supportedProfile: list[str] = []
   priority: _typing.Optional[int] = None
   discoverySvc: list[pyVmomi.vim.VasaStorageArray.DiscoverySvcInfo] = []


class StorageCapability(pyVmomi.vmodl.DynamicData):
   """This data object represents the storage capability."""
   uuid: str
   name: str
   description: str


class StorageContainer(pyVmomi.vmodl.DynamicData):
   """
   This data object represents the storage container.
   
   Attributes:
       uuid: Unique identifier
       name: Name of the container
       maxVvolSizeInMB: Maximum allowed capacity of the Virtual Volume in MBs
       providerId: `pyVmomi.sms.provider.ProviderInfo.uid` for providers that reports the storage container.
       vvolContainerType: Represents type of VVOL container, the supported values are listed in
           `pyVmomi.sms.storage.StorageContainer.VvolContainerTypeEnum`.
           
           If the storage array is not capable of supporting mixed PEs for a storage container,
           the VVOL VASA provider sets this property to the supported endpoint type
       stretched: Indicates if this storage container is stretched
   """
   class VvolContainerTypeEnum(pyVmomi.VmomiSupport.Enum):
      """List of supported VVOL Container types"""
      NFS: _typing.ClassVar['StorageContainer.VvolContainerTypeEnum'] = 'NFS'
      NFS4x: _typing.ClassVar['StorageContainer.VvolContainerTypeEnum'] = 'NFS4x'
      SCSI: _typing.ClassVar['StorageContainer.VvolContainerTypeEnum'] = 'SCSI'
      NVMe: _typing.ClassVar['StorageContainer.VvolContainerTypeEnum'] = 'NVMe'

   uuid: str
   name: str
   maxVvolSizeInMB: pyVmomi.VmomiSupport.long
   providerId: list[str] = []
   arrayId: list[str] = []
   vvolContainerType: _typing.Optional[str] = None
   stretched: _typing.Optional[bool] = None


class StorageContainerResult(pyVmomi.vmodl.DynamicData):
   """
   This data object represents information about storage containers and related providers.
   
   Attributes:
       storageContainer: `pyVmomi.sms.storage.StorageContainer` objects
       providerInfo: `pyVmomi.sms.provider.ProviderInfo` corresponding to providers that
           report these storage containers
   """
   storageContainer: list[StorageContainer] = []
   providerInfo: list[pyVmomi.sms.provider.ProviderInfo] = []


class StorageContainerSpec(pyVmomi.vmodl.DynamicData):
   """
   This data object represents the specification to query
   storage containers retrieved from VASA providers.
   """
   containerId: list[str] = []


class StorageFileSystem(pyVmomi.vmodl.DynamicData):
   """
   This data object represents the storage file-system.
   
   Attributes:
       uuid: Unique identifier
       info: Information about the file system
       backingConfig: Backing config information
   """
   class FileSystemInterfaceVersion(pyVmomi.VmomiSupport.Enum):
      NFSV3_0: _typing.ClassVar['StorageFileSystem.FileSystemInterfaceVersion'] = 'NFSV3_0'

   uuid: str
   info: list[FileSystemInfo] = []
   nativeSnapshotSupported: bool
   thinProvisioningStatus: str
   type: str
   version: str
   backingConfig: _typing.Optional[BackingConfig] = None


class StorageLun(pyVmomi.vmodl.DynamicData):
   """
   This data object represents the storage lun.
   
   Attributes:
       uuid: Unique Indentfier
       vSphereLunIdentifier: Identifier reported by vSphere(ESX) for this LUN
       vendorDisplayName: Display Name which appears in storage array management
           console
       capacityInMB: Capacity In MB
       usedSpaceInMB: Used space in MB for a thin provisioned LUN
       lunThinProvisioned: Indicates whether the LUN is thin provisioned
       alternateIdentifier: Alternate identifiers associated with the LUN
       drsManagementPermitted: Indicates whether Storage DRS is permitted to manage
           performance between this LUN and other LUNs from the same
           array.
       backingConfig: Backing config information
   """
   uuid: str
   vSphereLunIdentifier: str
   vendorDisplayName: str
   capacityInMB: pyVmomi.VmomiSupport.long
   usedSpaceInMB: pyVmomi.VmomiSupport.long
   lunThinProvisioned: bool
   alternateIdentifier: list[str] = []
   drsManagementPermitted: bool
   thinProvisioningStatus: str
   backingConfig: _typing.Optional[BackingConfig] = None


class StorageProcessor(pyVmomi.vmodl.DynamicData):
   """
   This data object represents the storage processor.
   
   Attributes:
       uuid: Unique Identifier
       alternateIdentifer: List of alternate identifiers
   """
   uuid: str
   alternateIdentifer: list[str] = []

class ThinProvisioningStatus:
   """List of possible values for thin provisioning status alarm."""
   pass
