# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import NoReturn
from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject
from pyVmomi.VmomiSupport import long

from pyVmomi.vim import Task

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import VffsVolume

from pyVmomi.vim.option import ChoiceOption
from pyVmomi.vim.option import LongOption

from pyVmomi.vim.vm.device import VirtualDisk

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
   def ConfigureVFlashResource(self, spec: VFlashResourceConfigSpec) -> NoReturn: ...
   def RemoveVFlashResource(self) -> NoReturn: ...
   def ConfigureHostVFlashCache(self, spec: VFlashCacheConfigSpec) -> NoReturn: ...
   def GetVFlashModuleDefaultConfig(self, vFlashModule: str) -> VirtualDisk.VFlashCacheConfigInfo: ...
