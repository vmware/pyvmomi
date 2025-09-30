# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vmodl.DynamicData import DynamicData

class LocalAccountManager(ManagedObject):
   class AccountSpecification(DynamicData):
      id: str
      password: Optional[str] = None
      description: Optional[str] = None

   class PosixAccountSpecification(AccountSpecification):
      posixId: Optional[int] = None
      shellAccess: Optional[bool] = None

   def CreateUser(self, user: AccountSpecification) -> None: ...
   def UpdateUser(self, user: AccountSpecification) -> None: ...
   def CreateGroup(self, group: AccountSpecification) -> None: ...
   def RemoveUser(self, userName: str) -> None: ...
   def RemoveGroup(self, groupName: str) -> None: ...
   def AssignUserToGroup(self, user: str, group: str) -> None: ...
   def UnassignUserFromGroup(self, user: str, group: str) -> None: ...
   def ChangePassword(self, user: str, oldPassword: str, newPassword: str) -> None: ...
