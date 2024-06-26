# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData

class VsanNetworkPeerHealthResult(DynamicData):
   peer: Optional[str] = None
   peerHostname: Optional[str] = None
   peerVmknicName: Optional[str] = None
   smallPingTestSuccessPct: Optional[int] = None
   largePingTestSuccessPct: Optional[int] = None
   maxLatencyUs: Optional[long] = None
   onSameIpSubnet: Optional[bool] = None
   sourceVmknicName: Optional[str] = None
   connectivityHealthState: Optional[str] = None
