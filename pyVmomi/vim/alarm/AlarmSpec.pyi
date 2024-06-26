# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.alarm import AlarmAction
from pyVmomi.vim.alarm import AlarmExpression
from pyVmomi.vim.alarm import AlarmSetting

class AlarmSpec(DynamicData):
   name: str
   systemName: Optional[str] = None
   description: str
   enabled: bool
   expression: AlarmExpression
   action: Optional[AlarmAction] = None
   actionFrequency: Optional[int] = None
   setting: Optional[AlarmSetting] = None
