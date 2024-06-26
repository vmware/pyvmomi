# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import NoReturn
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim import Datastore
from pyVmomi.vim import Folder
from pyVmomi.vim import HttpNfcLease
from pyVmomi.vim import ManagedEntity
from pyVmomi.vim import Network
from pyVmomi.vim import ResourcePool
from pyVmomi.vim import Task

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.vApp import CloneSpec
from pyVmomi.vim.vApp import ProductInfo
from pyVmomi.vim.vApp import VAppConfigInfo
from pyVmomi.vim.vApp import VAppConfigSpec

class VirtualApp(ResourcePool):
   class VAppState(Enum):
      started: ClassVar['VAppState'] = 'started'
      stopped: ClassVar['VAppState'] = 'stopped'
      starting: ClassVar['VAppState'] = 'starting'
      stopping: ClassVar['VAppState'] = 'stopping'

   class Summary(ResourcePool.Summary):
      product: Optional[ProductInfo] = None
      vAppState: Optional[VAppState] = None
      suspended: Optional[bool] = None
      installBootRequired: Optional[bool] = None
      instanceUuid: Optional[str] = None

   class LinkInfo(DynamicData):
      key: ManagedEntity
      destroyWithParent: Optional[bool] = None

   @property
   def parentFolder(self) -> Optional[Folder]: ...
   @property
   def datastore(self) -> list[Datastore]: ...
   @property
   def network(self) -> list[Network]: ...
   @property
   def vAppConfig(self) -> Optional[VAppConfigInfo]: ...
   @property
   def parentVApp(self) -> Optional[ManagedEntity]: ...
   @property
   def childLink(self) -> list[LinkInfo]: ...

   def UpdateVAppConfig(self, spec: VAppConfigSpec) -> NoReturn: ...
   def UpdateLinkedChildren(self, addChangeSet: list[LinkInfo], removeSet: list[ManagedEntity]) -> NoReturn: ...
   def Clone(self, name: str, target: ResourcePool, spec: CloneSpec) -> Task: ...
   def ExportVApp(self) -> HttpNfcLease: ...
   def PowerOn(self) -> Task: ...
   def PowerOff(self, force: bool) -> Task: ...
   def Suspend(self) -> Task: ...
   def Unregister(self) -> Task: ...
