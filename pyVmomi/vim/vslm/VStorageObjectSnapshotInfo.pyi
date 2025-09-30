# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.vslm.ID import ID

class VStorageObjectSnapshotInfo(DynamicData):
   class VStorageObjectSnapshot(DynamicData):
      id: Optional[ID] = None
      backingObjectId: Optional[str] = None
      createTime: datetime
      description: str

   snapshots: list[VStorageObjectSnapshot] = []
