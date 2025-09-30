# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim.CustomFieldsManager import CustomFieldsManager

class ExtensibleManagedObject(ManagedObject):
   @property
   def value(self) -> list[CustomFieldsManager.Value]: ...
   @property
   def availableField(self) -> list[CustomFieldsManager.FieldDef]: ...

   def SetCustomValue(self, key: str, value: str) -> None: ...
