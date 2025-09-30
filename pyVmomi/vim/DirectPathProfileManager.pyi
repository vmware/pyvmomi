# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim.ClusterComputeResource import ClusterComputeResource

from pyVmomi.vim.HostSystem import HostSystem

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vmodl.MethodFault import MethodFault

from pyVmomi.vim.vm.device.VirtualPCIPassthrough import VirtualPCIPassthrough

class DirectPathProfileManager(ManagedObject):
   class DirectPathConfig(DynamicData):
      pass

   class VmiopDirectPathConfig(DirectPathConfig):
      vgpuProfile: str

   class DvxDirectPathConfig(DirectPathConfig):
      dvxBacking: VirtualPCIPassthrough.DvxBackingInfo

   class DynamicDirectPathConfig(DirectPathConfig):
      dynamicDirectPathBacking: VirtualPCIPassthrough.DynamicBackingInfo

   class VirtualDeviceGroupDirectPathConfig(DirectPathConfig):
      deviceGroupName: str

   class CreateSpec(DynamicData):
      name: str
      description: Optional[str] = None
      deviceConfig: DirectPathConfig

   class UpdateSpec(DynamicData):
      name: Optional[str] = None
      description: Optional[str] = None

   class FilterSpec(DynamicData):
      ids: list[str] = []
      names: list[str] = []
      clusters: list[ClusterComputeResource] = []

   class DirectPathProfileInfo(DynamicData):
      id: str
      name: str
      description: Optional[str] = None
      vendorName: str
      deviceConfig: DirectPathConfig

   class TargetEntity(DynamicData):
      pass

   class TargetHost(TargetEntity):
      host: HostSystem

   class TargetCluster(TargetEntity):
      cluster: ClusterComputeResource

   class CapacityQuerySpec(DynamicData):
      pass

   class CapacityQueryById(CapacityQuerySpec):
      id: str

   class CapacityQueryByName(CapacityQuerySpec):
      name: str

   class CapacityQueryByDeviceConfig(CapacityQuerySpec):
      deviceConfig: DirectPathConfig

   class CapacityResult(DynamicData):
      pass

   class CapacityInfo(CapacityResult):
      profile: DirectPathProfileInfo
      consumed: int
      remaining: int
      max: int
      unusedReservation: int

   class CapacityUnknown(CapacityResult):
      querySpec: CapacityQuerySpec
      faultList: list[MethodFault] = []

   def CreateDirectPathProfile(self, spec: CreateSpec) -> str: ...
   def UpdateDirectPathProfile(self, id: str, spec: UpdateSpec) -> None: ...
   def DeleteDirectPathProfile(self, id: str) -> None: ...
   def ListDirectPathProfiles(self, filterSpec: FilterSpec) -> list[DirectPathProfileInfo]: ...
   def QueryDirectPathProfileCapacity(self, target: TargetEntity, querySpec: list[CapacityQuerySpec]) -> list[CapacityResult]: ...
