# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import NoReturn
from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim import AuthorizationDescription
from pyVmomi.vim import Description
from pyVmomi.vim import ManagedEntity

from pyVmomi.vmodl import DynamicData

class AuthorizationManager(ManagedObject):
   class Permission(DynamicData):
      entity: Optional[ManagedEntity] = None
      principal: str
      group: bool
      roleId: int
      propagate: bool

   class Role(DynamicData):
      roleId: int
      system: bool
      name: str
      info: Description
      privilege: list[str] = []

   class Privilege(DynamicData):
      privId: str
      onParent: bool
      name: str
      privGroupName: str

   class PrivilegeAvailability(DynamicData):
      privId: str
      isGranted: bool

   class EntityPrivilege(DynamicData):
      entity: ManagedEntity
      privAvailability: list[PrivilegeAvailability] = []

   class UserPrivilegeResult(DynamicData):
      entity: ManagedEntity
      privileges: list[str] = []

   @property
   def privilegeList(self) -> list[Privilege]: ...
   @property
   def roleList(self) -> list[Role]: ...
   @property
   def description(self) -> AuthorizationDescription: ...

   def AddRole(self, name: str, privIds: list[str]) -> int: ...
   def RemoveRole(self, roleId: int, failIfUsed: bool) -> NoReturn: ...
   def UpdateRole(self, roleId: int, newName: str, privIds: list[str]) -> NoReturn: ...
   def MergePermissions(self, srcRoleId: int, dstRoleId: int) -> NoReturn: ...
   def RetrieveRolePermissions(self, roleId: int) -> list[Permission]: ...
   def RetrieveEntityPermissions(self, entity: ManagedEntity, inherited: bool) -> list[Permission]: ...
   def RetrieveAllPermissions(self) -> list[Permission]: ...
   def SetEntityPermissions(self, entity: ManagedEntity, permission: list[Permission]) -> NoReturn: ...
   def ResetEntityPermissions(self, entity: ManagedEntity, permission: list[Permission]) -> NoReturn: ...
   def RemoveEntityPermission(self, entity: ManagedEntity, user: str, isGroup: bool) -> NoReturn: ...
   def HasPrivilegeOnEntity(self, entity: ManagedEntity, sessionId: str, privId: list[str]) -> list[bool]: ...
   def HasPrivilegeOnEntities(self, entity: list[ManagedEntity], sessionId: str, privId: list[str]) -> list[EntityPrivilege]: ...
   def HasUserPrivilegeOnEntities(self, entities: list[ManagedObject], userName: str, privId: list[str]) -> list[EntityPrivilege]: ...
   def FetchUserPrivilegeOnEntities(self, entities: list[ManagedEntity], userName: str) -> list[UserPrivilegeResult]: ...
