# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim import HostSystem
from pyVmomi.vim import ManagedEntity
from pyVmomi.vim import Task

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import LocalizableMessage
from pyVmomi.vmodl import MethodFault

from pyVmomi.vim.host import ConfigSpec

from pyVmomi.vim.profile import ApplyProfile
from pyVmomi.vim.profile import DeferredPolicyOptionParameter
from pyVmomi.vim.profile import Profile
from pyVmomi.vim.profile import ProfileMetadata
from pyVmomi.vim.profile import ProfileStructure

from pyVmomi.vim.profile.host import AnswerFile
from pyVmomi.vim.profile.host import AnswerFileStatusResult
from pyVmomi.vim.profile.host import ExecuteResult
from pyVmomi.vim.profile.host import HostApplyProfile

class ProfileManager(ProfileManager):
   class TaskListRequirement(Enum):
      maintenanceModeRequired: ClassVar['TaskListRequirement'] = 'maintenanceModeRequired'
      rebootRequired: ClassVar['TaskListRequirement'] = 'rebootRequired'

   class ConfigTaskList(DynamicData):
      configSpec: Optional[ConfigSpec] = None
      taskDescription: list[LocalizableMessage] = []
      taskListRequirement: list[str] = []

   class AnswerFileCreateSpec(DynamicData):
      validating: Optional[bool] = None

   class AnswerFileOptionsCreateSpec(AnswerFileCreateSpec):
      userInput: list[DeferredPolicyOptionParameter] = []

   class AnswerFileSerializedCreateSpec(AnswerFileCreateSpec):
      answerFileConfigString: str

   class AnswerFileStatus(Enum):
      valid: ClassVar['AnswerFileStatus'] = 'valid'
      invalid: ClassVar['AnswerFileStatus'] = 'invalid'
      unknown: ClassVar['AnswerFileStatus'] = 'unknown'

   class EntityCustomizations(DynamicData):
      pass

   class StructuredCustomizations(EntityCustomizations):
      entity: ManagedEntity
      customizations: Optional[AnswerFile] = None

   class HostToConfigSpecMap(DynamicData):
      host: HostSystem
      configSpec: AnswerFileCreateSpec

   class ApplyHostConfigSpec(ExecuteResult):
      host: HostSystem
      taskListRequirement: list[str] = []
      taskDescription: list[LocalizableMessage] = []
      rebootStateless: Optional[bool] = None
      rebootHost: Optional[bool] = None
      faultData: Optional[MethodFault] = None

   class ApplyHostConfigResult(DynamicData):
      class Status(Enum):
         success: ClassVar['Status'] = 'success'
         failed: ClassVar['Status'] = 'failed'
         reboot_failed: ClassVar['Status'] = 'reboot_failed'
         stateless_reboot_failed: ClassVar['Status'] = 'stateless_reboot_failed'
         check_compliance_failed: ClassVar['Status'] = 'check_compliance_failed'
         state_not_satisfied: ClassVar['Status'] = 'state_not_satisfied'
         exit_maintenancemode_failed: ClassVar['Status'] = 'exit_maintenancemode_failed'
         canceled: ClassVar['Status'] = 'canceled'

      startTime: datetime
      completeTime: datetime
      host: HostSystem
      status: str
      errors: list[MethodFault] = []

   class CompositionValidationResult(DynamicData):
      class ResultElement(DynamicData):
         class Status(Enum):
            success: ClassVar['Status'] = 'success'
            error: ClassVar['Status'] = 'error'

         target: Profile
         status: str
         errors: list[LocalizableMessage] = []
         sourceDiffForToBeMerged: Optional[HostApplyProfile] = None
         targetDiffForToBeMerged: Optional[HostApplyProfile] = None
         toBeAdded: Optional[HostApplyProfile] = None
         toBeDeleted: Optional[HostApplyProfile] = None
         toBeDisabled: Optional[HostApplyProfile] = None
         toBeEnabled: Optional[HostApplyProfile] = None
         toBeReenableCC: Optional[HostApplyProfile] = None

      results: list[ResultElement] = []
      errors: list[LocalizableMessage] = []

   class CompositionResult(DynamicData):
      class ResultElement(DynamicData):
         class Status(Enum):
            success: ClassVar['Status'] = 'success'
            error: ClassVar['Status'] = 'error'

         target: Profile
         status: str
         errors: list[LocalizableMessage] = []

      errors: list[LocalizableMessage] = []
      results: list[ResultElement] = []

   def ApplyHostConfiguration(self, host: HostSystem, configSpec: ConfigSpec, userInput: list[DeferredPolicyOptionParameter]) -> Task: ...
   def GenerateConfigTaskList(self, configSpec: ConfigSpec, host: HostSystem) -> ConfigTaskList: ...
   def GenerateTaskList(self, configSpec: ConfigSpec, host: HostSystem) -> Task: ...
   def QueryProfileMetadata(self, profileName: list[type], profile: Optional[Profile]) -> list[ProfileMetadata]: ...
   def QueryProfileStructure(self, profile: Optional[Profile]) -> ProfileStructure: ...
   def CreateDefaultProfile(self, profileType: type, profileTypeName: Optional[str], profile: Optional[Profile]) -> ApplyProfile: ...
   def UpdateAnswerFile(self, host: HostSystem, configSpec: AnswerFileCreateSpec) -> Task: ...
   def RetrieveAnswerFile(self, host: HostSystem) -> Optional[AnswerFile]: ...
   def RetrieveAnswerFileForProfile(self, host: HostSystem, applyProfile: HostApplyProfile) -> Optional[AnswerFile]: ...
   def ExportAnswerFile(self, host: HostSystem) -> Task: ...
   def CheckAnswerFileStatus(self, host: list[HostSystem]) -> Task: ...
   def QueryAnswerFileStatus(self, host: list[HostSystem]) -> list[AnswerFileStatusResult]: ...
   def RetrieveHostCustomizations(self, hosts: list[HostSystem]) -> list[StructuredCustomizations]: ...
   def RetrieveHostCustomizationsForProfile(self, hosts: list[HostSystem], applyProfile: HostApplyProfile) -> list[StructuredCustomizations]: ...
   def GenerateHostConfigTaskSpec(self, hostsInfo: list[StructuredCustomizations]) -> Task: ...
   def ApplyEntitiesConfiguration(self, applyConfigSpecs: list[ApplyHostConfigSpec]) -> Task: ...
   def ValidateComposition(self, source: Profile, targets: list[Profile], toBeMerged: Optional[HostApplyProfile], toReplaceWith: Optional[HostApplyProfile], toBeDeleted: Optional[HostApplyProfile], enableStatusToBeCopied: Optional[HostApplyProfile], errorOnly: Optional[bool]) -> Task: ...
   def CompositeProfile(self, source: Profile, targets: list[Profile], toBeMerged: Optional[HostApplyProfile], toBeReplacedWith: Optional[HostApplyProfile], toBeDeleted: Optional[HostApplyProfile], enableStatusToBeCopied: Optional[HostApplyProfile]) -> Task: ...
