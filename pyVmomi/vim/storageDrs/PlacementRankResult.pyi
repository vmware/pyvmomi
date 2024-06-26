# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import double
from pyVmomi.VmomiSupport import long

from pyVmomi.vim import ClusterComputeResource

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import MethodFault

class PlacementRankResult(DynamicData):
   key: str
   candidate: ClusterComputeResource
   reservedSpaceMB: long
   usedSpaceMB: long
   totalSpaceMB: long
   utilization: double
   faults: list[MethodFault] = []
