# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.dvs import PortConnection

from pyVmomi.vim.host import IpConfig
from pyVmomi.vim.host import IpRouteConfig
from pyVmomi.vim.host import PortGroup

class VirtualNic(DynamicData):
   class Specification(DynamicData):
      ip: Optional[IpConfig] = None
      mac: Optional[str] = None
      distributedVirtualPort: Optional[PortConnection] = None
      portgroup: Optional[str] = None
      mtu: Optional[int] = None
      tsoEnabled: Optional[bool] = None
      netStackInstanceKey: Optional[str] = None
      opaqueNetwork: Optional[OpaqueNetworkSpec] = None
      externalId: Optional[str] = None
      pinnedPnic: Optional[str] = None
      ipRouteSpec: Optional[IpRouteSpec] = None
      systemOwned: Optional[bool] = None
      dpuId: Optional[str] = None

   class Config(DynamicData):
      changeOperation: Optional[str] = None
      device: Optional[str] = None
      portgroup: str
      spec: Optional[Specification] = None

   class OpaqueNetworkSpec(DynamicData):
      opaqueNetworkId: str
      opaqueNetworkType: str

   class IpRouteSpec(DynamicData):
      ipRouteConfig: Optional[IpRouteConfig] = None

   device: str
   key: str
   portgroup: str
   spec: Specification
   port: Optional[PortGroup.Port] = None
