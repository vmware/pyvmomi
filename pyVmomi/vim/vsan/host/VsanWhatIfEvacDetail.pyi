# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData

class VsanWhatIfEvacDetail(DynamicData):
   success: Optional[bool] = None
   bytesToSync: Optional[long] = None
   inaccessibleObjects: list[str] = []
   incompliantObjects: list[str] = []
   extraSpaceNeeded: Optional[long] = None
   failedDueToInaccessibleObjects: Optional[bool] = None
