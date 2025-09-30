# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim.ManagedEntity import ManagedEntity

from pyVmomi.vim.view.ContainerView import ContainerView

from pyVmomi.vim.view.InventoryView import InventoryView

from pyVmomi.vim.view.ListView import ListView

from pyVmomi.vim.view.View import View

class ViewManager(ManagedObject):
   @property
   def viewList(self) -> list[View]: ...

   def CreateInventoryView(self) -> InventoryView: ...
   def CreateContainerView(self, container: ManagedEntity, type: list[type], recursive: bool) -> ContainerView: ...
   def CreateListView(self, obj: list[ManagedObject]) -> ListView: ...
   def CreateListViewFromView(self, view: View) -> ListView: ...
