# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import PropertyPath

from pyVmomi.vim.alarm import AlarmExpression

class StateAlarmExpression(AlarmExpression):
   class StateOperator(Enum):
      isEqual: ClassVar['StateOperator'] = 'isEqual'
      isUnequal: ClassVar['StateOperator'] = 'isUnequal'

   operator: StateOperator
   type: type
   statePath: PropertyPath
   yellow: Optional[str] = None
   red: Optional[str] = None
