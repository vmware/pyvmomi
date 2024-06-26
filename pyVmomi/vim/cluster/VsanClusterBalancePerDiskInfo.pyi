# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData

class VsanClusterBalancePerDiskInfo(DynamicData):
   uuid: Optional[str] = None
   fullness: long
   variance: long
   fullnessAboveThreshold: long
   dataToMoveB: long
   compFullness: Optional[long] = None
   compVariance: Optional[long] = None
