# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.vsan.FileShareSnapshotConfig import FileShareSnapshotConfig

class FileShareSnapshot(DynamicData):
   config: Optional[FileShareSnapshotConfig] = None
   creationTime: Optional[datetime] = None
   usedCapacity: Optional[long] = None
