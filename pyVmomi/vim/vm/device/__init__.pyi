from typing import List, Literal
from enum import Enum
from pyVmomi import vim, vmodl
from pyVmomi.VmomiSupport import PropertyPath, binary, long, short


class HostDiskMappingInfo(vmodl.DynamicData):
    @property
    def physicalPartition(self) -> HostDiskMappingInfo.PartitionInfo: ...
    @physicalPartition.setter
    def physicalPartition(self, value: HostDiskMappingInfo.PartitionInfo):
        self._physicalPartition = value
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def exclusive(self) -> bool: ...
    @exclusive.setter
    def exclusive(self, value: bool):
        self._exclusive = value


    class PartitionInfo(vmodl.DynamicData):
        @property
        def name(self) -> str: ...
        @name.setter
        def name(self, value: str):
            self._name = value
        @property
        def fileSystem(self) -> str: ...
        @fileSystem.setter
        def fileSystem(self, value: str):
            self._fileSystem = value
        @property
        def capacityInKb(self) -> long: ...
        @capacityInKb.setter
        def capacityInKb(self, value: long):
            self._capacityInKb = value


class HostDiskMappingOption(vmodl.DynamicData):
    @property
    def physicalPartition(self) -> List[HostDiskMappingOption.PartitionOption]: ...
    @physicalPartition.setter
    def physicalPartition(self, value: List[HostDiskMappingOption.PartitionOption]):
        self._physicalPartition = value
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value


    class PartitionOption(vmodl.DynamicData):
        @property
        def name(self) -> str: ...
        @name.setter
        def name(self, value: str):
            self._name = value
        @property
        def fileSystem(self) -> str: ...
        @fileSystem.setter
        def fileSystem(self, value: str):
            self._fileSystem = value
        @property
        def capacityInKb(self) -> long: ...
        @capacityInKb.setter
        def capacityInKb(self, value: long):
            self._capacityInKb = value


class ParaVirtualSCSIController(VirtualSCSIController): ...


class ParaVirtualSCSIControllerOption(VirtualSCSIControllerOption): ...


class VirtualAHCIController(VirtualSATAController): ...


class VirtualAHCIControllerOption(VirtualSATAControllerOption): ...


class VirtualBusLogicController(VirtualSCSIController): ...


class VirtualBusLogicControllerOption(VirtualSCSIControllerOption): ...


class VirtualCdrom(VirtualDevice):


    class AtapiBackingInfo(VirtualDevice.DeviceBackingInfo): ...


    class IsoBackingInfo(VirtualDevice.FileBackingInfo): ...


    class PassthroughBackingInfo(VirtualDevice.DeviceBackingInfo):
        @property
        def exclusive(self) -> bool: ...
        @exclusive.setter
        def exclusive(self, value: bool):
            self._exclusive = value


    class RemoteAtapiBackingInfo(VirtualDevice.RemoteDeviceBackingInfo): ...


    class RemotePassthroughBackingInfo(VirtualDevice.RemoteDeviceBackingInfo):
        @property
        def exclusive(self) -> bool: ...
        @exclusive.setter
        def exclusive(self, value: bool):
            self._exclusive = value


class VirtualCdromOption(VirtualDeviceOption):


    class AtapiBackingOption(VirtualDeviceOption.DeviceBackingOption): ...


    class IsoBackingOption(VirtualDeviceOption.FileBackingOption): ...


    class PassthroughBackingOption(VirtualDeviceOption.DeviceBackingOption):
        @property
        def exclusive(self) -> vim.option.BoolOption: ...
        @exclusive.setter
        def exclusive(self, value: vim.option.BoolOption):
            self._exclusive = value


    class RemoteAtapiBackingOption(VirtualDeviceOption.DeviceBackingOption): ...


    class RemotePassthroughBackingOption(VirtualDeviceOption.RemoteDeviceBackingOption):
        @property
        def exclusive(self) -> vim.option.BoolOption: ...
        @exclusive.setter
        def exclusive(self, value: vim.option.BoolOption):
            self._exclusive = value


class VirtualController(VirtualDevice):
    @property
    def busNumber(self) -> int: ...
    @busNumber.setter
    def busNumber(self, value: int):
        self._busNumber = value
    @property
    def device(self) -> List[int]: ...
    @device.setter
    def device(self, value: List[int]):
        self._device = value


class VirtualControllerOption(VirtualDeviceOption):
    @property
    def devices(self) -> vim.option.IntOption: ...
    @devices.setter
    def devices(self, value: vim.option.IntOption):
        self._devices = value
    @property
    def supportedDevice(self) -> List[type]: ...
    @supportedDevice.setter
    def supportedDevice(self, value: List[type]):
        self._supportedDevice = value


class VirtualDevice(vmodl.DynamicData):
    @property
    def key(self) -> int: ...
    @key.setter
    def key(self, value: int):
        self._key = value
    @property
    def deviceInfo(self) -> vim.Description: ...
    @deviceInfo.setter
    def deviceInfo(self, value: vim.Description):
        self._deviceInfo = value
    @property
    def backing(self) -> VirtualDevice.BackingInfo: ...
    @backing.setter
    def backing(self, value: VirtualDevice.BackingInfo):
        self._backing = value
    @property
    def connectable(self) -> VirtualDevice.ConnectInfo: ...
    @connectable.setter
    def connectable(self, value: VirtualDevice.ConnectInfo):
        self._connectable = value
    @property
    def slotInfo(self) -> VirtualDevice.BusSlotInfo: ...
    @slotInfo.setter
    def slotInfo(self, value: VirtualDevice.BusSlotInfo):
        self._slotInfo = value
    @property
    def controllerKey(self) -> int: ...
    @controllerKey.setter
    def controllerKey(self, value: int):
        self._controllerKey = value
    @property
    def unitNumber(self) -> int: ...
    @unitNumber.setter
    def unitNumber(self, value: int):
        self._unitNumber = value
    @property
    def numaNode(self) -> int: ...
    @numaNode.setter
    def numaNode(self, value: int):
        self._numaNode = value
    @property
    def deviceGroupInfo(self) -> VirtualDevice.DeviceGroupInfo: ...
    @deviceGroupInfo.setter
    def deviceGroupInfo(self, value: VirtualDevice.DeviceGroupInfo):
        self._deviceGroupInfo = value


    class BackingInfo(vmodl.DynamicData): ...


    class BusSlotInfo(vmodl.DynamicData): ...


    class ConnectInfo(vmodl.DynamicData):
        @property
        def migrateConnect(self) -> str: ...
        @migrateConnect.setter
        def migrateConnect(self, value: str):
            self._migrateConnect = value
        @property
        def startConnected(self) -> bool: ...
        @startConnected.setter
        def startConnected(self, value: bool):
            self._startConnected = value
        @property
        def allowGuestControl(self) -> bool: ...
        @allowGuestControl.setter
        def allowGuestControl(self, value: bool):
            self._allowGuestControl = value
        @property
        def connected(self) -> bool: ...
        @connected.setter
        def connected(self, value: bool):
            self._connected = value
        @property
        def status(self) -> str: ...
        @status.setter
        def status(self, value: str):
            self._status = value


        class MigrateConnectOp(Enum):
            connect = "connect"
            disconnect = "disconnect"
            unset = "unset"


        class Status(Enum):
            ok = "ok"
            recoverableError = "recoverableError"
            unrecoverableError = "unrecoverableError"
            untried = "untried"


    class DeviceBackingInfo(VirtualDevice.BackingInfo):
        @property
        def deviceName(self) -> str: ...
        @deviceName.setter
        def deviceName(self, value: str):
            self._deviceName = value
        @property
        def useAutoDetect(self) -> bool: ...
        @useAutoDetect.setter
        def useAutoDetect(self, value: bool):
            self._useAutoDetect = value


    class DeviceGroupInfo(vmodl.DynamicData):
        @property
        def groupInstanceKey(self) -> int: ...
        @groupInstanceKey.setter
        def groupInstanceKey(self, value: int):
            self._groupInstanceKey = value
        @property
        def sequenceId(self) -> int: ...
        @sequenceId.setter
        def sequenceId(self, value: int):
            self._sequenceId = value


    class FileBackingInfo(VirtualDevice.BackingInfo):
        @property
        def fileName(self) -> str: ...
        @fileName.setter
        def fileName(self, value: str):
            self._fileName = value
        @property
        def datastore(self) -> vim.Datastore: ...
        @datastore.setter
        def datastore(self, value: vim.Datastore):
            self._datastore = value
        @property
        def backingObjectId(self) -> str: ...
        @backingObjectId.setter
        def backingObjectId(self, value: str):
            self._backingObjectId = value


    class PciBusSlotInfo(VirtualDevice.BusSlotInfo):
        @property
        def pciSlotNumber(self) -> int: ...
        @pciSlotNumber.setter
        def pciSlotNumber(self, value: int):
            self._pciSlotNumber = value


    class PipeBackingInfo(VirtualDevice.BackingInfo):
        @property
        def pipeName(self) -> str: ...
        @pipeName.setter
        def pipeName(self, value: str):
            self._pipeName = value


    class RemoteDeviceBackingInfo(VirtualDevice.BackingInfo):
        @property
        def deviceName(self) -> str: ...
        @deviceName.setter
        def deviceName(self, value: str):
            self._deviceName = value
        @property
        def useAutoDetect(self) -> bool: ...
        @useAutoDetect.setter
        def useAutoDetect(self, value: bool):
            self._useAutoDetect = value


    class URIBackingInfo(VirtualDevice.BackingInfo):
        @property
        def serviceURI(self) -> str: ...
        @serviceURI.setter
        def serviceURI(self, value: str):
            self._serviceURI = value
        @property
        def direction(self) -> str: ...
        @direction.setter
        def direction(self, value: str):
            self._direction = value
        @property
        def proxyURI(self) -> str: ...
        @proxyURI.setter
        def proxyURI(self, value: str):
            self._proxyURI = value


class VirtualDeviceOption(vmodl.DynamicData):
    @property
    def type(self) -> type: ...
    @type.setter
    def type(self, value: type):
        self._type = value
    @property
    def connectOption(self) -> VirtualDeviceOption.ConnectOption: ...
    @connectOption.setter
    def connectOption(self, value: VirtualDeviceOption.ConnectOption):
        self._connectOption = value
    @property
    def busSlotOption(self) -> VirtualDeviceOption.BusSlotOption: ...
    @busSlotOption.setter
    def busSlotOption(self, value: VirtualDeviceOption.BusSlotOption):
        self._busSlotOption = value
    @property
    def controllerType(self) -> type: ...
    @controllerType.setter
    def controllerType(self, value: type):
        self._controllerType = value
    @property
    def autoAssignController(self) -> vim.option.BoolOption: ...
    @autoAssignController.setter
    def autoAssignController(self, value: vim.option.BoolOption):
        self._autoAssignController = value
    @property
    def backingOption(self) -> List[VirtualDeviceOption.BackingOption]: ...
    @backingOption.setter
    def backingOption(self, value: List[VirtualDeviceOption.BackingOption]):
        self._backingOption = value
    @property
    def defaultBackingOptionIndex(self) -> int: ...
    @defaultBackingOptionIndex.setter
    def defaultBackingOptionIndex(self, value: int):
        self._defaultBackingOptionIndex = value
    @property
    def licensingLimit(self) -> List[PropertyPath]: ...
    @licensingLimit.setter
    def licensingLimit(self, value: List[PropertyPath]):
        self._licensingLimit = value
    @property
    def deprecated(self) -> bool: ...
    @deprecated.setter
    def deprecated(self, value: bool):
        self._deprecated = value
    @property
    def plugAndPlay(self) -> bool: ...
    @plugAndPlay.setter
    def plugAndPlay(self, value: bool):
        self._plugAndPlay = value
    @property
    def hotRemoveSupported(self) -> bool: ...
    @hotRemoveSupported.setter
    def hotRemoveSupported(self, value: bool):
        self._hotRemoveSupported = value
    @property
    def numaSupported(self) -> bool: ...
    @numaSupported.setter
    def numaSupported(self, value: bool):
        self._numaSupported = value


    class BackingOption(vmodl.DynamicData):
        @property
        def type(self) -> type: ...
        @type.setter
        def type(self, value: type):
            self._type = value


    class BusSlotOption(vmodl.DynamicData):
        @property
        def type(self) -> type: ...
        @type.setter
        def type(self, value: type):
            self._type = value


    class ConnectOption(vmodl.DynamicData):
        @property
        def startConnected(self) -> vim.option.BoolOption: ...
        @startConnected.setter
        def startConnected(self, value: vim.option.BoolOption):
            self._startConnected = value
        @property
        def allowGuestControl(self) -> vim.option.BoolOption: ...
        @allowGuestControl.setter
        def allowGuestControl(self, value: vim.option.BoolOption):
            self._allowGuestControl = value


    class DeviceBackingOption(VirtualDeviceOption.BackingOption):
        @property
        def autoDetectAvailable(self) -> vim.option.BoolOption: ...
        @autoDetectAvailable.setter
        def autoDetectAvailable(self, value: vim.option.BoolOption):
            self._autoDetectAvailable = value


    class FileBackingOption(VirtualDeviceOption.BackingOption):
        @property
        def fileNameExtensions(self) -> vim.option.ChoiceOption: ...
        @fileNameExtensions.setter
        def fileNameExtensions(self, value: vim.option.ChoiceOption):
            self._fileNameExtensions = value


        class FileExtension(Enum):
            iso = "iso"
            flp = "flp"
            vmdk = "vmdk"
            dsk = "dsk"
            rdm = "rdm"


    class PipeBackingOption(VirtualDeviceOption.BackingOption): ...


    class RemoteDeviceBackingOption(VirtualDeviceOption.BackingOption):
        @property
        def autoDetectAvailable(self) -> vim.option.BoolOption: ...
        @autoDetectAvailable.setter
        def autoDetectAvailable(self, value: vim.option.BoolOption):
            self._autoDetectAvailable = value


    class URIBackingOption(VirtualDeviceOption.BackingOption):
        @property
        def directions(self) -> vim.option.ChoiceOption: ...
        @directions.setter
        def directions(self, value: vim.option.ChoiceOption):
            self._directions = value


        class Direction(Enum):
            server = "server"
            client = "client"


class VirtualDeviceSpec(vmodl.DynamicData):
    @property
    def operation(self) -> VirtualDeviceSpec.Operation | Literal['add', 'remove', 'edit']: ...
    @operation.setter
    def operation(self, value: VirtualDeviceSpec.Operation | Literal['add', 'remove', 'edit']):
        self._operation = value
    @property
    def fileOperation(self) -> VirtualDeviceSpec.FileOperation | Literal['create', 'destroy', 'replace']: ...
    @fileOperation.setter
    def fileOperation(self, value: VirtualDeviceSpec.FileOperation | Literal['create', 'destroy', 'replace']):
        self._fileOperation = value
    @property
    def device(self) -> VirtualDevice: ...
    @device.setter
    def device(self, value: VirtualDevice):
        self._device = value
    @property
    def profile(self) -> List[vim.vm.ProfileSpec]: ...
    @profile.setter
    def profile(self, value: List[vim.vm.ProfileSpec]):
        self._profile = value
    @property
    def backing(self) -> VirtualDeviceSpec.BackingSpec: ...
    @backing.setter
    def backing(self, value: VirtualDeviceSpec.BackingSpec):
        self._backing = value
    @property
    def filterSpec(self) -> List[vim.vm.BaseIndependentFilterSpec]: ...
    @filterSpec.setter
    def filterSpec(self, value: List[vim.vm.BaseIndependentFilterSpec]):
        self._filterSpec = value
    @property
    def changeMode(self) -> str: ...
    @changeMode.setter
    def changeMode(self, value: str):
        self._changeMode = value


    class BackingSpec(vmodl.DynamicData):
        @property
        def parent(self) -> VirtualDeviceSpec.BackingSpec: ...
        @parent.setter
        def parent(self, value: VirtualDeviceSpec.BackingSpec):
            self._parent = value
        @property
        def crypto(self) -> vim.encryption.CryptoSpec: ...
        @crypto.setter
        def crypto(self, value: vim.encryption.CryptoSpec):
            self._crypto = value


    class ChangeMode(Enum):
        fail = "fail"
        skip = "skip"


    class FileOperation(Enum):
        create = "create"
        destroy = "destroy"
        replace = "replace"


    class Operation(Enum):
        add = "add"
        remove = "remove"
        edit = "edit"


class VirtualDisk(VirtualDevice):
    @property
    def capacityInKB(self) -> long: ...
    @capacityInKB.setter
    def capacityInKB(self, value: long):
        self._capacityInKB = value
    @property
    def capacityInBytes(self) -> long: ...
    @capacityInBytes.setter
    def capacityInBytes(self, value: long):
        self._capacityInBytes = value
    @property
    def shares(self) -> vim.SharesInfo: ...
    @shares.setter
    def shares(self, value: vim.SharesInfo):
        self._shares = value
    @property
    def storageIOAllocation(self) -> vim.StorageResourceManager.IOAllocationInfo: ...
    @storageIOAllocation.setter
    def storageIOAllocation(self, value: vim.StorageResourceManager.IOAllocationInfo):
        self._storageIOAllocation = value
    @property
    def diskObjectId(self) -> str: ...
    @diskObjectId.setter
    def diskObjectId(self, value: str):
        self._diskObjectId = value
    @property
    def vFlashCacheConfigInfo(self) -> VirtualDisk.VFlashCacheConfigInfo: ...
    @vFlashCacheConfigInfo.setter
    def vFlashCacheConfigInfo(self, value: VirtualDisk.VFlashCacheConfigInfo):
        self._vFlashCacheConfigInfo = value
    @property
    def iofilter(self) -> List[str]: ...
    @iofilter.setter
    def iofilter(self, value: List[str]):
        self._iofilter = value
    @property
    def vDiskId(self) -> vim.vslm.ID: ...
    @vDiskId.setter
    def vDiskId(self, value: vim.vslm.ID):
        self._vDiskId = value
    @property
    def vDiskVersion(self) -> int: ...
    @vDiskVersion.setter
    def vDiskVersion(self, value: int):
        self._vDiskVersion = value
    @property
    def nativeUnmanagedLinkedClone(self) -> bool: ...
    @nativeUnmanagedLinkedClone.setter
    def nativeUnmanagedLinkedClone(self, value: bool):
        self._nativeUnmanagedLinkedClone = value
    @property
    def independentFilters(self) -> List[vim.vm.BaseIndependentFilterSpec]: ...
    @independentFilters.setter
    def independentFilters(self, value: List[vim.vm.BaseIndependentFilterSpec]):
        self._independentFilters = value
    @property
    def guestReadOnly(self) -> bool: ...
    @guestReadOnly.setter
    def guestReadOnly(self, value: bool):
        self._guestReadOnly = value


    class FlatVer1BackingInfo(VirtualDevice.FileBackingInfo):
        @property
        def diskMode(self) -> str: ...
        @diskMode.setter
        def diskMode(self, value: str):
            self._diskMode = value
        @property
        def split(self) -> bool: ...
        @split.setter
        def split(self, value: bool):
            self._split = value
        @property
        def writeThrough(self) -> bool: ...
        @writeThrough.setter
        def writeThrough(self, value: bool):
            self._writeThrough = value
        @property
        def contentId(self) -> str: ...
        @contentId.setter
        def contentId(self, value: str):
            self._contentId = value
        @property
        def parent(self) -> VirtualDisk.FlatVer1BackingInfo: ...
        @parent.setter
        def parent(self, value: VirtualDisk.FlatVer1BackingInfo):
            self._parent = value


    class FlatVer2BackingInfo(VirtualDevice.FileBackingInfo):
        @property
        def diskMode(self) -> str: ...
        @diskMode.setter
        def diskMode(self, value: str):
            self._diskMode = value
        @property
        def split(self) -> bool: ...
        @split.setter
        def split(self, value: bool):
            self._split = value
        @property
        def writeThrough(self) -> bool: ...
        @writeThrough.setter
        def writeThrough(self, value: bool):
            self._writeThrough = value
        @property
        def thinProvisioned(self) -> bool: ...
        @thinProvisioned.setter
        def thinProvisioned(self, value: bool):
            self._thinProvisioned = value
        @property
        def eagerlyScrub(self) -> bool: ...
        @eagerlyScrub.setter
        def eagerlyScrub(self, value: bool):
            self._eagerlyScrub = value
        @property
        def uuid(self) -> str: ...
        @uuid.setter
        def uuid(self, value: str):
            self._uuid = value
        @property
        def contentId(self) -> str: ...
        @contentId.setter
        def contentId(self, value: str):
            self._contentId = value
        @property
        def changeId(self) -> str: ...
        @changeId.setter
        def changeId(self, value: str):
            self._changeId = value
        @property
        def parent(self) -> VirtualDisk.FlatVer2BackingInfo: ...
        @parent.setter
        def parent(self, value: VirtualDisk.FlatVer2BackingInfo):
            self._parent = value
        @property
        def deltaDiskFormat(self) -> str: ...
        @deltaDiskFormat.setter
        def deltaDiskFormat(self, value: str):
            self._deltaDiskFormat = value
        @property
        def digestEnabled(self) -> bool: ...
        @digestEnabled.setter
        def digestEnabled(self, value: bool):
            self._digestEnabled = value
        @property
        def deltaGrainSize(self) -> int: ...
        @deltaGrainSize.setter
        def deltaGrainSize(self, value: int):
            self._deltaGrainSize = value
        @property
        def deltaDiskFormatVariant(self) -> str: ...
        @deltaDiskFormatVariant.setter
        def deltaDiskFormatVariant(self, value: str):
            self._deltaDiskFormatVariant = value
        @property
        def sharing(self) -> str: ...
        @sharing.setter
        def sharing(self, value: str):
            self._sharing = value
        @property
        def keyId(self) -> vim.encryption.CryptoKeyId: ...
        @keyId.setter
        def keyId(self, value: vim.encryption.CryptoKeyId):
            self._keyId = value


    class LocalPMemBackingInfo(VirtualDevice.FileBackingInfo):
        @property
        def diskMode(self) -> str: ...
        @diskMode.setter
        def diskMode(self, value: str):
            self._diskMode = value
        @property
        def uuid(self) -> str: ...
        @uuid.setter
        def uuid(self, value: str):
            self._uuid = value
        @property
        def volumeUUID(self) -> str: ...
        @volumeUUID.setter
        def volumeUUID(self, value: str):
            self._volumeUUID = value
        @property
        def contentId(self) -> str: ...
        @contentId.setter
        def contentId(self, value: str):
            self._contentId = value


    class PartitionedRawDiskVer2BackingInfo(VirtualDisk.RawDiskVer2BackingInfo):
        @property
        def partition(self) -> List[int]: ...
        @partition.setter
        def partition(self, value: List[int]):
            self._partition = value


    class RawDiskMappingVer1BackingInfo(VirtualDevice.FileBackingInfo):
        @property
        def lunUuid(self) -> str: ...
        @lunUuid.setter
        def lunUuid(self, value: str):
            self._lunUuid = value
        @property
        def deviceName(self) -> str: ...
        @deviceName.setter
        def deviceName(self, value: str):
            self._deviceName = value
        @property
        def compatibilityMode(self) -> str: ...
        @compatibilityMode.setter
        def compatibilityMode(self, value: str):
            self._compatibilityMode = value
        @property
        def diskMode(self) -> str: ...
        @diskMode.setter
        def diskMode(self, value: str):
            self._diskMode = value
        @property
        def uuid(self) -> str: ...
        @uuid.setter
        def uuid(self, value: str):
            self._uuid = value
        @property
        def contentId(self) -> str: ...
        @contentId.setter
        def contentId(self, value: str):
            self._contentId = value
        @property
        def changeId(self) -> str: ...
        @changeId.setter
        def changeId(self, value: str):
            self._changeId = value
        @property
        def parent(self) -> VirtualDisk.RawDiskMappingVer1BackingInfo: ...
        @parent.setter
        def parent(self, value: VirtualDisk.RawDiskMappingVer1BackingInfo):
            self._parent = value
        @property
        def deltaDiskFormat(self) -> str: ...
        @deltaDiskFormat.setter
        def deltaDiskFormat(self, value: str):
            self._deltaDiskFormat = value
        @property
        def deltaGrainSize(self) -> int: ...
        @deltaGrainSize.setter
        def deltaGrainSize(self, value: int):
            self._deltaGrainSize = value
        @property
        def sharing(self) -> str: ...
        @sharing.setter
        def sharing(self, value: str):
            self._sharing = value


    class RawDiskVer2BackingInfo(VirtualDevice.DeviceBackingInfo):
        @property
        def descriptorFileName(self) -> str: ...
        @descriptorFileName.setter
        def descriptorFileName(self, value: str):
            self._descriptorFileName = value
        @property
        def uuid(self) -> str: ...
        @uuid.setter
        def uuid(self, value: str):
            self._uuid = value
        @property
        def changeId(self) -> str: ...
        @changeId.setter
        def changeId(self, value: str):
            self._changeId = value
        @property
        def sharing(self) -> str: ...
        @sharing.setter
        def sharing(self, value: str):
            self._sharing = value


    class SeSparseBackingInfo(VirtualDevice.FileBackingInfo):
        @property
        def diskMode(self) -> str: ...
        @diskMode.setter
        def diskMode(self, value: str):
            self._diskMode = value
        @property
        def writeThrough(self) -> bool: ...
        @writeThrough.setter
        def writeThrough(self, value: bool):
            self._writeThrough = value
        @property
        def uuid(self) -> str: ...
        @uuid.setter
        def uuid(self, value: str):
            self._uuid = value
        @property
        def contentId(self) -> str: ...
        @contentId.setter
        def contentId(self, value: str):
            self._contentId = value
        @property
        def changeId(self) -> str: ...
        @changeId.setter
        def changeId(self, value: str):
            self._changeId = value
        @property
        def parent(self) -> VirtualDisk.SeSparseBackingInfo: ...
        @parent.setter
        def parent(self, value: VirtualDisk.SeSparseBackingInfo):
            self._parent = value
        @property
        def deltaDiskFormat(self) -> str: ...
        @deltaDiskFormat.setter
        def deltaDiskFormat(self, value: str):
            self._deltaDiskFormat = value
        @property
        def digestEnabled(self) -> bool: ...
        @digestEnabled.setter
        def digestEnabled(self, value: bool):
            self._digestEnabled = value
        @property
        def grainSize(self) -> int: ...
        @grainSize.setter
        def grainSize(self, value: int):
            self._grainSize = value
        @property
        def keyId(self) -> vim.encryption.CryptoKeyId: ...
        @keyId.setter
        def keyId(self, value: vim.encryption.CryptoKeyId):
            self._keyId = value


    class SparseVer1BackingInfo(VirtualDevice.FileBackingInfo):
        @property
        def diskMode(self) -> str: ...
        @diskMode.setter
        def diskMode(self, value: str):
            self._diskMode = value
        @property
        def split(self) -> bool: ...
        @split.setter
        def split(self, value: bool):
            self._split = value
        @property
        def writeThrough(self) -> bool: ...
        @writeThrough.setter
        def writeThrough(self, value: bool):
            self._writeThrough = value
        @property
        def spaceUsedInKB(self) -> long: ...
        @spaceUsedInKB.setter
        def spaceUsedInKB(self, value: long):
            self._spaceUsedInKB = value
        @property
        def contentId(self) -> str: ...
        @contentId.setter
        def contentId(self, value: str):
            self._contentId = value
        @property
        def parent(self) -> VirtualDisk.SparseVer1BackingInfo: ...
        @parent.setter
        def parent(self, value: VirtualDisk.SparseVer1BackingInfo):
            self._parent = value


    class SparseVer2BackingInfo(VirtualDevice.FileBackingInfo):
        @property
        def diskMode(self) -> str: ...
        @diskMode.setter
        def diskMode(self, value: str):
            self._diskMode = value
        @property
        def split(self) -> bool: ...
        @split.setter
        def split(self, value: bool):
            self._split = value
        @property
        def writeThrough(self) -> bool: ...
        @writeThrough.setter
        def writeThrough(self, value: bool):
            self._writeThrough = value
        @property
        def spaceUsedInKB(self) -> long: ...
        @spaceUsedInKB.setter
        def spaceUsedInKB(self, value: long):
            self._spaceUsedInKB = value
        @property
        def uuid(self) -> str: ...
        @uuid.setter
        def uuid(self, value: str):
            self._uuid = value
        @property
        def contentId(self) -> str: ...
        @contentId.setter
        def contentId(self, value: str):
            self._contentId = value
        @property
        def changeId(self) -> str: ...
        @changeId.setter
        def changeId(self, value: str):
            self._changeId = value
        @property
        def parent(self) -> VirtualDisk.SparseVer2BackingInfo: ...
        @parent.setter
        def parent(self, value: VirtualDisk.SparseVer2BackingInfo):
            self._parent = value
        @property
        def keyId(self) -> vim.encryption.CryptoKeyId: ...
        @keyId.setter
        def keyId(self, value: vim.encryption.CryptoKeyId):
            self._keyId = value


    class VFlashCacheConfigInfo(vmodl.DynamicData):
        @property
        def vFlashModule(self) -> str: ...
        @vFlashModule.setter
        def vFlashModule(self, value: str):
            self._vFlashModule = value
        @property
        def reservationInMB(self) -> long: ...
        @reservationInMB.setter
        def reservationInMB(self, value: long):
            self._reservationInMB = value
        @property
        def cacheConsistencyType(self) -> str: ...
        @cacheConsistencyType.setter
        def cacheConsistencyType(self, value: str):
            self._cacheConsistencyType = value
        @property
        def cacheMode(self) -> str: ...
        @cacheMode.setter
        def cacheMode(self, value: str):
            self._cacheMode = value
        @property
        def blockSizeInKB(self) -> long: ...
        @blockSizeInKB.setter
        def blockSizeInKB(self, value: long):
            self._blockSizeInKB = value


        class CacheConsistencyType(Enum):
            strong = "strong"
            weak = "weak"


        class CacheMode(Enum):
            write_thru = "write_thru"
            write_back = "write_back"


    class DeltaDiskFormat(Enum):
        redoLogFormat = "redoLogFormat"
        nativeFormat = "nativeFormat"
        seSparseFormat = "seSparseFormat"


    class DeltaDiskFormatVariant(Enum):
        vmfsSparseVariant = "vmfsSparseVariant"
        vsanSparseVariant = "vsanSparseVariant"


    class Sharing(Enum):
        sharingNone = "sharingNone"
        sharingMultiWriter = "sharingMultiWriter"


class VirtualDiskId(vmodl.DynamicData):
    @property
    def vm(self) -> vim.VirtualMachine: ...
    @vm.setter
    def vm(self, value: vim.VirtualMachine):
        self._vm = value
    @property
    def diskId(self) -> int: ...
    @diskId.setter
    def diskId(self, value: int):
        self._diskId = value


class VirtualDiskOption(VirtualDeviceOption):
    @property
    def capacityInKB(self) -> vim.option.LongOption: ...
    @capacityInKB.setter
    def capacityInKB(self, value: vim.option.LongOption):
        self._capacityInKB = value
    @property
    def ioAllocationOption(self) -> vim.StorageResourceManager.IOAllocationOption: ...
    @ioAllocationOption.setter
    def ioAllocationOption(self, value: vim.StorageResourceManager.IOAllocationOption):
        self._ioAllocationOption = value
    @property
    def vFlashCacheConfigOption(self) -> VirtualDiskOption.VFlashCacheConfigOption: ...
    @vFlashCacheConfigOption.setter
    def vFlashCacheConfigOption(self, value: VirtualDiskOption.VFlashCacheConfigOption):
        self._vFlashCacheConfigOption = value


    class DeltaDiskFormatsSupported(vmodl.DynamicData):
        @property
        def datastoreType(self) -> type: ...
        @datastoreType.setter
        def datastoreType(self, value: type):
            self._datastoreType = value
        @property
        def deltaDiskFormat(self) -> vim.option.ChoiceOption: ...
        @deltaDiskFormat.setter
        def deltaDiskFormat(self, value: vim.option.ChoiceOption):
            self._deltaDiskFormat = value


    class FlatVer1BackingOption(VirtualDeviceOption.FileBackingOption):
        @property
        def diskMode(self) -> vim.option.ChoiceOption: ...
        @diskMode.setter
        def diskMode(self, value: vim.option.ChoiceOption):
            self._diskMode = value
        @property
        def split(self) -> vim.option.BoolOption: ...
        @split.setter
        def split(self, value: vim.option.BoolOption):
            self._split = value
        @property
        def writeThrough(self) -> vim.option.BoolOption: ...
        @writeThrough.setter
        def writeThrough(self, value: vim.option.BoolOption):
            self._writeThrough = value
        @property
        def growable(self) -> bool: ...
        @growable.setter
        def growable(self, value: bool):
            self._growable = value


    class FlatVer2BackingOption(VirtualDeviceOption.FileBackingOption):
        @property
        def diskMode(self) -> vim.option.ChoiceOption: ...
        @diskMode.setter
        def diskMode(self, value: vim.option.ChoiceOption):
            self._diskMode = value
        @property
        def split(self) -> vim.option.BoolOption: ...
        @split.setter
        def split(self, value: vim.option.BoolOption):
            self._split = value
        @property
        def writeThrough(self) -> vim.option.BoolOption: ...
        @writeThrough.setter
        def writeThrough(self, value: vim.option.BoolOption):
            self._writeThrough = value
        @property
        def growable(self) -> bool: ...
        @growable.setter
        def growable(self, value: bool):
            self._growable = value
        @property
        def hotGrowable(self) -> bool: ...
        @hotGrowable.setter
        def hotGrowable(self, value: bool):
            self._hotGrowable = value
        @property
        def uuid(self) -> bool: ...
        @uuid.setter
        def uuid(self, value: bool):
            self._uuid = value
        @property
        def thinProvisioned(self) -> vim.option.BoolOption: ...
        @thinProvisioned.setter
        def thinProvisioned(self, value: vim.option.BoolOption):
            self._thinProvisioned = value
        @property
        def eagerlyScrub(self) -> vim.option.BoolOption: ...
        @eagerlyScrub.setter
        def eagerlyScrub(self, value: vim.option.BoolOption):
            self._eagerlyScrub = value
        @property
        def deltaDiskFormat(self) -> vim.option.ChoiceOption: ...
        @deltaDiskFormat.setter
        def deltaDiskFormat(self, value: vim.option.ChoiceOption):
            self._deltaDiskFormat = value
        @property
        def deltaDiskFormatsSupported(self) -> List[VirtualDiskOption.DeltaDiskFormatsSupported]: ...
        @deltaDiskFormatsSupported.setter
        def deltaDiskFormatsSupported(self, value: List[VirtualDiskOption.DeltaDiskFormatsSupported]):
            self._deltaDiskFormatsSupported = value


    class LocalPMemBackingOption(VirtualDeviceOption.FileBackingOption):
        @property
        def diskMode(self) -> vim.option.ChoiceOption: ...
        @diskMode.setter
        def diskMode(self, value: vim.option.ChoiceOption):
            self._diskMode = value
        @property
        def growable(self) -> bool: ...
        @growable.setter
        def growable(self, value: bool):
            self._growable = value
        @property
        def hotGrowable(self) -> bool: ...
        @hotGrowable.setter
        def hotGrowable(self, value: bool):
            self._hotGrowable = value
        @property
        def uuid(self) -> bool: ...
        @uuid.setter
        def uuid(self, value: bool):
            self._uuid = value


    class PartitionedRawDiskVer2BackingOption(VirtualDiskOption.RawDiskVer2BackingOption): ...


    class RawDiskMappingVer1BackingOption(VirtualDeviceOption.DeviceBackingOption):
        @property
        def descriptorFileNameExtensions(self) -> vim.option.ChoiceOption: ...
        @descriptorFileNameExtensions.setter
        def descriptorFileNameExtensions(self, value: vim.option.ChoiceOption):
            self._descriptorFileNameExtensions = value
        @property
        def compatibilityMode(self) -> vim.option.ChoiceOption: ...
        @compatibilityMode.setter
        def compatibilityMode(self, value: vim.option.ChoiceOption):
            self._compatibilityMode = value
        @property
        def diskMode(self) -> vim.option.ChoiceOption: ...
        @diskMode.setter
        def diskMode(self, value: vim.option.ChoiceOption):
            self._diskMode = value
        @property
        def uuid(self) -> bool: ...
        @uuid.setter
        def uuid(self, value: bool):
            self._uuid = value


    class RawDiskVer2BackingOption(VirtualDeviceOption.DeviceBackingOption):
        @property
        def descriptorFileNameExtensions(self) -> vim.option.ChoiceOption: ...
        @descriptorFileNameExtensions.setter
        def descriptorFileNameExtensions(self, value: vim.option.ChoiceOption):
            self._descriptorFileNameExtensions = value
        @property
        def uuid(self) -> bool: ...
        @uuid.setter
        def uuid(self, value: bool):
            self._uuid = value


    class SeSparseBackingOption(VirtualDeviceOption.FileBackingOption):
        @property
        def diskMode(self) -> vim.option.ChoiceOption: ...
        @diskMode.setter
        def diskMode(self, value: vim.option.ChoiceOption):
            self._diskMode = value
        @property
        def writeThrough(self) -> vim.option.BoolOption: ...
        @writeThrough.setter
        def writeThrough(self, value: vim.option.BoolOption):
            self._writeThrough = value
        @property
        def growable(self) -> bool: ...
        @growable.setter
        def growable(self, value: bool):
            self._growable = value
        @property
        def hotGrowable(self) -> bool: ...
        @hotGrowable.setter
        def hotGrowable(self, value: bool):
            self._hotGrowable = value
        @property
        def uuid(self) -> bool: ...
        @uuid.setter
        def uuid(self, value: bool):
            self._uuid = value
        @property
        def deltaDiskFormatsSupported(self) -> List[VirtualDiskOption.DeltaDiskFormatsSupported]: ...
        @deltaDiskFormatsSupported.setter
        def deltaDiskFormatsSupported(self, value: List[VirtualDiskOption.DeltaDiskFormatsSupported]):
            self._deltaDiskFormatsSupported = value


    class SparseVer1BackingOption(VirtualDeviceOption.FileBackingOption):
        @property
        def diskModes(self) -> vim.option.ChoiceOption: ...
        @diskModes.setter
        def diskModes(self, value: vim.option.ChoiceOption):
            self._diskModes = value
        @property
        def split(self) -> vim.option.BoolOption: ...
        @split.setter
        def split(self, value: vim.option.BoolOption):
            self._split = value
        @property
        def writeThrough(self) -> vim.option.BoolOption: ...
        @writeThrough.setter
        def writeThrough(self, value: vim.option.BoolOption):
            self._writeThrough = value
        @property
        def growable(self) -> bool: ...
        @growable.setter
        def growable(self, value: bool):
            self._growable = value


    class SparseVer2BackingOption(VirtualDeviceOption.FileBackingOption):
        @property
        def diskMode(self) -> vim.option.ChoiceOption: ...
        @diskMode.setter
        def diskMode(self, value: vim.option.ChoiceOption):
            self._diskMode = value
        @property
        def split(self) -> vim.option.BoolOption: ...
        @split.setter
        def split(self, value: vim.option.BoolOption):
            self._split = value
        @property
        def writeThrough(self) -> vim.option.BoolOption: ...
        @writeThrough.setter
        def writeThrough(self, value: vim.option.BoolOption):
            self._writeThrough = value
        @property
        def growable(self) -> bool: ...
        @growable.setter
        def growable(self, value: bool):
            self._growable = value
        @property
        def hotGrowable(self) -> bool: ...
        @hotGrowable.setter
        def hotGrowable(self, value: bool):
            self._hotGrowable = value
        @property
        def uuid(self) -> bool: ...
        @uuid.setter
        def uuid(self, value: bool):
            self._uuid = value


    class VFlashCacheConfigOption(vmodl.DynamicData):
        @property
        def cacheConsistencyType(self) -> vim.option.ChoiceOption: ...
        @cacheConsistencyType.setter
        def cacheConsistencyType(self, value: vim.option.ChoiceOption):
            self._cacheConsistencyType = value
        @property
        def cacheMode(self) -> vim.option.ChoiceOption: ...
        @cacheMode.setter
        def cacheMode(self, value: vim.option.ChoiceOption):
            self._cacheMode = value
        @property
        def reservationInMB(self) -> vim.option.LongOption: ...
        @reservationInMB.setter
        def reservationInMB(self, value: vim.option.LongOption):
            self._reservationInMB = value
        @property
        def blockSizeInKB(self) -> vim.option.LongOption: ...
        @blockSizeInKB.setter
        def blockSizeInKB(self, value: vim.option.LongOption):
            self._blockSizeInKB = value


    class CompatibilityMode(Enum):
        virtualMode = "virtualMode"
        physicalMode = "physicalMode"


    class DiskMode(Enum):
        persistent = "persistent"
        nonpersistent = "nonpersistent"
        undoable = "undoable"
        independent_persistent = "independent_persistent"
        independent_nonpersistent = "independent_nonpersistent"
        append = "append"


class VirtualDiskSpec(VirtualDeviceSpec):
    @property
    def diskMoveType(self) -> str: ...
    @diskMoveType.setter
    def diskMoveType(self, value: str):
        self._diskMoveType = value
    @property
    def migrateCache(self) -> bool: ...
    @migrateCache.setter
    def migrateCache(self, value: bool):
        self._migrateCache = value


class VirtualE1000(VirtualEthernetCard): ...


class VirtualE1000Option(VirtualEthernetCardOption): ...


class VirtualE1000e(VirtualEthernetCard): ...


class VirtualE1000eOption(VirtualEthernetCardOption): ...


class VirtualEnsoniq1371(VirtualSoundCard): ...


class VirtualEnsoniq1371Option(VirtualSoundCardOption): ...


class VirtualEthernetCard(VirtualDevice):
    @property
    def addressType(self) -> str: ...
    @addressType.setter
    def addressType(self, value: str):
        self._addressType = value
    @property
    def macAddress(self) -> str: ...
    @macAddress.setter
    def macAddress(self, value: str):
        self._macAddress = value
    @property
    def wakeOnLanEnabled(self) -> bool: ...
    @wakeOnLanEnabled.setter
    def wakeOnLanEnabled(self, value: bool):
        self._wakeOnLanEnabled = value
    @property
    def resourceAllocation(self) -> VirtualEthernetCard.ResourceAllocation: ...
    @resourceAllocation.setter
    def resourceAllocation(self, value: VirtualEthernetCard.ResourceAllocation):
        self._resourceAllocation = value
    @property
    def externalId(self) -> str: ...
    @externalId.setter
    def externalId(self, value: str):
        self._externalId = value
    @property
    def uptCompatibilityEnabled(self) -> bool: ...
    @uptCompatibilityEnabled.setter
    def uptCompatibilityEnabled(self, value: bool):
        self._uptCompatibilityEnabled = value


    class DistributedVirtualPortBackingInfo(VirtualDevice.BackingInfo):
        @property
        def port(self) -> vim.dvs.PortConnection: ...
        @port.setter
        def port(self, value: vim.dvs.PortConnection):
            self._port = value


    class LegacyNetworkBackingInfo(VirtualDevice.DeviceBackingInfo): ...


    class NetworkBackingInfo(VirtualDevice.DeviceBackingInfo):
        @property
        def network(self) -> vim.Network: ...
        @network.setter
        def network(self, value: vim.Network):
            self._network = value
        @property
        def inPassthroughMode(self) -> bool: ...
        @inPassthroughMode.setter
        def inPassthroughMode(self, value: bool):
            self._inPassthroughMode = value


    class OpaqueNetworkBackingInfo(VirtualDevice.BackingInfo):
        @property
        def opaqueNetworkId(self) -> str: ...
        @opaqueNetworkId.setter
        def opaqueNetworkId(self, value: str):
            self._opaqueNetworkId = value
        @property
        def opaqueNetworkType(self) -> str: ...
        @opaqueNetworkType.setter
        def opaqueNetworkType(self, value: str):
            self._opaqueNetworkType = value


    class ResourceAllocation(vmodl.DynamicData):
        @property
        def reservation(self) -> long: ...
        @reservation.setter
        def reservation(self, value: long):
            self._reservation = value
        @property
        def share(self) -> vim.SharesInfo: ...
        @share.setter
        def share(self, value: vim.SharesInfo):
            self._share = value
        @property
        def limit(self) -> long: ...
        @limit.setter
        def limit(self, value: long):
            self._limit = value


class VirtualEthernetCardOption(VirtualDeviceOption):
    @property
    def supportedOUI(self) -> vim.option.ChoiceOption: ...
    @supportedOUI.setter
    def supportedOUI(self, value: vim.option.ChoiceOption):
        self._supportedOUI = value
    @property
    def macType(self) -> vim.option.ChoiceOption: ...
    @macType.setter
    def macType(self, value: vim.option.ChoiceOption):
        self._macType = value
    @property
    def wakeOnLanEnabled(self) -> vim.option.BoolOption: ...
    @wakeOnLanEnabled.setter
    def wakeOnLanEnabled(self, value: vim.option.BoolOption):
        self._wakeOnLanEnabled = value
    @property
    def vmDirectPathGen2Supported(self) -> bool: ...
    @vmDirectPathGen2Supported.setter
    def vmDirectPathGen2Supported(self, value: bool):
        self._vmDirectPathGen2Supported = value
    @property
    def uptCompatibilityEnabled(self) -> vim.option.BoolOption: ...
    @uptCompatibilityEnabled.setter
    def uptCompatibilityEnabled(self, value: vim.option.BoolOption):
        self._uptCompatibilityEnabled = value


    class DistributedVirtualPortBackingOption(VirtualDeviceOption.BackingOption): ...


    class LegacyNetworkBackingOption(VirtualDeviceOption.DeviceBackingOption):


        class LegacyNetworkDeviceName(Enum):
            bridged = "bridged"
            nat = "nat"
            hostonly = "hostonly"


    class NetworkBackingOption(VirtualDeviceOption.DeviceBackingOption): ...


    class OpaqueNetworkBackingOption(VirtualDeviceOption.BackingOption): ...


    class MacTypes(Enum):
        manual = "manual"
        generated = "generated"
        assigned = "assigned"


class VirtualFloppy(VirtualDevice):


    class DeviceBackingInfo(VirtualDevice.DeviceBackingInfo): ...


    class ImageBackingInfo(VirtualDevice.FileBackingInfo): ...


    class RemoteDeviceBackingInfo(VirtualDevice.RemoteDeviceBackingInfo): ...


class VirtualFloppyOption(VirtualDeviceOption):


    class DeviceBackingOption(VirtualDeviceOption.DeviceBackingOption): ...


    class ImageBackingOption(VirtualDeviceOption.FileBackingOption): ...


    class RemoteDeviceBackingOption(VirtualDeviceOption.RemoteDeviceBackingOption): ...


class VirtualHdAudioCard(VirtualSoundCard): ...


class VirtualHdAudioCardOption(VirtualSoundCardOption): ...


class VirtualIDEController(VirtualController): ...


class VirtualIDEControllerOption(VirtualControllerOption):
    @property
    def numIDEDisks(self) -> vim.option.IntOption: ...
    @numIDEDisks.setter
    def numIDEDisks(self, value: vim.option.IntOption):
        self._numIDEDisks = value
    @property
    def numIDECdroms(self) -> vim.option.IntOption: ...
    @numIDECdroms.setter
    def numIDECdroms(self, value: vim.option.IntOption):
        self._numIDECdroms = value


class VirtualKeyboard(VirtualDevice): ...


class VirtualKeyboardOption(VirtualDeviceOption): ...


class VirtualLsiLogicController(VirtualSCSIController): ...


class VirtualLsiLogicControllerOption(VirtualSCSIControllerOption): ...


class VirtualLsiLogicSASController(VirtualSCSIController): ...


class VirtualLsiLogicSASControllerOption(VirtualSCSIControllerOption): ...


class VirtualNVDIMM(VirtualDevice):
    @property
    def capacityInMB(self) -> long: ...
    @capacityInMB.setter
    def capacityInMB(self, value: long):
        self._capacityInMB = value
    @property
    def configuredCapacityInMB(self) -> long: ...
    @configuredCapacityInMB.setter
    def configuredCapacityInMB(self, value: long):
        self._configuredCapacityInMB = value


    class BackingInfo(VirtualDevice.FileBackingInfo):
        @property
        def parent(self) -> VirtualNVDIMM.BackingInfo: ...
        @parent.setter
        def parent(self, value: VirtualNVDIMM.BackingInfo):
            self._parent = value
        @property
        def changeId(self) -> str: ...
        @changeId.setter
        def changeId(self, value: str):
            self._changeId = value


class VirtualNVDIMMController(VirtualController): ...


class VirtualNVDIMMControllerOption(VirtualControllerOption):
    @property
    def numNVDIMMControllers(self) -> vim.option.IntOption: ...
    @numNVDIMMControllers.setter
    def numNVDIMMControllers(self, value: vim.option.IntOption):
        self._numNVDIMMControllers = value


class VirtualNVDIMMOption(VirtualDeviceOption):
    @property
    def capacityInMB(self) -> vim.option.LongOption: ...
    @capacityInMB.setter
    def capacityInMB(self, value: vim.option.LongOption):
        self._capacityInMB = value
    @property
    def growable(self) -> bool: ...
    @growable.setter
    def growable(self, value: bool):
        self._growable = value
    @property
    def hotGrowable(self) -> bool: ...
    @hotGrowable.setter
    def hotGrowable(self, value: bool):
        self._hotGrowable = value
    @property
    def granularityInMB(self) -> long: ...
    @granularityInMB.setter
    def granularityInMB(self, value: long):
        self._granularityInMB = value


class VirtualNVMEController(VirtualController):
    @property
    def sharedBus(self) -> str: ...
    @sharedBus.setter
    def sharedBus(self, value: str):
        self._sharedBus = value


class VirtualNVMEControllerOption(VirtualControllerOption):
    @property
    def numNVMEDisks(self) -> vim.option.IntOption: ...
    @numNVMEDisks.setter
    def numNVMEDisks(self, value: vim.option.IntOption):
        self._numNVMEDisks = value
    @property
    def sharing(self) -> List[str]: ...
    @sharing.setter
    def sharing(self, value: List[str]):
        self._sharing = value


class VirtualPCIController(VirtualController): ...


class VirtualPCIControllerOption(VirtualControllerOption):
    @property
    def numSCSIControllers(self) -> vim.option.IntOption: ...
    @numSCSIControllers.setter
    def numSCSIControllers(self, value: vim.option.IntOption):
        self._numSCSIControllers = value
    @property
    def numEthernetCards(self) -> vim.option.IntOption: ...
    @numEthernetCards.setter
    def numEthernetCards(self, value: vim.option.IntOption):
        self._numEthernetCards = value
    @property
    def numVideoCards(self) -> vim.option.IntOption: ...
    @numVideoCards.setter
    def numVideoCards(self, value: vim.option.IntOption):
        self._numVideoCards = value
    @property
    def numSoundCards(self) -> vim.option.IntOption: ...
    @numSoundCards.setter
    def numSoundCards(self, value: vim.option.IntOption):
        self._numSoundCards = value
    @property
    def numVmiRoms(self) -> vim.option.IntOption: ...
    @numVmiRoms.setter
    def numVmiRoms(self, value: vim.option.IntOption):
        self._numVmiRoms = value
    @property
    def numVmciDevices(self) -> vim.option.IntOption: ...
    @numVmciDevices.setter
    def numVmciDevices(self, value: vim.option.IntOption):
        self._numVmciDevices = value
    @property
    def numPCIPassthroughDevices(self) -> vim.option.IntOption: ...
    @numPCIPassthroughDevices.setter
    def numPCIPassthroughDevices(self, value: vim.option.IntOption):
        self._numPCIPassthroughDevices = value
    @property
    def numSasSCSIControllers(self) -> vim.option.IntOption: ...
    @numSasSCSIControllers.setter
    def numSasSCSIControllers(self, value: vim.option.IntOption):
        self._numSasSCSIControllers = value
    @property
    def numVmxnet3EthernetCards(self) -> vim.option.IntOption: ...
    @numVmxnet3EthernetCards.setter
    def numVmxnet3EthernetCards(self, value: vim.option.IntOption):
        self._numVmxnet3EthernetCards = value
    @property
    def numParaVirtualSCSIControllers(self) -> vim.option.IntOption: ...
    @numParaVirtualSCSIControllers.setter
    def numParaVirtualSCSIControllers(self, value: vim.option.IntOption):
        self._numParaVirtualSCSIControllers = value
    @property
    def numSATAControllers(self) -> vim.option.IntOption: ...
    @numSATAControllers.setter
    def numSATAControllers(self, value: vim.option.IntOption):
        self._numSATAControllers = value
    @property
    def numNVMEControllers(self) -> vim.option.IntOption: ...
    @numNVMEControllers.setter
    def numNVMEControllers(self, value: vim.option.IntOption):
        self._numNVMEControllers = value
    @property
    def numVmxnet3VrdmaEthernetCards(self) -> vim.option.IntOption: ...
    @numVmxnet3VrdmaEthernetCards.setter
    def numVmxnet3VrdmaEthernetCards(self, value: vim.option.IntOption):
        self._numVmxnet3VrdmaEthernetCards = value


class VirtualPCIPassthrough(VirtualDevice):


    class AllowedDevice(vmodl.DynamicData):
        @property
        def vendorId(self) -> int: ...
        @vendorId.setter
        def vendorId(self, value: int):
            self._vendorId = value
        @property
        def deviceId(self) -> int: ...
        @deviceId.setter
        def deviceId(self, value: int):
            self._deviceId = value
        @property
        def subVendorId(self) -> int: ...
        @subVendorId.setter
        def subVendorId(self, value: int):
            self._subVendorId = value
        @property
        def subDeviceId(self) -> int: ...
        @subDeviceId.setter
        def subDeviceId(self, value: int):
            self._subDeviceId = value
        @property
        def revisionId(self) -> short: ...
        @revisionId.setter
        def revisionId(self, value: short):
            self._revisionId = value


    class DeviceBackingInfo(VirtualDevice.DeviceBackingInfo):
        @property
        def id(self) -> str: ...
        @id.setter
        def id(self, value: str):
            self._id = value
        @property
        def deviceId(self) -> str: ...
        @deviceId.setter
        def deviceId(self, value: str):
            self._deviceId = value
        @property
        def systemId(self) -> str: ...
        @systemId.setter
        def systemId(self, value: str):
            self._systemId = value
        @property
        def vendorId(self) -> short: ...
        @vendorId.setter
        def vendorId(self, value: short):
            self._vendorId = value


    class DvxBackingInfo(VirtualDevice.BackingInfo):
        @property
        def deviceClass(self) -> str: ...
        @deviceClass.setter
        def deviceClass(self, value: str):
            self._deviceClass = value
        @property
        def configParams(self) -> List[vim.option.OptionValue]: ...
        @configParams.setter
        def configParams(self, value: List[vim.option.OptionValue]):
            self._configParams = value


    class DynamicBackingInfo(VirtualDevice.DeviceBackingInfo):
        @property
        def allowedDevice(self) -> List[VirtualPCIPassthrough.AllowedDevice]: ...
        @allowedDevice.setter
        def allowedDevice(self, value: List[VirtualPCIPassthrough.AllowedDevice]):
            self._allowedDevice = value
        @property
        def customLabel(self) -> str: ...
        @customLabel.setter
        def customLabel(self, value: str):
            self._customLabel = value
        @property
        def assignedId(self) -> str: ...
        @assignedId.setter
        def assignedId(self, value: str):
            self._assignedId = value


    class PluginBackingInfo(VirtualDevice.BackingInfo): ...


    class VmiopBackingInfo(VirtualPCIPassthrough.PluginBackingInfo):
        @property
        def vgpu(self) -> str: ...
        @vgpu.setter
        def vgpu(self, value: str):
            self._vgpu = value
        @property
        def vgpuMigrateDataSizeMB(self) -> int: ...
        @vgpuMigrateDataSizeMB.setter
        def vgpuMigrateDataSizeMB(self, value: int):
            self._vgpuMigrateDataSizeMB = value
        @property
        def migrateSupported(self) -> bool: ...
        @migrateSupported.setter
        def migrateSupported(self, value: bool):
            self._migrateSupported = value
        @property
        def enhancedMigrateCapability(self) -> bool: ...
        @enhancedMigrateCapability.setter
        def enhancedMigrateCapability(self, value: bool):
            self._enhancedMigrateCapability = value


class VirtualPCIPassthroughOption(VirtualDeviceOption):


    class DeviceBackingOption(VirtualDeviceOption.DeviceBackingOption): ...


    class DvxBackingOption(VirtualDeviceOption.BackingOption): ...


    class DynamicBackingOption(VirtualDeviceOption.DeviceBackingOption): ...


    class PluginBackingOption(VirtualDeviceOption.BackingOption): ...


    class VmiopBackingOption(VirtualPCIPassthroughOption.PluginBackingOption):
        @property
        def vgpu(self) -> vim.option.StringOption: ...
        @vgpu.setter
        def vgpu(self, value: vim.option.StringOption):
            self._vgpu = value
        @property
        def maxInstances(self) -> int: ...
        @maxInstances.setter
        def maxInstances(self, value: int):
            self._maxInstances = value


class VirtualPCNet32(VirtualEthernetCard): ...


class VirtualPCNet32Option(VirtualEthernetCardOption):
    @property
    def supportsMorphing(self) -> bool: ...
    @supportsMorphing.setter
    def supportsMorphing(self, value: bool):
        self._supportsMorphing = value


class VirtualPS2Controller(VirtualController): ...


class VirtualPS2ControllerOption(VirtualControllerOption):
    @property
    def numKeyboards(self) -> vim.option.IntOption: ...
    @numKeyboards.setter
    def numKeyboards(self, value: vim.option.IntOption):
        self._numKeyboards = value
    @property
    def numPointingDevices(self) -> vim.option.IntOption: ...
    @numPointingDevices.setter
    def numPointingDevices(self, value: vim.option.IntOption):
        self._numPointingDevices = value


class VirtualParallelPort(VirtualDevice):


    class DeviceBackingInfo(VirtualDevice.DeviceBackingInfo): ...


    class FileBackingInfo(VirtualDevice.FileBackingInfo): ...


class VirtualParallelPortOption(VirtualDeviceOption):


    class DeviceBackingOption(VirtualDeviceOption.DeviceBackingOption): ...


    class FileBackingOption(VirtualDeviceOption.FileBackingOption): ...


class VirtualPointingDevice(VirtualDevice):


    class DeviceBackingInfo(VirtualDevice.DeviceBackingInfo):
        @property
        def hostPointingDevice(self) -> str: ...
        @hostPointingDevice.setter
        def hostPointingDevice(self, value: str):
            self._hostPointingDevice = value


class VirtualPointingDeviceOption(VirtualDeviceOption):


    class DeviceBackingOption(VirtualDeviceOption.DeviceBackingOption):
        @property
        def hostPointingDevice(self) -> vim.option.ChoiceOption: ...
        @hostPointingDevice.setter
        def hostPointingDevice(self, value: vim.option.ChoiceOption):
            self._hostPointingDevice = value


        class HostPointingDeviceChoice(Enum):
            autodetect = "autodetect"
            intellimouseExplorer = "intellimouseExplorer"
            intellimousePs2 = "intellimousePs2"
            logitechMouseman = "logitechMouseman"
            microsoft_serial = "microsoft_serial"
            mouseSystems = "mouseSystems"
            mousemanSerial = "mousemanSerial"
            ps2 = "ps2"


class VirtualPrecisionClock(VirtualDevice):


    class SystemClockBackingInfo(VirtualDevice.BackingInfo):
        @property
        def protocol(self) -> str: ...
        @protocol.setter
        def protocol(self, value: str):
            self._protocol = value


class VirtualPrecisionClockOption(VirtualDeviceOption):


    class SystemClockBackingOption(VirtualDeviceOption.BackingOption):
        @property
        def protocol(self) -> vim.option.ChoiceOption: ...
        @protocol.setter
        def protocol(self, value: vim.option.ChoiceOption):
            self._protocol = value


class VirtualSATAController(VirtualController): ...


class VirtualSATAControllerOption(VirtualControllerOption):
    @property
    def numSATADisks(self) -> vim.option.IntOption: ...
    @numSATADisks.setter
    def numSATADisks(self, value: vim.option.IntOption):
        self._numSATADisks = value
    @property
    def numSATACdroms(self) -> vim.option.IntOption: ...
    @numSATACdroms.setter
    def numSATACdroms(self, value: vim.option.IntOption):
        self._numSATACdroms = value


class VirtualSCSIController(VirtualController):
    @property
    def hotAddRemove(self) -> bool: ...
    @hotAddRemove.setter
    def hotAddRemove(self, value: bool):
        self._hotAddRemove = value
    @property
    def sharedBus(self) -> VirtualSCSIController.Sharing | Literal['noSharing', 'virtualSharing', 'physicalSharing']: ...
    @sharedBus.setter
    def sharedBus(self, value: VirtualSCSIController.Sharing | Literal['noSharing', 'virtualSharing', 'physicalSharing']):
        self._sharedBus = value
    @property
    def scsiCtlrUnitNumber(self) -> int: ...
    @scsiCtlrUnitNumber.setter
    def scsiCtlrUnitNumber(self, value: int):
        self._scsiCtlrUnitNumber = value


class VirtualSCSIControllerOption(VirtualControllerOption):
    @property
    def numSCSIDisks(self) -> vim.option.IntOption: ...
    @numSCSIDisks.setter
    def numSCSIDisks(self, value: vim.option.IntOption):
        self._numSCSIDisks = value
    @property
    def numSCSICdroms(self) -> vim.option.IntOption: ...
    @numSCSICdroms.setter
    def numSCSICdroms(self, value: vim.option.IntOption):
        self._numSCSICdroms = value
    @property
    def numSCSIPassthrough(self) -> vim.option.IntOption: ...
    @numSCSIPassthrough.setter
    def numSCSIPassthrough(self, value: vim.option.IntOption):
        self._numSCSIPassthrough = value
    @property
    def sharing(self) -> List[VirtualSCSIController.Sharing]: ...
    @sharing.setter
    def sharing(self, value: List[VirtualSCSIController.Sharing]):
        self._sharing = value
    @property
    def defaultSharedIndex(self) -> int: ...
    @defaultSharedIndex.setter
    def defaultSharedIndex(self, value: int):
        self._defaultSharedIndex = value
    @property
    def hotAddRemove(self) -> vim.option.BoolOption: ...
    @hotAddRemove.setter
    def hotAddRemove(self, value: vim.option.BoolOption):
        self._hotAddRemove = value
    @property
    def scsiCtlrUnitNumber(self) -> int: ...
    @scsiCtlrUnitNumber.setter
    def scsiCtlrUnitNumber(self, value: int):
        self._scsiCtlrUnitNumber = value


class VirtualSCSIPassthrough(VirtualDevice):


    class DeviceBackingInfo(VirtualDevice.DeviceBackingInfo): ...


class VirtualSCSIPassthroughOption(VirtualDeviceOption):


    class DeviceBackingOption(VirtualDeviceOption.DeviceBackingOption): ...


class VirtualSIOController(VirtualController): ...


class VirtualSIOControllerOption(VirtualControllerOption):
    @property
    def numFloppyDrives(self) -> vim.option.IntOption: ...
    @numFloppyDrives.setter
    def numFloppyDrives(self, value: vim.option.IntOption):
        self._numFloppyDrives = value
    @property
    def numSerialPorts(self) -> vim.option.IntOption: ...
    @numSerialPorts.setter
    def numSerialPorts(self, value: vim.option.IntOption):
        self._numSerialPorts = value
    @property
    def numParallelPorts(self) -> vim.option.IntOption: ...
    @numParallelPorts.setter
    def numParallelPorts(self, value: vim.option.IntOption):
        self._numParallelPorts = value


class VirtualSerialPort(VirtualDevice):
    @property
    def yieldOnPoll(self) -> bool: ...
    @yieldOnPoll.setter
    def yieldOnPoll(self, value: bool):
        self._yieldOnPoll = value


    class DeviceBackingInfo(VirtualDevice.DeviceBackingInfo): ...


    class FileBackingInfo(VirtualDevice.FileBackingInfo): ...


    class PipeBackingInfo(VirtualDevice.PipeBackingInfo):
        @property
        def endpoint(self) -> str: ...
        @endpoint.setter
        def endpoint(self, value: str):
            self._endpoint = value
        @property
        def noRxLoss(self) -> bool: ...
        @noRxLoss.setter
        def noRxLoss(self, value: bool):
            self._noRxLoss = value


    class ThinPrintBackingInfo(VirtualDevice.BackingInfo): ...


    class URIBackingInfo(VirtualDevice.URIBackingInfo): ...


class VirtualSerialPortOption(VirtualDeviceOption):
    @property
    def yieldOnPoll(self) -> vim.option.BoolOption: ...
    @yieldOnPoll.setter
    def yieldOnPoll(self, value: vim.option.BoolOption):
        self._yieldOnPoll = value


    class DeviceBackingOption(VirtualDeviceOption.DeviceBackingOption): ...


    class FileBackingOption(VirtualDeviceOption.FileBackingOption): ...


    class PipeBackingOption(VirtualDeviceOption.PipeBackingOption):
        @property
        def endpoint(self) -> vim.option.ChoiceOption: ...
        @endpoint.setter
        def endpoint(self, value: vim.option.ChoiceOption):
            self._endpoint = value
        @property
        def noRxLoss(self) -> vim.option.BoolOption: ...
        @noRxLoss.setter
        def noRxLoss(self, value: vim.option.BoolOption):
            self._noRxLoss = value


    class ThinPrintBackingOption(VirtualDeviceOption.BackingOption): ...


    class URIBackingOption(VirtualDeviceOption.URIBackingOption): ...


    class EndPoint(Enum):
        client = "client"
        server = "server"


class VirtualSoundBlaster16(VirtualSoundCard): ...


class VirtualSoundBlaster16Option(VirtualSoundCardOption): ...


class VirtualSoundCard(VirtualDevice):


    class DeviceBackingInfo(VirtualDevice.DeviceBackingInfo): ...


class VirtualSoundCardOption(VirtualDeviceOption):


    class DeviceBackingOption(VirtualDeviceOption.DeviceBackingOption): ...


class VirtualSriovEthernetCard(VirtualEthernetCard):
    @property
    def allowGuestOSMtuChange(self) -> bool: ...
    @allowGuestOSMtuChange.setter
    def allowGuestOSMtuChange(self, value: bool):
        self._allowGuestOSMtuChange = value
    @property
    def sriovBacking(self) -> VirtualSriovEthernetCard.SriovBackingInfo: ...
    @sriovBacking.setter
    def sriovBacking(self, value: VirtualSriovEthernetCard.SriovBackingInfo):
        self._sriovBacking = value
    @property
    def dvxBackingInfo(self) -> VirtualPCIPassthrough.DvxBackingInfo: ...
    @dvxBackingInfo.setter
    def dvxBackingInfo(self, value: VirtualPCIPassthrough.DvxBackingInfo):
        self._dvxBackingInfo = value


    class SriovBackingInfo(VirtualDevice.BackingInfo):
        @property
        def physicalFunctionBacking(self) -> VirtualPCIPassthrough.DeviceBackingInfo: ...
        @physicalFunctionBacking.setter
        def physicalFunctionBacking(self, value: VirtualPCIPassthrough.DeviceBackingInfo):
            self._physicalFunctionBacking = value
        @property
        def virtualFunctionBacking(self) -> VirtualPCIPassthrough.DeviceBackingInfo: ...
        @virtualFunctionBacking.setter
        def virtualFunctionBacking(self, value: VirtualPCIPassthrough.DeviceBackingInfo):
            self._virtualFunctionBacking = value
        @property
        def virtualFunctionIndex(self) -> int: ...
        @virtualFunctionIndex.setter
        def virtualFunctionIndex(self, value: int):
            self._virtualFunctionIndex = value


class VirtualSriovEthernetCardOption(VirtualEthernetCardOption):


    class SriovBackingOption(VirtualDeviceOption.BackingOption): ...


class VirtualTPM(VirtualDevice):
    @property
    def endorsementKeyCertificateSigningRequest(self) -> List[binary]: ...
    @endorsementKeyCertificateSigningRequest.setter
    def endorsementKeyCertificateSigningRequest(self, value: List[binary]):
        self._endorsementKeyCertificateSigningRequest = value
    @property
    def endorsementKeyCertificate(self) -> List[binary]: ...
    @endorsementKeyCertificate.setter
    def endorsementKeyCertificate(self, value: List[binary]):
        self._endorsementKeyCertificate = value


class VirtualTPMOption(VirtualDeviceOption):
    @property
    def supportedFirmware(self) -> List[str]: ...
    @supportedFirmware.setter
    def supportedFirmware(self, value: List[str]):
        self._supportedFirmware = value


class VirtualUSB(VirtualDevice):
    @property
    def connected(self) -> bool: ...
    @connected.setter
    def connected(self, value: bool):
        self._connected = value
    @property
    def vendor(self) -> int: ...
    @vendor.setter
    def vendor(self, value: int):
        self._vendor = value
    @property
    def product(self) -> int: ...
    @product.setter
    def product(self, value: int):
        self._product = value
    @property
    def family(self) -> List[str]: ...
    @family.setter
    def family(self, value: List[str]):
        self._family = value
    @property
    def speed(self) -> List[str]: ...
    @speed.setter
    def speed(self, value: List[str]):
        self._speed = value


    class RemoteClientBackingInfo(VirtualDevice.RemoteDeviceBackingInfo):
        @property
        def hostname(self) -> str: ...
        @hostname.setter
        def hostname(self, value: str):
            self._hostname = value


    class RemoteHostBackingInfo(VirtualDevice.DeviceBackingInfo):
        @property
        def hostname(self) -> str: ...
        @hostname.setter
        def hostname(self, value: str):
            self._hostname = value


    class USBBackingInfo(VirtualDevice.DeviceBackingInfo): ...


class VirtualUSBController(VirtualController):
    @property
    def autoConnectDevices(self) -> bool: ...
    @autoConnectDevices.setter
    def autoConnectDevices(self, value: bool):
        self._autoConnectDevices = value
    @property
    def ehciEnabled(self) -> bool: ...
    @ehciEnabled.setter
    def ehciEnabled(self, value: bool):
        self._ehciEnabled = value


    class PciBusSlotInfo(VirtualDevice.PciBusSlotInfo):
        @property
        def ehciPciSlotNumber(self) -> int: ...
        @ehciPciSlotNumber.setter
        def ehciPciSlotNumber(self, value: int):
            self._ehciPciSlotNumber = value


class VirtualUSBControllerOption(VirtualControllerOption):
    @property
    def autoConnectDevices(self) -> vim.option.BoolOption: ...
    @autoConnectDevices.setter
    def autoConnectDevices(self, value: vim.option.BoolOption):
        self._autoConnectDevices = value
    @property
    def ehciSupported(self) -> vim.option.BoolOption: ...
    @ehciSupported.setter
    def ehciSupported(self, value: vim.option.BoolOption):
        self._ehciSupported = value
    @property
    def supportedSpeeds(self) -> List[str]: ...
    @supportedSpeeds.setter
    def supportedSpeeds(self, value: List[str]):
        self._supportedSpeeds = value


class VirtualUSBOption(VirtualDeviceOption):


    class RemoteClientBackingOption(VirtualDeviceOption.RemoteDeviceBackingOption): ...


    class RemoteHostBackingOption(VirtualDeviceOption.DeviceBackingOption): ...


    class USBBackingOption(VirtualDeviceOption.DeviceBackingOption): ...


class VirtualUSBXHCIController(VirtualController):
    @property
    def autoConnectDevices(self) -> bool: ...
    @autoConnectDevices.setter
    def autoConnectDevices(self, value: bool):
        self._autoConnectDevices = value


class VirtualUSBXHCIControllerOption(VirtualControllerOption):
    @property
    def autoConnectDevices(self) -> vim.option.BoolOption: ...
    @autoConnectDevices.setter
    def autoConnectDevices(self, value: vim.option.BoolOption):
        self._autoConnectDevices = value
    @property
    def supportedSpeeds(self) -> List[str]: ...
    @supportedSpeeds.setter
    def supportedSpeeds(self, value: List[str]):
        self._supportedSpeeds = value


class VirtualVMCIDevice(VirtualDevice):
    @property
    def id(self) -> long: ...
    @id.setter
    def id(self, value: long):
        self._id = value
    @property
    def allowUnrestrictedCommunication(self) -> bool: ...
    @allowUnrestrictedCommunication.setter
    def allowUnrestrictedCommunication(self, value: bool):
        self._allowUnrestrictedCommunication = value
    @property
    def filterEnable(self) -> bool: ...
    @filterEnable.setter
    def filterEnable(self, value: bool):
        self._filterEnable = value
    @property
    def filterInfo(self) -> VirtualVMCIDevice.FilterInfo: ...
    @filterInfo.setter
    def filterInfo(self, value: VirtualVMCIDevice.FilterInfo):
        self._filterInfo = value


    class FilterInfo(vmodl.DynamicData):
        @property
        def filters(self) -> List[VirtualVMCIDevice.FilterSpec]: ...
        @filters.setter
        def filters(self, value: List[VirtualVMCIDevice.FilterSpec]):
            self._filters = value


    class FilterSpec(vmodl.DynamicData):
        @property
        def rank(self) -> long: ...
        @rank.setter
        def rank(self, value: long):
            self._rank = value
        @property
        def action(self) -> str: ...
        @action.setter
        def action(self, value: str):
            self._action = value
        @property
        def protocol(self) -> str: ...
        @protocol.setter
        def protocol(self, value: str):
            self._protocol = value
        @property
        def direction(self) -> str: ...
        @direction.setter
        def direction(self, value: str):
            self._direction = value
        @property
        def lowerDstPortBoundary(self) -> long: ...
        @lowerDstPortBoundary.setter
        def lowerDstPortBoundary(self, value: long):
            self._lowerDstPortBoundary = value
        @property
        def upperDstPortBoundary(self) -> long: ...
        @upperDstPortBoundary.setter
        def upperDstPortBoundary(self, value: long):
            self._upperDstPortBoundary = value


    class Action(Enum):
        allow = "allow"
        deny = "deny"


    class Protocol(Enum):
        hypervisor = "hypervisor"
        doorbell = "doorbell"
        queuepair = "queuepair"
        datagram = "datagram"
        stream = "stream"
        anyProtocol = "anyProtocol"


class VirtualVMCIDeviceOption(VirtualDeviceOption):
    @property
    def allowUnrestrictedCommunication(self) -> vim.option.BoolOption: ...
    @allowUnrestrictedCommunication.setter
    def allowUnrestrictedCommunication(self, value: vim.option.BoolOption):
        self._allowUnrestrictedCommunication = value
    @property
    def filterSpecOption(self) -> VirtualVMCIDeviceOption.FilterSpecOption: ...
    @filterSpecOption.setter
    def filterSpecOption(self, value: VirtualVMCIDeviceOption.FilterSpecOption):
        self._filterSpecOption = value
    @property
    def filterSupported(self) -> vim.option.BoolOption: ...
    @filterSupported.setter
    def filterSupported(self, value: vim.option.BoolOption):
        self._filterSupported = value


    class FilterSpecOption(vmodl.DynamicData):
        @property
        def action(self) -> vim.option.ChoiceOption: ...
        @action.setter
        def action(self, value: vim.option.ChoiceOption):
            self._action = value
        @property
        def protocol(self) -> vim.option.ChoiceOption: ...
        @protocol.setter
        def protocol(self, value: vim.option.ChoiceOption):
            self._protocol = value
        @property
        def direction(self) -> vim.option.ChoiceOption: ...
        @direction.setter
        def direction(self, value: vim.option.ChoiceOption):
            self._direction = value
        @property
        def lowerDstPortBoundary(self) -> vim.option.LongOption: ...
        @lowerDstPortBoundary.setter
        def lowerDstPortBoundary(self, value: vim.option.LongOption):
            self._lowerDstPortBoundary = value
        @property
        def upperDstPortBoundary(self) -> vim.option.LongOption: ...
        @upperDstPortBoundary.setter
        def upperDstPortBoundary(self, value: vim.option.LongOption):
            self._upperDstPortBoundary = value


class VirtualVMIROM(VirtualDevice): ...


class VirtualVMIROMOption(VirtualDeviceOption): ...


class VirtualVideoCard(VirtualDevice):
    @property
    def videoRamSizeInKB(self) -> long: ...
    @videoRamSizeInKB.setter
    def videoRamSizeInKB(self, value: long):
        self._videoRamSizeInKB = value
    @property
    def numDisplays(self) -> int: ...
    @numDisplays.setter
    def numDisplays(self, value: int):
        self._numDisplays = value
    @property
    def useAutoDetect(self) -> bool: ...
    @useAutoDetect.setter
    def useAutoDetect(self, value: bool):
        self._useAutoDetect = value
    @property
    def enable3DSupport(self) -> bool: ...
    @enable3DSupport.setter
    def enable3DSupport(self, value: bool):
        self._enable3DSupport = value
    @property
    def use3dRenderer(self) -> str: ...
    @use3dRenderer.setter
    def use3dRenderer(self, value: str):
        self._use3dRenderer = value
    @property
    def graphicsMemorySizeInKB(self) -> long: ...
    @graphicsMemorySizeInKB.setter
    def graphicsMemorySizeInKB(self, value: long):
        self._graphicsMemorySizeInKB = value


    class Use3dRenderer(Enum):
        automatic = "automatic"
        software = "software"
        hardware = "hardware"


class VirtualVideoCardOption(VirtualDeviceOption):
    @property
    def videoRamSizeInKB(self) -> vim.option.LongOption: ...
    @videoRamSizeInKB.setter
    def videoRamSizeInKB(self, value: vim.option.LongOption):
        self._videoRamSizeInKB = value
    @property
    def numDisplays(self) -> vim.option.IntOption: ...
    @numDisplays.setter
    def numDisplays(self, value: vim.option.IntOption):
        self._numDisplays = value
    @property
    def useAutoDetect(self) -> vim.option.BoolOption: ...
    @useAutoDetect.setter
    def useAutoDetect(self, value: vim.option.BoolOption):
        self._useAutoDetect = value
    @property
    def support3D(self) -> vim.option.BoolOption: ...
    @support3D.setter
    def support3D(self, value: vim.option.BoolOption):
        self._support3D = value
    @property
    def use3dRendererSupported(self) -> vim.option.BoolOption: ...
    @use3dRendererSupported.setter
    def use3dRendererSupported(self, value: vim.option.BoolOption):
        self._use3dRendererSupported = value
    @property
    def graphicsMemorySizeInKB(self) -> vim.option.LongOption: ...
    @graphicsMemorySizeInKB.setter
    def graphicsMemorySizeInKB(self, value: vim.option.LongOption):
        self._graphicsMemorySizeInKB = value
    @property
    def graphicsMemorySizeSupported(self) -> vim.option.BoolOption: ...
    @graphicsMemorySizeSupported.setter
    def graphicsMemorySizeSupported(self, value: vim.option.BoolOption):
        self._graphicsMemorySizeSupported = value


class VirtualVmxnet(VirtualEthernetCard): ...


class VirtualVmxnet2(VirtualVmxnet): ...


class VirtualVmxnet2Option(VirtualVmxnetOption): ...


class VirtualVmxnet3(VirtualVmxnet):
    @property
    def uptv2Enabled(self) -> bool: ...
    @uptv2Enabled.setter
    def uptv2Enabled(self, value: bool):
        self._uptv2Enabled = value


class VirtualVmxnet3Option(VirtualVmxnetOption):
    @property
    def uptv2Enabled(self) -> vim.option.BoolOption: ...
    @uptv2Enabled.setter
    def uptv2Enabled(self, value: vim.option.BoolOption):
        self._uptv2Enabled = value


class VirtualVmxnet3Vrdma(VirtualVmxnet3):
    @property
    def deviceProtocol(self) -> str: ...
    @deviceProtocol.setter
    def deviceProtocol(self, value: str):
        self._deviceProtocol = value


class VirtualVmxnet3VrdmaOption(VirtualVmxnet3Option):
    @property
    def deviceProtocol(self) -> vim.option.ChoiceOption: ...
    @deviceProtocol.setter
    def deviceProtocol(self, value: vim.option.ChoiceOption):
        self._deviceProtocol = value


    class DeviceProtocols(Enum):
        rocev1 = "rocev1"
        rocev2 = "rocev2"


class VirtualVmxnetOption(VirtualEthernetCardOption): ...


class VirtualWDT(VirtualDevice):
    @property
    def runOnBoot(self) -> bool: ...
    @runOnBoot.setter
    def runOnBoot(self, value: bool):
        self._runOnBoot = value
    @property
    def running(self) -> bool: ...
    @running.setter
    def running(self, value: bool):
        self._running = value


class VirtualWDTOption(VirtualDeviceOption):
    @property
    def runOnBoot(self) -> vim.option.BoolOption: ...
    @runOnBoot.setter
    def runOnBoot(self, value: vim.option.BoolOption):
        self._runOnBoot = value