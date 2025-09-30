# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vmodl.MethodFault import MethodFault

from pyVmomi.pbm.placement.MatchingResources import MatchingResources

from pyVmomi.pbm.placement.PlacementHub import PlacementHub

from pyVmomi.pbm.placement.ResourceUtilization import ResourceUtilization

class CompatibilityResult(DynamicData):
   hub: PlacementHub
   matchingResources: list[MatchingResources] = []
   howMany: Optional[long] = None
   utilization: list[ResourceUtilization] = []
   warning: list[MethodFault] = []
   error: list[MethodFault] = []
