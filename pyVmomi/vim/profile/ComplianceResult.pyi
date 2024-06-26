# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim import ManagedEntity

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import LocalizableMessage

from pyVmomi.vim.profile import Profile

class ComplianceResult(DynamicData):
   class Status(Enum):
      compliant: ClassVar['Status'] = 'compliant'
      nonCompliant: ClassVar['Status'] = 'nonCompliant'
      unknown: ClassVar['Status'] = 'unknown'
      running: ClassVar['Status'] = 'running'

   class ComplianceFailure(DynamicData):
      class ComplianceFailureValues(DynamicData):
         comparisonIdentifier: str
         profileInstance: Optional[str] = None
         hostValue: Optional[object] = None
         profileValue: Optional[object] = None

      failureType: str
      message: LocalizableMessage
      expressionName: Optional[str] = None
      failureValues: list[ComplianceFailureValues] = []

   profile: Optional[Profile] = None
   complianceStatus: str
   entity: Optional[ManagedEntity] = None
   checkTime: Optional[datetime] = None
   failure: list[ComplianceFailure] = []
