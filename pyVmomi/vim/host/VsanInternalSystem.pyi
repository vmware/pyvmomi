# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import NoReturn
from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject
from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import LocalizableMessage

class VsanInternalSystem(ManagedObject):
   class CmmdsQuery(DynamicData):
      type: Optional[str] = None
      uuid: Optional[str] = None
      owner: Optional[str] = None

   class PolicyCost(DynamicData):
      changeDataSize: Optional[long] = None
      currentDataSize: Optional[long] = None
      tempDataSize: Optional[long] = None
      copyDataSize: Optional[long] = None
      changeFlashReadCacheSize: Optional[long] = None
      currentFlashReadCacheSize: Optional[long] = None
      currentDiskSpaceToAddressSpaceRatio: Optional[float] = None
      diskSpaceToAddressSpaceRatio: Optional[float] = None

   class PolicySatisfiability(DynamicData):
      uuid: Optional[str] = None
      isSatisfiable: bool
      reason: Optional[LocalizableMessage] = None
      cost: Optional[PolicyCost] = None

   class PolicyChangeBatch(DynamicData):
      uuid: list[str] = []
      policy: Optional[str] = None

   class NewPolicyBatch(DynamicData):
      size: list[long] = []
      policy: Optional[str] = None

   class VsanPhysicalDiskDiagnosticsResult(DynamicData):
      diskUuid: str
      success: bool
      failureReason: Optional[str] = None

   class DeleteVsanObjectsResult(DynamicData):
      uuid: str
      success: bool
      failureReason: list[LocalizableMessage] = []

   class VsanObjectOperationResult(DynamicData):
      uuid: str
      failureReason: list[LocalizableMessage] = []

   def QueryCmmds(self, queries: list[CmmdsQuery]) -> str: ...
   def QueryPhysicalVsanDisks(self, props: list[str]) -> str: ...
   def QueryVsanObjects(self, uuids: list[str]) -> str: ...
   def QueryObjectsOnPhysicalVsanDisk(self, disks: list[str]) -> str: ...
   def AbdicateDomOwnership(self, uuids: list[str]) -> list[str]: ...
   def QueryVsanStatistics(self, labels: list[str]) -> str: ...
   def ReconfigureDomObject(self, uuid: str, policy: str) -> NoReturn: ...
   def QuerySyncingVsanObjects(self, uuids: list[str]) -> str: ...
   def RunVsanPhysicalDiskDiagnostics(self, disks: list[str]) -> list[VsanPhysicalDiskDiagnosticsResult]: ...
   def GetVsanObjExtAttrs(self, uuids: list[str]) -> str: ...
   def ReconfigurationSatisfiable(self, pcbs: list[PolicyChangeBatch], ignoreSatisfiability: Optional[bool]) -> list[PolicySatisfiability]: ...
   def CanProvisionObjects(self, npbs: list[NewPolicyBatch], ignoreSatisfiability: Optional[bool]) -> list[PolicySatisfiability]: ...
   def DeleteVsanObjects(self, uuids: list[str], force: Optional[bool]) -> list[DeleteVsanObjectsResult]: ...
   def UpgradeVsanObjects(self, uuids: list[str], newVersion: int) -> list[VsanObjectOperationResult]: ...
   def QueryVsanObjectUuidsByFilter(self, uuids: list[str], limit: Optional[int], version: Optional[int]) -> list[str]: ...
