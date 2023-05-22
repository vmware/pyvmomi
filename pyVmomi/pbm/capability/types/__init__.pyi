from typing import List
from pyVmomi import pbm, vmodl


class DescriptiveValue(vmodl.DynamicData):
    @property
    def description(self) -> pbm.ExtendedElementDescription: ...
    @description.setter
    def description(self, value: pbm.ExtendedElementDescription):
        self._description = value
    @property
    def value(self) -> object: ...
    @value.setter
    def value(self, value: object):
        self._value = value


class DiscreteSet(vmodl.DynamicData):
    @property
    def values(self) -> List[object]: ...
    @values.setter
    def values(self, value: List[object]):
        self._values = value


class Range(vmodl.DynamicData):
    @property
    def min(self) -> object: ...
    @min.setter
    def min(self, value: object):
        self._min = value
    @property
    def max(self) -> object: ...
    @max.setter
    def max(self, value: object):
        self._max = value


class TimeSpan(vmodl.DynamicData):
    @property
    def value(self) -> int: ...
    @value.setter
    def value(self, value: int):
        self._value = value
    @property
    def unit(self) -> str: ...
    @unit.setter
    def unit(self, value: str):
        self._unit = value