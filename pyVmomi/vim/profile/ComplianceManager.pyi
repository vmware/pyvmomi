# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import NoReturn
from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim import ManagedEntity
from pyVmomi.vim import Task

from pyVmomi.vim.profile import ComplianceResult
from pyVmomi.vim.profile import ExpressionMetadata
from pyVmomi.vim.profile import Profile

class ComplianceManager(ManagedObject):
   def CheckCompliance(self, profile: list[Profile], entity: list[ManagedEntity]) -> Task: ...
   def QueryComplianceStatus(self, profile: list[Profile], entity: list[ManagedEntity]) -> list[ComplianceResult]: ...
   def ClearComplianceStatus(self, profile: list[Profile], entity: list[ManagedEntity]) -> NoReturn: ...
   def QueryExpressionMetadata(self, expressionName: list[str], profile: Optional[Profile]) -> list[ExpressionMetadata]: ...
