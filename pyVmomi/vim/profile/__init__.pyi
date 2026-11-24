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
   """
   The `pyVmomi.vim.profile.ApplyProfile` data object is the base class for all data objects
   that define profile configuration data.
   
   `ApplyProfile` defines ESX configuration data storage and it
   supports recursive profile definition for the profile plug-in architecture.
   
   Attributes:
       enabled: Indicates whether the profile is enabled.
       policy: The list of policies comprising the profile.
           
           A `pyVmomi.vim.profile.Policy`
           stores one or more configuration data values in a `pyVmomi.vim.profile.PolicyOption`.
           The policy option is one of the configuration options from the
           `pyVmomi.vim.profile.PolicyMetadata`.`pyVmomi.vim.profile.PolicyMetadata.possibleOption`
           list.
       profileTypeName: Identifies the profile type.
       profileVersion: Profile engine version.
       property: List of subprofiles for this profile.
           
           This list can change depending on which profile plug-ins are available in the system.
           Subprofiles can be nested to arbitrary depths to represent host capabilities.
       favorite: Indicates whether this profile is marked as \"favorite\".
       toBeMerged: Indicates whether this profile is marked as to-be-merged.
       toReplaceWith: Indicates whether the selected array elements, with the current
           as one of them, replace the profile array in the target host
           profile.
       toBeDeleted: Indicates whether this profile is marked as to-be-deleted.
       copyEnableStatus: Indicates that the member variable `enabled` of this profile
           will be copied from source profile to target profiles at host profile
           composition.
       hidden: Indicates whether this profile will be displayed or not.
   """
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
   """
   DataObject which represents an ApplyProfile element.
   
   An ApplyProfile element is an ApplyProfile for a set of host
   configuration settings which may be instanced.
   For example, there may be multiple virtual switch instances
   represented by individual ApplyProfileElement DataObjects.
   
   Attributes:
       key: The linkable identifier.
   """
   key: str


class ApplyProfileProperty(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.vim.profile.ApplyProfileProperty` data object defines one or more subprofiles.
   
   Attributes:
       propertyName: Name of the property.
       array: Flag indicating whether this property is an array of profiles.
       profile: Subprofiles that define policies and nested subprofiles.
   """
   propertyName: str
   array: bool
   profile: list[ApplyProfile] = []


class ComplianceLocator(pyVmomi.vmodl.DynamicData):
   """
   This dataObject contains information about location of applyProfile
   which was responsible for generation of a particular ComplianceExpression.
   
   Attributes:
       expressionName: Expression for which the Locator corresponds to
       applyPath: Complete path to the profile/policy which was responsible for the
           generation of the ComplianceExpression.
           
           [ProfilePath + policyId] will uniquely identify a Policy.
   """
   expressionName: str
   applyPath: ProfilePropertyPath


class ComplianceManager(pyVmomi.VmomiSupport.ManagedObject):
   """Interface handling the Compliance aspects of entities."""
   def CheckCompliance(self, profile: list[Profile], entity: list[pyVmomi.vim.ManagedEntity]) -> pyVmomi.vim.Task:
      """
      Check compliance of an entity against a Profile.
      
      Args:
          profile: If specified, check compliance against the specified profiles.
              If not specified, use the profiles associated with the entities.
              If both Profiles and Entities are specified, Check the compliance of each
              Entity against each of the profile specified.
                
              For more information, look at the KMap below.
                
              P represents if Profile is specified.
                
              E represents if Entity is specified.
              
                              P                        ^P
                    ---------------------------------------------------
                    | Check compliance      |  Profiles associated    |
                   E|  of each entity       |   with the specified    |
                    |  against each of the  |   entity will be used   |
                    |  profiles specified.  |   for checking          |
                    |                       |   compliance.           |
                    |                       |                         |
                    |                       |                         |
                    ---------------------------------------------------
                    | All entities          |   InvalidArgument       |
                    |  associated with the  |   Exception is thrown.  |
                    |  profile are checked. |                         |
                  ^E|                       |                         |
                    |                       |                         |
                    |                       |                         |
                    |                       |                         |
                    ---------------------------------------------------
          entity: If specified, the compliance check is done against this entity.
      """
      ...
   def QueryComplianceStatus(self, profile: list[Profile], entity: list[pyVmomi.vim.ManagedEntity]) -> list[ComplianceResult]:
      """
      Query the compliance status based on Profile and Entity filter.
      
      Args:
          profile: If specified, compliance result for the specified profiles will be
              returned. This acts like a filtering criteria for the ComplianceResults based on
              specified profiles.
          entity: If specified, compliance results for these entities will be returned.
              This acts like a filtering criteria for the ComplianceResults based on entities.
      
      Returns:
          ComplianceResult. ComplianceResult information may not be
          available for all the entities. If the ComplianceResult is not available already,
          a new ComplianceCheck will not be triggered.
      """
      ...
   def ClearComplianceStatus(self, profile: list[Profile], entity: list[pyVmomi.vim.ManagedEntity]) -> None:
      """
      Clear the saved ComplianceResult based on profile and entity filtering criteria.
      
      Args:
          profile: If specified, clear the ComplianceResult related to the Profile.
          entity: If specified, clear the ComplianceResult related to the entity.
              If profile and entity are not specified, all the ComplianceResults will be cleared.
      """
      ...
   def QueryExpressionMetadata(self, expressionName: list[str], profile: _typing.Optional[Profile]) -> list[ExpressionMetadata]:
      """
      Query the metadata for the expressions.
      
      Args:
          expressionName: Names of the Expressions for which metadata is requested.
              If expressionNames are not specified, metadata for all known expressions is returned
          profile: Base profile whose context needs to be used during the operation
      """
      ...


class ComplianceProfile(pyVmomi.vmodl.DynamicData):
   """
   DataObject contains the verifications that need to be done
   to make sure the entity is in compliance.
   
   Attributes:
       expression: List of expressions that make up the ComplianceChecks.
       rootExpression: Name of the Expression which is the root of the expression tree.
   """
   expression: list[Expression] = []
   rootExpression: str


class ComplianceResult(pyVmomi.vmodl.DynamicData):
   """
   DataObject representing the result from a ComplianceCheck
   
   Attributes:
       profile: Profile for which the ComplianceResult applies
       complianceStatus: Indicates the compliance status of the entity.
           
           See @link Status
       entity: Entity on which the compliance check was carried out.
           
           Entity can be a Cluster, Host and so on.
       checkTime: Time at which compliance check was last run on the entity
       failure: If complianceStatus is non-compliant, failure will
           contain additional information about the compliance errors.
   """
   class Status(pyVmomi.VmomiSupport.Enum):
      """
      Attributes:
          compliant: Entity is in Compliance
          nonCompliant: Entity is out of Compliance
          unknown: Compliance status of the entity is not known
          running: Compliance check on this host is running.
      """
      compliant: _typing.ClassVar['ComplianceResult.Status'] = 'compliant'
      nonCompliant: _typing.ClassVar['ComplianceResult.Status'] = 'nonCompliant'
      unknown: _typing.ClassVar['ComplianceResult.Status'] = 'unknown'
      running: _typing.ClassVar['ComplianceResult.Status'] = 'running'

   class ComplianceFailure(pyVmomi.vmodl.DynamicData):
      """
      Attributes:
          failureType: String uniquely identifying the failure.
          message: Message which describes the compliance failures
              message.key serves as a key to the localized
              message catalog.
          expressionName: Name of the Expression which generated the ComplianceFailure
          failureValues: If complianceStatus is non-compliant, failureValues will
              contain values of the non-compliant fields on the host and
              in the profile.
      """
      class ComplianceFailureValues(pyVmomi.vmodl.DynamicData):
         """
         Attributes:
             comparisonIdentifier: Unique key to a message in the localized message catalog,
                 identifying the fields being compared.
             profileInstance: Name of the profile instance, in case of non-singleton profiles.
             hostValue: Value of the non-compliant field on the host.
             profileValue: Value of the non-compliant field in the profile.
         """
         comparisonIdentifier: str
         profileInstance: _typing.Optional[str] = None
         hostValue: _typing.Optional[object] = None
         profileValue: _typing.Optional[object] = None

      failureType: str
      message: pyVmomi.vmodl.LocalizableMessage
      expressionName: _typing.Optional[str] = None
      failureValues: list[ComplianceResult.ComplianceFailure.ComplianceFailureValues] = []

   profile: _typing.Optional[Profile] = None
   complianceStatus: str
   entity: _typing.Optional[pyVmomi.vim.ManagedEntity] = None
   checkTime: _typing.Optional[_datetime.datetime] = None
   failure: list[ComplianceResult.ComplianceFailure] = []


class Expression(pyVmomi.vmodl.DynamicData):
   """
   Attributes:
       id: Identifier of this expression.
           
           The id has to be unique within a Profile.
           The id can be used as a key while building composite expressions.
       displayName: User visible display name
       negated: Flag indicating if the condition of the expression should be negated.
           
           e.g: conditions like VSwitch0 has vmnic0 connected to it can be turned into
           VSwitch0 doesn't have vmnic0 connected to it.
   """
   id: str
   displayName: str
   negated: bool

class CompositeExpression(Expression):
   """
   DataObject to Compose expressions.
   
   It is used to group expressions
   together. They are similar to a parentheses in an expression.
   
   Attributes:
       operator: Logical operator to be applied between the expressions in
           the composite expression.
           
           e.g: or, and
       expressionName: List of expression names that will be used for this composition.
           
           The individual expressions will return a boolean. The return values
           of the individual expressions will be used to compute the final
           return value of the CompositeExpression.
           The expressions specified in the list can themselves be
           CompositeExpressions.
   """
   operator: str
   expressionName: list[str] = []


class PolicyOption(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.vim.profile.PolicyOption` data object represents one or more configuration
   values.
   
   A policy option is one of the configuration options from the
   `pyVmomi.vim.profile.PolicyMetadata`.`pyVmomi.vim.profile.PolicyMetadata.possibleOption`
   list.
   
   Attributes:
       id: Identifier for the policy option.
           
           This value matches one of the
           keys from the list of possible options in the policy metadata
           (`pyVmomi.vim.profile.PolicyMetadata`.`pyVmomi.vim.profile.PolicyMetadata.possibleOption`[].`pyVmomi.vim.profile.PolicyOptionMetadata.id`.`pyVmomi.vim.ElementDescription.key`).
       parameter: Parameters for the policy option.
           
           This list must include all parameters that are not marked as optional
           in the policy option metadata parameter list
           (`pyVmomi.vim.profile.PolicyMetadata`.`pyVmomi.vim.profile.PolicyMetadata.possibleOption`[].`pyVmomi.vim.profile.PolicyOptionMetadata.parameter`[].`pyVmomi.vim.profile.ParameterMetadata.optional`).
   """
   id: str
   parameter: list[pyVmomi.vmodl.KeyAnyValue] = []


class CompositePolicyOption(PolicyOption):
   """
   DataObject represents a composite Policy that is created by the user
   using different PolicyOptions.
   
   The options set in the CompositePolicyOption
   should be derived from the possible options as indicated by the
   CompositePolicyOptionMetadata.
   
   Attributes:
       option: List of policy options that are composed and applicable for
           this composite policy option.
           
           The selected PolicyOptions in a CompositePolicyOption will be used in the
           policy. PolicyOptions need not be specified if they are not desired for
           the CompositePolicyOption.
           Order of PolicyOptions in the PolicyOption array is not significant.
           The host profile policy engine will not respect order of PolicyOptions.
           It will apply PolicyOptions in a pre-determined order.
           Clients of the API must produce PolicyOption in the same order as specified
           in the metadata.
   """
   option: list[PolicyOption] = []


class PolicyOptionMetadata(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.vim.profile.PolicyOptionMetadata` data object contains the metadata information
   for a `pyVmomi.vim.profile.PolicyOption`.
   
   Attributes:
       id: Identifier for the policy option.
           - The `id.key` value
             (`pyVmomi.vim.ExtendedElementDescription`.`pyVmomi.vim.ElementDescription.key`)
             identifies the policy option type.
           - The `id.label` property
             (`pyVmomi.vim.ExtendedElementDescription`.`pyVmomi.vim.Description.label`)
             contains a brief localizable message describing the policy option.
           - The `id.summary` property
             (`pyVmomi.vim.ExtendedElementDescription`.`pyVmomi.vim.Description.summary`)
             contains a localizable summary of the policy option.
             Summary information can contain embedded variable names which can
             be replaced with values from the `parameter` property.
       parameter: Metadata about the parameters for the policy option.
   """
   id: pyVmomi.vim.ExtendedElementDescription
   parameter: list[ParameterMetadata] = []

class CompositePolicyOptionMetadata(PolicyOptionMetadata):
   """
   The `pyVmomi.vim.profile.CompositePolicyOptionMetadata` data object represents the metadata information
   for a composite `pyVmomi.vim.profile.PolicyOption`.
   
   The user will retrieve metadata
   information about a composite policy and then combine policy options to produce
   the composite policy option.
   
   Attributes:
       option: List of optional policy option identifiers that could be combined
           in this composite policy option.
           
           The policy options should already be
           part of the possible policy options for the policy. See the
           `pyVmomi.vim.profile.PolicyMetadata`.`pyVmomi.vim.profile.PolicyMetadata.possibleOption`
           list.
   """
   option: list[str] = []


class DeferredPolicyOptionParameter(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.vim.profile.DeferredPolicyOptionParameter` data object contains
   information about a single deferred parameter for host configuration.
   - The Server verifies deferred parameter data when it calls the
     `pyVmomi.vim.profile.host.HostProfile`.`pyVmomi.vim.profile.host.HostProfile.execute`
     method.
   - The client supplies deferred parameter data for host configuration when it calls the
     `pyVmomi.vim.profile.host.ProfileManager`.`pyVmomi.vim.profile.host.ProfileManager.applyHostConfiguration`
     method.
   - The vCenter Server stores deferred parameter data in answer files
     (`pyVmomi.vim.profile.host.AnswerFile`.`pyVmomi.vim.profile.host.AnswerFile.userInput`).
   
   Attributes:
       inputPath: Complete path to the `pyVmomi.vim.profile.PolicyOption` that defines the parameters.
       parameter: List that contains values for the policy parameters.
           
           During parameter verification, this property is unspecified
           if the client has not provided the values for this parameter.
           See `pyVmomi.vim.profile.host.ExecuteResult`.`pyVmomi.vim.profile.host.ExecuteResult.requireInput`.
   """
   inputPath: ProfilePropertyPath
   parameter: list[pyVmomi.vmodl.KeyAnyValue] = []


class ExpressionMetadata(pyVmomi.vmodl.DynamicData):
   """
   DataObject to represent the metadata associated with a SimpleExpression.
   
   Attributes:
       expressionId: Id of the SimpleExpression
       parameter: Parameters that can be specified for this SimpleExpression
   """
   expressionId: pyVmomi.vim.ExtendedElementDescription
   parameter: list[ParameterMetadata] = []

class NumericComparator:
   """
   Enumerates different operations supported for comparing
   numerical values.
   """
   pass


class ParameterMetadata(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.vim.profile.ParameterMetadata` data object represents the metadata information
   for expressions, policy options, and host-specific configuration data.
   
   Attributes:
       id: Identifier for the parameter.
       type: Type of the parameter.
       optional: Whether the parameter is optional.
       defaultValue: Default value that can be used for the parameter.
       hidden: Whether the parameter will not be displayed in UI.
       securitySensitive: Whether the parameter is security sensitive.
       readOnly: Indicates that the parameter value is read-only.
       parameterRelations: Relations with other profile or parameters.
   """
   class RelationType(pyVmomi.VmomiSupport.Enum):
      """
      The relation type to be supported.
      
      Attributes:
          dynamic_relation: The relation to a subprofile or a parameter.
          extensible_relation: The values from sources other than the parameter/profile or the static
              value list are allowed.
          localizable_relation: The value list contains localization keys instead of values.
          static_relation: The relation is defined by static valid value list.
          validation_relation: The relation is defined for validation purpose.
      """
      dynamic_relation: _typing.ClassVar['ParameterMetadata.RelationType'] = 'dynamic_relation'
      extensible_relation: _typing.ClassVar['ParameterMetadata.RelationType'] = 'extensible_relation'
      localizable_relation: _typing.ClassVar['ParameterMetadata.RelationType'] = 'localizable_relation'
      static_relation: _typing.ClassVar['ParameterMetadata.RelationType'] = 'static_relation'
      validation_relation: _typing.ClassVar['ParameterMetadata.RelationType'] = 'validation_relation'

   class ParameterRelationMetadata(pyVmomi.vmodl.DynamicData):
      """
      This class to define a relation between the parameter and a profile
      or a parameter, or a constant list of values.
      
      Attributes:
          relationTypes: The types of this relation.
          values: The valid value list.
          path: The property path of the related profile/parameter.
          minCount: The minimal count of values to map to.
          maxCount: The maximum count of values to map to.
      """
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
   parameterRelations: list[ParameterMetadata.ParameterRelationMetadata] = []


class Policy(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.vim.profile.Policy` data object represents a policy.
   
   Attributes:
       id: Identifier for the policy.
       policyOption: Configuration parameters.
   """
   id: str
   policyOption: PolicyOption


class PolicyMetadata(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.vim.profile.PolicyMetadata` data object represents the metadata information
   for a `pyVmomi.vim.profile.Policy`.
   
   Attributes:
       id: Identifier for the policy.
       possibleOption: Possible policy options that can be set for a policy of the
           given kind.
           
           `pyVmomi.vim.profile.host.HostProfile`s and subprofiles
           will contain selected policy options from this list. See
           `pyVmomi.vim.profile.PolicyOption`.
   """
   id: pyVmomi.vim.ExtendedElementDescription
   possibleOption: list[PolicyOptionMetadata] = []


class Profile(pyVmomi.VmomiSupport.ManagedObject):
   """
   The `Profile` managed object is the base class for host and cluster
   profiles.
   """
   class CreateSpec(pyVmomi.vmodl.DynamicData):
      """
      Specification describing the parameters during Profile creation
      
      Attributes:
          name: Name of the profile
          annotation: User Provided description of the profile
          enabled: Flag indicating if the Profile is enabled
      """
      name: _typing.Optional[str] = None
      annotation: _typing.Optional[str] = None
      enabled: _typing.Optional[bool] = None

   class SerializedCreateSpec(Profile.CreateSpec):
      """
      The `pyVmomi.vim.profile.Profile.SerializedCreateSpec` data object
      defines a string that contains a serialized representation of a host profile.
      
      Attributes:
          profileConfigString: Representation of the profile in the string form.
      """
      profileConfigString: str

   class ConfigInfo(pyVmomi.vmodl.DynamicData):
      """
      Attributes:
          name: Name of the profile
          annotation: User Provided description of the profile
          enabled: Flag indicating if the Profile is enabled
      """
      name: str
      annotation: _typing.Optional[str] = None
      enabled: bool

   class Description(pyVmomi.vmodl.DynamicData):
      """
      The `pyVmomi.vim.profile.Profile.Description` data object describes a profile.
      
      The description contains multiple sections. Each section
      describes a part of the profile.
      
      Attributes:
          section: Sections which make up the profile description.
      """
      class Section(pyVmomi.vmodl.DynamicData):
         """
         The `pyVmomi.vim.profile.Profile.Description.Section` data object
         contains a profile element description and any messages that may
         be associated with the profile section.
         
         Attributes:
             description: Localized message data.
             message: List of messages that make up the section.
         """
         description: pyVmomi.vim.ExtendedElementDescription
         message: list[pyVmomi.vmodl.LocalizableMessage] = []

      section: list[Profile.Description.Section] = []

   @property
   def config(self) -> Profile.ConfigInfo:
      """Configuration data for the profile."""
      ...
   @property
   def description(self) -> _typing.Optional[Profile.Description]:
      """Deprecated: As of vSphere API 5.0. use `pyVmomi.vim.profile.Profile.retrieveDescription` instead.Localizable description of the profile"""
      ...
   @property
   def name(self) -> str:
      """Name of the profile."""
      ...
   @property
   def createdTime(self) -> _datetime.datetime:
      """Time at which the profile was created."""
      ...
   @property
   def modifiedTime(self) -> _datetime.datetime:
      """Time at which the profile was last modified."""
      ...
   @property
   def entity(self) -> list[pyVmomi.vim.ManagedEntity]:
      """List of managed entities associated with the profile."""
      ...
   @property
   def complianceStatus(self) -> str:
      """
      Overall compliance of entities associated with this profile.
      
      If one of the entities is out of compliance, the profile is `nonCompliant`.
      If all entities are in compliance, the profile is `compliant`.
      If the compliance status of one of the entities is not known, compliance status
      of the profile is `unknown`.
      See `pyVmomi.vim.profile.ComplianceResult.Status`.
      """
      ...

   def RetrieveDescription(self) -> _typing.Optional[Profile.Description]:
      """
      Returns the localizable description for the profile.
      
      Returns:
          Profile divided into sections containing element descriptions and messages.
      """
      ...
   def Destroy(self) -> None:
      """Destroy the profile."""
      ...
   def AssociateEntities(self, entity: list[pyVmomi.vim.ManagedEntity]) -> None:
      """
      Associate a profile with a managed entity.
      
      You can check the compliance of
      entities associated with a profile by calling the
      `pyVmomi.vim.profile.Profile.checkCompliance` method.
      
      Args:
          entity: The entity(s) to associate with the profile.
              If an entity is already associated with the profile, the association is
              maintained and the vCenter Server does not perform any action.
      """
      ...
   def DissociateEntities(self, entity: list[pyVmomi.vim.ManagedEntity]) -> None:
      """
      Remove the association between a profile and a managed entity.
      
      Args:
          entity: List of entities. The vCenter Server will remove the associations
              that the profile has with the entities in the list. If unset,
              the Server removes all the associations that the profile has with any
              managed entities in the inventory.
              If the specified entity is not associated with the profile,
              the Server does not perform any action.
      """
      ...
   def CheckCompliance(self, entity: list[pyVmomi.vim.ManagedEntity]) -> pyVmomi.vim.Task:
      """
      Check compliance of an entity against a Profile.
      
      Args:
          entity: If specified, the compliance check is performed on this entity.
              If the entity is not specified, the vCenter Server runs a compliance check on all the
              entities associated with the profile. The entity does not have to be associated with the
              profile.
      
      Returns:
          The compliance result.
      """
      ...
   def ExportProfile(self) -> str:
      """
      Export the profile in a serialized form.
      
      To use the serialized string to create a profile,
      specify a `pyVmomi.vim.profile.Profile.SerializedCreateSpec` when you call the
      `pyVmomi.vim.profile.host.ProfileManager`.`pyVmomi.vim.profile.ProfileManager.createProfile`
      method.
      
      Returns:
          Serialized form of the profile.
      """
      ...


class ProfileManager(pyVmomi.VmomiSupport.ManagedObject):
   """This class is responsible for managing Profiles."""
   @property
   def profile(self) -> list[Profile]:
      """A list of profiles known to this ProfileManager."""
      ...

   def CreateProfile(self, createSpec: Profile.CreateSpec) -> Profile:
      """
      Create a profile from the specified CreateSpec.
      
      Args:
          createSpec: Specification for the profile being created.
              Usually a derived class CreateSpec can be used to create the Profile.
      
      Returns:
          Profile created from the specified createSpec.
      
      Raises:
          pyVmomi.vim.fault.DuplicateName: If a profile with the specified name already
              exists.
      """
      ...
   def QueryPolicyMetadata(self, policyName: list[str], profile: _typing.Optional[Profile]) -> list[PolicyMetadata]:
      """
      Get the Metadata information for the policyNames.
      
      PolicyNames are available with the defaultProfile obtained by invoking the
      method createDefaultProfile.
      
      Args:
          policyName: Retrieve metadata for the specified policyNames.
              If policyName is not specified, metadata for all policies will be returned.
          profile: Base profile whose context needs to be used during the operation
      
      Returns:
          The metadata information for the policy.
      """
      ...
   def FindAssociatedProfile(self, entity: pyVmomi.vim.ManagedEntity) -> list[Profile]:
      """
      Get the profile(s) to which this entity is associated.
      
      The list of profiles will only include profiles known to this
      profileManager.
      
      Args:
          entity: Entity for which profile is being looked up.
      """
      ...


class ProfileMetadata(pyVmomi.vmodl.DynamicData):
   """
   This data object represents the metadata information of a Profile.
   
   Attributes:
       key: Type of the Profile
       profileTypeName: Type identifier for the ApplyProfile
       description: Property which describes the profile
       sortSpec: Property that determines a sorting order for display purposes.
           
           If
           the list contains more than one sort spec, then the precedence should
           be determined by the list order (i.e. sort first by the first spec in
           the list, then sort by the second spec in the list, etc).
       profileCategory: Identifies the profile category that this subprofile is a part of.
           
           The
           value of this string should correspond to the key value of a
           `pyVmomi.vim.profile.ProfileCategoryMetadata` object's `pyVmomi.vim.ElementDescription.key`
           in its `pyVmomi.vim.profile.ProfileCategoryMetadata.id` property.
       profileComponent: Property indicating that the subprofile described by this
           `ProfileMetadata` object is declared in the
           `pyVmomi.vim.profile.ProfileComponentMetadata.profileTypeNames` of the specified
           profile component.
           
           The value of this property should correspond to the key
           value of the `pyVmomi.vim.profile.ProfileComponentMetadata` object's
           `pyVmomi.vim.ElementDescription.key` in its
           `pyVmomi.vim.profile.ProfileComponentMetadata.id` property.
           This property should not be present for subprofiles that are not directly
           declared in the `pyVmomi.vim.profile.ProfileComponentMetadata.profileTypeNames`
           property of a `pyVmomi.vim.profile.ProfileComponentMetadata` object.
       operationMessages: A list of `ProfileOperationMessage` for this profile.
   """
   class ProfileSortSpec(pyVmomi.vmodl.DynamicData):
      """
      Attributes:
          policyId: The id of the policy used to sort instances of the profile
          parameter: The parameter to be used for sorting.
              
              Note that if the policy to be
              used for sorting has multiple possible policy options, all possible
              policy options defined for that policy type must have this parameter.
      """
      policyId: str
      parameter: str

   class ProfileOperationMessage(pyVmomi.vmodl.DynamicData):
      """
      Some operations on host profile documents may cause unexpected result.
      
      For example, deleting a profile instance of vswitch may break the
      network connectivity.
      This data class provides the localizable message which may be
      presented before or after an operation happens.
      
      Attributes:
          operationName: The operation name.
          message: The localization message for the operation.
      """
      operationName: str
      message: pyVmomi.vmodl.LocalizableMessage

   key: type
   profileTypeName: _typing.Optional[str] = None
   description: _typing.Optional[pyVmomi.vim.ExtendedDescription] = None
   sortSpec: list[ProfileMetadata.ProfileSortSpec] = []
   profileCategory: _typing.Optional[str] = None
   profileComponent: _typing.Optional[str] = None
   operationMessages: list[ProfileMetadata.ProfileOperationMessage] = []


class ProfilePropertyPath(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.vim.profile.ProfilePropertyPath` data object represents
   the path to a profile, policy option, or specific parameter.
   
   If `profilePath`,
   `policyId`, and `parameterId` are all specified, the
   combination of the three identifies a particular parameter. If only `profilePath`
   and `policyId` are specified, the combination identifies a
   specific profile policy option. If just the `profilePath` is
   specified, the data object identifies a profile instance.
   
   Attributes:
       profilePath: Complete path to the leaf profile, relative to the root of the host profile
           document.
       policyId: Policy identifier.
       parameterId: Key for a parameter in the policy specified by `policyId`.
           
           See `pyVmomi.vim.profile.PolicyOption`.`pyVmomi.vim.profile.PolicyOption.parameter`
           and `pyVmomi.vmodl.KeyAnyValue.key`.
       policyOptionId: Policy option identifier.
   """
   profilePath: pyVmomi.VmomiSupport.PropertyPath
   policyId: _typing.Optional[str] = None
   parameterId: _typing.Optional[str] = None
   policyOptionId: _typing.Optional[str] = None


class ProfileStructure(pyVmomi.vmodl.DynamicData):
   """
   Attributes:
       profileTypeName: Identifier for the profile type
       child: SubProfile properties available for this profile
   """
   profileTypeName: str
   child: list[ProfileStructureProperty] = []


class ProfileStructureProperty(pyVmomi.vmodl.DynamicData):
   """
   Attributes:
       propertyName: Name of the property where this ProfileStructureProperty is being used
       array: Flag indicating if this property is an Array of profiles
       element: Details about the profile contained within this property
   """
   propertyName: str
   array: bool
   element: ProfileStructure


class SimpleExpression(Expression):
   """
   DataObject represents a pre-defined expression
   
   Attributes:
       expressionType: Type of the simple expression to instantiate.
           
           The expressionType should be derived from the available expressions as
           listed in the metadata.
       parameter: The parameters for the expressionType.
           
           The list of parameters needed for a simple expression can
           be obtained from the metadata.
   """
   expressionType: str
   parameter: list[pyVmomi.vmodl.KeyAnyValue] = []


class UserInputRequiredParameterMetadata(PolicyOptionMetadata):
   """
   The `pyVmomi.vim.profile.UserInputRequiredParameterMetadata` data object represents policy option metadata
   information for configuration data.
   
   The Profile Engine saves configuration
   data from the user input options in the host `pyVmomi.vim.profile.host.AnswerFile`.
   See the `pyVmomi.vim.profile.host.HostProfile.execute` and
   `pyVmomi.vim.profile.host.ProfileManager.applyHostConfiguration` methods.
   
   Attributes:
       userInputParameter: Metadata for user input options.
   """
   userInputParameter: list[ParameterMetadata] = []
