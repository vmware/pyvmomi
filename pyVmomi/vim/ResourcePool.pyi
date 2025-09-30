# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vim.ComputeResource import ComputeResource

from pyVmomi.vim.Folder import Folder

from pyVmomi.vim.HostSystem import HostSystem

from pyVmomi.vim.HttpNfcLease import HttpNfcLease

from pyVmomi.vim.ImportSpec import ImportSpec

from pyVmomi.vim.ManagedEntity import ManagedEntity

from pyVmomi.vim.ResourceConfigOption import ResourceConfigOption

from pyVmomi.vim.ResourceConfigSpec import ResourceConfigSpec

from pyVmomi.vim.Task import Task

from pyVmomi.vim.VirtualApp import VirtualApp

from pyVmomi.vim.VirtualMachine import VirtualMachine

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.vApp.VAppConfigSpec import VAppConfigSpec

from pyVmomi.vim.vm.ConfigSpec import ConfigSpec

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

   def UpdateConfig(self, name: Optional[str], config: Optional[ResourceConfigSpec]) -> None: ...
   def MoveInto(self, list: list[ManagedEntity]) -> None: ...
   def UpdateChildResourceConfiguration(self, spec: list[ResourceConfigSpec]) -> None: ...
   def CreateResourcePool(self, name: str, spec: ResourceConfigSpec) -> ResourcePool: ...
   def DestroyChildren(self) -> None: ...
   def CreateVApp(self, name: str, resSpec: ResourceConfigSpec, configSpec: VAppConfigSpec, vmFolder: Optional[Folder]) -> VirtualApp: ...
   def CreateVm(self, config: ConfigSpec, host: Optional[HostSystem]) -> Task: ...
   def RegisterVm(self, path: str, name: Optional[str], host: Optional[HostSystem]) -> Task: ...
   def ImportVApp(self, spec: ImportSpec, folder: Optional[Folder], host: Optional[HostSystem]) -> HttpNfcLease: ...
   def QueryResourceConfigOption(self) -> ResourceConfigOption: ...
   def RefreshRuntime(self) -> None: ...
