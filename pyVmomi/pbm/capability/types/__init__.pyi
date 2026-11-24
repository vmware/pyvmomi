# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import pyVmomi.pbm
import pyVmomi.vmodl


class BuiltinGenericTypesEnum:
   pass

class BuiltinTypesEnum:
   pass


class DescriptiveValue(pyVmomi.vmodl.DynamicData):
   description: pyVmomi.pbm.ExtendedElementDescription
   value: object


class DiscreteSet(pyVmomi.vmodl.DynamicData):
   values: list[object] = []


class Range(pyVmomi.vmodl.DynamicData):
   min: object
   max: object


class TimeSpan(pyVmomi.vmodl.DynamicData):
   value: int
   unit: str

class TimeUnitEnum:
   pass
