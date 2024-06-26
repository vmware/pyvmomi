# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

class InfraUpdateHaConfigInfo(DynamicData):
   class BehaviorType(Enum):
      Manual: ClassVar['BehaviorType'] = 'Manual'
      Automated: ClassVar['BehaviorType'] = 'Automated'

   class RemediationType(Enum):
      QuarantineMode: ClassVar['RemediationType'] = 'QuarantineMode'
      MaintenanceMode: ClassVar['RemediationType'] = 'MaintenanceMode'

   enabled: Optional[bool] = None
   behavior: Optional[str] = None
   moderateRemediation: Optional[str] = None
   severeRemediation: Optional[str] = None
   providers: list[str] = []
