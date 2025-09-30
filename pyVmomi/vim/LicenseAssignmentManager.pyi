# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim.LicenseManager import LicenseManager

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vmodl.KeyAnyValue import KeyAnyValue

class LicenseAssignmentManager(ManagedObject):
   class LicenseAssignment(DynamicData):
      entityId: str
      scope: Optional[str] = None
      entityDisplayName: Optional[str] = None
      assignedLicense: LicenseManager.LicenseInfo
      properties: list[KeyAnyValue] = []

   def UpdateAssignedLicense(self, entity: str, licenseKey: str, entityDisplayName: Optional[str]) -> LicenseManager.LicenseInfo: ...
   def RemoveAssignedLicense(self, entityId: str) -> None: ...
   def QueryAssignedLicenses(self, entityId: Optional[str]) -> list[LicenseAssignment]: ...
