# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vim.ExtensibleManagedObject import ExtensibleManagedObject

from pyVmomi.vim.alarm.AlarmInfo import AlarmInfo

from pyVmomi.vim.alarm.AlarmSpec import AlarmSpec

class Alarm(ExtensibleManagedObject):
   @property
   def info(self) -> AlarmInfo: ...

   def Remove(self) -> None: ...
   def Reconfigure(self, spec: AlarmSpec) -> None: ...
