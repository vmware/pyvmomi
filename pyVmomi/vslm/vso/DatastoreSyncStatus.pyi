# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import MethodFault

class DatastoreSyncStatus(DynamicData):
   datastoreURL: str
   objectVClock: long
   syncVClock: long
   syncTime: Optional[datetime] = None
   numberOfRetries: Optional[int] = None
   error: Optional[MethodFault] = None
