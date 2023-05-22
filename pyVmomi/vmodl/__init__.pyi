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
    @key.setter
    def key(self, value: str):
        self._key = value
    @property
    def value(self) -> object: ...
    @value.setter
    def value(self, value: object):
        self._value = value


class LocalizableMessage(DynamicData):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value
    @property
    def arg(self) -> List[KeyAnyValue]: ...
    @arg.setter
    def arg(self, value: List[KeyAnyValue]):
        self._arg = value
    @property
    def message(self) -> str: ...
    @message.setter
    def message(self, value: str):
        self._message = value


class LocalizedMethodFault(MethodFault):
    @property
    def fault(self) -> MethodFault: ...
    @fault.setter
    def fault(self, value: MethodFault):
        self._fault = value
    @property
    def localizedMessage(self) -> str: ...
    @localizedMessage.setter
    def localizedMessage(self, value: str):
        self._localizedMessage = value


class MethodFault(DynamicData):
    @property
    def msg(self) -> str: ...
    @msg.setter
    def msg(self, value: str):
        self._msg = value
    @property
    def faultCause(self) -> MethodFault: ...
    @faultCause.setter
    def faultCause(self, value: MethodFault):
        self._faultCause = value
    @property
    def faultMessage(self) -> List[LocalizableMessage]: ...
    @faultMessage.setter
    def faultMessage(self, value: List[LocalizableMessage]):
        self._faultMessage = value


class RuntimeFault(MethodFault): ...