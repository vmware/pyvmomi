# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.eam.Agency import Agency

from pyVmomi.eam.EamObject import EamObject

from pyVmomi.eam.issue.Issue import Issue

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
   def ScanForUnknownAgentVm(self) -> None: ...
   def SetMaintenanceModePolicy(self, policy: str) -> None: ...
   def GetMaintenanceModePolicy(self) -> str: ...
