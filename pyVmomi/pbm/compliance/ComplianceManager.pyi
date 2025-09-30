# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.pbm.ServerObjectRef import ServerObjectRef

from pyVmomi.pbm.compliance.ComplianceResult import ComplianceResult

from pyVmomi.pbm.compliance.RollupComplianceResult import RollupComplianceResult

from pyVmomi.pbm.profile.ProfileId import ProfileId

class ComplianceManager(ManagedObject):
   def CheckCompliance(self, entities: list[ServerObjectRef], profile: Optional[ProfileId]) -> list[ComplianceResult]: ...
   def FetchComplianceResult(self, entities: list[ServerObjectRef], profile: Optional[ProfileId]) -> list[ComplianceResult]: ...
   def CheckRollupCompliance(self, entity: list[ServerObjectRef]) -> list[RollupComplianceResult]: ...
   def FetchRollupComplianceResult(self, entity: list[ServerObjectRef]) -> list[RollupComplianceResult]: ...
   def QueryByRollupComplianceStatus(self, status: str) -> list[ServerObjectRef]: ...
