# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import PropertyPath

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import LocalizableMessage

from pyVmomi.vim.host import ConfigSpec

from pyVmomi.vim.profile import DeferredPolicyOptionParameter
from pyVmomi.vim.profile import ProfilePropertyPath

class ExecuteResult(DynamicData):
   class Status(Enum):
      success: ClassVar['Status'] = 'success'
      needInput: ClassVar['Status'] = 'needInput'
      error: ClassVar['Status'] = 'error'

   class ExecuteError(DynamicData):
      path: Optional[ProfilePropertyPath] = None
      message: LocalizableMessage

   status: str
   configSpec: Optional[ConfigSpec] = None
   inapplicablePath: list[PropertyPath] = []
   requireInput: list[DeferredPolicyOptionParameter] = []
   error: list[ExecuteError] = []
