# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim.ManagedEntity import ManagedEntity

class TenantManager(ManagedObject):
   def MarkServiceProviderEntities(self, entity: list[ManagedEntity]) -> None: ...
   def UnmarkServiceProviderEntities(self, entity: list[ManagedEntity]) -> None: ...
   def RetrieveServiceProviderEntities(self) -> list[ManagedEntity]: ...
