# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.vmodl import DynamicData

class VsanPerfQuerySpec(DynamicData):
   entityRefId: str
   startTime: Optional[datetime] = None
   endTime: Optional[datetime] = None
   group: Optional[str] = None
   labels: list[str] = []
   interval: Optional[int] = None
