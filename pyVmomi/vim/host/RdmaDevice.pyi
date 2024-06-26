# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import PhysicalNic

class RdmaDevice(DynamicData):
   class Backing(DynamicData):
      pass

   class PnicBacking(Backing):
      pairedUplink: PhysicalNic

   class ConnectionState(Enum):
      unknown: ClassVar['ConnectionState'] = 'unknown'
      down: ClassVar['ConnectionState'] = 'down'
      init: ClassVar['ConnectionState'] = 'init'
      armed: ClassVar['ConnectionState'] = 'armed'
      active: ClassVar['ConnectionState'] = 'active'
      activeDefer: ClassVar['ConnectionState'] = 'activeDefer'

   class ConnectionInfo(DynamicData):
      state: str
      mtu: int
      speedInMbps: int

   class Capability(DynamicData):
      roceV1Capable: bool
      roceV2Capable: bool
      iWarpCapable: bool

   key: str
   device: str
   driver: Optional[str] = None
   description: Optional[str] = None
   backing: Optional[Backing] = None
   connectionInfo: ConnectionInfo
   capability: Capability
