# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim import ManagedEntity

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.alarm import AlarmExpression

class EventAlarmExpression(AlarmExpression):
   class ComparisonOperator(Enum):
      equals: ClassVar['ComparisonOperator'] = 'equals'
      notEqualTo: ClassVar['ComparisonOperator'] = 'notEqualTo'
      startsWith: ClassVar['ComparisonOperator'] = 'startsWith'
      doesNotStartWith: ClassVar['ComparisonOperator'] = 'doesNotStartWith'
      endsWith: ClassVar['ComparisonOperator'] = 'endsWith'
      doesNotEndWith: ClassVar['ComparisonOperator'] = 'doesNotEndWith'

   class Comparison(DynamicData):
      attributeName: str
      operator: str
      value: str

   comparisons: list[Comparison] = []
   eventType: type
   eventTypeId: Optional[str] = None
   objectType: Optional[type] = None
   status: Optional[ManagedEntity.Status] = None
