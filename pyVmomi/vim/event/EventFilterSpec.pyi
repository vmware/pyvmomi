# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim.ManagedEntity import ManagedEntity

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.alarm.Alarm import Alarm

from pyVmomi.vim.scheduler.ScheduledTask import ScheduledTask

class EventFilterSpec(DynamicData):
   class RecursionOption(Enum):
      self: ClassVar['RecursionOption'] = 'self'
      children: ClassVar['RecursionOption'] = 'children'
      all: ClassVar['RecursionOption'] = 'all'

   class ByEntity(DynamicData):
      entity: ManagedEntity
      recursion: RecursionOption

   class ByTime(DynamicData):
      beginTime: Optional[datetime] = None
      endTime: Optional[datetime] = None

   class ByUsername(DynamicData):
      systemUser: bool
      userList: list[str] = []

   entity: Optional[ByEntity] = None
   time: Optional[ByTime] = None
   userName: Optional[ByUsername] = None
   eventChainId: Optional[int] = None
   alarm: Optional[Alarm] = None
   scheduledTask: Optional[ScheduledTask] = None
   disableFullMessage: Optional[bool] = None
   category: list[str] = []
   type: list[type] = []
   tag: list[str] = []
   eventTypeId: list[str] = []
   maxCount: Optional[int] = None
   delayedInit: Optional[bool] = None
