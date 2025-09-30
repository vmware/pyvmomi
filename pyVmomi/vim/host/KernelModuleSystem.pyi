# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject
from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl.DynamicData import DynamicData

class KernelModuleSystem(ManagedObject):
   class ModuleInfo(DynamicData):
      class SectionInfo(DynamicData):
         address: long
         length: Optional[int] = None

      id: int
      name: str
      version: str
      filename: str
      optionString: str
      loaded: bool
      enabled: bool
      useCount: int
      readOnlySection: SectionInfo
      writableSection: SectionInfo
      textSection: SectionInfo
      dataSection: SectionInfo
      bssSection: SectionInfo

   def QueryModules(self) -> list[ModuleInfo]: ...
   def UpdateModuleOptionString(self, name: str, options: str) -> None: ...
   def QueryConfiguredModuleOptionString(self, name: str) -> str: ...
