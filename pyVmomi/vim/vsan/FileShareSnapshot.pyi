# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.vsan import FileShareSnapshotConfig

class FileShareSnapshot(DynamicData):
   config: Optional[FileShareSnapshotConfig] = None
   creationTime: Optional[datetime] = None
   usedCapacity: Optional[long] = None
