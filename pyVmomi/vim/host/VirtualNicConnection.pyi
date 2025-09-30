# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.dvs.PortConnection import PortConnection

from pyVmomi.vim.host.VirtualNic import VirtualNic

class VirtualNicConnection(DynamicData):
   portgroup: Optional[str] = None
   dvPort: Optional[PortConnection] = None
   opNetwork: Optional[VirtualNic.OpaqueNetworkSpec] = None
