# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.pbm import ExtendedElementDescription
from pyVmomi.pbm import ServerObjectRef

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import MethodFault

from pyVmomi.pbm.compliance import OperationalStatus
from pyVmomi.pbm.compliance import PolicyStatus

from pyVmomi.pbm.profile import ProfileId

class ComplianceResult(DynamicData):
   class ComplianceStatus(Enum):
      compliant: ClassVar['ComplianceStatus'] = 'compliant'
      nonCompliant: ClassVar['ComplianceStatus'] = 'nonCompliant'
      unknown: ClassVar['ComplianceStatus'] = 'unknown'
      notApplicable: ClassVar['ComplianceStatus'] = 'notApplicable'
      outOfDate: ClassVar['ComplianceStatus'] = 'outOfDate'

   class ComplianceTaskStatus(Enum):
      inProgress: ClassVar['ComplianceTaskStatus'] = 'inProgress'
      success: ClassVar['ComplianceTaskStatus'] = 'success'
      failed: ClassVar['ComplianceTaskStatus'] = 'failed'

   checkTime: datetime
   entity: ServerObjectRef
   profile: Optional[ProfileId] = None
   complianceTaskStatus: Optional[str] = None
   complianceStatus: str
   mismatch: bool
   violatedPolicies: list[PolicyStatus] = []
   errorCause: list[MethodFault] = []
   operationalStatus: Optional[OperationalStatus] = None
   info: Optional[ExtendedElementDescription] = None
