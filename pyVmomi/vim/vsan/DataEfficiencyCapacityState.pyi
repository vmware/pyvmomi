# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.vsan import VsanSpaceEfficiencyMetadataSize

class DataEfficiencyCapacityState(DynamicData):
   logicalCapacity: Optional[long] = None
   logicalCapacityUsed: Optional[long] = None
   physicalCapacity: Optional[long] = None
   physicalCapacityUsed: Optional[long] = None
   dedupMetadataSize: Optional[long] = None
   spaceEfficiencyMetadataSize: Optional[VsanSpaceEfficiencyMetadataSize] = None
