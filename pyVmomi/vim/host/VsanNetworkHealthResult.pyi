# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import HostSystem

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import VsanNetworkPeerHealthResult
from pyVmomi.vim.host import VsanServerClusterInfo

class VsanNetworkHealthResult(DynamicData):
   host: Optional[HostSystem] = None
   hostname: Optional[str] = None
   vsanVmknicPresent: Optional[bool] = None
   ipSubnets: list[str] = []
   issueFound: Optional[bool] = None
   peerHealth: list[VsanNetworkPeerHealthResult] = []
   vMotionHealth: list[VsanNetworkPeerHealthResult] = []
   multicastConfig: Optional[str] = None
   unicastConfig: Optional[str] = None
   inUnicast: Optional[bool] = None
   rdmaEnabled: Optional[bool] = None
   rdtConnProtocol: Optional[str] = None
   serverClusters: list[VsanServerClusterInfo] = []
