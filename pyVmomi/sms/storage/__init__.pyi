from typing import List
from enum import Enum
from pyVmomi import sms, vim, vmodl
from datetime import datetime
from pyVmomi.VmomiSupport import long
from . import replication as replication


class BackingConfig(vmodl.DynamicData):
    @property
    def thinProvisionBackingIdentifier(self) -> str: ...
    @thinProvisionBackingIdentifier.setter
    def thinProvisionBackingIdentifier(self, value: str):
        self._thinProvisionBackingIdentifier = value
    @property
    def deduplicationBackingIdentifier(self) -> str: ...
    @deduplicationBackingIdentifier.setter
    def deduplicationBackingIdentifier(self, value: str):
        self._deduplicationBackingIdentifier = value
    @property
    def autoTieringEnabled(self) -> bool: ...
    @autoTieringEnabled.setter
    def autoTieringEnabled(self, value: bool):
        self._autoTieringEnabled = value
    @property
    def deduplicationEfficiency(self) -> long: ...
    @deduplicationEfficiency.setter
    def deduplicationEfficiency(self, value: long):
        self._deduplicationEfficiency = value
    @property
    def performanceOptimizationInterval(self) -> long: ...
    @performanceOptimizationInterval.setter
    def performanceOptimizationInterval(self, value: long):
        self._performanceOptimizationInterval = value


class BackingStoragePool(vmodl.DynamicData):
    @property
    def uuid(self) -> str: ...
    @uuid.setter
    def uuid(self, value: str):
        self._uuid = value
    @property
    def type(self) -> str: ...
    @type.setter
    def type(self, value: str):
        self._type = value
    @property
    def capacityInMB(self) -> long: ...
    @capacityInMB.setter
    def capacityInMB(self, value: long):
        self._capacityInMB = value
    @property
    def usedSpaceInMB(self) -> long: ...
    @usedSpaceInMB.setter
    def usedSpaceInMB(self, value: long):
        self._usedSpaceInMB = value


    class BackingStoragePoolType(Enum):
        thinProvisioningPool = "thinProvisioningPool"
        deduplicationPool = "deduplicationPool"
        thinAndDeduplicationCombinedPool = "thinAndDeduplicationCombinedPool"


class DatastoreBackingPoolMapping(vmodl.DynamicData):
    @property
    def datastore(self) -> List[vim.Datastore]: ...
    @datastore.setter
    def datastore(self, value: List[vim.Datastore]):
        self._datastore = value
    @property
    def backingStoragePool(self) -> List[BackingStoragePool]: ...
    @backingStoragePool.setter
    def backingStoragePool(self, value: List[BackingStoragePool]):
        self._backingStoragePool = value


class DatastorePair(vmodl.DynamicData):
    @property
    def datastore1(self) -> vim.Datastore: ...
    @datastore1.setter
    def datastore1(self, value: vim.Datastore):
        self._datastore1 = value
    @property
    def datastore2(self) -> vim.Datastore: ...
    @datastore2.setter
    def datastore2(self, value: vim.Datastore):
        self._datastore2 = value


class DrsMigrationCapabilityResult(vmodl.DynamicData):
    @property
    def recommendedDatastorePair(self) -> List[DatastorePair]: ...
    @recommendedDatastorePair.setter
    def recommendedDatastorePair(self, value: List[DatastorePair]):
        self._recommendedDatastorePair = value
    @property
    def nonRecommendedDatastorePair(self) -> List[DatastorePair]: ...
    @nonRecommendedDatastorePair.setter
    def nonRecommendedDatastorePair(self, value: List[DatastorePair]):
        self._nonRecommendedDatastorePair = value


class FaultDomainProviderMapping(vmodl.DynamicData):
    @property
    def activeProvider(self) -> sms.provider.Provider: ...
    @activeProvider.setter
    def activeProvider(self, value: sms.provider.Provider):
        self._activeProvider = value
    @property
    def faultDomainId(self) -> List[vim.vm.replication.FaultDomainId]: ...
    @faultDomainId.setter
    def faultDomainId(self, value: List[vim.vm.replication.FaultDomainId]):
        self._faultDomainId = value


class FcStoragePort(StoragePort):
    @property
    def portWwn(self) -> str: ...
    @portWwn.setter
    def portWwn(self, value: str):
        self._portWwn = value
    @property
    def nodeWwn(self) -> str: ...
    @nodeWwn.setter
    def nodeWwn(self, value: str):
        self._nodeWwn = value


class FcoeStoragePort(StoragePort):
    @property
    def portWwn(self) -> str: ...
    @portWwn.setter
    def portWwn(self, value: str):
        self._portWwn = value
    @property
    def nodeWwn(self) -> str: ...
    @nodeWwn.setter
    def nodeWwn(self, value: str):
        self._nodeWwn = value


class FileSystemInfo(vmodl.DynamicData):
    @property
    def fileServerName(self) -> str: ...
    @fileServerName.setter
    def fileServerName(self, value: str):
        self._fileServerName = value
    @property
    def fileSystemPath(self) -> str: ...
    @fileSystemPath.setter
    def fileSystemPath(self, value: str):
        self._fileSystemPath = value
    @property
    def ipAddress(self) -> str: ...
    @ipAddress.setter
    def ipAddress(self, value: str):
        self._ipAddress = value


class IscsiStoragePort(StoragePort):
    @property
    def identifier(self) -> str: ...
    @identifier.setter
    def identifier(self, value: str):
        self._identifier = value


class LunHbaAssociation(vmodl.DynamicData):
    @property
    def canonicalName(self) -> str: ...
    @canonicalName.setter
    def canonicalName(self, value: str):
        self._canonicalName = value
    @property
    def hba(self) -> List[vim.host.HostBusAdapter]: ...
    @hba.setter
    def hba(self, value: List[vim.host.HostBusAdapter]):
        self._hba = value


class NameValuePair(vmodl.DynamicData):
    @property
    def parameterName(self) -> str: ...
    @parameterName.setter
    def parameterName(self, value: str):
        self._parameterName = value
    @property
    def parameterValue(self) -> str: ...
    @parameterValue.setter
    def parameterValue(self, value: str):
        self._parameterValue = value


class StorageAlarm(vmodl.DynamicData):
    @property
    def alarmId(self) -> long: ...
    @alarmId.setter
    def alarmId(self, value: long):
        self._alarmId = value
    @property
    def alarmType(self) -> str: ...
    @alarmType.setter
    def alarmType(self, value: str):
        self._alarmType = value
    @property
    def containerId(self) -> str: ...
    @containerId.setter
    def containerId(self, value: str):
        self._containerId = value
    @property
    def objectId(self) -> str: ...
    @objectId.setter
    def objectId(self, value: str):
        self._objectId = value
    @property
    def objectType(self) -> str: ...
    @objectType.setter
    def objectType(self, value: str):
        self._objectType = value
    @property
    def status(self) -> str: ...
    @status.setter
    def status(self, value: str):
        self._status = value
    @property
    def alarmTimeStamp(self) -> datetime: ...
    @alarmTimeStamp.setter
    def alarmTimeStamp(self, value: datetime):
        self._alarmTimeStamp = value
    @property
    def messageId(self) -> str: ...
    @messageId.setter
    def messageId(self, value: str):
        self._messageId = value
    @property
    def parameterList(self) -> List[NameValuePair]: ...
    @parameterList.setter
    def parameterList(self, value: List[NameValuePair]):
        self._parameterList = value
    @property
    def alarmObject(self) -> object: ...
    @alarmObject.setter
    def alarmObject(self, value: object):
        self._alarmObject = value


class StorageArray(vmodl.DynamicData):
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def uuid(self) -> str: ...
    @uuid.setter
    def uuid(self, value: str):
        self._uuid = value
    @property
    def vendorId(self) -> str: ...
    @vendorId.setter
    def vendorId(self, value: str):
        self._vendorId = value
    @property
    def modelId(self) -> str: ...
    @modelId.setter
    def modelId(self, value: str):
        self._modelId = value
    @property
    def firmware(self) -> str: ...
    @firmware.setter
    def firmware(self, value: str):
        self._firmware = value
    @property
    def alternateName(self) -> List[str]: ...
    @alternateName.setter
    def alternateName(self, value: List[str]):
        self._alternateName = value
    @property
    def supportedBlockInterface(self) -> List[str]: ...
    @supportedBlockInterface.setter
    def supportedBlockInterface(self, value: List[str]):
        self._supportedBlockInterface = value
    @property
    def supportedFileSystemInterface(self) -> List[str]: ...
    @supportedFileSystemInterface.setter
    def supportedFileSystemInterface(self, value: List[str]):
        self._supportedFileSystemInterface = value
    @property
    def supportedProfile(self) -> List[str]: ...
    @supportedProfile.setter
    def supportedProfile(self, value: List[str]):
        self._supportedProfile = value
    @property
    def priority(self) -> int: ...
    @priority.setter
    def priority(self, value: int):
        self._priority = value
    @property
    def discoverySvc(self) -> List[vim.VasaStorageArray.DiscoverySvcInfo]: ...
    @discoverySvc.setter
    def discoverySvc(self, value: List[vim.VasaStorageArray.DiscoverySvcInfo]):
        self._discoverySvc = value


    class BlockDeviceInterface(Enum):
        fc = "fc"
        iscsi = "iscsi"
        fcoe = "fcoe"
        otherBlock = "otherBlock"


    class FileSystemInterface(Enum):
        nfs = "nfs"
        otherFileSystem = "otherFileSystem"


    class VasaProfile(Enum):
        blockDevice = "blockDevice"
        fileSystem = "fileSystem"
        capability = "capability"
        policy = "policy"
        object = "object"
        statistics = "statistics"
        storageDrsBlockDevice = "storageDrsBlockDevice"
        storageDrsFileSystem = "storageDrsFileSystem"


class StorageCapability(vmodl.DynamicData):
    @property
    def uuid(self) -> str: ...
    @uuid.setter
    def uuid(self, value: str):
        self._uuid = value
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def description(self) -> str: ...
    @description.setter
    def description(self, value: str):
        self._description = value


class StorageContainer(vmodl.DynamicData):
    @property
    def uuid(self) -> str: ...
    @uuid.setter
    def uuid(self, value: str):
        self._uuid = value
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def maxVvolSizeInMB(self) -> long: ...
    @maxVvolSizeInMB.setter
    def maxVvolSizeInMB(self, value: long):
        self._maxVvolSizeInMB = value
    @property
    def providerId(self) -> List[str]: ...
    @providerId.setter
    def providerId(self, value: List[str]):
        self._providerId = value
    @property
    def arrayId(self) -> List[str]: ...
    @arrayId.setter
    def arrayId(self, value: List[str]):
        self._arrayId = value
    @property
    def vvolContainerType(self) -> str: ...
    @vvolContainerType.setter
    def vvolContainerType(self, value: str):
        self._vvolContainerType = value


    class VvolContainerTypeEnum(Enum):
        NFS = "NFS"
        NFS4x = "NFS4x"
        SCSI = "SCSI"
        NVMe = "NVMe"


class StorageContainerResult(vmodl.DynamicData):
    @property
    def storageContainer(self) -> List[StorageContainer]: ...
    @storageContainer.setter
    def storageContainer(self, value: List[StorageContainer]):
        self._storageContainer = value
    @property
    def providerInfo(self) -> List[sms.provider.ProviderInfo]: ...
    @providerInfo.setter
    def providerInfo(self, value: List[sms.provider.ProviderInfo]):
        self._providerInfo = value


class StorageContainerSpec(vmodl.DynamicData):
    @property
    def containerId(self) -> List[str]: ...
    @containerId.setter
    def containerId(self, value: List[str]):
        self._containerId = value


class StorageFileSystem(vmodl.DynamicData):
    @property
    def uuid(self) -> str: ...
    @uuid.setter
    def uuid(self, value: str):
        self._uuid = value
    @property
    def info(self) -> List[FileSystemInfo]: ...
    @info.setter
    def info(self, value: List[FileSystemInfo]):
        self._info = value
    @property
    def nativeSnapshotSupported(self) -> bool: ...
    @nativeSnapshotSupported.setter
    def nativeSnapshotSupported(self, value: bool):
        self._nativeSnapshotSupported = value
    @property
    def thinProvisioningStatus(self) -> str: ...
    @thinProvisioningStatus.setter
    def thinProvisioningStatus(self, value: str):
        self._thinProvisioningStatus = value
    @property
    def type(self) -> str: ...
    @type.setter
    def type(self, value: str):
        self._type = value
    @property
    def version(self) -> str: ...
    @version.setter
    def version(self, value: str):
        self._version = value
    @property
    def backingConfig(self) -> BackingConfig: ...
    @backingConfig.setter
    def backingConfig(self, value: BackingConfig):
        self._backingConfig = value


    class FileSystemInterfaceVersion(Enum):
        NFSV3_0 = "NFSV3_0"


class StorageLun(vmodl.DynamicData):
    @property
    def uuid(self) -> str: ...
    @uuid.setter
    def uuid(self, value: str):
        self._uuid = value
    @property
    def vSphereLunIdentifier(self) -> str: ...
    @vSphereLunIdentifier.setter
    def vSphereLunIdentifier(self, value: str):
        self._vSphereLunIdentifier = value
    @property
    def vendorDisplayName(self) -> str: ...
    @vendorDisplayName.setter
    def vendorDisplayName(self, value: str):
        self._vendorDisplayName = value
    @property
    def capacityInMB(self) -> long: ...
    @capacityInMB.setter
    def capacityInMB(self, value: long):
        self._capacityInMB = value
    @property
    def usedSpaceInMB(self) -> long: ...
    @usedSpaceInMB.setter
    def usedSpaceInMB(self, value: long):
        self._usedSpaceInMB = value
    @property
    def lunThinProvisioned(self) -> bool: ...
    @lunThinProvisioned.setter
    def lunThinProvisioned(self, value: bool):
        self._lunThinProvisioned = value
    @property
    def alternateIdentifier(self) -> List[str]: ...
    @alternateIdentifier.setter
    def alternateIdentifier(self, value: List[str]):
        self._alternateIdentifier = value
    @property
    def drsManagementPermitted(self) -> bool: ...
    @drsManagementPermitted.setter
    def drsManagementPermitted(self, value: bool):
        self._drsManagementPermitted = value
    @property
    def thinProvisioningStatus(self) -> str: ...
    @thinProvisioningStatus.setter
    def thinProvisioningStatus(self, value: str):
        self._thinProvisioningStatus = value
    @property
    def backingConfig(self) -> BackingConfig: ...
    @backingConfig.setter
    def backingConfig(self, value: BackingConfig):
        self._backingConfig = value


class StoragePort(vmodl.DynamicData):
    @property
    def uuid(self) -> str: ...
    @uuid.setter
    def uuid(self, value: str):
        self._uuid = value
    @property
    def type(self) -> str: ...
    @type.setter
    def type(self, value: str):
        self._type = value
    @property
    def alternateName(self) -> List[str]: ...
    @alternateName.setter
    def alternateName(self, value: List[str]):
        self._alternateName = value


class StorageProcessor(vmodl.DynamicData):
    @property
    def uuid(self) -> str: ...
    @uuid.setter
    def uuid(self, value: str):
        self._uuid = value
    @property
    def alternateIdentifer(self) -> List[str]: ...
    @alternateIdentifer.setter
    def alternateIdentifer(self, value: List[str]):
        self._alternateIdentifer = value