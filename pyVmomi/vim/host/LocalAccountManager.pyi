# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import NoReturn
from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vmodl import DynamicData

class LocalAccountManager(ManagedObject):
   class AccountSpecification(DynamicData):
      id: str
      password: Optional[str] = None
      description: Optional[str] = None

   class PosixAccountSpecification(AccountSpecification):
      posixId: Optional[int] = None
      shellAccess: Optional[bool] = None

   def CreateUser(self, user: AccountSpecification) -> NoReturn: ...
   def UpdateUser(self, user: AccountSpecification) -> NoReturn: ...
   def CreateGroup(self, group: AccountSpecification) -> NoReturn: ...
   def RemoveUser(self, userName: str) -> NoReturn: ...
   def RemoveGroup(self, groupName: str) -> NoReturn: ...
   def AssignUserToGroup(self, user: str, group: str) -> NoReturn: ...
   def UnassignUserFromGroup(self, user: str, group: str) -> NoReturn: ...
   def ChangePassword(self, user: str, oldPassword: str, newPassword: str) -> NoReturn: ...
