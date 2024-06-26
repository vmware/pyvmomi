# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import MethodFault

class VsanProactiveRebalanceInfoEx(DynamicData):
   running: Optional[bool] = None
   startTs: Optional[datetime] = None
   stopTs: Optional[datetime] = None
   varianceThreshold: Optional[float] = None
   timeThreshold: Optional[int] = None
   rateThreshold: Optional[int] = None
   hostname: Optional[str] = None
   error: Optional[MethodFault] = None
