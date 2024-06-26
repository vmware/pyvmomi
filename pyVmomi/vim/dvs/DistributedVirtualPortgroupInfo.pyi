# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.dvs import DistributedVirtualPortgroup

class DistributedVirtualPortgroupInfo(DynamicData):
   switchName: str
   switchUuid: str
   portgroupName: str
   portgroupKey: str
   portgroupType: str
   uplinkPortgroup: bool
   portgroup: DistributedVirtualPortgroup
   networkReservationSupported: Optional[bool] = None
   backingType: Optional[str] = None
   logicalSwitchUuid: Optional[str] = None
   segmentId: Optional[str] = None
