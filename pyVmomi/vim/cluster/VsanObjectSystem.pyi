# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim.ComputeResource import ComputeResource

from pyVmomi.vim.Task import Task

from pyVmomi.vim.cluster.VsanObjIdentityQuerySpec import VsanObjIdentityQuerySpec

from pyVmomi.vim.cluster.VsanObjectIdentityAndHealth import VsanObjectIdentityAndHealth

from pyVmomi.vim.cluster.VsanObjectInformation import VsanObjectInformation

from pyVmomi.vim.cluster.VsanObjectQuerySpec import VsanObjectQuerySpec

from pyVmomi.vim.cluster.VsanSyncingObjectFilter import VsanSyncingObjectFilter

from pyVmomi.vim.vm.ProfileSpec import ProfileSpec

from pyVmomi.vim.vsan.host.VsanSyncingObjectQueryResult import VsanSyncingObjectQueryResult

class VsanObjectSystem(ManagedObject):
   def SetVsanObjectPolicy(self, cluster: Optional[ComputeResource], vsanObjectUuid: str, profile: Optional[ProfileSpec]) -> bool: ...
   def QueryVsanObjectInformation(self, cluster: Optional[ComputeResource], vsanObjectQuerySpecs: list[VsanObjectQuerySpec]) -> list[VsanObjectInformation]: ...
   def QueryObjectIdentities(self, cluster: Optional[ComputeResource], objUuids: list[str], objTypes: list[str], includeHealth: Optional[bool], includeObjIdentity: Optional[bool], includeSpaceSummary: Optional[bool], extraQuerySpec: Optional[VsanObjIdentityQuerySpec]) -> Optional[VsanObjectIdentityAndHealth]: ...
   def DeleteObjects(self, cluster: Optional[ComputeResource], objUuids: list[str], force: Optional[bool]) -> Task: ...
   def QueryInaccessibleVmSwapObjects(self, cluster: Optional[ComputeResource]) -> list[str]: ...
   def QuerySyncingVsanObjectsSummary(self, cluster: ComputeResource, syncingObjectFilter: Optional[VsanSyncingObjectFilter]) -> VsanSyncingObjectQueryResult: ...
   def RelayoutObjects(self, cluster: ComputeResource) -> Task: ...
