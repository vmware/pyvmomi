# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim import ManagedEntity

from pyVmomi.vim.view import ContainerView
from pyVmomi.vim.view import InventoryView
from pyVmomi.vim.view import ListView
from pyVmomi.vim.view import View

class ViewManager(ManagedObject):
   @property
   def viewList(self) -> list[View]: ...

   def CreateInventoryView(self) -> InventoryView: ...
   def CreateContainerView(self, container: ManagedEntity, type: list[type], recursive: bool) -> ContainerView: ...
   def CreateListView(self, obj: list[ManagedObject]) -> ListView: ...
   def CreateListViewFromView(self, view: View) -> ListView: ...
