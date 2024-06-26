# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import NoReturn
from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim import Datacenter

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.vApp import IpPool

class IpPoolManager(ManagedObject):
   class IpAllocation(DynamicData):
      ipAddress: str
      allocationId: str

   def QueryIpPools(self, dc: Datacenter) -> list[IpPool]: ...
   def CreateIpPool(self, dc: Datacenter, pool: IpPool) -> int: ...
   def UpdateIpPool(self, dc: Datacenter, pool: IpPool) -> NoReturn: ...
   def DestroyIpPool(self, dc: Datacenter, id: int, force: bool) -> NoReturn: ...
   def AllocateIpv4Address(self, dc: Datacenter, poolId: int, allocationId: str) -> str: ...
   def AllocateIpv6Address(self, dc: Datacenter, poolId: int, allocationId: str) -> str: ...
   def ReleaseIpAllocation(self, dc: Datacenter, poolId: int, allocationId: str) -> NoReturn: ...
   def QueryIPAllocations(self, dc: Datacenter, poolId: int, extensionKey: str) -> list[IpAllocation]: ...
