# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.vm.device import VirtualDevice

class VirtualVMCIDevice(VirtualDevice):
   class Action(Enum):
      allow: ClassVar['Action'] = 'allow'
      deny: ClassVar['Action'] = 'deny'

   class Protocol(Enum):
      hypervisor: ClassVar['Protocol'] = 'hypervisor'
      doorbell: ClassVar['Protocol'] = 'doorbell'
      queuepair: ClassVar['Protocol'] = 'queuepair'
      datagram: ClassVar['Protocol'] = 'datagram'
      stream: ClassVar['Protocol'] = 'stream'
      anyProtocol: ClassVar['Protocol'] = 'anyProtocol'

   class Direction(Enum):
      guest: ClassVar['Direction'] = 'guest'
      host: ClassVar['Direction'] = 'host'
      anyDirection: ClassVar['Direction'] = 'anyDirection'

   class FilterSpec(DynamicData):
      rank: long
      action: str
      protocol: str
      direction: str
      lowerDstPortBoundary: Optional[long] = None
      upperDstPortBoundary: Optional[long] = None

   class FilterInfo(DynamicData):
      filters: list[FilterSpec] = []

   id: Optional[long] = None
   allowUnrestrictedCommunication: Optional[bool] = None
   filterEnable: Optional[bool] = None
   filterInfo: Optional[FilterInfo] = None
