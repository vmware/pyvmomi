# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from . import cluster as cluster
from . import host as host

import datetime as _datetime
import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vim
import pyVmomi.vmodl



class ApplyProfile(pyVmomi.vmodl.DynamicData):
   enabled: bool
   policy: list[Policy] = []
   profileTypeName: _typing.Optional[str] = None
   profileVersion: _typing.Optional[str] = None
   property: list[ApplyProfileProperty] = []
   favorite: _typing.Optional[bool] = None
   toBeMerged: _typing.Optional[bool] = None
   toReplaceWith: _typing.Optional[bool] = None
   toBeDeleted: _typing.Optional[bool] = None
   copyEnableStatus: _typing.Optional[bool] = None
   hidden: _typing.Optional[bool] = None

class ApplyProfileElement(ApplyProfile):
   key: str


class ApplyProfileProperty(pyVmomi.vmodl.DynamicData):
   propertyName: str
   array: bool
   profile: list[ApplyProfile] = []


class ComplianceLocator(pyVmomi.vmodl.DynamicData):
   expressionName: str
   applyPath: ProfilePropertyPath


class ComplianceManager(pyVmomi.VmomiSupport.ManagedObject):
   def CheckCompliance(self, profile: list[Profile], entity: list[pyVmomi.vim.ManagedEntity]) -> pyVmomi.vim.Task: ...
   def QueryComplianceStatus(self, profile: list[Profile], entity: list[pyVmomi.vim.ManagedEntity]) -> list[ComplianceResult]: ...
   def ClearComplianceStatus(self, profile: list[Profile], entity: list[pyVmomi.vim.ManagedEntity]) -> None: ...
   def QueryExpressionMetadata(self, expressionName: list[str], profile: _typing.Optional[Profile]) -> list[ExpressionMetadata]: ...


class ComplianceProfile(pyVmomi.vmodl.DynamicData):
   expression: list[Expression] = []
   rootExpression: str


class ComplianceResult(pyVmomi.vmodl.DynamicData):
   class Status(pyVmomi.VmomiSupport.Enum):
      compliant: _typing.ClassVar['Status'] = 'compliant'
      nonCompliant: _typing.ClassVar['Status'] = 'nonCompliant'
      unknown: _typing.ClassVar['Status'] = 'unknown'
      running: _typing.ClassVar['Status'] = 'running'

   class ComplianceFailure(pyVmomi.vmodl.DynamicData):
      class ComplianceFailureValues(pyVmomi.vmodl.DynamicData):
         comparisonIdentifier: str
         profileInstance: _typing.Optional[str] = None
         hostValue: _typing.Optional[object] = None
         profileValue: _typing.Optional[object] = None

      failureType: str
      message: pyVmomi.vmodl.LocalizableMessage
      expressionName: _typing.Optional[str] = None
      failureValues: list[ComplianceFailureValues] = []

   profile: _typing.Optional[Profile] = None
   complianceStatus: str
   entity: _typing.Optional[pyVmomi.vim.ManagedEntity] = None
   checkTime: _typing.Optional[_datetime.datetime] = None
   failure: list[ComplianceFailure] = []

class CompositeExpression(Expression):
   operator: str
   expressionName: list[str] = []


class CompositePolicyOption(PolicyOption):
   option: list[PolicyOption] = []

class CompositePolicyOptionMetadata(PolicyOptionMetadata):
   option: list[str] = []


class DeferredPolicyOptionParameter(pyVmomi.vmodl.DynamicData):
   inputPath: ProfilePropertyPath
   parameter: list[pyVmomi.vmodl.KeyAnyValue] = []


class Expression(pyVmomi.vmodl.DynamicData):
   id: str
   displayName: str
   negated: bool


class ExpressionMetadata(pyVmomi.vmodl.DynamicData):
   expressionId: pyVmomi.vim.ExtendedElementDescription
   parameter: list[ParameterMetadata] = []

class NumericComparator:
   pass


class ParameterMetadata(pyVmomi.vmodl.DynamicData):
   class RelationType(pyVmomi.VmomiSupport.Enum):
      dynamic_relation: _typing.ClassVar['RelationType'] = 'dynamic_relation'
      extensible_relation: _typing.ClassVar['RelationType'] = 'extensible_relation'
      localizable_relation: _typing.ClassVar['RelationType'] = 'localizable_relation'
      static_relation: _typing.ClassVar['RelationType'] = 'static_relation'
      validation_relation: _typing.ClassVar['RelationType'] = 'validation_relation'

   class ParameterRelationMetadata(pyVmomi.vmodl.DynamicData):
      relationTypes: list[str] = []
      values: list[object] = []
      path: _typing.Optional[ProfilePropertyPath] = None
      minCount: int
      maxCount: int

   id: pyVmomi.vim.ExtendedElementDescription
   type: type
   optional: bool
   defaultValue: _typing.Optional[object] = None
   hidden: _typing.Optional[bool] = None
   securitySensitive: _typing.Optional[bool] = None
   readOnly: _typing.Optional[bool] = None
   parameterRelations: list[ParameterRelationMetadata] = []


class Policy(pyVmomi.vmodl.DynamicData):
   id: str
   policyOption: PolicyOption


class PolicyMetadata(pyVmomi.vmodl.DynamicData):
   id: pyVmomi.vim.ExtendedElementDescription
   possibleOption: list[PolicyOptionMetadata] = []


class PolicyOption(pyVmomi.vmodl.DynamicData):
   id: str
   parameter: list[pyVmomi.vmodl.KeyAnyValue] = []


class PolicyOptionMetadata(pyVmomi.vmodl.DynamicData):
   id: pyVmomi.vim.ExtendedElementDescription
   parameter: list[ParameterMetadata] = []


class Profile(pyVmomi.VmomiSupport.ManagedObject):
   class CreateSpec(pyVmomi.vmodl.DynamicData):
      name: _typing.Optional[str] = None
      annotation: _typing.Optional[str] = None
      enabled: _typing.Optional[bool] = None

   class SerializedCreateSpec(CreateSpec):
      profileConfigString: str

   class ConfigInfo(pyVmomi.vmodl.DynamicData):
      name: str
      annotation: _typing.Optional[str] = None
      enabled: bool

   class Description(pyVmomi.vmodl.DynamicData):
      class Section(pyVmomi.vmodl.DynamicData):
         description: pyVmomi.vim.ExtendedElementDescription
         message: list[pyVmomi.vmodl.LocalizableMessage] = []

      section: list[Section] = []

   @property
   def config(self) -> ConfigInfo: ...
   @property
   def description(self) -> _typing.Optional[Description]: ...
   @property
   def name(self) -> str: ...
   @property
   def createdTime(self) -> _datetime.datetime: ...
   @property
   def modifiedTime(self) -> _datetime.datetime: ...
   @property
   def entity(self) -> list[pyVmomi.vim.ManagedEntity]: ...
   @property
   def complianceStatus(self) -> str: ...

   def RetrieveDescription(self) -> _typing.Optional[Description]: ...
   def Destroy(self) -> None: ...
   def AssociateEntities(self, entity: list[pyVmomi.vim.ManagedEntity]) -> None: ...
   def DissociateEntities(self, entity: list[pyVmomi.vim.ManagedEntity]) -> None: ...
   def CheckCompliance(self, entity: list[pyVmomi.vim.ManagedEntity]) -> pyVmomi.vim.Task: ...
   def ExportProfile(self) -> str: ...


class ProfileManager(pyVmomi.VmomiSupport.ManagedObject):
   @property
   def profile(self) -> list[Profile]: ...

   def CreateProfile(self, createSpec: Profile.CreateSpec) -> Profile: ...
   def QueryPolicyMetadata(self, policyName: list[str], profile: _typing.Optional[Profile]) -> list[PolicyMetadata]: ...
   def FindAssociatedProfile(self, entity: pyVmomi.vim.ManagedEntity) -> list[Profile]: ...


class ProfileMetadata(pyVmomi.vmodl.DynamicData):
   class ProfileSortSpec(pyVmomi.vmodl.DynamicData):
      policyId: str
      parameter: str

   class ProfileOperationMessage(pyVmomi.vmodl.DynamicData):
      operationName: str
      message: pyVmomi.vmodl.LocalizableMessage

   key: type
   profileTypeName: _typing.Optional[str] = None
   description: _typing.Optional[pyVmomi.vim.ExtendedDescription] = None
   sortSpec: list[ProfileSortSpec] = []
   profileCategory: _typing.Optional[str] = None
   profileComponent: _typing.Optional[str] = None
   operationMessages: list[ProfileOperationMessage] = []


class ProfilePropertyPath(pyVmomi.vmodl.DynamicData):
   profilePath: pyVmomi.VmomiSupport.PropertyPath
   policyId: _typing.Optional[str] = None
   parameterId: _typing.Optional[str] = None
   policyOptionId: _typing.Optional[str] = None


class ProfileStructure(pyVmomi.vmodl.DynamicData):
   profileTypeName: str
   child: list[ProfileStructureProperty] = []


class ProfileStructureProperty(pyVmomi.vmodl.DynamicData):
   propertyName: str
   array: bool
   element: ProfileStructure


class SimpleExpression(Expression):
   expressionType: str
   parameter: list[pyVmomi.vmodl.KeyAnyValue] = []


class UserInputRequiredParameterMetadata(PolicyOptionMetadata):
   userInputParameter: list[ParameterMetadata] = []
