from typing import List
from pyVmomi import vmodl
from pyVmomi.VmomiSupport import DataObject, PropertyPath


class DynamicArray(DataObject):
    @property
    def dynamicType(self) -> str: ...
    @property
    def val(self) -> List[object]: ...


class DynamicData(DataObject):
    @property
    def dynamicType(self) -> str: ...
    @property
    def dynamicProperty(self) -> List[DynamicProperty]: ...


class DynamicProperty(DataObject):
    @property
    def name(self) -> PropertyPath: ...
    @property
    def val(self) -> object: ...


class KeyAnyValue(DynamicData):
    @property
    def key(self) -> str: ...
    @property
    def value(self) -> object: ...


class LocalizableMessage(DynamicData):
    @property
    def key(self) -> str: ...
    @property
    def arg(self) -> List[KeyAnyValue]: ...
    @property
    def message(self) -> str: ...


class LocalizedMethodFault(MethodFault):
    @property
    def fault(self) -> MethodFault: ...
    @property
    def localizedMessage(self) -> str: ...


class MethodFault(DynamicData):
    @property
    def msg(self) -> str: ...
    @property
    def faultCause(self) -> MethodFault: ...
    @property
    def faultMessage(self) -> List[LocalizableMessage]: ...


class RuntimeFault(MethodFault): ...