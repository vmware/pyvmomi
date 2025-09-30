# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim.HostSystem import HostSystem

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vmodl.MethodFault import MethodFault

from pyVmomi.vim.fault.ProfileUpdateFailed import ProfileUpdateFailed

from pyVmomi.vim.profile.ComplianceLocator import ComplianceLocator

from pyVmomi.vim.profile.ComplianceProfile import ComplianceProfile

from pyVmomi.vim.profile.DeferredPolicyOptionParameter import DeferredPolicyOptionParameter

from pyVmomi.vim.profile.Profile import Profile

from pyVmomi.vim.profile.host.ExecuteResult import ExecuteResult

from pyVmomi.vim.profile.host.HostApplyProfile import HostApplyProfile

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

   def ResetValidationState(self) -> None: ...
   def UpdateReferenceHost(self, host: Optional[HostSystem]) -> None: ...
   def Update(self, config: ConfigSpec) -> None: ...
   def Execute(self, host: HostSystem, deferredParam: list[DeferredPolicyOptionParameter]) -> ExecuteResult: ...
