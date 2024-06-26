# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import NoReturn
from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject
from pyVmomi.VmomiSupport import long

from pyVmomi.vim import Datacenter
from pyVmomi.vim import Datastore

from pyVmomi.vmodl import DynamicData

class DatastoreNamespaceManager(ManagedObject):
   class DirectoryInfo(DynamicData):
      capacity: long
      used: long

   def CreateDirectory(self, datastore: Datastore, displayName: Optional[str], policy: Optional[str], size: Optional[long]) -> str: ...
   def DeleteDirectory(self, datacenter: Optional[Datacenter], datastorePath: str) -> NoReturn: ...
   def ConvertNamespacePathToUuidPath(self, datacenter: Optional[Datacenter], namespaceUrl: str) -> str: ...
   def IncreaseDirectorySize(self, datacenter: Optional[Datacenter], stableName: str, size: long) -> NoReturn: ...
   def QueryDirectoryInfo(self, datacenter: Optional[Datacenter], stableName: str) -> DirectoryInfo: ...
