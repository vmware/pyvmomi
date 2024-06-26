# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim import ClusterComputeResource
from pyVmomi.vim import HostSystem
from pyVmomi.vim import Task

class VsanClusterMgmtInternalSystem(ManagedObject):
   def RemediateVsanCluster(self, cluster: ClusterComputeResource) -> Task: ...
   def RemediateVsanHost(self, host: HostSystem) -> Task: ...
