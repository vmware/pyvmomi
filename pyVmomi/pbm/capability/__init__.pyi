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
   id: CapabilityMetadata.UniqueId
   constraint: list[ConstraintInstance] = []


class CapabilityMetadata(pyVmomi.vmodl.DynamicData):
   class UniqueId(pyVmomi.vmodl.DynamicData):
      namespace: str
      id: str

   id: UniqueId
   summary: pyVmomi.pbm.ExtendedElementDescription
   mandatory: _typing.Optional[bool] = None
   hint: _typing.Optional[bool] = None
   keyId: _typing.Optional[str] = None
   allowMultipleConstraints: _typing.Optional[bool] = None
   propertyMetadata: list[PropertyMetadata] = []


class CapabilityMetadataManager(pyVmomi.VmomiSupport.ManagedObject):
   pass


class ConstraintInstance(pyVmomi.vmodl.DynamicData):
   propertyInstance: list[PropertyInstance] = []

class GenericTypeInfo(TypeInfo):
   genericTypeName: str

class Operator:
   pass


class PropertyInstance(pyVmomi.vmodl.DynamicData):
   id: str
   operator: _typing.Optional[str] = None
   value: object


class PropertyMetadata(pyVmomi.vmodl.DynamicData):
   id: str
   summary: pyVmomi.pbm.ExtendedElementDescription
   mandatory: bool
   type: _typing.Optional[TypeInfo] = None
   defaultValue: _typing.Optional[object] = None
   allowedValue: _typing.Optional[object] = None
   requirementsTypeHint: _typing.Optional[str] = None


class TypeInfo(pyVmomi.vmodl.DynamicData):
   typeName: str
