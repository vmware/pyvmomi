# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import byte
from pyVmomi.VmomiSupport import long
from pyVmomi.VmomiSupport import short

from pyVmomi.vmodl import DynamicData

class NumaNode(DynamicData):
   typeId: byte
   cpuID: list[short] = []
   memorySize: Optional[long] = None
   memoryRangeBegin: long
   memoryRangeLength: long
   pciId: list[str] = []
