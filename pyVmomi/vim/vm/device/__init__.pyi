# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vim
import pyVmomi.vmodl
import pyVmomi.vim.dvs
import pyVmomi.vim.encryption
import pyVmomi.vim.option
import pyVmomi.vim.vm
import pyVmomi.vim.vslm



class HostDiskMappingInfo(pyVmomi.vmodl.DynamicData):
   class PartitionInfo(pyVmomi.vmodl.DynamicData):
      name: str
      fileSystem: str
      capacityInKb: pyVmomi.VmomiSupport.long

   physicalPartition: _typing.Optional[PartitionInfo] = None
   name: str
   exclusive: _typing.Optional[bool] = None


class HostDiskMappingOption(pyVmomi.vmodl.DynamicData):
   class PartitionOption(pyVmomi.vmodl.DynamicData):
      name: str
      fileSystem: str
      capacityInKb: pyVmomi.VmomiSupport.long

   physicalPartition: list[PartitionOption] = []
   name: str

class ParaVirtualSCSIController(VirtualSCSIController):
   pass

class ParaVirtualSCSIControllerOption(VirtualSCSIControllerOption):
   pass

class VirtualAHCIController(VirtualSATAController):
   pass

class VirtualAHCIControllerOption(VirtualSATAControllerOption):
   pass

class VirtualBusLogicController(VirtualSCSIController):
   pass

class VirtualBusLogicControllerOption(VirtualSCSIControllerOption):
   pass

class VirtualCdrom(VirtualDevice):
   class IsoBackingInfo(VirtualDevice.FileBackingInfo):
      pass

   class PassthroughBackingInfo(VirtualDevice.DeviceBackingInfo):
      exclusive: bool

   class RemotePassthroughBackingInfo(VirtualDevice.RemoteDeviceBackingInfo):
      exclusive: bool

   class AtapiBackingInfo(VirtualDevice.DeviceBackingInfo):
      pass

   class RemoteAtapiBackingInfo(VirtualDevice.RemoteDeviceBackingInfo):
      pass


class VirtualCdromOption(VirtualDeviceOption):
   class IsoBackingOption(VirtualDeviceOption.FileBackingOption):
      pass

   class PassthroughBackingOption(VirtualDeviceOption.DeviceBackingOption):
      exclusive: pyVmomi.vim.option.BoolOption

   class RemotePassthroughBackingOption(VirtualDeviceOption.RemoteDeviceBackingOption):
      exclusive: pyVmomi.vim.option.BoolOption

   class AtapiBackingOption(VirtualDeviceOption.DeviceBackingOption):
      pass

   class RemoteAtapiBackingOption(VirtualDeviceOption.DeviceBackingOption):
      pass


class VirtualController(VirtualDevice):
   busNumber: int
   device: list[int] = []


class VirtualControllerOption(VirtualDeviceOption):
   devices: pyVmomi.vim.option.IntOption
   supportedDevice: list[type] = []


class VirtualDevice(pyVmomi.vmodl.DynamicData):
   class BackingInfo(pyVmomi.vmodl.DynamicData):
      pass

   class FileBackingInfo(BackingInfo):
      fileName: str
      datastore: _typing.Optional[pyVmomi.vim.Datastore] = None
      backingObjectId: _typing.Optional[str] = None

   class DeviceBackingInfo(BackingInfo):
      deviceName: str
      useAutoDetect: _typing.Optional[bool] = None

   class RemoteDeviceBackingInfo(BackingInfo):
      deviceName: str
      useAutoDetect: _typing.Optional[bool] = None

   class PipeBackingInfo(BackingInfo):
      pipeName: str

   class URIBackingInfo(BackingInfo):
      serviceURI: str
      direction: str
      proxyURI: _typing.Optional[str] = None

   class ConnectInfo(pyVmomi.vmodl.DynamicData):
      class Status(pyVmomi.VmomiSupport.Enum):
         ok: _typing.ClassVar['Status'] = 'ok'
         recoverableError: _typing.ClassVar['Status'] = 'recoverableError'
         unrecoverableError: _typing.ClassVar['Status'] = 'unrecoverableError'
         untried: _typing.ClassVar['Status'] = 'untried'

      class MigrateConnectOp(pyVmomi.VmomiSupport.Enum):
         connect: _typing.ClassVar['MigrateConnectOp'] = 'connect'
         disconnect: _typing.ClassVar['MigrateConnectOp'] = 'disconnect'
         unset: _typing.ClassVar['MigrateConnectOp'] = 'unset'

      migrateConnect: _typing.Optional[str] = None
      startConnected: bool
      allowGuestControl: bool
      connected: bool
      status: _typing.Optional[str] = None

   class BusSlotInfo(pyVmomi.vmodl.DynamicData):
      pass

   class PciBusSlotInfo(BusSlotInfo):
      pciSlotNumber: int

   class DeviceGroupInfo(pyVmomi.vmodl.DynamicData):
      groupInstanceKey: int
      sequenceId: int

   key: int
   deviceInfo: _typing.Optional[pyVmomi.vim.Description] = None
   backing: _typing.Optional[BackingInfo] = None
   connectable: _typing.Optional[ConnectInfo] = None
   slotInfo: _typing.Optional[BusSlotInfo] = None
   controllerKey: _typing.Optional[int] = None
   unitNumber: _typing.Optional[int] = None
   numaNode: _typing.Optional[int] = None
   deviceGroupInfo: _typing.Optional[DeviceGroupInfo] = None


class VirtualDeviceOption(pyVmomi.vmodl.DynamicData):
   class BackingOption(pyVmomi.vmodl.DynamicData):
      type: type

   class FileBackingOption(BackingOption):
      class FileExtension(pyVmomi.VmomiSupport.Enum):
         iso: _typing.ClassVar['FileExtension'] = 'iso'
         flp: _typing.ClassVar['FileExtension'] = 'flp'
         vmdk: _typing.ClassVar['FileExtension'] = 'vmdk'
         dsk: _typing.ClassVar['FileExtension'] = 'dsk'
         rdm: _typing.ClassVar['FileExtension'] = 'rdm'

      fileNameExtensions: _typing.Optional[pyVmomi.vim.option.ChoiceOption] = None

   class DeviceBackingOption(BackingOption):
      autoDetectAvailable: pyVmomi.vim.option.BoolOption

   class RemoteDeviceBackingOption(BackingOption):
      autoDetectAvailable: pyVmomi.vim.option.BoolOption

   class PipeBackingOption(BackingOption):
      pass

   class URIBackingOption(BackingOption):
      class Direction(pyVmomi.VmomiSupport.Enum):
         server: _typing.ClassVar['Direction'] = 'server'
         client: _typing.ClassVar['Direction'] = 'client'

      directions: pyVmomi.vim.option.ChoiceOption

   class ConnectOption(pyVmomi.vmodl.DynamicData):
      startConnected: pyVmomi.vim.option.BoolOption
      allowGuestControl: pyVmomi.vim.option.BoolOption

   class BusSlotOption(pyVmomi.vmodl.DynamicData):
      type: type

   type: type
   connectOption: _typing.Optional[ConnectOption] = None
   busSlotOption: _typing.Optional[BusSlotOption] = None
   controllerType: _typing.Optional[type] = None
   autoAssignController: _typing.Optional[pyVmomi.vim.option.BoolOption] = None
   backingOption: list[BackingOption] = []
   defaultBackingOptionIndex: _typing.Optional[int] = None
   licensingLimit: list[pyVmomi.VmomiSupport.PropertyPath] = []
   deprecated: bool
   plugAndPlay: bool
   hotRemoveSupported: bool
   numaSupported: _typing.Optional[bool] = None


class VirtualDeviceSpec(pyVmomi.vmodl.DynamicData):
   class Operation(pyVmomi.VmomiSupport.Enum):
      add: _typing.ClassVar['Operation'] = 'add'
      remove: _typing.ClassVar['Operation'] = 'remove'
      edit: _typing.ClassVar['Operation'] = 'edit'

   class FileOperation(pyVmomi.VmomiSupport.Enum):
      create: _typing.ClassVar['FileOperation'] = 'create'
      destroy: _typing.ClassVar['FileOperation'] = 'destroy'
      replace: _typing.ClassVar['FileOperation'] = 'replace'

   class BackingSpec(pyVmomi.vmodl.DynamicData):
      parent: _typing.Optional[BackingSpec] = None
      crypto: _typing.Optional[pyVmomi.vim.encryption.CryptoSpec] = None

   class ChangeMode(pyVmomi.VmomiSupport.Enum):
      fail: _typing.ClassVar['ChangeMode'] = 'fail'
      skip: _typing.ClassVar['ChangeMode'] = 'skip'

   operation: _typing.Optional[Operation] = None
   fileOperation: _typing.Optional[FileOperation] = None
   device: VirtualDevice
   profile: list[pyVmomi.vim.vm.ProfileSpec] = []
   backing: _typing.Optional[BackingSpec] = None
   filterSpec: list[pyVmomi.vim.vm.BaseIndependentFilterSpec] = []
   changeMode: _typing.Optional[str] = None


class VirtualDisk(VirtualDevice):
   class DeltaDiskFormat(pyVmomi.VmomiSupport.Enum):
      redoLogFormat: _typing.ClassVar['DeltaDiskFormat'] = 'redoLogFormat'
      nativeFormat: _typing.ClassVar['DeltaDiskFormat'] = 'nativeFormat'
      seSparseFormat: _typing.ClassVar['DeltaDiskFormat'] = 'seSparseFormat'

   class DeltaDiskFormatVariant(pyVmomi.VmomiSupport.Enum):
      vmfsSparseVariant: _typing.ClassVar['DeltaDiskFormatVariant'] = 'vmfsSparseVariant'
      vsanSparseVariant: _typing.ClassVar['DeltaDiskFormatVariant'] = 'vsanSparseVariant'

   class DiskChainBrokenIssue(pyVmomi.VmomiSupport.Enum):
      noIssue: _typing.ClassVar['DiskChainBrokenIssue'] = 'noIssue'
      cidMismatch: _typing.ClassVar['DiskChainBrokenIssue'] = 'cidMismatch'

   class Sharing(pyVmomi.VmomiSupport.Enum):
      sharingNone: _typing.ClassVar['Sharing'] = 'sharingNone'
      sharingMultiWriter: _typing.ClassVar['Sharing'] = 'sharingMultiWriter'

   class SparseVer1BackingInfo(VirtualDevice.FileBackingInfo):
      diskMode: str
      split: _typing.Optional[bool] = None
      writeThrough: _typing.Optional[bool] = None
      spaceUsedInKB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      contentId: _typing.Optional[str] = None
      parent: _typing.Optional[SparseVer1BackingInfo] = None

   class SparseVer2BackingInfo(VirtualDevice.FileBackingInfo):
      diskMode: str
      split: _typing.Optional[bool] = None
      writeThrough: _typing.Optional[bool] = None
      spaceUsedInKB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      uuid: _typing.Optional[str] = None
      contentId: _typing.Optional[str] = None
      changeId: _typing.Optional[str] = None
      parent: _typing.Optional[SparseVer2BackingInfo] = None
      keyId: _typing.Optional[pyVmomi.vim.encryption.CryptoKeyId] = None

   class FlatVer1BackingInfo(VirtualDevice.FileBackingInfo):
      diskMode: str
      split: _typing.Optional[bool] = None
      writeThrough: _typing.Optional[bool] = None
      contentId: _typing.Optional[str] = None
      parent: _typing.Optional[FlatVer1BackingInfo] = None

   class FlatVer2BackingInfo(VirtualDevice.FileBackingInfo):
      diskMode: str
      split: _typing.Optional[bool] = None
      writeThrough: _typing.Optional[bool] = None
      thinProvisioned: _typing.Optional[bool] = None
      eagerlyScrub: _typing.Optional[bool] = None
      uuid: _typing.Optional[str] = None
      contentId: _typing.Optional[str] = None
      changeId: _typing.Optional[str] = None
      parent: _typing.Optional[FlatVer2BackingInfo] = None
      deltaDiskFormat: _typing.Optional[str] = None
      digestEnabled: _typing.Optional[bool] = None
      deltaGrainSize: _typing.Optional[int] = None
      deltaDiskFormatVariant: _typing.Optional[str] = None
      sharing: _typing.Optional[str] = None
      keyId: _typing.Optional[pyVmomi.vim.encryption.CryptoKeyId] = None

   class SeSparseBackingInfo(VirtualDevice.FileBackingInfo):
      diskMode: str
      writeThrough: _typing.Optional[bool] = None
      uuid: _typing.Optional[str] = None
      contentId: _typing.Optional[str] = None
      changeId: _typing.Optional[str] = None
      parent: _typing.Optional[SeSparseBackingInfo] = None
      deltaDiskFormat: _typing.Optional[str] = None
      digestEnabled: _typing.Optional[bool] = None
      grainSize: _typing.Optional[int] = None
      keyId: _typing.Optional[pyVmomi.vim.encryption.CryptoKeyId] = None

   class RawDiskVer2BackingInfo(VirtualDevice.DeviceBackingInfo):
      descriptorFileName: str
      uuid: _typing.Optional[str] = None
      changeId: _typing.Optional[str] = None
      sharing: _typing.Optional[str] = None

   class PartitionedRawDiskVer2BackingInfo(RawDiskVer2BackingInfo):
      partition: list[int] = []

   class RawDiskMappingVer1BackingInfo(VirtualDevice.FileBackingInfo):
      lunUuid: _typing.Optional[str] = None
      deviceName: _typing.Optional[str] = None
      compatibilityMode: _typing.Optional[str] = None
      diskMode: _typing.Optional[str] = None
      uuid: _typing.Optional[str] = None
      contentId: _typing.Optional[str] = None
      changeId: _typing.Optional[str] = None
      parent: _typing.Optional[RawDiskMappingVer1BackingInfo] = None
      deltaDiskFormat: _typing.Optional[str] = None
      deltaGrainSize: _typing.Optional[int] = None
      sharing: _typing.Optional[str] = None

   class LocalPMemBackingInfo(VirtualDevice.FileBackingInfo):
      diskMode: str
      uuid: _typing.Optional[str] = None
      volumeUUID: _typing.Optional[str] = None
      contentId: _typing.Optional[str] = None

   class VFlashCacheConfigInfo(pyVmomi.vmodl.DynamicData):
      class CacheConsistencyType(pyVmomi.VmomiSupport.Enum):
         strong: _typing.ClassVar['CacheConsistencyType'] = 'strong'
         weak: _typing.ClassVar['CacheConsistencyType'] = 'weak'

      class CacheMode(pyVmomi.VmomiSupport.Enum):
         write_thru: _typing.ClassVar['CacheMode'] = 'write_thru'
         write_back: _typing.ClassVar['CacheMode'] = 'write_back'

      vFlashModule: _typing.Optional[str] = None
      reservationInMB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      cacheConsistencyType: _typing.Optional[str] = None
      cacheMode: _typing.Optional[str] = None
      blockSizeInKB: _typing.Optional[pyVmomi.VmomiSupport.long] = None

   capacityInKB: pyVmomi.VmomiSupport.long
   capacityInBytes: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   shares: _typing.Optional[pyVmomi.vim.SharesInfo] = None
   storageIOAllocation: _typing.Optional[pyVmomi.vim.StorageResourceManager.IOAllocationInfo] = None
   diskObjectId: _typing.Optional[str] = None
   vFlashCacheConfigInfo: _typing.Optional[VFlashCacheConfigInfo] = None
   iofilter: list[str] = []
   vDiskId: _typing.Optional[pyVmomi.vim.vslm.ID] = None
   vDiskVersion: _typing.Optional[int] = None
   virtualDiskFormat: _typing.Optional[str] = None
   nativeUnmanagedLinkedClone: _typing.Optional[bool] = None
   independentFilters: list[pyVmomi.vim.vm.BaseIndependentFilterSpec] = []
   guestReadOnly: _typing.Optional[bool] = None
   diskChainBrokenIssue: _typing.Optional[str] = None


class VirtualDiskId(pyVmomi.vmodl.DynamicData):
   vm: pyVmomi.vim.VirtualMachine
   diskId: int


class VirtualDiskOption(VirtualDeviceOption):
   class DiskMode(pyVmomi.VmomiSupport.Enum):
      persistent: _typing.ClassVar['DiskMode'] = 'persistent'
      nonpersistent: _typing.ClassVar['DiskMode'] = 'nonpersistent'
      undoable: _typing.ClassVar['DiskMode'] = 'undoable'
      independent_persistent: _typing.ClassVar['DiskMode'] = 'independent_persistent'
      independent_nonpersistent: _typing.ClassVar['DiskMode'] = 'independent_nonpersistent'
      append: _typing.ClassVar['DiskMode'] = 'append'

   class CompatibilityMode(pyVmomi.VmomiSupport.Enum):
      virtualMode: _typing.ClassVar['CompatibilityMode'] = 'virtualMode'
      physicalMode: _typing.ClassVar['CompatibilityMode'] = 'physicalMode'

   class SparseVer1BackingOption(VirtualDeviceOption.FileBackingOption):
      diskModes: pyVmomi.vim.option.ChoiceOption
      split: pyVmomi.vim.option.BoolOption
      writeThrough: pyVmomi.vim.option.BoolOption
      growable: bool

   class SparseVer2BackingOption(VirtualDeviceOption.FileBackingOption):
      diskMode: pyVmomi.vim.option.ChoiceOption
      split: pyVmomi.vim.option.BoolOption
      writeThrough: pyVmomi.vim.option.BoolOption
      growable: bool
      hotGrowable: bool
      uuid: bool
      virtualDiskFormat: _typing.Optional[pyVmomi.vim.option.ChoiceOption] = None

   class FlatVer1BackingOption(VirtualDeviceOption.FileBackingOption):
      diskMode: pyVmomi.vim.option.ChoiceOption
      split: pyVmomi.vim.option.BoolOption
      writeThrough: pyVmomi.vim.option.BoolOption
      growable: bool

   class DeltaDiskFormatsSupported(pyVmomi.vmodl.DynamicData):
      datastoreType: type
      deltaDiskFormat: pyVmomi.vim.option.ChoiceOption

   class FlatVer2BackingOption(VirtualDeviceOption.FileBackingOption):
      diskMode: pyVmomi.vim.option.ChoiceOption
      split: pyVmomi.vim.option.BoolOption
      writeThrough: pyVmomi.vim.option.BoolOption
      growable: bool
      hotGrowable: bool
      uuid: bool
      thinProvisioned: pyVmomi.vim.option.BoolOption
      eagerlyScrub: pyVmomi.vim.option.BoolOption
      deltaDiskFormat: pyVmomi.vim.option.ChoiceOption
      deltaDiskFormatsSupported: list[DeltaDiskFormatsSupported] = []
      virtualDiskFormat: _typing.Optional[pyVmomi.vim.option.ChoiceOption] = None

   class SeSparseBackingOption(VirtualDeviceOption.FileBackingOption):
      diskMode: pyVmomi.vim.option.ChoiceOption
      writeThrough: pyVmomi.vim.option.BoolOption
      growable: bool
      hotGrowable: bool
      uuid: bool
      deltaDiskFormatsSupported: list[DeltaDiskFormatsSupported] = []
      virtualDiskFormat: _typing.Optional[pyVmomi.vim.option.ChoiceOption] = None

   class RawDiskVer2BackingOption(VirtualDeviceOption.DeviceBackingOption):
      descriptorFileNameExtensions: pyVmomi.vim.option.ChoiceOption
      uuid: bool

   class PartitionedRawDiskVer2BackingOption(RawDiskVer2BackingOption):
      pass

   class RawDiskMappingVer1BackingOption(VirtualDeviceOption.DeviceBackingOption):
      descriptorFileNameExtensions: _typing.Optional[pyVmomi.vim.option.ChoiceOption] = None
      compatibilityMode: pyVmomi.vim.option.ChoiceOption
      diskMode: pyVmomi.vim.option.ChoiceOption
      uuid: bool
      virtualDiskFormat: _typing.Optional[pyVmomi.vim.option.ChoiceOption] = None

   class LocalPMemBackingOption(VirtualDeviceOption.FileBackingOption):
      diskMode: pyVmomi.vim.option.ChoiceOption
      growable: bool
      hotGrowable: bool
      uuid: bool

   class VFlashCacheConfigOption(pyVmomi.vmodl.DynamicData):
      cacheConsistencyType: pyVmomi.vim.option.ChoiceOption
      cacheMode: pyVmomi.vim.option.ChoiceOption
      reservationInMB: pyVmomi.vim.option.LongOption
      blockSizeInKB: pyVmomi.vim.option.LongOption

   capacityInKB: pyVmomi.vim.option.LongOption
   ioAllocationOption: pyVmomi.vim.StorageResourceManager.IOAllocationOption
   vFlashCacheConfigOption: _typing.Optional[VFlashCacheConfigOption] = None


class VirtualDiskSpec(VirtualDeviceSpec):
   diskMoveType: _typing.Optional[str] = None
   migrateCache: _typing.Optional[bool] = None

class VirtualE1000(VirtualEthernetCard):
   pass

class VirtualE1000Option(VirtualEthernetCardOption):
   pass

class VirtualE1000e(VirtualEthernetCard):
   pass

class VirtualE1000eOption(VirtualEthernetCardOption):
   pass

class VirtualEnsoniq1371(VirtualSoundCard):
   pass

class VirtualEnsoniq1371Option(VirtualSoundCardOption):
   pass


class VirtualEthernetCard(VirtualDevice):
   class NetworkBackingInfo(VirtualDevice.DeviceBackingInfo):
      network: _typing.Optional[pyVmomi.vim.Network] = None
      inPassthroughMode: _typing.Optional[bool] = None

   class LegacyNetworkBackingInfo(VirtualDevice.DeviceBackingInfo):
      pass

   class DistributedVirtualPortBackingInfo(VirtualDevice.BackingInfo):
      port: pyVmomi.vim.dvs.PortConnection

   class OpaqueNetworkBackingInfo(VirtualDevice.BackingInfo):
      opaqueNetworkId: str
      opaqueNetworkType: str

   class ResourceAllocation(pyVmomi.vmodl.DynamicData):
      reservation: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      share: pyVmomi.vim.SharesInfo
      limit: _typing.Optional[pyVmomi.VmomiSupport.long] = None

   addressType: _typing.Optional[str] = None
   macAddress: _typing.Optional[str] = None
   wakeOnLanEnabled: _typing.Optional[bool] = None
   resourceAllocation: _typing.Optional[ResourceAllocation] = None
   externalId: _typing.Optional[str] = None
   uptCompatibilityEnabled: _typing.Optional[bool] = None
   subnetId: _typing.Optional[str] = None


class VirtualEthernetCardOption(VirtualDeviceOption):
   class NetworkBackingOption(VirtualDeviceOption.DeviceBackingOption):
      pass

   class OpaqueNetworkBackingOption(VirtualDeviceOption.BackingOption):
      pass

   class LegacyNetworkBackingOption(VirtualDeviceOption.DeviceBackingOption):
      class LegacyNetworkDeviceName(pyVmomi.VmomiSupport.Enum):
         bridged: _typing.ClassVar['LegacyNetworkDeviceName'] = 'bridged'
         nat: _typing.ClassVar['LegacyNetworkDeviceName'] = 'nat'
         hostonly: _typing.ClassVar['LegacyNetworkDeviceName'] = 'hostonly'

   class DistributedVirtualPortBackingOption(VirtualDeviceOption.BackingOption):
      pass

   class MacTypes(pyVmomi.VmomiSupport.Enum):
      manual: _typing.ClassVar['MacTypes'] = 'manual'
      generated: _typing.ClassVar['MacTypes'] = 'generated'
      assigned: _typing.ClassVar['MacTypes'] = 'assigned'

   supportedOUI: pyVmomi.vim.option.ChoiceOption
   macType: pyVmomi.vim.option.ChoiceOption
   wakeOnLanEnabled: pyVmomi.vim.option.BoolOption
   vmDirectPathGen2Supported: _typing.Optional[bool] = None
   uptCompatibilityEnabled: _typing.Optional[pyVmomi.vim.option.BoolOption] = None

class VirtualFloppy(VirtualDevice):
   class ImageBackingInfo(VirtualDevice.FileBackingInfo):
      pass

   class DeviceBackingInfo(VirtualDevice.DeviceBackingInfo):
      pass

   class RemoteDeviceBackingInfo(VirtualDevice.RemoteDeviceBackingInfo):
      pass

class VirtualFloppyOption(VirtualDeviceOption):
   class ImageBackingOption(VirtualDeviceOption.FileBackingOption):
      pass

   class DeviceBackingOption(VirtualDeviceOption.DeviceBackingOption):
      pass

   class RemoteDeviceBackingOption(VirtualDeviceOption.RemoteDeviceBackingOption):
      pass

class VirtualHdAudioCard(VirtualSoundCard):
   pass

class VirtualHdAudioCardOption(VirtualSoundCardOption):
   pass

class VirtualIDEController(VirtualController):
   pass


class VirtualIDEControllerOption(VirtualControllerOption):
   numIDEDisks: pyVmomi.vim.option.IntOption
   numIDECdroms: pyVmomi.vim.option.IntOption

class VirtualKeyboard(VirtualDevice):
   pass

class VirtualKeyboardOption(VirtualDeviceOption):
   pass

class VirtualLsiLogicController(VirtualSCSIController):
   pass

class VirtualLsiLogicControllerOption(VirtualSCSIControllerOption):
   pass

class VirtualLsiLogicSASController(VirtualSCSIController):
   pass

class VirtualLsiLogicSASControllerOption(VirtualSCSIControllerOption):
   pass


class VirtualNVDIMM(VirtualDevice):
   class BackingInfo(VirtualDevice.FileBackingInfo):
      parent: _typing.Optional[BackingInfo] = None
      changeId: _typing.Optional[str] = None

   capacityInMB: pyVmomi.VmomiSupport.long
   configuredCapacityInMB: _typing.Optional[pyVmomi.VmomiSupport.long] = None

class VirtualNVDIMMController(VirtualController):
   pass


class VirtualNVDIMMControllerOption(VirtualControllerOption):
   numNVDIMMControllers: pyVmomi.vim.option.IntOption


class VirtualNVDIMMOption(VirtualDeviceOption):
   capacityInMB: pyVmomi.vim.option.LongOption
   growable: bool
   hotGrowable: bool
   granularityInMB: pyVmomi.VmomiSupport.long


class VirtualNVMEController(VirtualController):
   class Sharing(pyVmomi.VmomiSupport.Enum):
      noSharing: _typing.ClassVar['Sharing'] = 'noSharing'
      physicalSharing: _typing.ClassVar['Sharing'] = 'physicalSharing'

   sharedBus: _typing.Optional[str] = None


class VirtualNVMEControllerOption(VirtualControllerOption):
   numNVMEDisks: pyVmomi.vim.option.IntOption
   sharing: list[str] = []

class VirtualPCIController(VirtualController):
   pass


class VirtualPCIControllerOption(VirtualControllerOption):
   numSCSIControllers: pyVmomi.vim.option.IntOption
   numEthernetCards: pyVmomi.vim.option.IntOption
   numVideoCards: pyVmomi.vim.option.IntOption
   numSoundCards: pyVmomi.vim.option.IntOption
   numVmiRoms: pyVmomi.vim.option.IntOption
   numVmciDevices: pyVmomi.vim.option.IntOption
   numPCIPassthroughDevices: pyVmomi.vim.option.IntOption
   numSasSCSIControllers: pyVmomi.vim.option.IntOption
   numVmxnet3EthernetCards: pyVmomi.vim.option.IntOption
   numParaVirtualSCSIControllers: pyVmomi.vim.option.IntOption
   numSATAControllers: pyVmomi.vim.option.IntOption
   numNVMEControllers: _typing.Optional[pyVmomi.vim.option.IntOption] = None
   numVmxnet3VrdmaEthernetCards: _typing.Optional[pyVmomi.vim.option.IntOption] = None


class VirtualPCIPassthrough(VirtualDevice):
   class DeviceBackingInfo(VirtualDevice.DeviceBackingInfo):
      id: str
      deviceId: str
      systemId: str
      vendorId: pyVmomi.VmomiSupport.short

   class AllowedDevice(pyVmomi.vmodl.DynamicData):
      vendorId: int
      deviceId: int
      subVendorId: _typing.Optional[int] = None
      subDeviceId: _typing.Optional[int] = None
      revisionId: _typing.Optional[pyVmomi.VmomiSupport.short] = None

   class DynamicBackingInfo(VirtualDevice.DeviceBackingInfo):
      allowedDevice: list[AllowedDevice] = []
      customLabel: _typing.Optional[str] = None
      assignedId: _typing.Optional[str] = None

   class PluginBackingInfo(VirtualDevice.BackingInfo):
      pass

   class VmiopBackingInfo(PluginBackingInfo):
      vgpu: _typing.Optional[str] = None
      vgpuMigrateDataSizeMB: _typing.Optional[int] = None
      migrateSupported: _typing.Optional[bool] = None
      enhancedMigrateCapability: _typing.Optional[bool] = None

   class DvxBackingInfo(VirtualDevice.BackingInfo):
      deviceClass: _typing.Optional[str] = None
      configParams: list[pyVmomi.vim.option.OptionValue] = []


class VirtualPCIPassthroughOption(VirtualDeviceOption):
   class DeviceBackingOption(VirtualDeviceOption.DeviceBackingOption):
      pass

   class PluginBackingOption(VirtualDeviceOption.BackingOption):
      pass

   class VmiopBackingOption(PluginBackingOption):
      vgpu: pyVmomi.vim.option.StringOption
      maxInstances: int

   class DynamicBackingOption(VirtualDeviceOption.DeviceBackingOption):
      pass

   class DvxBackingOption(VirtualDeviceOption.BackingOption):
      pass

class VirtualPCNet32(VirtualEthernetCard):
   pass

class VirtualPCNet32Option(VirtualEthernetCardOption):
   supportsMorphing: bool

class VirtualPS2Controller(VirtualController):
   pass


class VirtualPS2ControllerOption(VirtualControllerOption):
   numKeyboards: pyVmomi.vim.option.IntOption
   numPointingDevices: pyVmomi.vim.option.IntOption

class VirtualParallelPort(VirtualDevice):
   class FileBackingInfo(VirtualDevice.FileBackingInfo):
      pass

   class DeviceBackingInfo(VirtualDevice.DeviceBackingInfo):
      pass

class VirtualParallelPortOption(VirtualDeviceOption):
   class FileBackingOption(VirtualDeviceOption.FileBackingOption):
      pass

   class DeviceBackingOption(VirtualDeviceOption.DeviceBackingOption):
      pass

class VirtualPointingDevice(VirtualDevice):
   class DeviceBackingInfo(VirtualDevice.DeviceBackingInfo):
      hostPointingDevice: str


class VirtualPointingDeviceOption(VirtualDeviceOption):
   class DeviceBackingOption(VirtualDeviceOption.DeviceBackingOption):
      class HostPointingDeviceChoice(pyVmomi.VmomiSupport.Enum):
         autodetect: _typing.ClassVar['HostPointingDeviceChoice'] = 'autodetect'
         intellimouseExplorer: _typing.ClassVar['HostPointingDeviceChoice'] = 'intellimouseExplorer'
         intellimousePs2: _typing.ClassVar['HostPointingDeviceChoice'] = 'intellimousePs2'
         logitechMouseman: _typing.ClassVar['HostPointingDeviceChoice'] = 'logitechMouseman'
         microsoft_serial: _typing.ClassVar['HostPointingDeviceChoice'] = 'microsoft_serial'
         mouseSystems: _typing.ClassVar['HostPointingDeviceChoice'] = 'mouseSystems'
         mousemanSerial: _typing.ClassVar['HostPointingDeviceChoice'] = 'mousemanSerial'
         ps2: _typing.ClassVar['HostPointingDeviceChoice'] = 'ps2'

      hostPointingDevice: pyVmomi.vim.option.ChoiceOption


class VirtualPrecisionClock(VirtualDevice):
   class SystemClockBackingInfo(VirtualDevice.BackingInfo):
      protocol: _typing.Optional[str] = None


class VirtualPrecisionClockOption(VirtualDeviceOption):
   class SystemClockBackingOption(VirtualDeviceOption.BackingOption):
      protocol: pyVmomi.vim.option.ChoiceOption

class VirtualSATAController(VirtualController):
   pass


class VirtualSATAControllerOption(VirtualControllerOption):
   numSATADisks: pyVmomi.vim.option.IntOption
   numSATACdroms: pyVmomi.vim.option.IntOption


class VirtualSCSIController(VirtualController):
   class Sharing(pyVmomi.VmomiSupport.Enum):
      noSharing: _typing.ClassVar['Sharing'] = 'noSharing'
      virtualSharing: _typing.ClassVar['Sharing'] = 'virtualSharing'
      physicalSharing: _typing.ClassVar['Sharing'] = 'physicalSharing'

   hotAddRemove: _typing.Optional[bool] = None
   sharedBus: Sharing
   scsiCtlrUnitNumber: _typing.Optional[int] = None


class VirtualSCSIControllerOption(VirtualControllerOption):
   numSCSIDisks: pyVmomi.vim.option.IntOption
   numSCSICdroms: pyVmomi.vim.option.IntOption
   numSCSIPassthrough: pyVmomi.vim.option.IntOption
   sharing: list[VirtualSCSIController.Sharing] = []
   defaultSharedIndex: int
   hotAddRemove: pyVmomi.vim.option.BoolOption
   scsiCtlrUnitNumber: int

class VirtualSCSIPassthrough(VirtualDevice):
   class DeviceBackingInfo(VirtualDevice.DeviceBackingInfo):
      pass

class VirtualSCSIPassthroughOption(VirtualDeviceOption):
   class DeviceBackingOption(VirtualDeviceOption.DeviceBackingOption):
      pass

class VirtualSIOController(VirtualController):
   pass


class VirtualSIOControllerOption(VirtualControllerOption):
   numFloppyDrives: pyVmomi.vim.option.IntOption
   numSerialPorts: pyVmomi.vim.option.IntOption
   numParallelPorts: pyVmomi.vim.option.IntOption


class VirtualSerialPort(VirtualDevice):
   class FileBackingInfo(VirtualDevice.FileBackingInfo):
      pass

   class DeviceBackingInfo(VirtualDevice.DeviceBackingInfo):
      pass

   class PipeBackingInfo(VirtualDevice.PipeBackingInfo):
      endpoint: str
      noRxLoss: _typing.Optional[bool] = None

   class URIBackingInfo(VirtualDevice.URIBackingInfo):
      pass

   class ThinPrintBackingInfo(VirtualDevice.BackingInfo):
      pass

   yieldOnPoll: bool


class VirtualSerialPortOption(VirtualDeviceOption):
   class EndPoint(pyVmomi.VmomiSupport.Enum):
      client: _typing.ClassVar['EndPoint'] = 'client'
      server: _typing.ClassVar['EndPoint'] = 'server'

   class FileBackingOption(VirtualDeviceOption.FileBackingOption):
      pass

   class DeviceBackingOption(VirtualDeviceOption.DeviceBackingOption):
      pass

   class PipeBackingOption(VirtualDeviceOption.PipeBackingOption):
      endpoint: pyVmomi.vim.option.ChoiceOption
      noRxLoss: pyVmomi.vim.option.BoolOption

   class URIBackingOption(VirtualDeviceOption.URIBackingOption):
      pass

   class ThinPrintBackingOption(VirtualDeviceOption.BackingOption):
      pass

   yieldOnPoll: pyVmomi.vim.option.BoolOption

class VirtualSoundBlaster16(VirtualSoundCard):
   pass

class VirtualSoundBlaster16Option(VirtualSoundCardOption):
   pass

class VirtualSoundCard(VirtualDevice):
   class DeviceBackingInfo(VirtualDevice.DeviceBackingInfo):
      pass

class VirtualSoundCardOption(VirtualDeviceOption):
   class DeviceBackingOption(VirtualDeviceOption.DeviceBackingOption):
      pass


class VirtualSriovEthernetCard(VirtualEthernetCard):
   class SriovBackingInfo(VirtualDevice.BackingInfo):
      physicalFunctionBacking: _typing.Optional[VirtualPCIPassthrough.DeviceBackingInfo] = None
      virtualFunctionBacking: _typing.Optional[VirtualPCIPassthrough.DeviceBackingInfo] = None
      virtualFunctionIndex: _typing.Optional[int] = None

   allowGuestOSMtuChange: _typing.Optional[bool] = None
   sriovBacking: _typing.Optional[SriovBackingInfo] = None
   dvxBackingInfo: _typing.Optional[VirtualPCIPassthrough.DvxBackingInfo] = None

class VirtualSriovEthernetCardOption(VirtualEthernetCardOption):
   class SriovBackingOption(VirtualDeviceOption.BackingOption):
      pass


class VirtualTPM(VirtualDevice):
   endorsementKeyCertificateSigningRequest: list[pyVmomi.VmomiSupport.binary] = []
   endorsementKeyCertificate: list[pyVmomi.VmomiSupport.binary] = []


class VirtualTPMOption(VirtualDeviceOption):
   supportedFirmware: list[str] = []


class VirtualUSB(VirtualDevice):
   class USBBackingInfo(VirtualDevice.DeviceBackingInfo):
      pass

   class RemoteHostBackingInfo(VirtualDevice.DeviceBackingInfo):
      hostname: str

   class RemoteClientBackingInfo(VirtualDevice.RemoteDeviceBackingInfo):
      hostname: str

   connected: bool
   vendor: _typing.Optional[int] = None
   product: _typing.Optional[int] = None
   family: list[str] = []
   speed: list[str] = []


class VirtualUSBController(VirtualController):
   class PciBusSlotInfo(VirtualDevice.PciBusSlotInfo):
      ehciPciSlotNumber: _typing.Optional[int] = None

   autoConnectDevices: _typing.Optional[bool] = None
   ehciEnabled: _typing.Optional[bool] = None


class VirtualUSBControllerOption(VirtualControllerOption):
   autoConnectDevices: pyVmomi.vim.option.BoolOption
   ehciSupported: pyVmomi.vim.option.BoolOption
   supportedSpeeds: list[str] = []

class VirtualUSBOption(VirtualDeviceOption):
   class USBBackingOption(VirtualDeviceOption.DeviceBackingOption):
      pass

   class RemoteHostBackingOption(VirtualDeviceOption.DeviceBackingOption):
      pass

   class RemoteClientBackingOption(VirtualDeviceOption.RemoteDeviceBackingOption):
      pass


class VirtualUSBXHCIController(VirtualController):
   autoConnectDevices: _typing.Optional[bool] = None


class VirtualUSBXHCIControllerOption(VirtualControllerOption):
   autoConnectDevices: pyVmomi.vim.option.BoolOption
   supportedSpeeds: list[str] = []


class VirtualVMCIDevice(VirtualDevice):
   class Action(pyVmomi.VmomiSupport.Enum):
      allow: _typing.ClassVar['Action'] = 'allow'
      deny: _typing.ClassVar['Action'] = 'deny'

   class Protocol(pyVmomi.VmomiSupport.Enum):
      hypervisor: _typing.ClassVar['Protocol'] = 'hypervisor'
      doorbell: _typing.ClassVar['Protocol'] = 'doorbell'
      queuepair: _typing.ClassVar['Protocol'] = 'queuepair'
      datagram: _typing.ClassVar['Protocol'] = 'datagram'
      stream: _typing.ClassVar['Protocol'] = 'stream'
      anyProtocol: _typing.ClassVar['Protocol'] = 'anyProtocol'

   class Direction(pyVmomi.VmomiSupport.Enum):
      guest: _typing.ClassVar['Direction'] = 'guest'
      host: _typing.ClassVar['Direction'] = 'host'
      anyDirection: _typing.ClassVar['Direction'] = 'anyDirection'

   class FilterSpec(pyVmomi.vmodl.DynamicData):
      rank: pyVmomi.VmomiSupport.long
      action: str
      protocol: str
      direction: str
      lowerDstPortBoundary: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      upperDstPortBoundary: _typing.Optional[pyVmomi.VmomiSupport.long] = None

   class FilterInfo(pyVmomi.vmodl.DynamicData):
      filters: list[FilterSpec] = []

   id: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   allowUnrestrictedCommunication: _typing.Optional[bool] = None
   filterEnable: _typing.Optional[bool] = None
   filterInfo: _typing.Optional[FilterInfo] = None


class VirtualVMCIDeviceOption(VirtualDeviceOption):
   class FilterSpecOption(pyVmomi.vmodl.DynamicData):
      action: pyVmomi.vim.option.ChoiceOption
      protocol: pyVmomi.vim.option.ChoiceOption
      direction: pyVmomi.vim.option.ChoiceOption
      lowerDstPortBoundary: pyVmomi.vim.option.LongOption
      upperDstPortBoundary: pyVmomi.vim.option.LongOption

   allowUnrestrictedCommunication: pyVmomi.vim.option.BoolOption
   filterSpecOption: _typing.Optional[FilterSpecOption] = None
   filterSupported: _typing.Optional[pyVmomi.vim.option.BoolOption] = None

class VirtualVMIROM(VirtualDevice):
   pass

class VirtualVMIROMOption(VirtualDeviceOption):
   pass


class VirtualVideoCard(VirtualDevice):
   class Use3dRenderer(pyVmomi.VmomiSupport.Enum):
      automatic: _typing.ClassVar['Use3dRenderer'] = 'automatic'
      software: _typing.ClassVar['Use3dRenderer'] = 'software'
      hardware: _typing.ClassVar['Use3dRenderer'] = 'hardware'

   videoRamSizeInKB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   numDisplays: _typing.Optional[int] = None
   useAutoDetect: _typing.Optional[bool] = None
   enable3DSupport: _typing.Optional[bool] = None
   use3dRenderer: _typing.Optional[str] = None
   graphicsMemorySizeInKB: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class VirtualVideoCardOption(VirtualDeviceOption):
   videoRamSizeInKB: _typing.Optional[pyVmomi.vim.option.LongOption] = None
   numDisplays: _typing.Optional[pyVmomi.vim.option.IntOption] = None
   useAutoDetect: _typing.Optional[pyVmomi.vim.option.BoolOption] = None
   support3D: _typing.Optional[pyVmomi.vim.option.BoolOption] = None
   use3dRendererSupported: _typing.Optional[pyVmomi.vim.option.BoolOption] = None
   graphicsMemorySizeInKB: _typing.Optional[pyVmomi.vim.option.LongOption] = None
   graphicsMemorySizeSupported: _typing.Optional[pyVmomi.vim.option.BoolOption] = None

class VirtualVmxnet(VirtualEthernetCard):
   pass

class VirtualVmxnet2(VirtualVmxnet):
   pass

class VirtualVmxnet2Option(VirtualVmxnetOption):
   pass


class VirtualVmxnet3(VirtualVmxnet):
   class StrictLatencyConfig(pyVmomi.vmodl.DynamicData):
      class DisableOffload(pyVmomi.VmomiSupport.Enum):
         NONE: _typing.ClassVar['DisableOffload'] = 'NONE'
         TSO: _typing.ClassVar['DisableOffload'] = 'TSO'
         LRO: _typing.ClassVar['DisableOffload'] = 'LRO'
         TSO_LRO: _typing.ClassVar['DisableOffload'] = 'TSO_LRO'

      allowed: _typing.Optional[bool] = None
      measureLatency: _typing.Optional[bool] = None
      maxTxQueues: _typing.Optional[int] = None
      maxRxQueues: _typing.Optional[int] = None
      txDataRingDescSize: _typing.Optional[int] = None
      rxDataRingDescSize: _typing.Optional[int] = None
      disableOffload: _typing.Optional[str] = None

   uptv2Enabled: _typing.Optional[bool] = None
   strictLatencyConfig: _typing.Optional[StrictLatencyConfig] = None


class VirtualVmxnet3Option(VirtualVmxnetOption):
   class StrictLatencyConfigOption(pyVmomi.vmodl.DynamicData):
      allowed: pyVmomi.vim.option.BoolOption
      measureLatency: pyVmomi.vim.option.BoolOption
      maxTxQueues: pyVmomi.vim.option.IntOption
      maxRxQueues: pyVmomi.vim.option.IntOption
      txDataRingDescSize: pyVmomi.vim.option.IntOption
      rxDataRingDescSize: pyVmomi.vim.option.IntOption
      disableOffload: pyVmomi.vim.option.ChoiceOption

   uptv2Enabled: _typing.Optional[pyVmomi.vim.option.BoolOption] = None
   strictLatencyConfigOption: _typing.Optional[StrictLatencyConfigOption] = None


class VirtualVmxnet3Vrdma(VirtualVmxnet3):
   deviceProtocol: _typing.Optional[str] = None


class VirtualVmxnet3VrdmaOption(VirtualVmxnet3Option):
   class DeviceProtocols(pyVmomi.VmomiSupport.Enum):
      rocev1: _typing.ClassVar['DeviceProtocols'] = 'rocev1'
      rocev2: _typing.ClassVar['DeviceProtocols'] = 'rocev2'

   deviceProtocol: _typing.Optional[pyVmomi.vim.option.ChoiceOption] = None

class VirtualVmxnetOption(VirtualEthernetCardOption):
   pass

class VirtualWDT(VirtualDevice):
   runOnBoot: bool
   running: bool


class VirtualWDTOption(VirtualDeviceOption):
   runOnBoot: pyVmomi.vim.option.BoolOption
