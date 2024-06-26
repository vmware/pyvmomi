# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim import ComputeResource
from pyVmomi.vim import Task

from pyVmomi.vim.cluster import VsanObjIdentityQuerySpec
from pyVmomi.vim.cluster import VsanObjectIdentityAndHealth
from pyVmomi.vim.cluster import VsanObjectInformation
from pyVmomi.vim.cluster import VsanObjectQuerySpec
from pyVmomi.vim.cluster import VsanSyncingObjectFilter

from pyVmomi.vim.vm import ProfileSpec

from pyVmomi.vim.vsan.host import VsanSyncingObjectQueryResult

class VsanObjectSystem(ManagedObject):
   def SetVsanObjectPolicy(self, cluster: Optional[ComputeResource], vsanObjectUuid: str, profile: Optional[ProfileSpec]) -> bool: ...
   def QueryVsanObjectInformation(self, cluster: Optional[ComputeResource], vsanObjectQuerySpecs: list[VsanObjectQuerySpec]) -> list[VsanObjectInformation]: ...
   def QueryObjectIdentities(self, cluster: Optional[ComputeResource], objUuids: list[str], objTypes: list[str], includeHealth: Optional[bool], includeObjIdentity: Optional[bool], includeSpaceSummary: Optional[bool], extraQuerySpec: Optional[VsanObjIdentityQuerySpec]) -> Optional[VsanObjectIdentityAndHealth]: ...
   def DeleteObjects(self, cluster: Optional[ComputeResource], objUuids: list[str], force: Optional[bool]) -> Task: ...
   def QueryInaccessibleVmSwapObjects(self, cluster: Optional[ComputeResource]) -> list[str]: ...
   def QuerySyncingVsanObjectsSummary(self, cluster: ComputeResource, syncingObjectFilter: Optional[VsanSyncingObjectFilter]) -> VsanSyncingObjectQueryResult: ...
   def RelayoutObjects(self, cluster: ComputeResource) -> Task: ...
