# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim import IntExpression
from pyVmomi.vim import IpAddress
from pyVmomi.vim import MacAddress
from pyVmomi.vim import NegatableExpression
from pyVmomi.vim import SingleIp
from pyVmomi.vim import StringExpression

from pyVmomi.vmodl import DynamicData

class TrafficRule(DynamicData):
   class Qualifier(DynamicData):
      key: Optional[str] = None

   class Action(DynamicData):
      pass

   class RuleDirectionType(Enum):
      incomingPackets: ClassVar['RuleDirectionType'] = 'incomingPackets'
      outgoingPackets: ClassVar['RuleDirectionType'] = 'outgoingPackets'
      both: ClassVar['RuleDirectionType'] = 'both'

   class IpQualifier(Qualifier):
      sourceAddress: Optional[IpAddress] = None
      destinationAddress: Optional[IpAddress] = None
      protocol: Optional[IntExpression] = None
      sourceIpPort: Optional[IpPort] = None
      destinationIpPort: Optional[IpPort] = None
      tcpFlags: Optional[IntExpression] = None

   class IpPort(NegatableExpression):
      pass

   class SingleIpPort(IpPort):
      portNumber: int

   class IpPortRange(IpPort):
      startPortNumber: int
      endPortNumber: int

   class MacQualifier(Qualifier):
      sourceAddress: Optional[MacAddress] = None
      destinationAddress: Optional[MacAddress] = None
      protocol: Optional[IntExpression] = None
      vlanId: Optional[IntExpression] = None

   class SystemTrafficQualifier(Qualifier):
      typeOfSystemTraffic: Optional[StringExpression] = None

   class DropAction(Action):
      pass

   class AcceptAction(Action):
      pass

   class UpdateTagAction(Action):
      qosTag: Optional[int] = None
      dscpTag: Optional[int] = None

   class RateLimitAction(Action):
      packetsPerSecond: int

   class LogAction(Action):
      pass

   class GreAction(Action):
      encapsulationIp: SingleIp

   class MacRewriteAction(Action):
      rewriteMac: str

   class PuntAction(Action):
      pass

   class CopyAction(Action):
      pass

   key: Optional[str] = None
   description: Optional[str] = None
   sequence: Optional[int] = None
   qualifier: list[Qualifier] = []
   action: Optional[Action] = None
   direction: Optional[str] = None
