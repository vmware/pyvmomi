# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vim import KeyValue

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import MethodFault

from pyVmomi.vim.vslm import ID

from pyVmomi.vslm.vso import VStorageObjectSnapshotResult

class VStorageObjectResult(DynamicData):
   id: ID
   name: Optional[str] = None
   capacityInMB: long
   createTime: Optional[datetime] = None
   datastoreUrl: Optional[str] = None
   diskPath: Optional[str] = None
   usedCapacityInMB: Optional[long] = None
   backingObjectId: Optional[ID] = None
   snapshotInfo: list[VStorageObjectSnapshotResult] = []
   metadata: list[KeyValue] = []
   error: Optional[MethodFault] = None
