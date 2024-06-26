# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim import Task

from pyVmomi.vmodl import DynamicData

class PatchManager(ManagedObject):
   class Result(DynamicData):
      version: str
      status: list[Status] = []
      xmlResult: Optional[str] = None

   class Status(DynamicData):
      class Reason(Enum):
         obsoleted: ClassVar['Reason'] = 'obsoleted'
         missingPatch: ClassVar['Reason'] = 'missingPatch'
         missingLib: ClassVar['Reason'] = 'missingLib'
         hasDependentPatch: ClassVar['Reason'] = 'hasDependentPatch'
         conflictPatch: ClassVar['Reason'] = 'conflictPatch'
         conflictLib: ClassVar['Reason'] = 'conflictLib'

      class Integrity(Enum):
         validated: ClassVar['Integrity'] = 'validated'
         keyNotFound: ClassVar['Integrity'] = 'keyNotFound'
         keyRevoked: ClassVar['Integrity'] = 'keyRevoked'
         keyExpired: ClassVar['Integrity'] = 'keyExpired'
         digestMismatch: ClassVar['Integrity'] = 'digestMismatch'
         notEnoughSignatures: ClassVar['Integrity'] = 'notEnoughSignatures'
         validationError: ClassVar['Integrity'] = 'validationError'

      class InstallState(Enum):
         hostRestarted: ClassVar['InstallState'] = 'hostRestarted'
         imageActive: ClassVar['InstallState'] = 'imageActive'

      class PrerequisitePatch(DynamicData):
         id: str
         installState: list[str] = []

      id: str
      applicable: bool
      reason: list[str] = []
      integrity: Optional[str] = None
      installed: bool
      installState: list[str] = []
      prerequisitePatch: list[PrerequisitePatch] = []
      restartRequired: bool
      reconnectRequired: bool
      vmOffRequired: bool
      supersededPatchIds: list[str] = []

   class Locator(DynamicData):
      url: str
      proxy: Optional[str] = None

   class PatchManagerOperationSpec(DynamicData):
      proxy: Optional[str] = None
      port: Optional[int] = None
      userName: Optional[str] = None
      password: Optional[str] = None
      cmdOption: Optional[str] = None

   def Check(self, metaUrls: list[str], bundleUrls: list[str], spec: Optional[PatchManagerOperationSpec]) -> Task: ...
   def Scan(self, repository: Locator, updateID: list[str]) -> Task: ...
   def ScanV2(self, metaUrls: list[str], bundleUrls: list[str], spec: Optional[PatchManagerOperationSpec]) -> Task: ...
   def Stage(self, metaUrls: list[str], bundleUrls: list[str], vibUrls: list[str], spec: Optional[PatchManagerOperationSpec]) -> Task: ...
   def Install(self, repository: Locator, updateID: str, force: Optional[bool]) -> Task: ...
   def InstallV2(self, metaUrls: list[str], bundleUrls: list[str], vibUrls: list[str], spec: Optional[PatchManagerOperationSpec]) -> Task: ...
   def Uninstall(self, bulletinIds: list[str], spec: Optional[PatchManagerOperationSpec]) -> Task: ...
   def Query(self, spec: Optional[PatchManagerOperationSpec]) -> Task: ...
