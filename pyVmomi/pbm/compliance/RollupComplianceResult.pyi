# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.pbm import ServerObjectRef

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import MethodFault

from pyVmomi.pbm.compliance import ComplianceResult

class RollupComplianceResult(DynamicData):
   oldestCheckTime: datetime
   entity: ServerObjectRef
   overallComplianceStatus: str
   overallComplianceTaskStatus: Optional[str] = None
   result: list[ComplianceResult] = []
   errorCause: list[MethodFault] = []
   profileMismatch: bool
