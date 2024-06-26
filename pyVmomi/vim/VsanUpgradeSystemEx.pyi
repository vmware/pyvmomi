# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim import ClusterComputeResource
from pyVmomi.vim import HostSystem
from pyVmomi.vim import Task

from pyVmomi.vim.cluster import VsanDiskFormatConversionCheckResult
from pyVmomi.vim.cluster import VsanDiskFormatConversionSpec
from pyVmomi.vim.cluster import VsanUpgradeStatusEx

class VsanUpgradeSystemEx(ManagedObject):
   def PerformUpgrade(self, cluster: ClusterComputeResource, performObjectUpgrade: Optional[bool], downgradeFormat: Optional[bool], allowReducedRedundancy: Optional[bool], excludeHosts: list[HostSystem], spec: Optional[VsanDiskFormatConversionSpec]) -> Task: ...
   def PerformUpgradePreflightAsyncCheck(self, cluster: ClusterComputeResource, downgradeFormat: Optional[bool], spec: Optional[VsanDiskFormatConversionSpec]) -> Task: ...
   def PerformUpgradePreflightCheck(self, cluster: ClusterComputeResource, downgradeFormat: Optional[bool], spec: Optional[VsanDiskFormatConversionSpec]) -> VsanDiskFormatConversionCheckResult: ...
   def RetrieveSupportedFormatVersion(self, cluster: ClusterComputeResource) -> int: ...
   def QueryUpgradeStatus(self, cluster: ClusterComputeResource) -> VsanUpgradeStatusEx: ...
