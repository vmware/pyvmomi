# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import NoReturn
from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import HardwareStatusInfo
from pyVmomi.vim.host import SystemEventInfo
from pyVmomi.vim.host import SystemHealthInfo

class HealthStatusSystem(ManagedObject):
   class Runtime(DynamicData):
      systemHealthInfo: Optional[SystemHealthInfo] = None
      hardwareStatusInfo: Optional[HardwareStatusInfo] = None

   @property
   def runtime(self) -> Runtime: ...

   def Refresh(self) -> NoReturn: ...
   def ResetSystemHealthInfo(self) -> NoReturn: ...
   def ClearSystemEventLog(self) -> NoReturn: ...
   def FetchSystemEventLog(self) -> list[SystemEventInfo]: ...
