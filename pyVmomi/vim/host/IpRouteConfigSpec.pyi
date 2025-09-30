# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.host.IpRouteConfig import IpRouteConfig

from pyVmomi.vim.host.VirtualNicConnection import VirtualNicConnection

class IpRouteConfigSpec(IpRouteConfig):
   gatewayDeviceConnection: Optional[VirtualNicConnection] = None
   ipV6GatewayDeviceConnection: Optional[VirtualNicConnection] = None
