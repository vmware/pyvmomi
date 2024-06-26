# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import NoReturn
from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vslm import QueryDatastoreInfoResult

from pyVmomi.vim.vslm import ID

class StorageLifecycleManager(ManagedObject):
   def SyncDatastore(self, datastoreUrl: str, fullSync: bool, fcdId: Optional[ID]) -> NoReturn: ...
   def QueryDatastoreInfo(self, datastoreUrl: str) -> list[QueryDatastoreInfoResult]: ...
