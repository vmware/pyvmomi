# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData

class DiskClaimConfiguration(DynamicData):
   diskType: str
   diskNamePrefix: Optional[str] = None
   numberOfDisks: Optional[int] = None
   diskModel: Optional[str] = None
   vendor: Optional[str] = None
   diskCapacity: Optional[long] = None
