# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import NetworkPolicy
from pyVmomi.vim.host import VirtualSwitch

class PortGroup(DynamicData):
   class PortConnecteeType(Enum):
      virtualMachine: ClassVar['PortConnecteeType'] = 'virtualMachine'
      systemManagement: ClassVar['PortConnecteeType'] = 'systemManagement'
      host: ClassVar['PortConnecteeType'] = 'host'
      unknown: ClassVar['PortConnecteeType'] = 'unknown'

   class Specification(DynamicData):
      name: str
      vlanId: int
      vswitchName: str
      policy: NetworkPolicy

   class Config(DynamicData):
      changeOperation: Optional[str] = None
      spec: Optional[Specification] = None

   class Port(DynamicData):
      key: Optional[str] = None
      mac: list[str] = []
      type: str

   key: Optional[str] = None
   port: list[Port] = []
   vswitch: Optional[VirtualSwitch] = None
   computedPolicy: NetworkPolicy
   spec: Specification
