# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import ClusterComputeResource

from pyVmomi.vmodl import DynamicData

class VsanClusterNetworkPerfTaskSpec(DynamicData):
   Cluster: Optional[ClusterComputeResource] = None
   DurationSec: Optional[int] = None
   ownerVc: Optional[str] = None
