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
    @property
    def removeKey(self) -> object: ...


    class Operation(Enum):
        add = "add"
        remove = "remove"
        edit = "edit"


class BoolOption(OptionType):
    @property
    def supported(self) -> bool: ...
    @property
    def defaultValue(self) -> bool: ...


class ChoiceOption(OptionType):
    @property
    def choiceInfo(self) -> List[vim.ElementDescription]: ...
    @property
    def defaultIndex(self) -> int: ...


class FloatOption(OptionType):
    @property
    def min(self) -> float: ...
    @property
    def max(self) -> float: ...
    @property
    def defaultValue(self) -> float: ...


class IntOption(OptionType):
    @property
    def min(self) -> int: ...
    @property
    def max(self) -> int: ...
    @property
    def defaultValue(self) -> int: ...


class LongOption(OptionType):
    @property
    def min(self) -> long: ...
    @property
    def max(self) -> long: ...
    @property
    def defaultValue(self) -> long: ...


class OptionDef(vim.ElementDescription):
    @property
    def optionType(self) -> OptionType: ...


class OptionType(vmodl.DynamicData):
    @property
    def valueIsReadonly(self) -> bool: ...


class OptionValue(vmodl.DynamicData):
    @property
    def key(self) -> str: ...
    @property
    def value(self) -> object: ...


class StringOption(OptionType):
    @property
    def defaultValue(self) -> str: ...
    @property
    def validCharacters(self) -> str: ...