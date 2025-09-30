# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.pbm.ServerObjectRef import ServerObjectRef

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vmodl.MethodFault import MethodFault

from pyVmomi.pbm.compliance.ComplianceResult import ComplianceResult

class RollupComplianceResult(DynamicData):
   oldestCheckTime: datetime
   entity: ServerObjectRef
   overallComplianceStatus: str
   overallComplianceTaskStatus: Optional[str] = None
   result: list[ComplianceResult] = []
   errorCause: list[MethodFault] = []
   profileMismatch: bool
