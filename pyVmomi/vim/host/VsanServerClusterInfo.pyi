# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import ClusterComputeResource

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import VsanClusterMembershipInfo
from pyVmomi.vim.host import VsanNetworkPeerHealthResult

class VsanServerClusterInfo(DynamicData):
   cluster: Optional[ClusterComputeResource] = None
   peerHealth: list[VsanNetworkPeerHealthResult] = []
   membership: Optional[VsanClusterMembershipInfo] = None
