# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import DhcpService
from pyVmomi.vim.host import DnsConfig
from pyVmomi.vim.host import HostProxySwitch
from pyVmomi.vim.host import IpRouteConfig
from pyVmomi.vim.host import IpRouteTableInfo
from pyVmomi.vim.host import NatService
from pyVmomi.vim.host import NetStackInstance
from pyVmomi.vim.host import OpaqueNetworkInfo
from pyVmomi.vim.host import OpaqueSwitch
from pyVmomi.vim.host import PhysicalNic
from pyVmomi.vim.host import PortGroup
from pyVmomi.vim.host import RdmaDevice
from pyVmomi.vim.host import VirtualNic
from pyVmomi.vim.host import VirtualSwitch

class NetworkInfo(DynamicData):
   vswitch: list[VirtualSwitch] = []
   proxySwitch: list[HostProxySwitch] = []
   portgroup: list[PortGroup] = []
   pnic: list[PhysicalNic] = []
   rdmaDevice: list[RdmaDevice] = []
   vnic: list[VirtualNic] = []
   consoleVnic: list[VirtualNic] = []
   dnsConfig: Optional[DnsConfig] = None
   ipRouteConfig: Optional[IpRouteConfig] = None
   consoleIpRouteConfig: Optional[IpRouteConfig] = None
   routeTableInfo: Optional[IpRouteTableInfo] = None
   dhcp: list[DhcpService] = []
   nat: list[NatService] = []
   ipV6Enabled: Optional[bool] = None
   atBootIpV6Enabled: Optional[bool] = None
   netStackInstance: list[NetStackInstance] = []
   opaqueSwitch: list[OpaqueSwitch] = []
   opaqueNetwork: list[OpaqueNetworkInfo] = []
   nsxTransportNodeId: Optional[str] = None
   nvdsToVdsMigrationRequired: Optional[bool] = None
   migrationStatus: Optional[str] = None
