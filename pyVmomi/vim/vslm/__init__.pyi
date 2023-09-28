from typing import List
from enum import Enum
from pyVmomi import vim, vmodl
from datetime import datetime
from pyVmomi.VmomiSupport import ManagedObject, long
from . import host as host
from . import vcenter as vcenter


class VStorageObjectManagerBase(ManagedObject):
    def ExtendDiskEx(self, id: ID, datastore: vim.Datastore, newCapacityInMB: long) -> vim.Task: ...
    def RenameVStorageObjectEx(self, id: ID, datastore: vim.Datastore, name: str) -> VClockInfo: ...
    def CreateSnapshotEx(self, id: ID, datastore: vim.Datastore, description: str) -> vim.Task: ...
    def DeleteSnapshotEx(self, id: ID, datastore: vim.Datastore, snapshotId: ID) -> vim.Task: ...
    def RevertVStorageObjectEx(self, id: ID, datastore: vim.Datastore, snapshotId: ID) -> vim.Task: ...


class BaseConfigInfo(vmodl.DynamicData):
    @property
    def id(self) -> ID: ...
    @id.setter
    def id(self, value: ID):
        self._id = value
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def createTime(self) -> datetime: ...
    @createTime.setter
    def createTime(self, value: datetime):
        self._createTime = value
    @property
    def keepAfterDeleteVm(self) -> bool: ...
    @keepAfterDeleteVm.setter
    def keepAfterDeleteVm(self, value: bool):
        self._keepAfterDeleteVm = value
    @property
    def relocationDisabled(self) -> bool: ...
    @relocationDisabled.setter
    def relocationDisabled(self, value: bool):
        self._relocationDisabled = value
    @property
    def nativeSnapshotSupported(self) -> bool: ...
    @nativeSnapshotSupported.setter
    def nativeSnapshotSupported(self, value: bool):
        self._nativeSnapshotSupported = value
    @property
    def changedBlockTrackingEnabled(self) -> bool: ...
    @changedBlockTrackingEnabled.setter
    def changedBlockTrackingEnabled(self, value: bool):
        self._changedBlockTrackingEnabled = value
    @property
    def backing(self) -> BaseConfigInfo.BackingInfo: ...
    @backing.setter
    def backing(self, value: BaseConfigInfo.BackingInfo):
        self._backing = value
    @property
    def metadata(self) -> List[vim.KeyValue]: ...
    @metadata.setter
    def metadata(self, value: List[vim.KeyValue]):
        self._metadata = value
    @property
    def vclock(self) -> VClockInfo: ...
    @vclock.setter
    def vclock(self, value: VClockInfo):
        self._vclock = value
    @property
    def iofilter(self) -> List[str]: ...
    @iofilter.setter
    def iofilter(self, value: List[str]):
        self._iofilter = value


    class BackingInfo(vmodl.DynamicData):
        @property
        def datastore(self) -> vim.Datastore: ...
        @datastore.setter
        def datastore(self, value: vim.Datastore):
            self._datastore = value


    class DiskFileBackingInfo(BaseConfigInfo.FileBackingInfo):
        @property
        def provisioningType(self) -> str: ...
        @provisioningType.setter
        def provisioningType(self, value: str):
            self._provisioningType = value


        class ProvisioningType(Enum):
            thin = "thin"
            eagerZeroedThick = "eagerZeroedThick"
            lazyZeroedThick = "lazyZeroedThick"


    class FileBackingInfo(BaseConfigInfo.BackingInfo):
        @property
        def filePath(self) -> str: ...
        @filePath.setter
        def filePath(self, value: str):
            self._filePath = value
        @property
        def backingObjectId(self) -> str: ...
        @backingObjectId.setter
        def backingObjectId(self, value: str):
            self._backingObjectId = value
        @property
        def parent(self) -> BaseConfigInfo.FileBackingInfo: ...
        @parent.setter
        def parent(self, value: BaseConfigInfo.FileBackingInfo):
            self._parent = value
        @property
        def deltaSizeInMB(self) -> long: ...
        @deltaSizeInMB.setter
        def deltaSizeInMB(self, value: long):
            self._deltaSizeInMB = value
        @property
        def keyId(self) -> vim.encryption.CryptoKeyId: ...
        @keyId.setter
        def keyId(self, value: vim.encryption.CryptoKeyId):
            self._keyId = value


    class RawDiskMappingBackingInfo(BaseConfigInfo.FileBackingInfo):
        @property
        def lunUuid(self) -> str: ...
        @lunUuid.setter
        def lunUuid(self, value: str):
            self._lunUuid = value
        @property
        def compatibilityMode(self) -> str: ...
        @compatibilityMode.setter
        def compatibilityMode(self, value: str):
            self._compatibilityMode = value


class CloneSpec(MigrateSpec):
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def keepAfterDeleteVm(self) -> bool: ...
    @keepAfterDeleteVm.setter
    def keepAfterDeleteVm(self, value: bool):
        self._keepAfterDeleteVm = value
    @property
    def metadata(self) -> List[vim.KeyValue]: ...
    @metadata.setter
    def metadata(self, value: List[vim.KeyValue]):
        self._metadata = value


class CreateSpec(vmodl.DynamicData):
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def keepAfterDeleteVm(self) -> bool: ...
    @keepAfterDeleteVm.setter
    def keepAfterDeleteVm(self, value: bool):
        self._keepAfterDeleteVm = value
    @property
    def backingSpec(self) -> CreateSpec.BackingSpec: ...
    @backingSpec.setter
    def backingSpec(self, value: CreateSpec.BackingSpec):
        self._backingSpec = value
    @property
    def capacityInMB(self) -> long: ...
    @capacityInMB.setter
    def capacityInMB(self, value: long):
        self._capacityInMB = value
    @property
    def profile(self) -> List[vim.vm.ProfileSpec]: ...
    @profile.setter
    def profile(self, value: List[vim.vm.ProfileSpec]):
        self._profile = value
    @property
    def crypto(self) -> vim.encryption.CryptoSpec: ...
    @crypto.setter
    def crypto(self, value: vim.encryption.CryptoSpec):
        self._crypto = value
    @property
    def metadata(self) -> List[vim.KeyValue]: ...
    @metadata.setter
    def metadata(self, value: List[vim.KeyValue]):
        self._metadata = value


    class BackingSpec(vmodl.DynamicData):
        @property
        def datastore(self) -> vim.Datastore: ...
        @datastore.setter
        def datastore(self, value: vim.Datastore):
            self._datastore = value
        @property
        def path(self) -> str: ...
        @path.setter
        def path(self, value: str):
            self._path = value


    class DiskFileBackingSpec(CreateSpec.BackingSpec):
        @property
        def provisioningType(self) -> str: ...
        @provisioningType.setter
        def provisioningType(self, value: str):
            self._provisioningType = value


    class RawDiskMappingBackingSpec(CreateSpec.BackingSpec):
        @property
        def lunUuid(self) -> str: ...
        @lunUuid.setter
        def lunUuid(self, value: str):
            self._lunUuid = value
        @property
        def compatibilityMode(self) -> str: ...
        @compatibilityMode.setter
        def compatibilityMode(self, value: str):
            self._compatibilityMode = value


class DiskCryptoSpec(vmodl.DynamicData):
    @property
    def parent(self) -> DiskCryptoSpec: ...
    @parent.setter
    def parent(self, value: DiskCryptoSpec):
        self._parent = value
    @property
    def crypto(self) -> vim.encryption.CryptoSpec: ...
    @crypto.setter
    def crypto(self, value: vim.encryption.CryptoSpec):
        self._crypto = value


class ID(vmodl.DynamicData):
    @property
    def id(self) -> str: ...
    @id.setter
    def id(self, value: str):
        self._id = value


class InfrastructureObjectPolicy(vmodl.DynamicData):
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def backingObjectId(self) -> str: ...
    @backingObjectId.setter
    def backingObjectId(self, value: str):
        self._backingObjectId = value
    @property
    def profileId(self) -> str: ...
    @profileId.setter
    def profileId(self, value: str):
        self._profileId = value
    @property
    def error(self) -> vmodl.MethodFault: ...
    @error.setter
    def error(self, value: vmodl.MethodFault):
        self._error = value


class InfrastructureObjectPolicySpec(vmodl.DynamicData):
    @property
    def datastore(self) -> vim.Datastore: ...
    @datastore.setter
    def datastore(self, value: vim.Datastore):
        self._datastore = value
    @property
    def profile(self) -> List[vim.vm.ProfileSpec]: ...
    @profile.setter
    def profile(self, value: List[vim.vm.ProfileSpec]):
        self._profile = value


class MigrateSpec(vmodl.DynamicData):
    @property
    def backingSpec(self) -> CreateSpec.BackingSpec: ...
    @backingSpec.setter
    def backingSpec(self, value: CreateSpec.BackingSpec):
        self._backingSpec = value
    @property
    def profile(self) -> List[vim.vm.ProfileSpec]: ...
    @profile.setter
    def profile(self, value: List[vim.vm.ProfileSpec]):
        self._profile = value
    @property
    def consolidate(self) -> bool: ...
    @consolidate.setter
    def consolidate(self, value: bool):
        self._consolidate = value
    @property
    def disksCrypto(self) -> DiskCryptoSpec: ...
    @disksCrypto.setter
    def disksCrypto(self, value: DiskCryptoSpec):
        self._disksCrypto = value


class RelocateSpec(MigrateSpec): ...


class StateInfo(vmodl.DynamicData):
    @property
    def tentative(self) -> bool: ...
    @tentative.setter
    def tentative(self, value: bool):
        self._tentative = value


class TagEntry(vmodl.DynamicData):
    @property
    def tagName(self) -> str: ...
    @tagName.setter
    def tagName(self, value: str):
        self._tagName = value
    @property
    def parentCategoryName(self) -> str: ...
    @parentCategoryName.setter
    def parentCategoryName(self, value: str):
        self._parentCategoryName = value


class VClockInfo(vmodl.DynamicData):
    @property
    def vClockTime(self) -> long: ...
    @vClockTime.setter
    def vClockTime(self, value: long):
        self._vClockTime = value


class VStorageObject(vmodl.DynamicData):
    @property
    def config(self) -> VStorageObject.ConfigInfo: ...
    @config.setter
    def config(self, value: VStorageObject.ConfigInfo):
        self._config = value


    class ConfigInfo(BaseConfigInfo):
        @property
        def descriptorVersion(self) -> int: ...
        @descriptorVersion.setter
        def descriptorVersion(self, value: int):
            self._descriptorVersion = value
        @property
        def capacityInMB(self) -> long: ...
        @capacityInMB.setter
        def capacityInMB(self, value: long):
            self._capacityInMB = value
        @property
        def consumptionType(self) -> List[str]: ...
        @consumptionType.setter
        def consumptionType(self, value: List[str]):
            self._consumptionType = value
        @property
        def consumerId(self) -> List[ID]: ...
        @consumerId.setter
        def consumerId(self, value: List[ID]):
            self._consumerId = value


    class ConsumptionType(Enum):
        disk = "disk"


class VStorageObjectSnapshot(vmodl.DynamicData):
    @property
    def id(self) -> ID: ...
    @id.setter
    def id(self, value: ID):
        self._id = value
    @property
    def vclock(self) -> VClockInfo: ...
    @vclock.setter
    def vclock(self, value: VClockInfo):
        self._vclock = value


class VStorageObjectSnapshotDetails(vmodl.DynamicData):
    @property
    def path(self) -> str: ...
    @path.setter
    def path(self, value: str):
        self._path = value
    @property
    def changedBlockTrackingId(self) -> str: ...
    @changedBlockTrackingId.setter
    def changedBlockTrackingId(self, value: str):
        self._changedBlockTrackingId = value


class VStorageObjectSnapshotInfo(vmodl.DynamicData):
    @property
    def snapshots(self) -> List[VStorageObjectSnapshotInfo.VStorageObjectSnapshot]: ...
    @snapshots.setter
    def snapshots(self, value: List[VStorageObjectSnapshotInfo.VStorageObjectSnapshot]):
        self._snapshots = value


    class VStorageObjectSnapshot(vmodl.DynamicData):
        @property
        def id(self) -> ID: ...
        @id.setter
        def id(self, value: ID):
            self._id = value
        @property
        def backingObjectId(self) -> str: ...
        @backingObjectId.setter
        def backingObjectId(self, value: str):
            self._backingObjectId = value
        @property
        def createTime(self) -> datetime: ...
        @createTime.setter
        def createTime(self, value: datetime):
            self._createTime = value
        @property
        def description(self) -> str: ...
        @description.setter
        def description(self, value: str):
            self._description = value