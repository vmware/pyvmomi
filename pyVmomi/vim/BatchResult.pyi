# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim import Datastore

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import MethodFault

class BatchResult(DynamicData):
   class Result(Enum):
      success: ClassVar['Result'] = 'success'
      fail: ClassVar['Result'] = 'fail'

   result: str
   hostKey: str
   ds: Optional[Datastore] = None
   fault: Optional[MethodFault] = None
