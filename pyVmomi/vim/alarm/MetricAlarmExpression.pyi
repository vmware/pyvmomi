# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim import PerformanceManager

from pyVmomi.vim.alarm import AlarmExpression

class MetricAlarmExpression(AlarmExpression):
   class MetricOperator(Enum):
      isAbove: ClassVar['MetricOperator'] = 'isAbove'
      isBelow: ClassVar['MetricOperator'] = 'isBelow'

   operator: MetricOperator
   type: type
   metric: PerformanceManager.MetricId
   yellow: Optional[int] = None
   yellowInterval: Optional[int] = None
   red: Optional[int] = None
   redInterval: Optional[int] = None
