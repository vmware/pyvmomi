# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import NoReturn

from pyVmomi.VmomiSupport import ManagedObject

class HistoryCollector(ManagedObject):
   @property
   def filter(self) -> object: ...

   def SetLatestPageSize(self, maxCount: int) -> NoReturn: ...
   def Rewind(self) -> NoReturn: ...
   def Reset(self) -> NoReturn: ...
   def Remove(self) -> NoReturn: ...
