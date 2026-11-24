# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from . import fault as fault
from . import query as query

import typing as _typing
import pyVmomi.VmomiSupport



class DynamicArray(pyVmomi.VmomiSupport.DataObject):
   dynamicType: _typing.Optional[str] = None
   val: list[object] = []


class DynamicData(pyVmomi.VmomiSupport.DataObject):
   dynamicType: _typing.Optional[str] = None
   dynamicProperty: list[DynamicProperty] = []


class DynamicProperty(pyVmomi.VmomiSupport.DataObject):
   name: pyVmomi.VmomiSupport.PropertyPath
   val: object

class KeyAnyValue(DynamicData):
   key: str
   value: object


class LocalizableMessage(DynamicData):
   key: str
   arg: list[KeyAnyValue] = []
   message: _typing.Optional[str] = None


class LocalizedMethodFault(DynamicData):
   fault: MethodFault
   localizedMessage: _typing.Optional[str] = None


class MethodFault(DynamicData, Exception):
   faultCause: _typing.Optional[MethodFault] = None
   faultMessage: list[LocalizableMessage] = []

class RuntimeFault(MethodFault):
   pass
