# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vim.ClusterComputeResource import ClusterComputeResource

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.cluster.PlacementSpec import PlacementSpec

class PlacementRankVmSpec(DynamicData):
   vmPlacementSpec: PlacementSpec
   vmClusters: list[ClusterComputeResource] = []
