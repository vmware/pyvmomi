# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import ClusterComputeResource

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.cluster import PlacementSpec

from pyVmomi.vim.storageDrs import PlacementAffinityRule
from pyVmomi.vim.storageDrs import PlacementRankVmSpec

class PlacementRankSpec(DynamicData):
   specs: list[PlacementSpec] = []
   clusters: list[ClusterComputeResource] = []
   rules: list[PlacementAffinityRule] = []
   placementRankByVm: list[PlacementRankVmSpec] = []
