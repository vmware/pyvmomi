# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import NoReturn
from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim import Datacenter
from pyVmomi.vim import HostSystem
from pyVmomi.vim import Task

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import MethodFault

class FileManager(ManagedObject):
   class FileLockInfo(DynamicData):
      filePath: str
      host: str
      mac: str
      id: str
      worldName: str
      ownerId: Optional[str] = None
      lockMode: str
      acquired: Optional[datetime] = None
      heartbeat: Optional[datetime] = None
      refCount: Optional[int] = None

   class FileLockInfoResult(DynamicData):
      lockInfo: list[FileLockInfo] = []
      fault: Optional[MethodFault] = None

   def MoveFile(self, sourceName: str, sourceDatacenter: Optional[Datacenter], destinationName: str, destinationDatacenter: Optional[Datacenter], force: Optional[bool]) -> Task: ...
   def CopyFile(self, sourceName: str, sourceDatacenter: Optional[Datacenter], destinationName: str, destinationDatacenter: Optional[Datacenter], force: Optional[bool]) -> Task: ...
   def DeleteFile(self, name: str, datacenter: Optional[Datacenter]) -> Task: ...
   def MakeDirectory(self, name: str, datacenter: Optional[Datacenter], createParentDirectories: Optional[bool]) -> NoReturn: ...
   def ChangeOwner(self, name: str, datacenter: Optional[Datacenter], owner: str) -> NoReturn: ...
   def QueryFileLockInfo(self, path: str, host: Optional[HostSystem]) -> FileLockInfoResult: ...
