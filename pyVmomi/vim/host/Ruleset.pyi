# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

class Ruleset(DynamicData):
   class IpNetwork(DynamicData):
      network: str
      prefixLength: int

   class IpList(DynamicData):
      ipAddress: list[str] = []
      ipNetwork: list[IpNetwork] = []
      allIp: bool

   class RulesetSpec(DynamicData):
      allowedHosts: IpList

   class Rule(DynamicData):
      class Direction(Enum):
         inbound: ClassVar['Direction'] = 'inbound'
         outbound: ClassVar['Direction'] = 'outbound'

      class PortType(Enum):
         src: ClassVar['PortType'] = 'src'
         dst: ClassVar['PortType'] = 'dst'

      class Protocol(Enum):
         tcp: ClassVar['Protocol'] = 'tcp'
         udp: ClassVar['Protocol'] = 'udp'

      port: int
      endPort: Optional[int] = None
      direction: Direction
      portType: Optional[PortType] = None
      protocol: str

   key: str
   label: str
   required: bool
   rule: list[Rule] = []
   service: Optional[str] = None
   enabled: bool
   allowedHosts: Optional[IpList] = None
   userControllable: Optional[bool] = None
   ipListUserConfigurable: Optional[bool] = None
