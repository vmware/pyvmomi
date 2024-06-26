# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.vim import HostSystem

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import LocalizableMessage

from pyVmomi.vim.profile import ProfilePropertyPath

class AnswerFileStatusResult(DynamicData):
   class AnswerFileStatusError(DynamicData):
      userInputPath: ProfilePropertyPath
      errMsg: LocalizableMessage

   checkedTime: datetime
   host: HostSystem
   status: str
   error: list[AnswerFileStatusError] = []
