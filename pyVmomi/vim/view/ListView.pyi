# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import NoReturn
from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim.view import ManagedObjectView
from pyVmomi.vim.view import View

class ListView(ManagedObjectView):
   def Modify(self, add: list[ManagedObject], remove: list[ManagedObject]) -> list[ManagedObject]: ...
   def Reset(self, obj: list[ManagedObject]) -> list[ManagedObject]: ...
   def ResetFromView(self, view: View) -> NoReturn: ...
