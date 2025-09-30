# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.ClusterComputeResource import ClusterComputeResource

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.cluster.PlacementSpec import PlacementSpec

from pyVmomi.vim.storageDrs.PlacementAffinityRule import PlacementAffinityRule

from pyVmomi.vim.storageDrs.PlacementRankVmSpec import PlacementRankVmSpec

class PlacementRankSpec(DynamicData):
   specs: list[PlacementSpec] = []
   clusters: list[ClusterComputeResource] = []
   rules: list[PlacementAffinityRule] = []
   placementRankByVm: list[PlacementRankVmSpec] = []
