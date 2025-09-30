# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim.ManagedEntity import ManagedEntity

from pyVmomi.vim.Task import Task

from pyVmomi.vim.profile.ComplianceResult import ComplianceResult

from pyVmomi.vim.profile.ExpressionMetadata import ExpressionMetadata

from pyVmomi.vim.profile.Profile import Profile

class ComplianceManager(ManagedObject):
   def CheckCompliance(self, profile: list[Profile], entity: list[ManagedEntity]) -> Task: ...
   def QueryComplianceStatus(self, profile: list[Profile], entity: list[ManagedEntity]) -> list[ComplianceResult]: ...
   def ClearComplianceStatus(self, profile: list[Profile], entity: list[ManagedEntity]) -> None: ...
   def QueryExpressionMetadata(self, expressionName: list[str], profile: Optional[Profile]) -> list[ExpressionMetadata]: ...
