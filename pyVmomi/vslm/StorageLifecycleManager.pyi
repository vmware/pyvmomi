# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vslm.QueryDatastoreInfoResult import QueryDatastoreInfoResult

from pyVmomi.vim.vslm.ID import ID

class StorageLifecycleManager(ManagedObject):
   def SyncDatastore(self, datastoreUrl: str, fullSync: bool, fcdId: Optional[ID]) -> None: ...
   def QueryDatastoreInfo(self, datastoreUrl: str) -> list[QueryDatastoreInfoResult]: ...
