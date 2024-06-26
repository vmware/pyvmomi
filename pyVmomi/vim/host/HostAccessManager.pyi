# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import NoReturn
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vmodl import DynamicData

class HostAccessManager(ManagedObject):
   class AccessMode(Enum):
      accessNone: ClassVar['AccessMode'] = 'accessNone'
      accessAdmin: ClassVar['AccessMode'] = 'accessAdmin'
      accessNoAccess: ClassVar['AccessMode'] = 'accessNoAccess'
      accessReadOnly: ClassVar['AccessMode'] = 'accessReadOnly'
      accessOther: ClassVar['AccessMode'] = 'accessOther'

   class AccessEntry(DynamicData):
      principal: str
      group: bool
      accessMode: AccessMode

   class LockdownMode(Enum):
      lockdownDisabled: ClassVar['LockdownMode'] = 'lockdownDisabled'
      lockdownNormal: ClassVar['LockdownMode'] = 'lockdownNormal'
      lockdownStrict: ClassVar['LockdownMode'] = 'lockdownStrict'

   @property
   def lockdownMode(self) -> LockdownMode: ...

   def RetrieveAccessEntries(self) -> list[AccessEntry]: ...
   def ChangeAccessMode(self, principal: str, isGroup: bool, accessMode: AccessMode) -> NoReturn: ...
   def QuerySystemUsers(self) -> list[str]: ...
   def UpdateSystemUsers(self, users: list[str]) -> NoReturn: ...
   def QueryLockdownExceptions(self) -> list[str]: ...
   def UpdateLockdownExceptions(self, users: list[str]) -> NoReturn: ...
   def ChangeLockdownMode(self, mode: LockdownMode) -> NoReturn: ...
