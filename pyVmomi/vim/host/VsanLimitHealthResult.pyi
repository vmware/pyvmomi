# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.vsan import VsanSpaceEfficiencyMetadataSize

class VsanLimitHealthResult(DynamicData):
   hostname: Optional[str] = None
   issueFound: bool
   maxComponents: int
   freeComponents: int
   componentLimitHealth: str
   lowestFreeDiskSpacePct: int
   usedDiskSpaceB: long
   totalDiskSpaceB: long
   diskFreeSpaceHealth: str
   reservedRcSizeB: long
   totalRcSizeB: long
   rcFreeReservationHealth: str
   totalLogicalSpaceB: Optional[long] = None
   logicalSpaceUsedB: Optional[long] = None
   dedupMetadataSizeB: Optional[long] = None
   diskTransientCapacityUsedB: Optional[long] = None
   dgTransientCapacityUsedB: Optional[long] = None
   slackSpaceCapRequired: Optional[long] = None
   resyncPauseThreshold: Optional[long] = None
   spaceEfficiencyMetadataSizeB: Optional[VsanSpaceEfficiencyMetadataSize] = None
   hostRebuildCapacity: Optional[long] = None
   minSpaceRequiredForVsanOp: Optional[long] = None
   enforceCapResrvSpace: Optional[long] = None
   cdReservedSizeB: Optional[long] = None
