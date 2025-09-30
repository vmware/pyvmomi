# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import ManagedObject
from pyVmomi.VmomiSupport import long

from pyVmomi.vim.Datacenter import Datacenter

from pyVmomi.vim.Task import Task

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.encryption.CryptoSpec import CryptoSpec

from pyVmomi.vim.host.DiskDimensions import DiskDimensions

from pyVmomi.vim.vm.ProfileSpec import ProfileSpec

class VirtualDiskManager(ManagedObject):
   class VirtualDiskType(Enum):
      preallocated: ClassVar['VirtualDiskType'] = 'preallocated'
      thin: ClassVar['VirtualDiskType'] = 'thin'
      seSparse: ClassVar['VirtualDiskType'] = 'seSparse'
      rdm: ClassVar['VirtualDiskType'] = 'rdm'
      rdmp: ClassVar['VirtualDiskType'] = 'rdmp'
      raw: ClassVar['VirtualDiskType'] = 'raw'
      delta: ClassVar['VirtualDiskType'] = 'delta'
      sparse2Gb: ClassVar['VirtualDiskType'] = 'sparse2Gb'
      thick2Gb: ClassVar['VirtualDiskType'] = 'thick2Gb'
      eagerZeroedThick: ClassVar['VirtualDiskType'] = 'eagerZeroedThick'
      sparseMonolithic: ClassVar['VirtualDiskType'] = 'sparseMonolithic'
      flatMonolithic: ClassVar['VirtualDiskType'] = 'flatMonolithic'
      thick: ClassVar['VirtualDiskType'] = 'thick'

   class VirtualDiskAdapterType(Enum):
      ide: ClassVar['VirtualDiskAdapterType'] = 'ide'
      busLogic: ClassVar['VirtualDiskAdapterType'] = 'busLogic'
      lsiLogic: ClassVar['VirtualDiskAdapterType'] = 'lsiLogic'

   class VirtualDiskSpec(DynamicData):
      diskType: str
      adapterType: str

   class FileBackedVirtualDiskSpec(VirtualDiskSpec):
      capacityKb: long
      profile: list[ProfileSpec] = []
      crypto: Optional[CryptoSpec] = None
      sectorFormat: Optional[str] = None

   class SeSparseVirtualDiskSpec(FileBackedVirtualDiskSpec):
      grainSizeKb: Optional[int] = None

   class DeviceBackedVirtualDiskSpec(VirtualDiskSpec):
      device: str

   def CreateVirtualDisk(self, name: str, datacenter: Optional[Datacenter], spec: VirtualDiskSpec) -> Task: ...
   def DeleteVirtualDisk(self, name: str, datacenter: Optional[Datacenter]) -> Task: ...
   def MoveVirtualDisk(self, sourceName: str, sourceDatacenter: Optional[Datacenter], destName: str, destDatacenter: Optional[Datacenter], force: Optional[bool], profile: list[ProfileSpec]) -> Task: ...
   def CopyVirtualDisk(self, sourceName: str, sourceDatacenter: Optional[Datacenter], destName: str, destDatacenter: Optional[Datacenter], destSpec: Optional[VirtualDiskSpec], force: Optional[bool]) -> Task: ...
   def ExtendVirtualDisk(self, name: str, datacenter: Optional[Datacenter], newCapacityKb: long, eagerZero: Optional[bool]) -> Task: ...
   def QueryVirtualDiskFragmentation(self, name: str, datacenter: Optional[Datacenter]) -> int: ...
   def DefragmentVirtualDisk(self, name: str, datacenter: Optional[Datacenter]) -> Task: ...
   def ShrinkVirtualDisk(self, name: str, datacenter: Optional[Datacenter], copy: Optional[bool]) -> Task: ...
   def InflateVirtualDisk(self, name: str, datacenter: Optional[Datacenter]) -> Task: ...
   def EagerZeroVirtualDisk(self, name: str, datacenter: Optional[Datacenter]) -> Task: ...
   def ZeroFillVirtualDisk(self, name: str, datacenter: Optional[Datacenter]) -> Task: ...
   def SetVirtualDiskUuid(self, name: str, datacenter: Optional[Datacenter], uuid: str) -> None: ...
   def QueryVirtualDiskUuid(self, name: str, datacenter: Optional[Datacenter]) -> str: ...
   def QueryVirtualDiskGeometry(self, name: str, datacenter: Optional[Datacenter]) -> DiskDimensions.Chs: ...
   def ImportUnmanagedSnapshot(self, vdisk: str, datacenter: Optional[Datacenter], vvolId: str) -> None: ...
   def ReleaseManagedSnapshot(self, vdisk: str, datacenter: Optional[Datacenter]) -> None: ...
