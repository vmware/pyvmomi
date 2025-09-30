# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.pbm.profile.ProfileId import ProfileId

from pyVmomi.vmodl.fault.SecurityError import SecurityError

class NoPermission(SecurityError):
   class EntityPrivileges(DynamicData):
      profileId: Optional[ProfileId] = None
      privilegeIds: list[str] = []

   missingPrivileges: list[EntityPrivileges] = []
