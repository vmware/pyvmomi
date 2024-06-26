# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import ScsiDisk
from pyVmomi.vim.host import VsanDiskRebalanceResult

class VsanPhysicalDiskHealth(DynamicData):
   name: str
   uuid: str
   inCmmds: bool
   inVsi: bool
   dedupScope: Optional[long] = None
   formatVersion: Optional[int] = None
   isAllFlash: Optional[int] = None
   congestionValue: Optional[int] = None
   congestionArea: Optional[str] = None
   congestionHealth: Optional[str] = None
   metadataHealth: Optional[str] = None
   operationalHealthDescription: Optional[str] = None
   operationalHealth: Optional[str] = None
   dedupUsageHealth: Optional[str] = None
   capacityHealth: Optional[str] = None
   summaryHealth: str
   capacity: Optional[long] = None
   usedCapacity: Optional[long] = None
   reservedCapacity: Optional[long] = None
   totalBytes: Optional[long] = None
   freeBytes: Optional[long] = None
   hashedBytes: Optional[long] = None
   dedupedBytes: Optional[long] = None
   scsiDisk: Optional[ScsiDisk] = None
   usedComponents: Optional[long] = None
   maxComponents: Optional[long] = None
   compLimitHealth: Optional[str] = None
   encryptionEnabled: Optional[bool] = None
   kmsProviderId: Optional[str] = None
   kekId: Optional[str] = None
   dekGenerationId: Optional[long] = None
   encryptedUnlocked: Optional[bool] = None
   rebalanceResult: Optional[VsanDiskRebalanceResult] = None
   dekId: Optional[str] = None
   kekVerifierHealth: Optional[bool] = None
   dekVerifierHealth: Optional[bool] = None
   logicalCapacity: Optional[long] = None
   logicalCapacityUsed: Optional[long] = None
   logicalCapacityHealth: Optional[str] = None
   vsanDiskGroupUuid: Optional[str] = None
   dgLayoutIssue: Optional[bool] = None
   usedMetadataComponents: Optional[long] = None
   maxMetadataComponents: Optional[long] = None
   pendingClusterDekId: Optional[str] = None
   dmekVerifierHealth: Optional[bool] = None
