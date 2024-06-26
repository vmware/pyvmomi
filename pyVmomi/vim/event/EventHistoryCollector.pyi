# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import HistoryCollector

from pyVmomi.vim.event import Event

class EventHistoryCollector(HistoryCollector):
   @property
   def latestPage(self) -> list[Event]: ...
   @property
   def initialized(self) -> Optional[bool]: ...

   def ReadNext(self, maxCount: int) -> list[Event]: ...
   def ReadPrev(self, maxCount: int) -> list[Event]: ...
