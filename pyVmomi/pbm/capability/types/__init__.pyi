from typing import List
from pyVmomi import pbm, vmodl


class DescriptiveValue(vmodl.DynamicData):
    @property
    def description(self) -> pbm.ExtendedElementDescription: ...
    @property
    def value(self) -> object: ...


class DiscreteSet(vmodl.DynamicData):
    @property
    def values(self) -> List[object]: ...


class Range(vmodl.DynamicData):
    @property
    def min(self) -> object: ...
    @property
    def max(self) -> object: ...


class TimeSpan(vmodl.DynamicData):
    @property
    def value(self) -> int: ...
    @property
    def unit(self) -> str: ...