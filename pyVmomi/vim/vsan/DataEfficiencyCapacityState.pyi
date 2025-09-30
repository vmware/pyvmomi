# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.vsan.VsanSpaceEfficiencyMetadataSize import VsanSpaceEfficiencyMetadataSize

class DataEfficiencyCapacityState(DynamicData):
   logicalCapacity: Optional[long] = None
   logicalCapacityUsed: Optional[long] = None
   physicalCapacity: Optional[long] = None
   physicalCapacityUsed: Optional[long] = None
   dedupMetadataSize: Optional[long] = None
   spaceEfficiencyMetadataSize: Optional[VsanSpaceEfficiencyMetadataSize] = None
   esaDedupSpaceSaving: Optional[long] = None
   esaCompressionSpaceSaving: Optional[long] = None
   totalSpaceUsedWithoutOverhead: Optional[long] = None
