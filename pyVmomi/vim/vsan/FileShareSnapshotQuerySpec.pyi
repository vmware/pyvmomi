# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.vmodl import DynamicData

class FileShareSnapshotQuerySpec(DynamicData):
   shareUuid: str
   snapshotNames: list[str] = []
   startTime: Optional[datetime] = None
   endTime: Optional[datetime] = None
   pageSize: Optional[int] = None
   pageNumber: Optional[int] = None
