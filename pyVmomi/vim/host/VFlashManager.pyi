# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject
from pyVmomi.VmomiSupport import long

from pyVmomi.vim.Task import Task

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.host.VffsVolume import VffsVolume

from pyVmomi.vim.option.ChoiceOption import ChoiceOption

from pyVmomi.vim.option.LongOption import LongOption

from pyVmomi.vim.vm.device.VirtualDisk import VirtualDisk

class VFlashManager(ManagedObject):
   class VFlashResourceConfigSpec(DynamicData):
      vffsUuid: str

   class VFlashResourceConfigInfo(DynamicData):
      vffs: Optional[VffsVolume] = None
      capacity: long

   class VFlashResourceRunTimeInfo(DynamicData):
      usage: long
      capacity: long
      accessible: bool
      capacityForVmCache: long
      freeForVmCache: long

   class VFlashCacheConfigSpec(DynamicData):
      defaultVFlashModule: str
      swapCacheReservationInGB: long

   class VFlashCacheConfigInfo(DynamicData):
      class VFlashModuleConfigOption(DynamicData):
         vFlashModule: str
         vFlashModuleVersion: str
         minSupportedModuleVersion: str
         cacheConsistencyType: ChoiceOption
         cacheMode: ChoiceOption
         blockSizeInKBOption: LongOption
         reservationInMBOption: LongOption
         maxDiskSizeInKB: long

      vFlashModuleConfigOption: list[VFlashModuleConfigOption] = []
      defaultVFlashModule: Optional[str] = None
      swapCacheReservationInGB: Optional[long] = None

   class VFlashConfigInfo(DynamicData):
      vFlashResourceConfigInfo: Optional[VFlashResourceConfigInfo] = None
      vFlashCacheConfigInfo: Optional[VFlashCacheConfigInfo] = None

   @property
   def vFlashConfigInfo(self) -> Optional[VFlashConfigInfo]: ...

   def ConfigureVFlashResourceEx(self, devicePath: list[str]) -> Task: ...
   def ConfigureVFlashResource(self, spec: VFlashResourceConfigSpec) -> None: ...
   def RemoveVFlashResource(self) -> None: ...
   def ConfigureHostVFlashCache(self, spec: VFlashCacheConfigSpec) -> None: ...
   def GetVFlashModuleDefaultConfig(self, vFlashModule: str) -> VirtualDisk.VFlashCacheConfigInfo: ...
