# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim import ManagedEntity
from pyVmomi.vim import TaskInfo

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.alarm import Alarm

from pyVmomi.vim.scheduler import ScheduledTask

class TaskFilterSpec(DynamicData):
   class RecursionOption(Enum):
      self: ClassVar['RecursionOption'] = 'self'
      children: ClassVar['RecursionOption'] = 'children'
      all: ClassVar['RecursionOption'] = 'all'

   class TimeOption(Enum):
      queuedTime: ClassVar['TimeOption'] = 'queuedTime'
      startedTime: ClassVar['TimeOption'] = 'startedTime'
      completedTime: ClassVar['TimeOption'] = 'completedTime'

   class ByEntity(DynamicData):
      entity: ManagedEntity
      recursion: RecursionOption

   class ByTime(DynamicData):
      timeType: TimeOption
      beginTime: Optional[datetime] = None
      endTime: Optional[datetime] = None

   class ByUsername(DynamicData):
      systemUser: bool
      userList: list[str] = []

   entity: Optional[ByEntity] = None
   time: Optional[ByTime] = None
   userName: Optional[ByUsername] = None
   activationId: list[str] = []
   state: list[TaskInfo.State] = []
   alarm: Optional[Alarm] = None
   scheduledTask: Optional[ScheduledTask] = None
   eventChainId: list[int] = []
   tag: list[str] = []
   parentTaskKey: list[str] = []
   rootTaskKey: list[str] = []
