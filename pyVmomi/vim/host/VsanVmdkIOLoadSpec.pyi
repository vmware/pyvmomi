# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData

class VsanVmdkIOLoadSpec(DynamicData):
   readPct: int
   oio: int
   iosizeB: int
   dataSizeMb: long
   random: bool
   startOffsetB: Optional[long] = None
