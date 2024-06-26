# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import NoReturn
from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vim import ComputeResource
from pyVmomi.vim import Folder
from pyVmomi.vim import HostSystem
from pyVmomi.vim import HttpNfcLease
from pyVmomi.vim import ImportSpec
from pyVmomi.vim import ManagedEntity
from pyVmomi.vim import ResourceConfigOption
from pyVmomi.vim import ResourceConfigSpec
from pyVmomi.vim import Task
from pyVmomi.vim import VirtualApp
from pyVmomi.vim import VirtualMachine

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.vApp import VAppConfigSpec

from pyVmomi.vim.vm import ConfigSpec

class ResourcePool(ManagedEntity):
   class ResourceUsage(DynamicData):
      reservationUsed: long
      reservationUsedForVm: long
      unreservedForPool: long
      unreservedForVm: long
      overallUsage: long
      maxUsage: long

   class RuntimeInfo(DynamicData):
      memory: ResourceUsage
      cpu: ResourceUsage
      overallStatus: ManagedEntity.Status
      sharesScalable: Optional[str] = None

   class Summary(DynamicData):
      class QuickStats(DynamicData):
         overallCpuUsage: Optional[long] = None
         overallCpuDemand: Optional[long] = None
         guestMemoryUsage: Optional[long] = None
         hostMemoryUsage: Optional[long] = None
         distributedCpuEntitlement: Optional[long] = None
         distributedMemoryEntitlement: Optional[long] = None
         staticCpuEntitlement: Optional[int] = None
         staticMemoryEntitlement: Optional[int] = None
         privateMemory: Optional[long] = None
         sharedMemory: Optional[long] = None
         swappedMemory: Optional[long] = None
         balloonedMemory: Optional[long] = None
         overheadMemory: Optional[long] = None
         consumedOverheadMemory: Optional[long] = None
         compressedMemory: Optional[long] = None

      name: str
      config: ResourceConfigSpec
      runtime: RuntimeInfo
      quickStats: Optional[QuickStats] = None
      configuredMemoryMB: Optional[int] = None

   @property
   def summary(self) -> Summary: ...
   @property
   def runtime(self) -> RuntimeInfo: ...
   @property
   def owner(self) -> ComputeResource: ...
   @property
   def resourcePool(self) -> list[ResourcePool]: ...
   @property
   def vm(self) -> list[VirtualMachine]: ...
   @property
   def config(self) -> ResourceConfigSpec: ...
   @property
   def namespace(self) -> Optional[str]: ...
   @property
   def childConfiguration(self) -> list[ResourceConfigSpec]: ...

   def UpdateConfig(self, name: Optional[str], config: Optional[ResourceConfigSpec]) -> NoReturn: ...
   def MoveInto(self, list: list[ManagedEntity]) -> NoReturn: ...
   def UpdateChildResourceConfiguration(self, spec: list[ResourceConfigSpec]) -> NoReturn: ...
   def CreateResourcePool(self, name: str, spec: ResourceConfigSpec) -> ResourcePool: ...
   def DestroyChildren(self) -> NoReturn: ...
   def CreateVApp(self, name: str, resSpec: ResourceConfigSpec, configSpec: VAppConfigSpec, vmFolder: Optional[Folder]) -> VirtualApp: ...
   def CreateVm(self, config: ConfigSpec, host: Optional[HostSystem]) -> Task: ...
   def RegisterVm(self, path: str, name: Optional[str], host: Optional[HostSystem]) -> Task: ...
   def ImportVApp(self, spec: ImportSpec, folder: Optional[Folder], host: Optional[HostSystem]) -> HttpNfcLease: ...
   def QueryResourceConfigOption(self) -> ResourceConfigOption: ...
   def RefreshRuntime(self) -> NoReturn: ...
