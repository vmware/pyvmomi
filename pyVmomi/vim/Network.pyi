# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import NoReturn
from typing import Optional

from pyVmomi.vim import HostSystem
from pyVmomi.vim import ManagedEntity
from pyVmomi.vim import VirtualMachine

from pyVmomi.vmodl import DynamicData

class Network(ManagedEntity):
   class Summary(DynamicData):
      network: Optional[Network] = None
      name: str
      accessible: bool
      ipPoolName: str
      ipPoolId: Optional[int] = None

   @property
   def summary(self) -> Summary: ...
   @property
   def host(self) -> list[HostSystem]: ...
   @property
   def vm(self) -> list[VirtualMachine]: ...

   def DestroyNetwork(self) -> NoReturn: ...
