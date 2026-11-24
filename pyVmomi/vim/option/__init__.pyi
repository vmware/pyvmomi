# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vim
import pyVmomi.vmodl



class ArrayUpdateSpec(pyVmomi.vmodl.DynamicData):
   class Operation(pyVmomi.VmomiSupport.Enum):
      add: _typing.ClassVar['Operation'] = 'add'
      remove: _typing.ClassVar['Operation'] = 'remove'
      edit: _typing.ClassVar['Operation'] = 'edit'

   operation: Operation
   removeKey: _typing.Optional[object] = None

class BoolOption(OptionType):
   supported: bool
   defaultValue: bool


class ChoiceOption(OptionType):
   choiceInfo: list[pyVmomi.vim.ElementDescription] = []
   defaultIndex: _typing.Optional[int] = None

class FloatOption(OptionType):
   min: float
   max: float
   defaultValue: float

class IntOption(OptionType):
   min: int
   max: int
   defaultValue: int


class LongOption(OptionType):
   min: pyVmomi.VmomiSupport.long
   max: pyVmomi.VmomiSupport.long
   defaultValue: pyVmomi.VmomiSupport.long


class OptionDef(pyVmomi.vim.ElementDescription):
   optionType: OptionType


class OptionManager(pyVmomi.VmomiSupport.ManagedObject):
   @property
   def supportedOption(self) -> list[OptionDef]: ...
   @property
   def setting(self) -> list[OptionValue]: ...

   def QueryView(self, name: _typing.Optional[str]) -> list[OptionValue]: ...
   def UpdateValues(self, changedValue: list[OptionValue]) -> None: ...


class OptionType(pyVmomi.vmodl.DynamicData):
   valueIsReadonly: _typing.Optional[bool] = None


class OptionValue(pyVmomi.vmodl.DynamicData):
   key: str
   value: _typing.Optional[object] = None


class StringOption(OptionType):
   defaultValue: str
   validCharacters: _typing.Optional[str] = None
