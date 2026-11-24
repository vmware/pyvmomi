# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vim



class TenantManager(pyVmomi.VmomiSupport.ManagedObject):
   def MarkServiceProviderEntities(self, entity: list[pyVmomi.vim.ManagedEntity]) -> None: ...
   def UnmarkServiceProviderEntities(self, entity: list[pyVmomi.vim.ManagedEntity]) -> None: ...
   def RetrieveServiceProviderEntities(self) -> list[pyVmomi.vim.ManagedEntity]: ...
