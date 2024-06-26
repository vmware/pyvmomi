# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.pbm import ServerObjectRef

from pyVmomi.pbm.compliance import ComplianceResult
from pyVmomi.pbm.compliance import RollupComplianceResult

from pyVmomi.pbm.profile import ProfileId

class ComplianceManager(ManagedObject):
   def CheckCompliance(self, entities: list[ServerObjectRef], profile: Optional[ProfileId]) -> list[ComplianceResult]: ...
   def FetchComplianceResult(self, entities: list[ServerObjectRef], profile: Optional[ProfileId]) -> list[ComplianceResult]: ...
   def CheckRollupCompliance(self, entity: list[ServerObjectRef]) -> list[RollupComplianceResult]: ...
   def FetchRollupComplianceResult(self, entity: list[ServerObjectRef]) -> list[RollupComplianceResult]: ...
   def QueryByRollupComplianceStatus(self, status: str) -> list[ServerObjectRef]: ...
