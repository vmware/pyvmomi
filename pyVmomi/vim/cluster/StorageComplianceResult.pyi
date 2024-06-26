# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.cluster import StorageOperationalStatus
from pyVmomi.vim.cluster import StoragePolicyStatus

class StorageComplianceResult(DynamicData):
   class StorageComplianceStatus(Enum):
      compliant: ClassVar['StorageComplianceStatus'] = 'compliant'
      nonCompliant: ClassVar['StorageComplianceStatus'] = 'nonCompliant'
      unknown: ClassVar['StorageComplianceStatus'] = 'unknown'
      notApplicable: ClassVar['StorageComplianceStatus'] = 'notApplicable'

   checkTime: Optional[datetime] = None
   profile: Optional[str] = None
   objectUUID: Optional[str] = None
   complianceStatus: str
   mismatch: bool
   violatedPolicies: list[StoragePolicyStatus] = []
   operationalStatus: Optional[StorageOperationalStatus] = None
   objPolicyGenerationId: Optional[str] = None
