# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import ManagedMethod

from pyVmomi.vim import ManagedEntity
from pyVmomi.vim import Task
from pyVmomi.vim import TaskReason

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import KeyAnyValue
from pyVmomi.vmodl import LocalizableMessage
from pyVmomi.vmodl import MethodFault

class TaskInfo(DynamicData):
   class State(Enum):
      queued: ClassVar['State'] = 'queued'
      running: ClassVar['State'] = 'running'
      success: ClassVar['State'] = 'success'
      error: ClassVar['State'] = 'error'

   key: str
   task: Task
   description: Optional[LocalizableMessage] = None
   name: Optional[ManagedMethod] = None
   descriptionId: str
   entity: Optional[ManagedEntity] = None
   entityName: Optional[str] = None
   locked: list[ManagedEntity] = []
   state: State
   cancelled: bool
   cancelable: bool
   error: Optional[MethodFault] = None
   result: Optional[object] = None
   progress: Optional[int] = None
   progressDetails: list[KeyAnyValue] = []
   reason: TaskReason
   queueTime: datetime
   startTime: Optional[datetime] = None
   completeTime: Optional[datetime] = None
   eventChainId: int
   changeTag: Optional[str] = None
   parentTaskKey: Optional[str] = None
   rootTaskKey: Optional[str] = None
   activationId: Optional[str] = None
