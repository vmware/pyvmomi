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
from pyVmomi.vim.host import IpRouteTableConfig
from pyVmomi.vim.host import NatService
from pyVmomi.vim.host import NetStackInstance
from pyVmomi.vim.host import PhysicalNic
from pyVmomi.vim.host import PortGroup
from pyVmomi.vim.host import VirtualNic
from pyVmomi.vim.host import VirtualSwitch

class NetworkConfig(DynamicData):
   class Result(DynamicData):
      vnicDevice: list[str] = []
      consoleVnicDevice: list[str] = []

   class NetStackSpec(DynamicData):
      netStackInstance: NetStackInstance
      operation: Optional[str] = None

   vswitch: list[VirtualSwitch.Config] = []
   proxySwitch: list[HostProxySwitch.Config] = []
   portgroup: list[PortGroup.Config] = []
   pnic: list[PhysicalNic.Config] = []
   vnic: list[VirtualNic.Config] = []
   consoleVnic: list[VirtualNic.Config] = []
   dnsConfig: Optional[DnsConfig] = None
   ipRouteConfig: Optional[IpRouteConfig] = None
   consoleIpRouteConfig: Optional[IpRouteConfig] = None
   routeTableConfig: Optional[IpRouteTableConfig] = None
   dhcp: list[DhcpService.Config] = []
   nat: list[NatService.Config] = []
   ipV6Enabled: Optional[bool] = None
   netStackSpec: list[NetStackSpec] = []
   migrationStatus: Optional[str] = None
