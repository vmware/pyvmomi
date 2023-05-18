from typing import List
from enum import Enum
from pyVmomi import vim, vmodl
from pyVmomi.VmomiSupport import PropertyPath, binary, long, short


class HostDiskMappingInfo(vmodl.DynamicData):
    @property
    def physicalPartition(self) -> HostDiskMappingInfo.PartitionInfo: ...
    @property
    def name(self) -> str: ...
    @property
    def exclusive(self) -> bool: ...


    class PartitionInfo(vmodl.DynamicData):
        @property
        def name(self) -> str: ...
        @property
        def fileSystem(self) -> str: ...
        @property
        def capacityInKb(self) -> long: ...


class HostDiskMappingOption(vmodl.DynamicData):
    @property
    def physicalPartition(self) -> List[HostDiskMappingOption.PartitionOption]: ...
    @property
    def name(self) -> str: ...


    class PartitionOption(vmodl.DynamicData):
        @property
        def name(self) -> str: ...
        @property
        def fileSystem(self) -> str: ...
        @property
        def capacityInKb(self) -> long: ...


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


    class RemoteAtapiBackingInfo(VirtualDevice.RemoteDeviceBackingInfo): ...


    class RemotePassthroughBackingInfo(VirtualDevice.RemoteDeviceBackingInfo):
        @property
        def exclusive(self) -> bool: ...


class VirtualCdromOption(VirtualDeviceOption):


    class AtapiBackingOption(VirtualDeviceOption.DeviceBackingOption): ...


    class IsoBackingOption(VirtualDeviceOption.FileBackingOption): ...


    class PassthroughBackingOption(VirtualDeviceOption.DeviceBackingOption):
        @property
        def exclusive(self) -> vim.option.BoolOption: ...


    class RemoteAtapiBackingOption(VirtualDeviceOption.DeviceBackingOption): ...


    class RemotePassthroughBackingOption(VirtualDeviceOption.RemoteDeviceBackingOption):
        @property
        def exclusive(self) -> vim.option.BoolOption: ...


class VirtualController(VirtualDevice):
    @property
    def busNumber(self) -> int: ...
    @property
    def device(self) -> List[int]: ...


class VirtualControllerOption(VirtualDeviceOption):
    @property
    def devices(self) -> vim.option.IntOption: ...
    @property
    def supportedDevice(self) -> List[type]: ...


class VirtualDevice(vmodl.DynamicData):
    @property
    def key(self) -> int: ...
    @property
    def deviceInfo(self) -> vim.Description: ...
    @property
    def backing(self) -> VirtualDevice.BackingInfo: ...
    @property
    def connectable(self) -> VirtualDevice.ConnectInfo: ...
    @property
    def slotInfo(self) -> VirtualDevice.BusSlotInfo: ...
    @property
    def controllerKey(self) -> int: ...
    @property
    def unitNumber(self) -> int: ...
    @property
    def numaNode(self) -> int: ...
    @property
    def deviceGroupInfo(self) -> VirtualDevice.DeviceGroupInfo: ...


    class BackingInfo(vmodl.DynamicData): ...


    class BusSlotInfo(vmodl.DynamicData): ...


    class ConnectInfo(vmodl.DynamicData):
        @property
        def migrateConnect(self) -> str: ...
        @property
        def startConnected(self) -> bool: ...
        @property
        def allowGuestControl(self) -> bool: ...
        @property
        def connected(self) -> bool: ...
        @property
        def status(self) -> str: ...


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
        @property
        def useAutoDetect(self) -> bool: ...


    class DeviceGroupInfo(vmodl.DynamicData):
        @property
        def groupInstanceKey(self) -> int: ...
        @property
        def sequenceId(self) -> int: ...


    class FileBackingInfo(VirtualDevice.BackingInfo):
        @property
        def fileName(self) -> str: ...
        @property
        def datastore(self) -> vim.Datastore: ...
        @property
        def backingObjectId(self) -> str: ...


    class PciBusSlotInfo(VirtualDevice.BusSlotInfo):
        @property
        def pciSlotNumber(self) -> int: ...


    class PipeBackingInfo(VirtualDevice.BackingInfo):
        @property
        def pipeName(self) -> str: ...


    class RemoteDeviceBackingInfo(VirtualDevice.BackingInfo):
        @property
        def deviceName(self) -> str: ...
        @property
        def useAutoDetect(self) -> bool: ...


    class URIBackingInfo(VirtualDevice.BackingInfo):
        @property
        def serviceURI(self) -> str: ...
        @property
        def direction(self) -> str: ...
        @property
        def proxyURI(self) -> str: ...


class VirtualDeviceOption(vmodl.DynamicData):
    @property
    def type(self) -> type: ...
    @property
    def connectOption(self) -> VirtualDeviceOption.ConnectOption: ...
    @property
    def busSlotOption(self) -> VirtualDeviceOption.BusSlotOption: ...
    @property
    def controllerType(self) -> type: ...
    @property
    def autoAssignController(self) -> vim.option.BoolOption: ...
    @property
    def backingOption(self) -> List[VirtualDeviceOption.BackingOption]: ...
    @property
    def defaultBackingOptionIndex(self) -> int: ...
    @property
    def licensingLimit(self) -> List[PropertyPath]: ...
    @property
    def deprecated(self) -> bool: ...
    @property
    def plugAndPlay(self) -> bool: ...
    @property
    def hotRemoveSupported(self) -> bool: ...
    @property
    def numaSupported(self) -> bool: ...


    class BackingOption(vmodl.DynamicData):
        @property
        def type(self) -> type: ...


    class BusSlotOption(vmodl.DynamicData):
        @property
        def type(self) -> type: ...


    class ConnectOption(vmodl.DynamicData):
        @property
        def startConnected(self) -> vim.option.BoolOption: ...
        @property
        def allowGuestControl(self) -> vim.option.BoolOption: ...


    class DeviceBackingOption(VirtualDeviceOption.BackingOption):
        @property
        def autoDetectAvailable(self) -> vim.option.BoolOption: ...


    class FileBackingOption(VirtualDeviceOption.BackingOption):
        @property
        def fileNameExtensions(self) -> vim.option.ChoiceOption: ...


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


    class URIBackingOption(VirtualDeviceOption.BackingOption):
        @property
        def directions(self) -> vim.option.ChoiceOption: ...


        class Direction(Enum):
            server = "server"
            client = "client"


class VirtualDeviceSpec(vmodl.DynamicData):
    @property
    def operation(self) -> VirtualDeviceSpec.Operation: ...
    @property
    def fileOperation(self) -> VirtualDeviceSpec.FileOperation: ...
    @property
    def device(self) -> VirtualDevice: ...
    @property
    def profile(self) -> List[vim.vm.ProfileSpec]: ...
    @property
    def backing(self) -> VirtualDeviceSpec.BackingSpec: ...
    @property
    def filterSpec(self) -> List[vim.vm.BaseIndependentFilterSpec]: ...
    @property
    def changeMode(self) -> str: ...


    class BackingSpec(vmodl.DynamicData):
        @property
        def parent(self) -> VirtualDeviceSpec.BackingSpec: ...
        @property
        def crypto(self) -> vim.encryption.CryptoSpec: ...


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
    @property
    def capacityInBytes(self) -> long: ...
    @property
    def shares(self) -> vim.SharesInfo: ...
    @property
    def storageIOAllocation(self) -> vim.StorageResourceManager.IOAllocationInfo: ...
    @property
    def diskObjectId(self) -> str: ...
    @property
    def vFlashCacheConfigInfo(self) -> VirtualDisk.VFlashCacheConfigInfo: ...
    @property
    def iofilter(self) -> List[str]: ...
    @property
    def vDiskId(self) -> vim.vslm.ID: ...
    @property
    def vDiskVersion(self) -> int: ...
    @property
    def nativeUnmanagedLinkedClone(self) -> bool: ...
    @property
    def independentFilters(self) -> List[vim.vm.BaseIndependentFilterSpec]: ...


    class FlatVer1BackingInfo(VirtualDevice.FileBackingInfo):
        @property
        def diskMode(self) -> str: ...
        @property
        def split(self) -> bool: ...
        @property
        def writeThrough(self) -> bool: ...
        @property
        def contentId(self) -> str: ...
        @property
        def parent(self) -> VirtualDisk.FlatVer1BackingInfo: ...


    class FlatVer2BackingInfo(VirtualDevice.FileBackingInfo):
        @property
        def diskMode(self) -> str: ...
        @property
        def split(self) -> bool: ...
        @property
        def writeThrough(self) -> bool: ...
        @property
        def thinProvisioned(self) -> bool: ...
        @property
        def eagerlyScrub(self) -> bool: ...
        @property
        def uuid(self) -> str: ...
        @property
        def contentId(self) -> str: ...
        @property
        def changeId(self) -> str: ...
        @property
        def parent(self) -> VirtualDisk.FlatVer2BackingInfo: ...
        @property
        def deltaDiskFormat(self) -> str: ...
        @property
        def digestEnabled(self) -> bool: ...
        @property
        def deltaGrainSize(self) -> int: ...
        @property
        def deltaDiskFormatVariant(self) -> str: ...
        @property
        def sharing(self) -> str: ...
        @property
        def keyId(self) -> vim.encryption.CryptoKeyId: ...


    class LocalPMemBackingInfo(VirtualDevice.FileBackingInfo):
        @property
        def diskMode(self) -> str: ...
        @property
        def uuid(self) -> str: ...
        @property
        def volumeUUID(self) -> str: ...
        @property
        def contentId(self) -> str: ...


    class PartitionedRawDiskVer2BackingInfo(VirtualDisk.RawDiskVer2BackingInfo):
        @property
        def partition(self) -> List[int]: ...


    class RawDiskMappingVer1BackingInfo(VirtualDevice.FileBackingInfo):
        @property
        def lunUuid(self) -> str: ...
        @property
        def deviceName(self) -> str: ...
        @property
        def compatibilityMode(self) -> str: ...
        @property
        def diskMode(self) -> str: ...
        @property
        def uuid(self) -> str: ...
        @property
        def contentId(self) -> str: ...
        @property
        def changeId(self) -> str: ...
        @property
        def parent(self) -> VirtualDisk.RawDiskMappingVer1BackingInfo: ...
        @property
        def deltaDiskFormat(self) -> str: ...
        @property
        def deltaGrainSize(self) -> int: ...
        @property
        def sharing(self) -> str: ...


    class RawDiskVer2BackingInfo(VirtualDevice.DeviceBackingInfo):
        @property
        def descriptorFileName(self) -> str: ...
        @property
        def uuid(self) -> str: ...
        @property
        def changeId(self) -> str: ...
        @property
        def sharing(self) -> str: ...


    class SeSparseBackingInfo(VirtualDevice.FileBackingInfo):
        @property
        def diskMode(self) -> str: ...
        @property
        def writeThrough(self) -> bool: ...
        @property
        def uuid(self) -> str: ...
        @property
        def contentId(self) -> str: ...
        @property
        def changeId(self) -> str: ...
        @property
        def parent(self) -> VirtualDisk.SeSparseBackingInfo: ...
        @property
        def deltaDiskFormat(self) -> str: ...
        @property
        def digestEnabled(self) -> bool: ...
        @property
        def grainSize(self) -> int: ...
        @property
        def keyId(self) -> vim.encryption.CryptoKeyId: ...


    class SparseVer1BackingInfo(VirtualDevice.FileBackingInfo):
        @property
        def diskMode(self) -> str: ...
        @property
        def split(self) -> bool: ...
        @property
        def writeThrough(self) -> bool: ...
        @property
        def spaceUsedInKB(self) -> long: ...
        @property
        def contentId(self) -> str: ...
        @property
        def parent(self) -> VirtualDisk.SparseVer1BackingInfo: ...


    class SparseVer2BackingInfo(VirtualDevice.FileBackingInfo):
        @property
        def diskMode(self) -> str: ...
        @property
        def split(self) -> bool: ...
        @property
        def writeThrough(self) -> bool: ...
        @property
        def spaceUsedInKB(self) -> long: ...
        @property
        def uuid(self) -> str: ...
        @property
        def contentId(self) -> str: ...
        @property
        def changeId(self) -> str: ...
        @property
        def parent(self) -> VirtualDisk.SparseVer2BackingInfo: ...
        @property
        def keyId(self) -> vim.encryption.CryptoKeyId: ...


    class VFlashCacheConfigInfo(vmodl.DynamicData):
        @property
        def vFlashModule(self) -> str: ...
        @property
        def reservationInMB(self) -> long: ...
        @property
        def cacheConsistencyType(self) -> str: ...
        @property
        def cacheMode(self) -> str: ...
        @property
        def blockSizeInKB(self) -> long: ...


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
    @property
    def diskId(self) -> int: ...


class VirtualDiskOption(VirtualDeviceOption):
    @property
    def capacityInKB(self) -> vim.option.LongOption: ...
    @property
    def ioAllocationOption(self) -> vim.StorageResourceManager.IOAllocationOption: ...
    @property
    def vFlashCacheConfigOption(self) -> VirtualDiskOption.VFlashCacheConfigOption: ...


    class DeltaDiskFormatsSupported(vmodl.DynamicData):
        @property
        def datastoreType(self) -> type: ...
        @property
        def deltaDiskFormat(self) -> vim.option.ChoiceOption: ...


    class FlatVer1BackingOption(VirtualDeviceOption.FileBackingOption):
        @property
        def diskMode(self) -> vim.option.ChoiceOption: ...
        @property
        def split(self) -> vim.option.BoolOption: ...
        @property
        def writeThrough(self) -> vim.option.BoolOption: ...
        @property
        def growable(self) -> bool: ...


    class FlatVer2BackingOption(VirtualDeviceOption.FileBackingOption):
        @property
        def diskMode(self) -> vim.option.ChoiceOption: ...
        @property
        def split(self) -> vim.option.BoolOption: ...
        @property
        def writeThrough(self) -> vim.option.BoolOption: ...
        @property
        def growable(self) -> bool: ...
        @property
        def hotGrowable(self) -> bool: ...
        @property
        def uuid(self) -> bool: ...
        @property
        def thinProvisioned(self) -> vim.option.BoolOption: ...
        @property
        def eagerlyScrub(self) -> vim.option.BoolOption: ...
        @property
        def deltaDiskFormat(self) -> vim.option.ChoiceOption: ...
        @property
        def deltaDiskFormatsSupported(self) -> List[VirtualDiskOption.DeltaDiskFormatsSupported]: ...


    class LocalPMemBackingOption(VirtualDeviceOption.FileBackingOption):
        @property
        def diskMode(self) -> vim.option.ChoiceOption: ...
        @property
        def growable(self) -> bool: ...
        @property
        def hotGrowable(self) -> bool: ...
        @property
        def uuid(self) -> bool: ...


    class PartitionedRawDiskVer2BackingOption(VirtualDiskOption.RawDiskVer2BackingOption): ...


    class RawDiskMappingVer1BackingOption(VirtualDeviceOption.DeviceBackingOption):
        @property
        def descriptorFileNameExtensions(self) -> vim.option.ChoiceOption: ...
        @property
        def compatibilityMode(self) -> vim.option.ChoiceOption: ...
        @property
        def diskMode(self) -> vim.option.ChoiceOption: ...
        @property
        def uuid(self) -> bool: ...


    class RawDiskVer2BackingOption(VirtualDeviceOption.DeviceBackingOption):
        @property
        def descriptorFileNameExtensions(self) -> vim.option.ChoiceOption: ...
        @property
        def uuid(self) -> bool: ...


    class SeSparseBackingOption(VirtualDeviceOption.FileBackingOption):
        @property
        def diskMode(self) -> vim.option.ChoiceOption: ...
        @property
        def writeThrough(self) -> vim.option.BoolOption: ...
        @property
        def growable(self) -> bool: ...
        @property
        def hotGrowable(self) -> bool: ...
        @property
        def uuid(self) -> bool: ...
        @property
        def deltaDiskFormatsSupported(self) -> List[VirtualDiskOption.DeltaDiskFormatsSupported]: ...


    class SparseVer1BackingOption(VirtualDeviceOption.FileBackingOption):
        @property
        def diskModes(self) -> vim.option.ChoiceOption: ...
        @property
        def split(self) -> vim.option.BoolOption: ...
        @property
        def writeThrough(self) -> vim.option.BoolOption: ...
        @property
        def growable(self) -> bool: ...


    class SparseVer2BackingOption(VirtualDeviceOption.FileBackingOption):
        @property
        def diskMode(self) -> vim.option.ChoiceOption: ...
        @property
        def split(self) -> vim.option.BoolOption: ...
        @property
        def writeThrough(self) -> vim.option.BoolOption: ...
        @property
        def growable(self) -> bool: ...
        @property
        def hotGrowable(self) -> bool: ...
        @property
        def uuid(self) -> bool: ...


    class VFlashCacheConfigOption(vmodl.DynamicData):
        @property
        def cacheConsistencyType(self) -> vim.option.ChoiceOption: ...
        @property
        def cacheMode(self) -> vim.option.ChoiceOption: ...
        @property
        def reservationInMB(self) -> vim.option.LongOption: ...
        @property
        def blockSizeInKB(self) -> vim.option.LongOption: ...


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
    @property
    def migrateCache(self) -> bool: ...


class VirtualE1000(VirtualEthernetCard): ...


class VirtualE1000Option(VirtualEthernetCardOption): ...


class VirtualE1000e(VirtualEthernetCard): ...


class VirtualE1000eOption(VirtualEthernetCardOption): ...


class VirtualEnsoniq1371(VirtualSoundCard): ...


class VirtualEnsoniq1371Option(VirtualSoundCardOption): ...


class VirtualEthernetCard(VirtualDevice):
    @property
    def addressType(self) -> str: ...
    @property
    def macAddress(self) -> str: ...
    @property
    def wakeOnLanEnabled(self) -> bool: ...
    @property
    def resourceAllocation(self) -> VirtualEthernetCard.ResourceAllocation: ...
    @property
    def externalId(self) -> str: ...
    @property
    def uptCompatibilityEnabled(self) -> bool: ...


    class DistributedVirtualPortBackingInfo(VirtualDevice.BackingInfo):
        @property
        def port(self) -> vim.dvs.PortConnection: ...


    class LegacyNetworkBackingInfo(VirtualDevice.DeviceBackingInfo): ...


    class NetworkBackingInfo(VirtualDevice.DeviceBackingInfo):
        @property
        def network(self) -> vim.Network: ...
        @property
        def inPassthroughMode(self) -> bool: ...


    class OpaqueNetworkBackingInfo(VirtualDevice.BackingInfo):
        @property
        def opaqueNetworkId(self) -> str: ...
        @property
        def opaqueNetworkType(self) -> str: ...


    class ResourceAllocation(vmodl.DynamicData):
        @property
        def reservation(self) -> long: ...
        @property
        def share(self) -> vim.SharesInfo: ...
        @property
        def limit(self) -> long: ...


class VirtualEthernetCardOption(VirtualDeviceOption):
    @property
    def supportedOUI(self) -> vim.option.ChoiceOption: ...
    @property
    def macType(self) -> vim.option.ChoiceOption: ...
    @property
    def wakeOnLanEnabled(self) -> vim.option.BoolOption: ...
    @property
    def vmDirectPathGen2Supported(self) -> bool: ...
    @property
    def uptCompatibilityEnabled(self) -> vim.option.BoolOption: ...


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
    @property
    def numIDECdroms(self) -> vim.option.IntOption: ...


class VirtualKeyboard(VirtualDevice): ...


class VirtualKeyboardOption(VirtualDeviceOption): ...


class VirtualLsiLogicController(VirtualSCSIController): ...


class VirtualLsiLogicControllerOption(VirtualSCSIControllerOption): ...


class VirtualLsiLogicSASController(VirtualSCSIController): ...


class VirtualLsiLogicSASControllerOption(VirtualSCSIControllerOption): ...


class VirtualNVDIMM(VirtualDevice):
    @property
    def capacityInMB(self) -> long: ...
    @property
    def configuredCapacityInMB(self) -> long: ...


    class BackingInfo(VirtualDevice.FileBackingInfo):
        @property
        def parent(self) -> VirtualNVDIMM.BackingInfo: ...
        @property
        def changeId(self) -> str: ...


class VirtualNVDIMMController(VirtualController): ...


class VirtualNVDIMMControllerOption(VirtualControllerOption):
    @property
    def numNVDIMMControllers(self) -> vim.option.IntOption: ...


class VirtualNVDIMMOption(VirtualDeviceOption):
    @property
    def capacityInMB(self) -> vim.option.LongOption: ...
    @property
    def growable(self) -> bool: ...
    @property
    def hotGrowable(self) -> bool: ...
    @property
    def granularityInMB(self) -> long: ...


class VirtualNVMEController(VirtualController): ...


class VirtualNVMEControllerOption(VirtualControllerOption):
    @property
    def numNVMEDisks(self) -> vim.option.IntOption: ...


class VirtualPCIController(VirtualController): ...


class VirtualPCIControllerOption(VirtualControllerOption):
    @property
    def numSCSIControllers(self) -> vim.option.IntOption: ...
    @property
    def numEthernetCards(self) -> vim.option.IntOption: ...
    @property
    def numVideoCards(self) -> vim.option.IntOption: ...
    @property
    def numSoundCards(self) -> vim.option.IntOption: ...
    @property
    def numVmiRoms(self) -> vim.option.IntOption: ...
    @property
    def numVmciDevices(self) -> vim.option.IntOption: ...
    @property
    def numPCIPassthroughDevices(self) -> vim.option.IntOption: ...
    @property
    def numSasSCSIControllers(self) -> vim.option.IntOption: ...
    @property
    def numVmxnet3EthernetCards(self) -> vim.option.IntOption: ...
    @property
    def numParaVirtualSCSIControllers(self) -> vim.option.IntOption: ...
    @property
    def numSATAControllers(self) -> vim.option.IntOption: ...
    @property
    def numNVMEControllers(self) -> vim.option.IntOption: ...
    @property
    def numVmxnet3VrdmaEthernetCards(self) -> vim.option.IntOption: ...


class VirtualPCIPassthrough(VirtualDevice):


    class AllowedDevice(vmodl.DynamicData):
        @property
        def vendorId(self) -> int: ...
        @property
        def deviceId(self) -> int: ...
        @property
        def subVendorId(self) -> int: ...
        @property
        def subDeviceId(self) -> int: ...
        @property
        def revisionId(self) -> short: ...


    class DeviceBackingInfo(VirtualDevice.DeviceBackingInfo):
        @property
        def id(self) -> str: ...
        @property
        def deviceId(self) -> str: ...
        @property
        def systemId(self) -> str: ...
        @property
        def vendorId(self) -> short: ...


    class DvxBackingInfo(VirtualDevice.BackingInfo):
        @property
        def deviceClass(self) -> str: ...
        @property
        def configParams(self) -> List[vim.option.OptionValue]: ...


    class DynamicBackingInfo(VirtualDevice.DeviceBackingInfo):
        @property
        def allowedDevice(self) -> List[VirtualPCIPassthrough.AllowedDevice]: ...
        @property
        def customLabel(self) -> str: ...
        @property
        def assignedId(self) -> str: ...


    class PluginBackingInfo(VirtualDevice.BackingInfo): ...


    class VmiopBackingInfo(VirtualPCIPassthrough.PluginBackingInfo):
        @property
        def vgpu(self) -> str: ...
        @property
        def vgpuMigrateDataSizeMB(self) -> int: ...
        @property
        def migrateSupported(self) -> bool: ...
        @property
        def enhancedMigrateCapability(self) -> bool: ...


class VirtualPCIPassthroughOption(VirtualDeviceOption):


    class DeviceBackingOption(VirtualDeviceOption.DeviceBackingOption): ...


    class DvxBackingOption(VirtualDeviceOption.BackingOption): ...


    class DynamicBackingOption(VirtualDeviceOption.DeviceBackingOption): ...


    class PluginBackingOption(VirtualDeviceOption.BackingOption): ...


    class VmiopBackingOption(VirtualPCIPassthroughOption.PluginBackingOption):
        @property
        def vgpu(self) -> vim.option.StringOption: ...
        @property
        def maxInstances(self) -> int: ...


class VirtualPCNet32(VirtualEthernetCard): ...


class VirtualPCNet32Option(VirtualEthernetCardOption):
    @property
    def supportsMorphing(self) -> bool: ...


class VirtualPS2Controller(VirtualController): ...


class VirtualPS2ControllerOption(VirtualControllerOption):
    @property
    def numKeyboards(self) -> vim.option.IntOption: ...
    @property
    def numPointingDevices(self) -> vim.option.IntOption: ...


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


class VirtualPointingDeviceOption(VirtualDeviceOption):


    class DeviceBackingOption(VirtualDeviceOption.DeviceBackingOption):
        @property
        def hostPointingDevice(self) -> vim.option.ChoiceOption: ...


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


class VirtualPrecisionClockOption(VirtualDeviceOption):


    class SystemClockBackingOption(VirtualDeviceOption.BackingOption):
        @property
        def protocol(self) -> vim.option.ChoiceOption: ...


class VirtualSATAController(VirtualController): ...


class VirtualSATAControllerOption(VirtualControllerOption):
    @property
    def numSATADisks(self) -> vim.option.IntOption: ...
    @property
    def numSATACdroms(self) -> vim.option.IntOption: ...


class VirtualSCSIController(VirtualController):
    @property
    def hotAddRemove(self) -> bool: ...
    @property
    def sharedBus(self) -> VirtualSCSIController.Sharing: ...
    @property
    def scsiCtlrUnitNumber(self) -> int: ...


class VirtualSCSIControllerOption(VirtualControllerOption):
    @property
    def numSCSIDisks(self) -> vim.option.IntOption: ...
    @property
    def numSCSICdroms(self) -> vim.option.IntOption: ...
    @property
    def numSCSIPassthrough(self) -> vim.option.IntOption: ...
    @property
    def sharing(self) -> List[VirtualSCSIController.Sharing]: ...
    @property
    def defaultSharedIndex(self) -> int: ...
    @property
    def hotAddRemove(self) -> vim.option.BoolOption: ...
    @property
    def scsiCtlrUnitNumber(self) -> int: ...


class VirtualSCSIPassthrough(VirtualDevice):


    class DeviceBackingInfo(VirtualDevice.DeviceBackingInfo): ...


class VirtualSCSIPassthroughOption(VirtualDeviceOption):


    class DeviceBackingOption(VirtualDeviceOption.DeviceBackingOption): ...


class VirtualSIOController(VirtualController): ...


class VirtualSIOControllerOption(VirtualControllerOption):
    @property
    def numFloppyDrives(self) -> vim.option.IntOption: ...
    @property
    def numSerialPorts(self) -> vim.option.IntOption: ...
    @property
    def numParallelPorts(self) -> vim.option.IntOption: ...


class VirtualSerialPort(VirtualDevice):
    @property
    def yieldOnPoll(self) -> bool: ...


    class DeviceBackingInfo(VirtualDevice.DeviceBackingInfo): ...


    class FileBackingInfo(VirtualDevice.FileBackingInfo): ...


    class PipeBackingInfo(VirtualDevice.PipeBackingInfo):
        @property
        def endpoint(self) -> str: ...
        @property
        def noRxLoss(self) -> bool: ...


    class ThinPrintBackingInfo(VirtualDevice.BackingInfo): ...


    class URIBackingInfo(VirtualDevice.URIBackingInfo): ...


class VirtualSerialPortOption(VirtualDeviceOption):
    @property
    def yieldOnPoll(self) -> vim.option.BoolOption: ...


    class DeviceBackingOption(VirtualDeviceOption.DeviceBackingOption): ...


    class FileBackingOption(VirtualDeviceOption.FileBackingOption): ...


    class PipeBackingOption(VirtualDeviceOption.PipeBackingOption):
        @property
        def endpoint(self) -> vim.option.ChoiceOption: ...
        @property
        def noRxLoss(self) -> vim.option.BoolOption: ...


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
    @property
    def sriovBacking(self) -> VirtualSriovEthernetCard.SriovBackingInfo: ...
    @property
    def dvxBackingInfo(self) -> VirtualPCIPassthrough.DvxBackingInfo: ...


    class SriovBackingInfo(VirtualDevice.BackingInfo):
        @property
        def physicalFunctionBacking(self) -> VirtualPCIPassthrough.DeviceBackingInfo: ...
        @property
        def virtualFunctionBacking(self) -> VirtualPCIPassthrough.DeviceBackingInfo: ...
        @property
        def virtualFunctionIndex(self) -> int: ...


class VirtualSriovEthernetCardOption(VirtualEthernetCardOption):


    class SriovBackingOption(VirtualDeviceOption.BackingOption): ...


class VirtualTPM(VirtualDevice):
    @property
    def endorsementKeyCertificateSigningRequest(self) -> List[binary]: ...
    @property
    def endorsementKeyCertificate(self) -> List[binary]: ...


class VirtualTPMOption(VirtualDeviceOption):
    @property
    def supportedFirmware(self) -> List[str]: ...


class VirtualUSB(VirtualDevice):
    @property
    def connected(self) -> bool: ...
    @property
    def vendor(self) -> int: ...
    @property
    def product(self) -> int: ...
    @property
    def family(self) -> List[str]: ...
    @property
    def speed(self) -> List[str]: ...


    class RemoteClientBackingInfo(VirtualDevice.RemoteDeviceBackingInfo):
        @property
        def hostname(self) -> str: ...


    class RemoteHostBackingInfo(VirtualDevice.DeviceBackingInfo):
        @property
        def hostname(self) -> str: ...


    class USBBackingInfo(VirtualDevice.DeviceBackingInfo): ...


class VirtualUSBController(VirtualController):
    @property
    def autoConnectDevices(self) -> bool: ...
    @property
    def ehciEnabled(self) -> bool: ...


    class PciBusSlotInfo(VirtualDevice.PciBusSlotInfo):
        @property
        def ehciPciSlotNumber(self) -> int: ...


class VirtualUSBControllerOption(VirtualControllerOption):
    @property
    def autoConnectDevices(self) -> vim.option.BoolOption: ...
    @property
    def ehciSupported(self) -> vim.option.BoolOption: ...
    @property
    def supportedSpeeds(self) -> List[str]: ...


class VirtualUSBOption(VirtualDeviceOption):


    class RemoteClientBackingOption(VirtualDeviceOption.RemoteDeviceBackingOption): ...


    class RemoteHostBackingOption(VirtualDeviceOption.DeviceBackingOption): ...


    class USBBackingOption(VirtualDeviceOption.DeviceBackingOption): ...


class VirtualUSBXHCIController(VirtualController):
    @property
    def autoConnectDevices(self) -> bool: ...


class VirtualUSBXHCIControllerOption(VirtualControllerOption):
    @property
    def autoConnectDevices(self) -> vim.option.BoolOption: ...
    @property
    def supportedSpeeds(self) -> List[str]: ...


class VirtualVMCIDevice(VirtualDevice):
    @property
    def id(self) -> long: ...
    @property
    def allowUnrestrictedCommunication(self) -> bool: ...
    @property
    def filterEnable(self) -> bool: ...
    @property
    def filterInfo(self) -> VirtualVMCIDevice.FilterInfo: ...


    class FilterInfo(vmodl.DynamicData):
        @property
        def filters(self) -> List[VirtualVMCIDevice.FilterSpec]: ...


    class FilterSpec(vmodl.DynamicData):
        @property
        def rank(self) -> long: ...
        @property
        def action(self) -> str: ...
        @property
        def protocol(self) -> str: ...
        @property
        def direction(self) -> str: ...
        @property
        def lowerDstPortBoundary(self) -> long: ...
        @property
        def upperDstPortBoundary(self) -> long: ...


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
    @property
    def filterSpecOption(self) -> VirtualVMCIDeviceOption.FilterSpecOption: ...
    @property
    def filterSupported(self) -> vim.option.BoolOption: ...


    class FilterSpecOption(vmodl.DynamicData):
        @property
        def action(self) -> vim.option.ChoiceOption: ...
        @property
        def protocol(self) -> vim.option.ChoiceOption: ...
        @property
        def direction(self) -> vim.option.ChoiceOption: ...
        @property
        def lowerDstPortBoundary(self) -> vim.option.LongOption: ...
        @property
        def upperDstPortBoundary(self) -> vim.option.LongOption: ...


class VirtualVMIROM(VirtualDevice): ...


class VirtualVMIROMOption(VirtualDeviceOption): ...


class VirtualVideoCard(VirtualDevice):
    @property
    def videoRamSizeInKB(self) -> long: ...
    @property
    def numDisplays(self) -> int: ...
    @property
    def useAutoDetect(self) -> bool: ...
    @property
    def enable3DSupport(self) -> bool: ...
    @property
    def use3dRenderer(self) -> str: ...
    @property
    def graphicsMemorySizeInKB(self) -> long: ...


    class Use3dRenderer(Enum):
        automatic = "automatic"
        software = "software"
        hardware = "hardware"


class VirtualVideoCardOption(VirtualDeviceOption):
    @property
    def videoRamSizeInKB(self) -> vim.option.LongOption: ...
    @property
    def numDisplays(self) -> vim.option.IntOption: ...
    @property
    def useAutoDetect(self) -> vim.option.BoolOption: ...
    @property
    def support3D(self) -> vim.option.BoolOption: ...
    @property
    def use3dRendererSupported(self) -> vim.option.BoolOption: ...
    @property
    def graphicsMemorySizeInKB(self) -> vim.option.LongOption: ...
    @property
    def graphicsMemorySizeSupported(self) -> vim.option.BoolOption: ...


class VirtualVmxnet(VirtualEthernetCard): ...


class VirtualVmxnet2(VirtualVmxnet): ...


class VirtualVmxnet2Option(VirtualVmxnetOption): ...


class VirtualVmxnet3(VirtualVmxnet):
    @property
    def uptv2Enabled(self) -> bool: ...


class VirtualVmxnet3Option(VirtualVmxnetOption):
    @property
    def uptv2Enabled(self) -> vim.option.BoolOption: ...


class VirtualVmxnet3Vrdma(VirtualVmxnet3):
    @property
    def deviceProtocol(self) -> str: ...


class VirtualVmxnet3VrdmaOption(VirtualVmxnet3Option):
    @property
    def deviceProtocol(self) -> vim.option.ChoiceOption: ...


    class DeviceProtocols(Enum):
        rocev1 = "rocev1"
        rocev2 = "rocev2"


class VirtualVmxnetOption(VirtualEthernetCardOption): ...


class VirtualWDT(VirtualDevice):
    @property
    def runOnBoot(self) -> bool: ...
    @property
    def running(self) -> bool: ...


class VirtualWDTOption(VirtualDeviceOption):
    @property
    def runOnBoot(self) -> vim.option.BoolOption: ...