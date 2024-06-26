# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.vmodl import DynamicData

class VsanPerfTimeRangeQuerySpec(DynamicData):
   name: Optional[str] = None
   startTimeFrom: Optional[datetime] = None
   startTimeTo: Optional[datetime] = None
   endTimeFrom: Optional[datetime] = None
   endTimeTo: Optional[datetime] = None
