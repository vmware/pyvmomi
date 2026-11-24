# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from . import provider as provider
from . import types as types

import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.pbm
import pyVmomi.vmodl



class CapabilityInstance(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.pbm.capability.CapabilityInstance` data object defines a storage capability instance.
   
   Metadata for the capability is described in `pyVmomi.pbm.capability.CapabilityMetadata`.
   
   Attributes:
       id: Identifier for the capability.
           
           The identifier value corresponds to
           `pyVmomi.pbm.capability.CapabilityMetadata`.`pyVmomi.pbm.capability.CapabilityMetadata.id`.
       constraint: Constraints on the properties that comprise this capability.
           
           Each entry represents a constraint on one or more of the properties that
           constitute this capability. A datum must meet one of the
           constraints to be compliant.
   """
   id: CapabilityMetadata.UniqueId
   constraint: list[ConstraintInstance] = []


class CapabilityMetadata(pyVmomi.vmodl.DynamicData):
   """
   Metadata for a single unique setting defined by a provider.
   
   A simple setting is a setting with one property.
   A complex setting contains more than one property.
   
   Attributes:
       id: Unique identifier for the capability.
       summary: Capability name and description
       mandatory: Indicates whether incorporating given capability is mandatory during creation of
           profile.
       hint: The flag hint dictates the interpretation of constraints specified for this capability
           in a storage policy profile.
           
           If hint is false, then constraints will affect placement.
           If hint is true, constraints will not affect placement,
           but will still be passed to provisioning operations if the provider understands the
           relevant namespace. Optional property, false if not set.
       keyId: Property Id of the key property, if this capability represents a key
           value pair.
           
           Value is empty string if not set.
       allowMultipleConstraints: Flag to indicate if multiple constraints are allowed in the capability
           instance.
           
           False if not set.
       propertyMetadata: Metadata for the properties that comprise this capability.
   """
   class UniqueId(pyVmomi.vmodl.DynamicData):
      """
      Attributes:
          namespace: Namespace to which this capability belongs.
              
              Must be the same as
              { @link CapabilityObjectSchema#namespace } defined for this
              capability
          id: unique identifier for this capability within given namespace
      """
      namespace: str
      id: str

   id: CapabilityMetadata.UniqueId
   summary: pyVmomi.pbm.ExtendedElementDescription
   mandatory: _typing.Optional[bool] = None
   hint: _typing.Optional[bool] = None
   keyId: _typing.Optional[str] = None
   allowMultipleConstraints: _typing.Optional[bool] = None
   propertyMetadata: list[PropertyMetadata] = []


class CapabilityMetadataManager(pyVmomi.VmomiSupport.ManagedObject):
   """Intended for internal use."""
   pass


class ConstraintInstance(pyVmomi.vmodl.DynamicData):
   """
   Constraints on the properties for a single occurrence of a capability.
   
   All properties must satisfy their respective constraints to be compliant.
   
   Attributes:
       propertyInstance: Property instance array for this constraint
   """
   propertyInstance: list[PropertyInstance] = []


class TypeInfo(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.pbm.capability.TypeInfo` data object defines the datatype for a requirement
   or capability property.
   
   See `pyVmomi.pbm.capability.PropertyMetadata`.
   
   Attributes:
       typeName: Datatype for a property.
           
           Must be one of the types defined
           in `pyVmomi.pbm.capability.types.BuiltinTypesEnum`.
           
           A property value might consist of a collection of values of the specified
           datatype. The interpretation of the collection is determined by the
           generic type (`pyVmomi.pbm.capability.GenericTypeInfo.genericTypeName`).
           The generic type indicates how a collection of values
           of the specified datatype will be interpreted. See the descriptions of the
           `pyVmomi.pbm.capability.types.BuiltinTypesEnum` definitions.
   """
   typeName: str

class GenericTypeInfo(TypeInfo):
   """
   Generic type definition for capabilities.
   
   Indicates how a collection of values of a specific datatype
   (`pyVmomi.pbm.capability.TypeInfo.typeName`)
   will be interpreted.
   
   Attributes:
       genericTypeName: Name of the generic type.
           
           Must correspond to one of the values defined in
           `pyVmomi.pbm.capability.types.BuiltinGenericTypesEnum`.
   """
   genericTypeName: str

class Operator:
   """
   List of operators that are supported for constructing policy.
   
   Currently only tag based properties can use this operator.
   Other operators can be added as required.
   """
   pass


class PropertyInstance(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.pbm.capability.PropertyInstance` data object describes a virtual machine
   storage requirement.
   
   A storage requirement is based on the storage capability
   described in the `pyVmomi.pbm.capability.PropertyMetadata` and in the
   datastore profile property instance.
   
   Attributes:
       id: Requirement property identifier.
           
           This identifier corresponds to the
           storage capability metadata identifier
           (`pyVmomi.pbm.capability.PropertyMetadata`.`pyVmomi.pbm.capability.PropertyMetadata.id`).
       operator: Operator for the values.
           
           Currently only support NOT operator for
           tag namespace
           See operator definition in (`pyVmomi.pbm.capability.Operator`).
       value: Property value.
           
           You must specify the value.
           A property value is one value or a collection of values.
           - A single property value is expressed as a scalar value.
           - A collection of values is expressed as a `pyVmomi.pbm.capability.types.DiscreteSet`
             or a `pyVmomi.pbm.capability.types.Range` of values.
             
           The datatype of each value must be one of the
           `pyVmomi.pbm.capability.types.BuiltinTypesEnum` datatypes.
           If the property consists of a collection of values,
           the interpretation of those values is determined by the
           `pyVmomi.pbm.capability.GenericTypeInfo`.
           
           Type information for a property instance is described in the property metadata
           (`pyVmomi.pbm.capability.PropertyMetadata`.`pyVmomi.pbm.capability.PropertyMetadata.type`).
   """
   id: str
   operator: _typing.Optional[str] = None
   value: object


class PropertyMetadata(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.pbm.capability.PropertyMetadata` data object describes storage capability.
   
   An instance of property metadata may apply to many property instances
   (`pyVmomi.pbm.capability.PropertyInstance`).
   
   Attributes:
       id: Property identifier.
           
           Should be unique within the definition of the
           capability. Property instances refer to this identifier
           (`pyVmomi.pbm.capability.PropertyInstance`.`pyVmomi.pbm.capability.PropertyInstance.id`).
       summary: Property name and description.
           - The `summary.label` property
             (`pyVmomi.pbm.ExtendedElementDescription.label`)
             contains property 'name' in server locale.
           - The `summary.summary` property
             (`pyVmomi.pbm.ExtendedElementDescription.summary`)
             contains property 'description' in server locale.
           - The `summary.messageCatalogKeyPrefix` property
             (`pyVmomi.pbm.ExtendedElementDescription.messageCatalogKeyPrefix`)
             contains unique prefix for this property within given message catalog.
             Prefix format: <capability_unique_identifier>.<property_id>
             capability_unique_identifier -- string representation of
             `pyVmomi.pbm.capability.CapabilityMetadata.UniqueId` which globally identifies given
             capability metadata definition uniquely.
             property_id -- 'id' of this property `pyVmomi.pbm.capability.PropertyMetadata.id`
             Eg www.emc.com.storage.Recovery.Recovery_site
             www.emc.com.storage.Recovery.RPO
             www.emc.com.storage.Recovery.RTO
       mandatory: Indicates whether incorporating given capability is mandatory during creation of
           profile.
       type: Type information for the capability.
           
           The type of a property value
           (`pyVmomi.pbm.capability.PropertyInstance`.`pyVmomi.pbm.capability.PropertyInstance.value`)
           is specified as a builtin datatype and may also specify the interpretation of a
           collection of values of that datatype.
           - `pyVmomi.pbm.capability.PropertyMetadata.type`.`pyVmomi.pbm.capability.TypeInfo.typeName`
             specifies the `pyVmomi.pbm.capability.types.BuiltinTypesEnum`.
           - `pyVmomi.pbm.capability.PropertyMetadata.type`.`pyVmomi.pbm.capability.GenericTypeInfo.genericTypeName`
             indicates how a collection of values of the specified datatype will be interpreted
             (`pyVmomi.pbm.capability.types.BuiltinGenericTypesEnum`).
       defaultValue: Default value, if any, that the property will assume when not
           constrained by requirements.
           
           This object must be of the
           `pyVmomi.pbm.capability.PropertyMetadata.type`
           defined for the property.
       allowedValue: All legal values that the property may take on, across all
           implementations of the property.
           
           This definition of legal values is not
           determined by any particular resource configuration; rather it is
           inherent to the definition of the property. If undefined, then any value
           of the correct type is legal. This object must be a generic container for
           the `pyVmomi.pbm.capability.PropertyMetadata.type`
           defined for the property;
           see `pyVmomi.pbm.capability.types.BuiltinGenericTypesEnum`
           for the supported generic container types.
       requirementsTypeHint: A hint for data-driven systems that assist in authoring requirements
           constraints.
           
           Acceptable values defined by
           `pyVmomi.pbm.capability.types.BuiltinGenericTypesEnum`.
           A property will typically only have constraints of a given type in
           requirement profiles, even if it is likely to use constraints of
           different types across capability profiles. This value, if specified,
           specifies the expected kind of constraint used in requirement profiles.
           Considerations for using this information:
           - This is only a hint; any properly formed constraint
             (see `pyVmomi.pbm.capability.PropertyInstance.value`)
             is still valid for a requirement profile.
           - If VMW_SET is hinted, then a single value matching the property metadata type is
             also an expected form of constraint, as the latter is an allowed convenience
             for expressing a single-member set.
           - If this hint is not specified, then the authoring system may default to a form of
             constraint determined by its own criteria.
   """
   id: str
   summary: pyVmomi.pbm.ExtendedElementDescription
   mandatory: bool
   type: _typing.Optional[TypeInfo] = None
   defaultValue: _typing.Optional[object] = None
   allowedValue: _typing.Optional[object] = None
   requirementsTypeHint: _typing.Optional[str] = None
