# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.host.HardwareStatusInfo import HardwareStatusInfo

from pyVmomi.vim.host.SystemEventInfo import SystemEventInfo

from pyVmomi.vim.host.SystemHealthInfo import SystemHealthInfo

class HealthStatusSystem(ManagedObject):
   class Runtime(DynamicData):
      systemHealthInfo: Optional[SystemHealthInfo] = None
      hardwareStatusInfo: Optional[HardwareStatusInfo] = None

   @property
   def runtime(self) -> Runtime: ...

   def Refresh(self) -> None: ...
   def ResetSystemHealthInfo(self) -> None: ...
   def ClearSystemEventLog(self) -> None: ...
   def FetchSystemEventLog(self) -> list[SystemEventInfo]: ...
