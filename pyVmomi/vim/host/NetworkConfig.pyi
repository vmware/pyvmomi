# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.host.DhcpService import DhcpService

from pyVmomi.vim.host.DnsConfig import DnsConfig

from pyVmomi.vim.host.HostProxySwitch import HostProxySwitch

from pyVmomi.vim.host.IpRouteConfig import IpRouteConfig

from pyVmomi.vim.host.IpRouteTableConfig import IpRouteTableConfig

from pyVmomi.vim.host.NatService import NatService

from pyVmomi.vim.host.NetStackInstance import NetStackInstance

from pyVmomi.vim.host.PhysicalNic import PhysicalNic

from pyVmomi.vim.host.PortGroup import PortGroup

from pyVmomi.vim.host.VirtualNic import VirtualNic

from pyVmomi.vim.host.VirtualSwitch import VirtualSwitch

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
