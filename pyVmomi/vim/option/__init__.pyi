from typing import List
from enum import Enum
from pyVmomi import vim, vmodl
from pyVmomi.VmomiSupport import ManagedObject, NoneType, long


class OptionManager(ManagedObject):
    @property
    def supportedOption(self) -> List[OptionDef]: ...
    @property
    def setting(self) -> List[OptionValue]: ...
    def QueryView(self, name: str) -> List[OptionValue]: ...
    def UpdateValues(self, changedValue: List[OptionValue]) -> NoneType: ...


class ArrayUpdateSpec(vmodl.DynamicData):
    @property
    def operation(self) -> ArrayUpdateSpec.Operation: ...
    @operation.setter
    def operation(self, value: ArrayUpdateSpec.Operation):
        self._operation = value
    @property
    def removeKey(self) -> object: ...
    @removeKey.setter
    def removeKey(self, value: object):
        self._removeKey = value


    class Operation(Enum):
        add = "add"
        remove = "remove"
        edit = "edit"


class BoolOption(OptionType):
    @property
    def supported(self) -> bool: ...
    @supported.setter
    def supported(self, value: bool):
        self._supported = value
    @property
    def defaultValue(self) -> bool: ...
    @defaultValue.setter
    def defaultValue(self, value: bool):
        self._defaultValue = value


class ChoiceOption(OptionType):
    @property
    def choiceInfo(self) -> List[vim.ElementDescription]: ...
    @choiceInfo.setter
    def choiceInfo(self, value: List[vim.ElementDescription]):
        self._choiceInfo = value
    @property
    def defaultIndex(self) -> int: ...
    @defaultIndex.setter
    def defaultIndex(self, value: int):
        self._defaultIndex = value


class FloatOption(OptionType):
    @property
    def min(self) -> float: ...
    @min.setter
    def min(self, value: float):
        self._min = value
    @property
    def max(self) -> float: ...
    @max.setter
    def max(self, value: float):
        self._max = value
    @property
    def defaultValue(self) -> float: ...
    @defaultValue.setter
    def defaultValue(self, value: float):
        self._defaultValue = value


class IntOption(OptionType):
    @property
    def min(self) -> int: ...
    @min.setter
    def min(self, value: int):
        self._min = value
    @property
    def max(self) -> int: ...
    @max.setter
    def max(self, value: int):
        self._max = value
    @property
    def defaultValue(self) -> int: ...
    @defaultValue.setter
    def defaultValue(self, value: int):
        self._defaultValue = value


class LongOption(OptionType):
    @property
    def min(self) -> long: ...
    @min.setter
    def min(self, value: long):
        self._min = value
    @property
    def max(self) -> long: ...
    @max.setter
    def max(self, value: long):
        self._max = value
    @property
    def defaultValue(self) -> long: ...
    @defaultValue.setter
    def defaultValue(self, value: long):
        self._defaultValue = value


class OptionDef(vim.ElementDescription):
    @property
    def optionType(self) -> OptionType: ...
    @optionType.setter
    def optionType(self, value: OptionType):
        self._optionType = value


class OptionType(vmodl.DynamicData):
    @property
    def valueIsReadonly(self) -> bool: ...
    @valueIsReadonly.setter
    def valueIsReadonly(self, value: bool):
        self._valueIsReadonly = value


class OptionValue(vmodl.DynamicData):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value
    @property
    def value(self) -> object: ...
    @value.setter
    def value(self, value: object):
        self._value = value


class StringOption(OptionType):
    @property
    def defaultValue(self) -> str: ...
    @defaultValue.setter
    def defaultValue(self, value: str):
        self._defaultValue = value
    @property
    def validCharacters(self) -> str: ...
    @validCharacters.setter
    def validCharacters(self, value: str):
        self._validCharacters = value