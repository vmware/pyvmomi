# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import NoReturn
from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim import ManagedEntity
from pyVmomi.vim import PrivilegePolicyDef

from pyVmomi.vmodl import DynamicData

class CustomFieldsManager(ManagedObject):
   class FieldDef(DynamicData):
      key: int
      name: str
      type: type
      managedObjectType: Optional[type] = None
      fieldDefPrivileges: Optional[PrivilegePolicyDef] = None
      fieldInstancePrivileges: Optional[PrivilegePolicyDef] = None

   class Value(DynamicData):
      key: int

   class StringValue(Value):
      value: str

   @property
   def field(self) -> list[FieldDef]: ...

   def AddFieldDefinition(self, name: str, moType: Optional[type], fieldDefPolicy: Optional[PrivilegePolicyDef], fieldPolicy: Optional[PrivilegePolicyDef]) -> FieldDef: ...
   def RemoveFieldDefinition(self, key: int) -> NoReturn: ...
   def RenameFieldDefinition(self, key: int, name: str) -> NoReturn: ...
   def SetField(self, entity: ManagedEntity, key: int, value: str) -> NoReturn: ...
