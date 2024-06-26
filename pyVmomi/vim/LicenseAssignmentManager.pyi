# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import NoReturn
from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim import LicenseManager

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import KeyAnyValue

class LicenseAssignmentManager(ManagedObject):
   class LicenseAssignment(DynamicData):
      entityId: str
      scope: Optional[str] = None
      entityDisplayName: Optional[str] = None
      assignedLicense: LicenseManager.LicenseInfo
      properties: list[KeyAnyValue] = []

   def UpdateAssignedLicense(self, entity: str, licenseKey: str, entityDisplayName: Optional[str]) -> LicenseManager.LicenseInfo: ...
   def RemoveAssignedLicense(self, entityId: str) -> NoReturn: ...
   def QueryAssignedLicenses(self, entityId: Optional[str]) -> list[LicenseAssignment]: ...
