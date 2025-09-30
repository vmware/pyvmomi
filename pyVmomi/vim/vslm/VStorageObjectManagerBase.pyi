# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.VmomiSupport import ManagedObject
from pyVmomi.VmomiSupport import long

from pyVmomi.vim.Datastore import Datastore

from pyVmomi.vim.Task import Task

from pyVmomi.vim.vslm.ID import ID

from pyVmomi.vim.vslm.VClockInfo import VClockInfo

class VStorageObjectManagerBase(ManagedObject):
   def ExtendDiskEx(self, id: ID, datastore: Datastore, newCapacityInMB: long) -> Task: ...
   def RenameVStorageObjectEx(self, id: ID, datastore: Datastore, name: str) -> VClockInfo: ...
   def CreateSnapshotEx(self, id: ID, datastore: Datastore, description: str) -> Task: ...
   def DeleteSnapshotEx(self, id: ID, datastore: Datastore, snapshotId: ID) -> Task: ...
   def DeleteSnapshotEx2(self, id: ID, datastore: Datastore, snapshotId: ID) -> Task: ...
   def RevertVStorageObjectEx(self, id: ID, datastore: Datastore, snapshotId: ID) -> Task: ...
