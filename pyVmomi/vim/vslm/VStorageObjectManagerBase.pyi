# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.VmomiSupport import ManagedObject
from pyVmomi.VmomiSupport import long

from pyVmomi.vim import Datastore
from pyVmomi.vim import Task

from pyVmomi.vim.vslm import ID
from pyVmomi.vim.vslm import VClockInfo

class VStorageObjectManagerBase(ManagedObject):
   def ExtendDiskEx(self, id: ID, datastore: Datastore, newCapacityInMB: long) -> Task: ...
   def RenameVStorageObjectEx(self, id: ID, datastore: Datastore, name: str) -> VClockInfo: ...
   def CreateSnapshotEx(self, id: ID, datastore: Datastore, description: str) -> Task: ...
   def DeleteSnapshotEx(self, id: ID, datastore: Datastore, snapshotId: ID) -> Task: ...
   def RevertVStorageObjectEx(self, id: ID, datastore: Datastore, snapshotId: ID) -> Task: ...
