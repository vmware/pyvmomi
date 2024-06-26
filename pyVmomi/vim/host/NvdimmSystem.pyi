# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import ManagedObject
from pyVmomi.VmomiSupport import long

from pyVmomi.vim import Task

from pyVmomi.vmodl import DynamicData

class NvdimmSystem(ManagedObject):
   class RangeType(Enum):
      volatileRange: ClassVar['RangeType'] = 'volatileRange'
      persistentRange: ClassVar['RangeType'] = 'persistentRange'
      controlRange: ClassVar['RangeType'] = 'controlRange'
      blockRange: ClassVar['RangeType'] = 'blockRange'
      volatileVirtualDiskRange: ClassVar['RangeType'] = 'volatileVirtualDiskRange'
      volatileVirtualCDRange: ClassVar['RangeType'] = 'volatileVirtualCDRange'
      persistentVirtualDiskRange: ClassVar['RangeType'] = 'persistentVirtualDiskRange'
      persistentVirtualCDRange: ClassVar['RangeType'] = 'persistentVirtualCDRange'

   class NamespaceType(Enum):
      blockNamespace: ClassVar['NamespaceType'] = 'blockNamespace'
      persistentNamespace: ClassVar['NamespaceType'] = 'persistentNamespace'

   class HealthInfo(DynamicData):
      class StateFlag(Enum):
         normal: ClassVar['StateFlag'] = 'normal'
         error: ClassVar['StateFlag'] = 'error'

      healthStatus: str
      healthInformation: str
      stateFlagInfo: list[str] = []
      dimmTemperature: int
      dimmTemperatureThreshold: int
      spareBlocksPercentage: int
      spareBlockThreshold: int
      dimmLifespanPercentage: int
      esTemperature: Optional[int] = None
      esTemperatureThreshold: Optional[int] = None
      esLifespanPercentage: Optional[int] = None

   class RegionInfo(DynamicData):
      regionId: int
      setId: int
      rangeType: str
      startAddr: long
      size: long
      offset: long

   class Summary(DynamicData):
      numDimms: int
      healthStatus: str
      totalCapacity: long
      persistentCapacity: long
      blockCapacity: long
      availableCapacity: long
      numInterleavesets: int
      numNamespaces: int

   class DimmInfo(DynamicData):
      dimmHandle: int
      healthInfo: HealthInfo
      totalCapacity: long
      persistentCapacity: long
      availablePersistentCapacity: long
      volatileCapacity: long
      availableVolatileCapacity: long
      blockCapacity: long
      regionInfo: list[RegionInfo] = []
      representationString: str

   class InterleaveSetInfo(DynamicData):
      class InterleaveSetState(Enum):
         invalid: ClassVar['InterleaveSetState'] = 'invalid'
         active: ClassVar['InterleaveSetState'] = 'active'

      setId: int
      rangeType: str
      baseAddress: long
      size: long
      availableSize: long
      deviceList: list[int] = []
      state: str

   class Guid(DynamicData):
      uuid: str

   class NamespaceInfo(DynamicData):
      class NamespaceHealthStatus(Enum):
         normal: ClassVar['NamespaceHealthStatus'] = 'normal'
         missing: ClassVar['NamespaceHealthStatus'] = 'missing'
         labelMissing: ClassVar['NamespaceHealthStatus'] = 'labelMissing'
         interleaveBroken: ClassVar['NamespaceHealthStatus'] = 'interleaveBroken'
         labelInconsistent: ClassVar['NamespaceHealthStatus'] = 'labelInconsistent'
         bttCorrupt: ClassVar['NamespaceHealthStatus'] = 'bttCorrupt'
         badBlockSize: ClassVar['NamespaceHealthStatus'] = 'badBlockSize'

      class NamespaceState(Enum):
         invalid: ClassVar['NamespaceState'] = 'invalid'
         notInUse: ClassVar['NamespaceState'] = 'notInUse'
         inUse: ClassVar['NamespaceState'] = 'inUse'

      uuid: str
      friendlyName: str
      blockSize: long
      blockCount: long
      type: str
      namespaceHealthStatus: str
      locationID: int
      state: str

   class NamespaceDetails(DynamicData):
      class NamespaceHealthStatus(Enum):
         normal: ClassVar['NamespaceHealthStatus'] = 'normal'
         missing: ClassVar['NamespaceHealthStatus'] = 'missing'
         labelMissing: ClassVar['NamespaceHealthStatus'] = 'labelMissing'
         interleaveBroken: ClassVar['NamespaceHealthStatus'] = 'interleaveBroken'
         labelInconsistent: ClassVar['NamespaceHealthStatus'] = 'labelInconsistent'

      class NamespaceState(Enum):
         invalid: ClassVar['NamespaceState'] = 'invalid'
         notInUse: ClassVar['NamespaceState'] = 'notInUse'
         inUse: ClassVar['NamespaceState'] = 'inUse'

      uuid: str
      friendlyName: str
      size: long
      type: str
      namespaceHealthStatus: str
      interleavesetID: int
      state: str

   class NamespaceCreateSpec(DynamicData):
      friendlyName: Optional[str] = None
      blockSize: long
      blockCount: long
      type: str
      locationID: int

   class PMemNamespaceCreateSpec(DynamicData):
      friendlyName: Optional[str] = None
      size: long
      interleavesetID: int

   class NamespaceDeleteSpec(DynamicData):
      uuid: str

   class NvdimmSystemInfo(DynamicData):
      summary: Optional[Summary] = None
      dimms: list[int] = []
      dimmInfo: list[DimmInfo] = []
      interleaveSet: list[int] = []
      iSetInfo: list[InterleaveSetInfo] = []
      namespace: list[Guid] = []
      nsInfo: list[NamespaceInfo] = []
      nsDetails: list[NamespaceDetails] = []

   @property
   def nvdimmSystemInfo(self) -> NvdimmSystemInfo: ...

   def CreateNamespace(self, createSpec: NamespaceCreateSpec) -> Task: ...
   def CreatePMemNamespace(self, createSpec: PMemNamespaceCreateSpec) -> Task: ...
   def DeleteNamespace(self, deleteSpec: NamespaceDeleteSpec) -> Task: ...
   def DeleteBlockNamespaces(self) -> Task: ...
