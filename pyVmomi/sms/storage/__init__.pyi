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
   pass

class AlarmType:
   pass


class BackingConfig(pyVmomi.vmodl.DynamicData):
   thinProvisionBackingIdentifier: _typing.Optional[str] = None
   deduplicationBackingIdentifier: _typing.Optional[str] = None
   autoTieringEnabled: _typing.Optional[bool] = None
   deduplicationEfficiency: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   performanceOptimizationInterval: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class BackingStoragePool(pyVmomi.vmodl.DynamicData):
   class BackingStoragePoolType(pyVmomi.VmomiSupport.Enum):
      thinProvisioningPool: _typing.ClassVar['BackingStoragePoolType'] = 'thinProvisioningPool'
      deduplicationPool: _typing.ClassVar['BackingStoragePoolType'] = 'deduplicationPool'
      thinAndDeduplicationCombinedPool: _typing.ClassVar['BackingStoragePoolType'] = 'thinAndDeduplicationCombinedPool'

   uuid: str
   type: str
   capacityInMB: pyVmomi.VmomiSupport.long
   usedSpaceInMB: pyVmomi.VmomiSupport.long


class DatastoreBackingPoolMapping(pyVmomi.vmodl.DynamicData):
   datastore: list[pyVmomi.vim.Datastore] = []
   backingStoragePool: list[BackingStoragePool] = []


class DatastorePair(pyVmomi.vmodl.DynamicData):
   datastore1: pyVmomi.vim.Datastore
   datastore2: pyVmomi.vim.Datastore


class DrsMigrationCapabilityResult(pyVmomi.vmodl.DynamicData):
   recommendedDatastorePair: list[DatastorePair] = []
   nonRecommendedDatastorePair: list[DatastorePair] = []

class EntityType:
   pass


class FaultDomainProviderMapping(pyVmomi.vmodl.DynamicData):
   activeProvider: pyVmomi.sms.provider.Provider
   faultDomainId: list[pyVmomi.vim.vm.replication.FaultDomainId] = []

class FcStoragePort(StoragePort):
   portWwn: str
   nodeWwn: str

class FcoeStoragePort(StoragePort):
   portWwn: str
   nodeWwn: str


class FileSystemInfo(pyVmomi.vmodl.DynamicData):
   fileServerName: str
   fileSystemPath: str
   ipAddress: _typing.Optional[str] = None

class IscsiStoragePort(StoragePort):
   identifier: str


class LunHbaAssociation(pyVmomi.vmodl.DynamicData):
   canonicalName: str
   hba: list[pyVmomi.vim.host.HostBusAdapter] = []


class NameValuePair(pyVmomi.vmodl.DynamicData):
   parameterName: str
   parameterValue: str


class StorageAlarm(pyVmomi.vmodl.DynamicData):
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
   class BlockDeviceInterface(pyVmomi.VmomiSupport.Enum):
      fc: _typing.ClassVar['BlockDeviceInterface'] = 'fc'
      iscsi: _typing.ClassVar['BlockDeviceInterface'] = 'iscsi'
      fcoe: _typing.ClassVar['BlockDeviceInterface'] = 'fcoe'
      otherBlock: _typing.ClassVar['BlockDeviceInterface'] = 'otherBlock'

   class FileSystemInterface(pyVmomi.VmomiSupport.Enum):
      nfs: _typing.ClassVar['FileSystemInterface'] = 'nfs'
      otherFileSystem: _typing.ClassVar['FileSystemInterface'] = 'otherFileSystem'

   class VasaProfile(pyVmomi.VmomiSupport.Enum):
      blockDevice: _typing.ClassVar['VasaProfile'] = 'blockDevice'
      fileSystem: _typing.ClassVar['VasaProfile'] = 'fileSystem'
      capability: _typing.ClassVar['VasaProfile'] = 'capability'
      policy: _typing.ClassVar['VasaProfile'] = 'policy'
      object: _typing.ClassVar['VasaProfile'] = 'object'
      statistics: _typing.ClassVar['VasaProfile'] = 'statistics'
      storageDrsBlockDevice: _typing.ClassVar['VasaProfile'] = 'storageDrsBlockDevice'
      storageDrsFileSystem: _typing.ClassVar['VasaProfile'] = 'storageDrsFileSystem'

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
   uuid: str
   name: str
   description: str


class StorageContainer(pyVmomi.vmodl.DynamicData):
   class VvolContainerTypeEnum(pyVmomi.VmomiSupport.Enum):
      NFS: _typing.ClassVar['VvolContainerTypeEnum'] = 'NFS'
      NFS4x: _typing.ClassVar['VvolContainerTypeEnum'] = 'NFS4x'
      SCSI: _typing.ClassVar['VvolContainerTypeEnum'] = 'SCSI'
      NVMe: _typing.ClassVar['VvolContainerTypeEnum'] = 'NVMe'

   uuid: str
   name: str
   maxVvolSizeInMB: pyVmomi.VmomiSupport.long
   providerId: list[str] = []
   arrayId: list[str] = []
   vvolContainerType: _typing.Optional[str] = None
   stretched: _typing.Optional[bool] = None


class StorageContainerResult(pyVmomi.vmodl.DynamicData):
   storageContainer: list[StorageContainer] = []
   providerInfo: list[pyVmomi.sms.provider.ProviderInfo] = []


class StorageContainerSpec(pyVmomi.vmodl.DynamicData):
   containerId: list[str] = []


class StorageFileSystem(pyVmomi.vmodl.DynamicData):
   class FileSystemInterfaceVersion(pyVmomi.VmomiSupport.Enum):
      NFSV3_0: _typing.ClassVar['FileSystemInterfaceVersion'] = 'NFSV3_0'

   uuid: str
   info: list[FileSystemInfo] = []
   nativeSnapshotSupported: bool
   thinProvisioningStatus: str
   type: str
   version: str
   backingConfig: _typing.Optional[BackingConfig] = None


class StorageLun(pyVmomi.vmodl.DynamicData):
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


class StoragePort(pyVmomi.vmodl.DynamicData):
   uuid: str
   type: str
   alternateName: list[str] = []


class StorageProcessor(pyVmomi.vmodl.DynamicData):
   uuid: str
   alternateIdentifer: list[str] = []

class ThinProvisioningStatus:
   pass
