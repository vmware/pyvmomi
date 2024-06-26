# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import ClassVar
from typing import NoReturn
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim import HostSystem

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import MethodFault

from pyVmomi.vim.fault import ProfileUpdateFailed

from pyVmomi.vim.profile import ComplianceLocator
from pyVmomi.vim.profile import ComplianceProfile
from pyVmomi.vim.profile import DeferredPolicyOptionParameter
from pyVmomi.vim.profile import Profile

from pyVmomi.vim.profile.host import ExecuteResult
from pyVmomi.vim.profile.host import HostApplyProfile

class HostProfile(Profile):
   class ConfigInfo(Profile.ConfigInfo):
      applyProfile: Optional[HostApplyProfile] = None
      defaultComplyProfile: Optional[ComplianceProfile] = None
      defaultComplyLocator: list[ComplianceLocator] = []
      customComplyProfile: Optional[ComplianceProfile] = None
      disabledExpressionList: list[str] = []
      description: Optional[Profile.Description] = None

   class ConfigSpec(Profile.CreateSpec):
      pass

   class SerializedHostProfileSpec(Profile.SerializedCreateSpec):
      validatorHost: Optional[HostSystem] = None
      validating: Optional[bool] = None

   class CompleteConfigSpec(ConfigSpec):
      applyProfile: Optional[HostApplyProfile] = None
      customComplyProfile: Optional[ComplianceProfile] = None
      disabledExpressionListChanged: bool
      disabledExpressionList: list[str] = []
      validatorHost: Optional[HostSystem] = None
      validating: Optional[bool] = None
      hostConfig: Optional[ConfigInfo] = None

   class HostBasedConfigSpec(ConfigSpec):
      host: HostSystem
      useHostProfileEngine: Optional[bool] = None

   class ValidationState(Enum):
      Ready: ClassVar['ValidationState'] = 'Ready'
      Running: ClassVar['ValidationState'] = 'Running'
      Failed: ClassVar['ValidationState'] = 'Failed'

   class ValidationFailureInfo(DynamicData):
      class UpdateType(Enum):
         HostBased: ClassVar['UpdateType'] = 'HostBased'
         Import: ClassVar['UpdateType'] = 'Import'
         Edit: ClassVar['UpdateType'] = 'Edit'
         Compose: ClassVar['UpdateType'] = 'Compose'

      name: str
      annotation: str
      updateType: str
      host: Optional[HostSystem] = None
      applyProfile: Optional[HostApplyProfile] = None
      failures: list[ProfileUpdateFailed.UpdateFailure] = []
      faults: list[MethodFault] = []

   @property
   def validationState(self) -> Optional[str]: ...
   @property
   def validationStateUpdateTime(self) -> Optional[datetime]: ...
   @property
   def validationFailureInfo(self) -> Optional[ValidationFailureInfo]: ...
   @property
   def complianceCheckTime(self) -> Optional[datetime]: ...
   @property
   def referenceHost(self) -> Optional[HostSystem]: ...

   def ResetValidationState(self) -> NoReturn: ...
   def UpdateReferenceHost(self, host: Optional[HostSystem]) -> NoReturn: ...
   def Update(self, config: ConfigSpec) -> NoReturn: ...
   def Execute(self, host: HostSystem, deferredParam: list[DeferredPolicyOptionParameter]) -> ExecuteResult: ...
