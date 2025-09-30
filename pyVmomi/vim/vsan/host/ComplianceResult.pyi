# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.vsan.host.ComplianceDetail import ComplianceDetail

class ComplianceResult(DynamicData):
   checkTime: datetime
   policyId: Optional[str] = None
   policyGen: Optional[int] = None
   objComplianceDetail: list[ComplianceDetail] = []
