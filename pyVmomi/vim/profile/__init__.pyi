from typing import List
from enum import Enum
from pyVmomi import vim, vmodl
from datetime import datetime
from pyVmomi.VmomiSupport import ManagedObject, NoneType, PropertyPath
from . import cluster, host


class ComplianceManager(ManagedObject):
    def CheckCompliance(self, profile: List[Profile], entity: List[vim.ManagedEntity]) -> vim.Task: ...
    def QueryComplianceStatus(self, profile: List[Profile], entity: List[vim.ManagedEntity]) -> List[ComplianceResult]: ...
    def ClearComplianceStatus(self, profile: List[Profile], entity: List[vim.ManagedEntity]) -> NoneType: ...
    def QueryExpressionMetadata(self, expressionName: List[str], profile: Profile) -> List[ExpressionMetadata]: ...


class Profile(ManagedObject):
    @property
    def config(self) -> Profile.ConfigInfo: ...
    @property
    def description(self) -> Profile.Description: ...
    @property
    def name(self) -> str: ...
    @property
    def createdTime(self) -> datetime: ...
    @property
    def modifiedTime(self) -> datetime: ...
    @property
    def entity(self) -> List[vim.ManagedEntity]: ...
    @property
    def complianceStatus(self) -> str: ...
    def RetrieveDescription(self) -> Profile.Description: ...
    def Destroy(self) -> NoneType: ...
    def AssociateEntities(self, entity: List[vim.ManagedEntity]) -> NoneType: ...
    def DissociateEntities(self, entity: List[vim.ManagedEntity]) -> NoneType: ...
    def CheckCompliance(self, entity: List[vim.ManagedEntity]) -> vim.Task: ...
    def ExportProfile(self) -> str: ...


    class ConfigInfo(vmodl.DynamicData):
        @property
        def name(self) -> str: ...
        @name.setter
        def name(self, value: str):
            self._name = value
        @property
        def annotation(self) -> str: ...
        @annotation.setter
        def annotation(self, value: str):
            self._annotation = value
        @property
        def enabled(self) -> bool: ...
        @enabled.setter
        def enabled(self, value: bool):
            self._enabled = value


    class CreateSpec(vmodl.DynamicData):
        @property
        def name(self) -> str: ...
        @name.setter
        def name(self, value: str):
            self._name = value
        @property
        def annotation(self) -> str: ...
        @annotation.setter
        def annotation(self, value: str):
            self._annotation = value
        @property
        def enabled(self) -> bool: ...
        @enabled.setter
        def enabled(self, value: bool):
            self._enabled = value


    class Description(vmodl.DynamicData):
        @property
        def section(self) -> List[Profile.Description.Section]: ...
        @section.setter
        def section(self, value: List[Profile.Description.Section]):
            self._section = value


        class Section(vmodl.DynamicData):
            @property
            def description(self) -> vim.ExtendedElementDescription: ...
            @description.setter
            def description(self, value: vim.ExtendedElementDescription):
                self._description = value
            @property
            def message(self) -> List[vmodl.LocalizableMessage]: ...
            @message.setter
            def message(self, value: List[vmodl.LocalizableMessage]):
                self._message = value


    class SerializedCreateSpec(Profile.CreateSpec):
        @property
        def profileConfigString(self) -> str: ...
        @profileConfigString.setter
        def profileConfigString(self, value: str):
            self._profileConfigString = value


class ProfileManager(ManagedObject):
    @property
    def profile(self) -> List[Profile]: ...
    def CreateProfile(self, createSpec: Profile.CreateSpec) -> Profile: ...
    def QueryPolicyMetadata(self, policyName: List[str], profile: Profile) -> List[PolicyMetadata]: ...
    def FindAssociatedProfile(self, entity: vim.ManagedEntity) -> List[Profile]: ...


class ApplyProfile(vmodl.DynamicData):
    @property
    def enabled(self) -> bool: ...
    @enabled.setter
    def enabled(self, value: bool):
        self._enabled = value
    @property
    def policy(self) -> List[Policy]: ...
    @policy.setter
    def policy(self, value: List[Policy]):
        self._policy = value
    @property
    def profileTypeName(self) -> str: ...
    @profileTypeName.setter
    def profileTypeName(self, value: str):
        self._profileTypeName = value
    @property
    def profileVersion(self) -> str: ...
    @profileVersion.setter
    def profileVersion(self, value: str):
        self._profileVersion = value
    @property
    def property(self) -> List[ApplyProfileProperty]: ...
    @property.setter
    def property(self, value: List[ApplyProfileProperty]):
        self._property = value
    @property
    def favorite(self) -> bool: ...
    @favorite.setter
    def favorite(self, value: bool):
        self._favorite = value
    @property
    def toBeMerged(self) -> bool: ...
    @toBeMerged.setter
    def toBeMerged(self, value: bool):
        self._toBeMerged = value
    @property
    def toReplaceWith(self) -> bool: ...
    @toReplaceWith.setter
    def toReplaceWith(self, value: bool):
        self._toReplaceWith = value
    @property
    def toBeDeleted(self) -> bool: ...
    @toBeDeleted.setter
    def toBeDeleted(self, value: bool):
        self._toBeDeleted = value
    @property
    def copyEnableStatus(self) -> bool: ...
    @copyEnableStatus.setter
    def copyEnableStatus(self, value: bool):
        self._copyEnableStatus = value
    @property
    def hidden(self) -> bool: ...
    @hidden.setter
    def hidden(self, value: bool):
        self._hidden = value


class ApplyProfileElement(ApplyProfile):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value


class ApplyProfileProperty(vmodl.DynamicData):
    @property
    def propertyName(self) -> str: ...
    @propertyName.setter
    def propertyName(self, value: str):
        self._propertyName = value
    @property
    def array(self) -> bool: ...
    @array.setter
    def array(self, value: bool):
        self._array = value
    @property
    def profile(self) -> List[ApplyProfile]: ...
    @profile.setter
    def profile(self, value: List[ApplyProfile]):
        self._profile = value


class ComplianceLocator(vmodl.DynamicData):
    @property
    def expressionName(self) -> str: ...
    @expressionName.setter
    def expressionName(self, value: str):
        self._expressionName = value
    @property
    def applyPath(self) -> ProfilePropertyPath: ...
    @applyPath.setter
    def applyPath(self, value: ProfilePropertyPath):
        self._applyPath = value


class ComplianceProfile(vmodl.DynamicData):
    @property
    def expression(self) -> List[Expression]: ...
    @expression.setter
    def expression(self, value: List[Expression]):
        self._expression = value
    @property
    def rootExpression(self) -> str: ...
    @rootExpression.setter
    def rootExpression(self, value: str):
        self._rootExpression = value


class ComplianceResult(vmodl.DynamicData):
    @property
    def profile(self) -> Profile: ...
    @profile.setter
    def profile(self, value: Profile):
        self._profile = value
    @property
    def complianceStatus(self) -> str: ...
    @complianceStatus.setter
    def complianceStatus(self, value: str):
        self._complianceStatus = value
    @property
    def entity(self) -> vim.ManagedEntity: ...
    @entity.setter
    def entity(self, value: vim.ManagedEntity):
        self._entity = value
    @property
    def checkTime(self) -> datetime: ...
    @checkTime.setter
    def checkTime(self, value: datetime):
        self._checkTime = value
    @property
    def failure(self) -> List[ComplianceResult.ComplianceFailure]: ...
    @failure.setter
    def failure(self, value: List[ComplianceResult.ComplianceFailure]):
        self._failure = value


    class ComplianceFailure(vmodl.DynamicData):
        @property
        def failureType(self) -> str: ...
        @failureType.setter
        def failureType(self, value: str):
            self._failureType = value
        @property
        def message(self) -> vmodl.LocalizableMessage: ...
        @message.setter
        def message(self, value: vmodl.LocalizableMessage):
            self._message = value
        @property
        def expressionName(self) -> str: ...
        @expressionName.setter
        def expressionName(self, value: str):
            self._expressionName = value
        @property
        def failureValues(self) -> List[ComplianceResult.ComplianceFailure.ComplianceFailureValues]: ...
        @failureValues.setter
        def failureValues(self, value: List[ComplianceResult.ComplianceFailure.ComplianceFailureValues]):
            self._failureValues = value


        class ComplianceFailureValues(vmodl.DynamicData):
            @property
            def comparisonIdentifier(self) -> str: ...
            @comparisonIdentifier.setter
            def comparisonIdentifier(self, value: str):
                self._comparisonIdentifier = value
            @property
            def profileInstance(self) -> str: ...
            @profileInstance.setter
            def profileInstance(self, value: str):
                self._profileInstance = value
            @property
            def hostValue(self) -> object: ...
            @hostValue.setter
            def hostValue(self, value: object):
                self._hostValue = value
            @property
            def profileValue(self) -> object: ...
            @profileValue.setter
            def profileValue(self, value: object):
                self._profileValue = value


    class Status(Enum):
        compliant = "compliant"
        nonCompliant = "nonCompliant"
        unknown = "unknown"
        running = "running"


class CompositeExpression(Expression):
    @property
    def operator(self) -> str: ...
    @operator.setter
    def operator(self, value: str):
        self._operator = value
    @property
    def expressionName(self) -> List[str]: ...
    @expressionName.setter
    def expressionName(self, value: List[str]):
        self._expressionName = value


class CompositePolicyOption(PolicyOption):
    @property
    def option(self) -> List[PolicyOption]: ...
    @option.setter
    def option(self, value: List[PolicyOption]):
        self._option = value


class CompositePolicyOptionMetadata(PolicyOptionMetadata):
    @property
    def option(self) -> List[str]: ...
    @option.setter
    def option(self, value: List[str]):
        self._option = value


class DeferredPolicyOptionParameter(vmodl.DynamicData):
    @property
    def inputPath(self) -> ProfilePropertyPath: ...
    @inputPath.setter
    def inputPath(self, value: ProfilePropertyPath):
        self._inputPath = value
    @property
    def parameter(self) -> List[vmodl.KeyAnyValue]: ...
    @parameter.setter
    def parameter(self, value: List[vmodl.KeyAnyValue]):
        self._parameter = value


class Expression(vmodl.DynamicData):
    @property
    def id(self) -> str: ...
    @id.setter
    def id(self, value: str):
        self._id = value
    @property
    def displayName(self) -> str: ...
    @displayName.setter
    def displayName(self, value: str):
        self._displayName = value
    @property
    def negated(self) -> bool: ...
    @negated.setter
    def negated(self, value: bool):
        self._negated = value


class ExpressionMetadata(vmodl.DynamicData):
    @property
    def expressionId(self) -> vim.ExtendedElementDescription: ...
    @expressionId.setter
    def expressionId(self, value: vim.ExtendedElementDescription):
        self._expressionId = value
    @property
    def parameter(self) -> List[ParameterMetadata]: ...
    @parameter.setter
    def parameter(self, value: List[ParameterMetadata]):
        self._parameter = value


class ParameterMetadata(vmodl.DynamicData):
    @property
    def id(self) -> vim.ExtendedElementDescription: ...
    @id.setter
    def id(self, value: vim.ExtendedElementDescription):
        self._id = value
    @property
    def type(self) -> type: ...
    @type.setter
    def type(self, value: type):
        self._type = value
    @property
    def optional(self) -> bool: ...
    @optional.setter
    def optional(self, value: bool):
        self._optional = value
    @property
    def defaultValue(self) -> object: ...
    @defaultValue.setter
    def defaultValue(self, value: object):
        self._defaultValue = value
    @property
    def hidden(self) -> bool: ...
    @hidden.setter
    def hidden(self, value: bool):
        self._hidden = value
    @property
    def securitySensitive(self) -> bool: ...
    @securitySensitive.setter
    def securitySensitive(self, value: bool):
        self._securitySensitive = value
    @property
    def readOnly(self) -> bool: ...
    @readOnly.setter
    def readOnly(self, value: bool):
        self._readOnly = value
    @property
    def parameterRelations(self) -> List[ParameterMetadata.ParameterRelationMetadata]: ...
    @parameterRelations.setter
    def parameterRelations(self, value: List[ParameterMetadata.ParameterRelationMetadata]):
        self._parameterRelations = value


    class ParameterRelationMetadata(vmodl.DynamicData):
        @property
        def relationTypes(self) -> List[str]: ...
        @relationTypes.setter
        def relationTypes(self, value: List[str]):
            self._relationTypes = value
        @property
        def values(self) -> List[object]: ...
        @values.setter
        def values(self, value: List[object]):
            self._values = value
        @property
        def path(self) -> ProfilePropertyPath: ...
        @path.setter
        def path(self, value: ProfilePropertyPath):
            self._path = value
        @property
        def minCount(self) -> int: ...
        @minCount.setter
        def minCount(self, value: int):
            self._minCount = value
        @property
        def maxCount(self) -> int: ...
        @maxCount.setter
        def maxCount(self, value: int):
            self._maxCount = value


    class RelationType(Enum):
        dynamic_relation = "dynamic_relation"
        extensible_relation = "extensible_relation"
        localizable_relation = "localizable_relation"
        static_relation = "static_relation"
        validation_relation = "validation_relation"


class Policy(vmodl.DynamicData):
    @property
    def id(self) -> str: ...
    @id.setter
    def id(self, value: str):
        self._id = value
    @property
    def policyOption(self) -> PolicyOption: ...
    @policyOption.setter
    def policyOption(self, value: PolicyOption):
        self._policyOption = value


class PolicyMetadata(vmodl.DynamicData):
    @property
    def id(self) -> vim.ExtendedElementDescription: ...
    @id.setter
    def id(self, value: vim.ExtendedElementDescription):
        self._id = value
    @property
    def possibleOption(self) -> List[PolicyOptionMetadata]: ...
    @possibleOption.setter
    def possibleOption(self, value: List[PolicyOptionMetadata]):
        self._possibleOption = value


class PolicyOption(vmodl.DynamicData):
    @property
    def id(self) -> str: ...
    @id.setter
    def id(self, value: str):
        self._id = value
    @property
    def parameter(self) -> List[vmodl.KeyAnyValue]: ...
    @parameter.setter
    def parameter(self, value: List[vmodl.KeyAnyValue]):
        self._parameter = value


class PolicyOptionMetadata(vmodl.DynamicData):
    @property
    def id(self) -> vim.ExtendedElementDescription: ...
    @id.setter
    def id(self, value: vim.ExtendedElementDescription):
        self._id = value
    @property
    def parameter(self) -> List[ParameterMetadata]: ...
    @parameter.setter
    def parameter(self, value: List[ParameterMetadata]):
        self._parameter = value


class ProfileMetadata(vmodl.DynamicData):
    @property
    def key(self) -> type: ...
    @key.setter
    def key(self, value: type):
        self._key = value
    @property
    def profileTypeName(self) -> str: ...
    @profileTypeName.setter
    def profileTypeName(self, value: str):
        self._profileTypeName = value
    @property
    def description(self) -> vim.ExtendedDescription: ...
    @description.setter
    def description(self, value: vim.ExtendedDescription):
        self._description = value
    @property
    def sortSpec(self) -> List[ProfileMetadata.ProfileSortSpec]: ...
    @sortSpec.setter
    def sortSpec(self, value: List[ProfileMetadata.ProfileSortSpec]):
        self._sortSpec = value
    @property
    def profileCategory(self) -> str: ...
    @profileCategory.setter
    def profileCategory(self, value: str):
        self._profileCategory = value
    @property
    def profileComponent(self) -> str: ...
    @profileComponent.setter
    def profileComponent(self, value: str):
        self._profileComponent = value
    @property
    def operationMessages(self) -> List[ProfileMetadata.ProfileOperationMessage]: ...
    @operationMessages.setter
    def operationMessages(self, value: List[ProfileMetadata.ProfileOperationMessage]):
        self._operationMessages = value


    class ProfileOperationMessage(vmodl.DynamicData):
        @property
        def operationName(self) -> str: ...
        @operationName.setter
        def operationName(self, value: str):
            self._operationName = value
        @property
        def message(self) -> vmodl.LocalizableMessage: ...
        @message.setter
        def message(self, value: vmodl.LocalizableMessage):
            self._message = value


    class ProfileSortSpec(vmodl.DynamicData):
        @property
        def policyId(self) -> str: ...
        @policyId.setter
        def policyId(self, value: str):
            self._policyId = value
        @property
        def parameter(self) -> str: ...
        @parameter.setter
        def parameter(self, value: str):
            self._parameter = value


class ProfilePropertyPath(vmodl.DynamicData):
    @property
    def profilePath(self) -> PropertyPath: ...
    @profilePath.setter
    def profilePath(self, value: PropertyPath):
        self._profilePath = value
    @property
    def policyId(self) -> str: ...
    @policyId.setter
    def policyId(self, value: str):
        self._policyId = value
    @property
    def parameterId(self) -> str: ...
    @parameterId.setter
    def parameterId(self, value: str):
        self._parameterId = value
    @property
    def policyOptionId(self) -> str: ...
    @policyOptionId.setter
    def policyOptionId(self, value: str):
        self._policyOptionId = value


class ProfileStructure(vmodl.DynamicData):
    @property
    def profileTypeName(self) -> str: ...
    @profileTypeName.setter
    def profileTypeName(self, value: str):
        self._profileTypeName = value
    @property
    def child(self) -> List[ProfileStructureProperty]: ...
    @child.setter
    def child(self, value: List[ProfileStructureProperty]):
        self._child = value


class ProfileStructureProperty(vmodl.DynamicData):
    @property
    def propertyName(self) -> str: ...
    @propertyName.setter
    def propertyName(self, value: str):
        self._propertyName = value
    @property
    def array(self) -> bool: ...
    @array.setter
    def array(self, value: bool):
        self._array = value
    @property
    def element(self) -> ProfileStructure: ...
    @element.setter
    def element(self, value: ProfileStructure):
        self._element = value


class SimpleExpression(Expression):
    @property
    def expressionType(self) -> str: ...
    @expressionType.setter
    def expressionType(self, value: str):
        self._expressionType = value
    @property
    def parameter(self) -> List[vmodl.KeyAnyValue]: ...
    @parameter.setter
    def parameter(self, value: List[vmodl.KeyAnyValue]):
        self._parameter = value


class UserInputRequiredParameterMetadata(PolicyOptionMetadata):
    @property
    def userInputParameter(self) -> List[ParameterMetadata]: ...
    @userInputParameter.setter
    def userInputParameter(self, value: List[ParameterMetadata]):
        self._userInputParameter = value