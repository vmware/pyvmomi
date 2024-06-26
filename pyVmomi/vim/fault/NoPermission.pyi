# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vmodl import DynamicData

from pyVmomi.vmodl.fault import SecurityError

class NoPermission(SecurityError):
   class EntityPrivileges(DynamicData):
      entity: ManagedObject
      privilegeIds: list[str] = []

   object: Optional[ManagedObject] = None
   privilegeId: Optional[str] = None
   missingPrivileges: list[EntityPrivileges] = []
