# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vim import ElementDescription
from pyVmomi.vim import TypeDescription

from pyVmomi.vmodl import DynamicData

class ScheduledTaskDescription(DynamicData):
   class SchedulerDetail(TypeDescription):
      frequency: str

   action: list[TypeDescription] = []
   schedulerInfo: list[SchedulerDetail] = []
   state: list[ElementDescription] = []
   dayOfWeek: list[ElementDescription] = []
   weekOfMonth: list[ElementDescription] = []
