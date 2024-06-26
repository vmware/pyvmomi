# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import NoReturn

from pyVmomi.vim import ExtensibleManagedObject

from pyVmomi.vim.alarm import AlarmInfo
from pyVmomi.vim.alarm import AlarmSpec

class Alarm(ExtensibleManagedObject):
   @property
   def info(self) -> AlarmInfo: ...

   def Remove(self) -> NoReturn: ...
   def Reconfigure(self, spec: AlarmSpec) -> NoReturn: ...
