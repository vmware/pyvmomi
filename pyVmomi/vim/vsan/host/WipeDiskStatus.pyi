# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import LocalizableMessage

class WipeDiskStatus(DynamicData):
   disk: str
   eligible: str
   ineligibleReason: list[LocalizableMessage] = []
   wipeState: Optional[str] = None
   percentageCompleted: Optional[int] = None
   estimatedTime: Optional[long] = None
   wipeStartTime: Optional[datetime] = None
   wipeCompleteTime: Optional[datetime] = None
