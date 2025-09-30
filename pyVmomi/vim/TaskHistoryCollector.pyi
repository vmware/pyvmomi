# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.HistoryCollector import HistoryCollector

from pyVmomi.vim.TaskInfo import TaskInfo

class TaskHistoryCollector(HistoryCollector):
   @property
   def latestPage(self) -> list[TaskInfo]: ...

   def ReadNext(self, maxCount: int) -> list[TaskInfo]: ...
   def ReadPrev(self, maxCount: int) -> list[TaskInfo]: ...
