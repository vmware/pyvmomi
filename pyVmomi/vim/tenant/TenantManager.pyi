# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import NoReturn
from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim import ManagedEntity

class TenantManager(ManagedObject):
   def MarkServiceProviderEntities(self, entity: list[ManagedEntity]) -> NoReturn: ...
   def UnmarkServiceProviderEntities(self, entity: list[ManagedEntity]) -> NoReturn: ...
   def RetrieveServiceProviderEntities(self) -> list[ManagedEntity]: ...
