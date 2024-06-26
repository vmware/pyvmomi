# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import NoReturn
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim import ExtensibleManagedObject

from pyVmomi.vmodl import DynamicData

class CpuSchedulerSystem(ExtensibleManagedObject):
   class HyperThreadScheduleInfo(DynamicData):
      available: bool
      active: bool
      config: bool

   class CpuSchedulerInfo(DynamicData):
      class CpuSchedulerPolicyInfo(Enum):
         systemDefault: ClassVar['CpuSchedulerPolicyInfo'] = 'systemDefault'
         scav1: ClassVar['CpuSchedulerPolicyInfo'] = 'scav1'
         scav2: ClassVar['CpuSchedulerPolicyInfo'] = 'scav2'

      policy: str

   @property
   def cpuSchedulerInfo(self) -> Optional[CpuSchedulerInfo]: ...
   @property
   def hyperthreadInfo(self) -> Optional[HyperThreadScheduleInfo]: ...

   def EnableHyperThreading(self) -> NoReturn: ...
   def DisableHyperThreading(self) -> NoReturn: ...
