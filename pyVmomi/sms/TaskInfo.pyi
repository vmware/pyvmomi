# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.sms import Task

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import MethodFault

class TaskInfo(DynamicData):
   class State(Enum):
      queued: ClassVar['State'] = 'queued'
      running: ClassVar['State'] = 'running'
      success: ClassVar['State'] = 'success'
      error: ClassVar['State'] = 'error'

   key: str
   task: Task
   object: Optional[ManagedObject] = None
   error: Optional[MethodFault] = None
   result: Optional[object] = None
   startTime: Optional[datetime] = None
   completionTime: Optional[datetime] = None
   state: str
   progress: Optional[int] = None
