# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.ClusterComputeResource import ClusterComputeResource

from pyVmomi.vmodl.DynamicData import DynamicData

class VSANStretchedClusterHostVirtualApplianceStatus(DynamicData):
   vcCluster: Optional[ClusterComputeResource] = None
   isVirtualApp: Optional[bool] = None
   vcClusters: list[ClusterComputeResource] = []
   isVirtualAppValid: Optional[bool] = None
