# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim.ManagedEntity import ManagedEntity

from pyVmomi.vim.TaskInfo import TaskInfo

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.event.Event import Event

from pyVmomi.vim.event.EventDescription import EventDescription

from pyVmomi.vim.event.EventFilterSpec import EventFilterSpec

from pyVmomi.vim.event.EventHistoryCollector import EventHistoryCollector

class EventManager(ManagedObject):
   class EventViewSpec(DynamicData):
      pass

   class ViewByStartId(EventViewSpec):
      startEventId: int
      isForward: bool

   @property
   def description(self) -> EventDescription: ...
   @property
   def latestEvent(self) -> Optional[Event]: ...
   @property
   def maxCollector(self) -> int: ...

   def RetrieveArgumentDescription(self, eventTypeId: str) -> list[EventDescription.EventArgDesc]: ...
   def CreateCollector(self, filter: EventFilterSpec) -> EventHistoryCollector: ...
   def LogUserEvent(self, entity: ManagedEntity, msg: str) -> None: ...
   def QueryEvent(self, filter: EventFilterSpec, eventViewSpec: Optional[EventViewSpec]) -> list[Event]: ...
   def PostEvent(self, eventToPost: Event, taskInfo: Optional[TaskInfo]) -> None: ...
