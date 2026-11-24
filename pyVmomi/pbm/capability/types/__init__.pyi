# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import pyVmomi.pbm
import pyVmomi.vmodl


class BuiltinGenericTypesEnum:
   """
   The `pyVmomi.pbm.capability.types.BuiltinGenericTypesEnum` enumerated type defines the list
   of builtin generic datatypes.
   
   See
   `pyVmomi.pbm.capability.GenericTypeInfo`.`pyVmomi.pbm.capability.GenericTypeInfo.genericTypeName`.
   
   A generic datatype indicates how to interpret a collection of values
   of a specific datatype (`pyVmomi.pbm.capability.TypeInfo.typeName`).
   """
   pass

class BuiltinTypesEnum:
   """
   The `pyVmomi.pbm.capability.types.BuiltinTypesEnum` enumerated type defines datatypes
   for storage profiles.
   
   Property metadata
   (`pyVmomi.pbm.capability.PropertyMetadata`) uses the builtin types
   to define data types for storage capabilities and requirements.
   It may also specify the semantics that are applied to a collection
   of builtin type values. See `pyVmomi.pbm.capability.TypeInfo`.
   These semantics are specified as a generic builtin type.
   See `pyVmomi.pbm.capability.GenericTypeInfo`.
   The type information determines how capability constraints are interpreted
   `pyVmomi.pbm.capability.PropertyInstance.value`).
   """
   pass


class DescriptiveValue(pyVmomi.vmodl.DynamicData):
   """
   A property value with description.
   
   It can be repeated under DiscreteSet.
   E.g., set of tags, each with description and tag name.
   
   Attributes:
       description: Description of the property value
       value: Values for the set.
           
           must be one of the supported datatypes as
           defined in `pyVmomi.pbm.capability.types.BuiltinTypesEnum`
           Must only contain unique values to comply with the Set semantics
   """
   description: pyVmomi.pbm.ExtendedElementDescription
   value: object


class DiscreteSet(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.pbm.capability.types.DiscreteSet` data object defines a set of values
   for storage profile property instances (`pyVmomi.pbm.capability.PropertyInstance`).
   
   Use the discrete set type to define a set of values of a supported builtin type
   (`pyVmomi.pbm.capability.types.BuiltinTypesEnum`), for example a set of integers
   (XSD_INT) or a set of unsigned long values (XSD_LONG).
   See `pyVmomi.pbm.capability.types.BuiltinGenericTypesEnum`.`VMW_SET`.
   
   A discrete set of values is declared as an array of `xsd:anyType` values.
   - When you define a property instance for a storage profile requirement
     and pass an array of values to the Server, you must set the array elements
     to values of the appropriate datatype.
   - When you read a discrete set from a property instance for a storage profile
     capability, you must cast the `xsd:anyType` array element values
     to the appropriate datatype.
   
   Attributes:
       values: Array of values for the set.
           
           The values must be one of the supported datatypes
           as defined in `pyVmomi.pbm.capability.types.BuiltinTypesEnum` or `pyVmomi.pbm.capability.types.BuiltinGenericTypesEnum`.
   """
   values: list[object] = []


class Range(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.pbm.capability.types.Range` data object defines a range of values for storage property
   instances (`pyVmomi.pbm.capability.PropertyInstance`).
   
   Use the range type to define a range of values of a supported builtin type,
   for example range<int>, range<long>, or range<timespan>.
   You can specify a partial range by omitting one of the properties, min or max.
   
   Attributes:
       min: Minimum value of range.
           
           Must be one of the supported
           datatypes as defined in `pyVmomi.pbm.capability.types.BuiltinTypesEnum`.
           Must be the same datatype as min.
       max: Maximum value of range.
           
           Must be one of the supported
           datatypes as defined in `pyVmomi.pbm.capability.types.BuiltinTypesEnum`.
           Must be the same datatype as max.
   """
   min: object
   max: object


class TimeSpan(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.pbm.capability.types.TimeSpan` data object defines a time value and time unit,
   for example 10 hours or 5 minutes.
   
   See
   `pyVmomi.pbm.capability.types.BuiltinTypesEnum`.`VMW_TIMESPAN`.
   
   Attributes:
       value: Time value.
           
           Must be a positive integer.
       unit: Unit value for time.
           
           The string value must correspond
           to one of the `pyVmomi.pbm.capability.types.TimeUnitEnum` values.
   """
   value: int
   unit: str

class TimeUnitEnum:
   """
   The `pyVmomi.pbm.capability.types.TimeUnitEnum` enumeration type
   defines the supported list of time units for profiles that specify
   time span capabilities and constraints.
   
   See `pyVmomi.pbm.capability.types.TimeSpan`.
   """
   pass
