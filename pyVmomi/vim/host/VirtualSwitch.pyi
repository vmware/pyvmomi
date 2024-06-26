# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import LinkDiscoveryProtocolConfig
from pyVmomi.vim.host import NetworkPolicy
from pyVmomi.vim.host import PhysicalNic
from pyVmomi.vim.host import PortGroup

class VirtualSwitch(DynamicData):
   class Bridge(DynamicData):
      pass

   class AutoBridge(Bridge):
      excludedNicDevice: list[str] = []

   class SimpleBridge(Bridge):
      nicDevice: str

   class BondBridge(Bridge):
      nicDevice: list[str] = []
      beacon: Optional[BeaconConfig] = None
      linkDiscoveryProtocolConfig: Optional[LinkDiscoveryProtocolConfig] = None

   class BeaconConfig(DynamicData):
      interval: int

   class Specification(DynamicData):
      numPorts: int
      bridge: Optional[Bridge] = None
      policy: Optional[NetworkPolicy] = None
      mtu: Optional[int] = None

   class Config(DynamicData):
      changeOperation: Optional[str] = None
      name: str
      spec: Optional[Specification] = None

   name: str
   key: str
   numPorts: int
   numPortsAvailable: int
   mtu: Optional[int] = None
   portgroup: list[PortGroup] = []
   pnic: list[PhysicalNic] = []
   spec: Specification
