# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim import ComputeResource

from pyVmomi.vim.cluster import QueryVsanManagedStorageSpaceUsageSpec
from pyVmomi.vim.cluster import VsanEntitySpaceUsage
from pyVmomi.vim.cluster import VsanSpaceQuerySpec
from pyVmomi.vim.cluster import VsanSpaceUsage
from pyVmomi.vim.cluster import VsanSpaceUsageWithDatastoreType

from pyVmomi.vim.vm import ProfileSpec

class VsanSpaceReportSystem(ManagedObject):
   def QuerySpaceUsage(self, cluster: ComputeResource, storagePolicies: list[ProfileSpec], whatifCapacityOnly: Optional[bool]) -> VsanSpaceUsage: ...
   def QueryVsanManagedStorageSpaceUsage(self, cluster: ComputeResource, querySpec: QueryVsanManagedStorageSpaceUsageSpec) -> list[VsanSpaceUsageWithDatastoreType]: ...
   def QueryEntitySpaceUsage(self, cluster: ComputeResource, querySpec: VsanSpaceQuerySpec) -> list[VsanEntitySpaceUsage]: ...
