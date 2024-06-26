# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import NoReturn
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.eam import Agency
from pyVmomi.eam import EamObject

from pyVmomi.eam.issue import Issue

class EsxAgentManager(EamObject):
   class MaintenanceModePolicy(Enum):
      singleHost: ClassVar['MaintenanceModePolicy'] = 'singleHost'
      multipleHosts: ClassVar['MaintenanceModePolicy'] = 'multipleHosts'

   @property
   def agency(self) -> list[Agency]: ...
   @property
   def issue(self) -> list[Issue]: ...

   def QueryAgency(self) -> list[Agency]: ...
   def CreateAgency(self, agencyConfigInfo: Agency.ConfigInfo, initialGoalState: str) -> Agency: ...
   def ScanForUnknownAgentVm(self) -> NoReturn: ...
   def SetMaintenanceModePolicy(self, policy: str) -> NoReturn: ...
   def GetMaintenanceModePolicy(self) -> str: ...
