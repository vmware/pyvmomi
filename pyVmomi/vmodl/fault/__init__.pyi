from pyVmomi import vmodl
from pyVmomi.VmomiSupport import ManagedObject, PropertyPath


class HostCommunication(vmodl.RuntimeFault): ...


class HostNotConnected(HostCommunication): ...


class HostNotReachable(HostCommunication): ...


class InvalidArgument(vmodl.RuntimeFault):
    @property
    def invalidProperty(self) -> PropertyPath: ...
    @invalidProperty.setter
    def invalidProperty(self, value: PropertyPath):
        self._invalidProperty = value


class InvalidRequest(vmodl.RuntimeFault): ...


class InvalidType(InvalidRequest):
    @property
    def argument(self) -> PropertyPath: ...
    @argument.setter
    def argument(self, value: PropertyPath):
        self._argument = value


class ManagedObjectNotFound(vmodl.RuntimeFault):
    @property
    def obj(self) -> ManagedObject: ...
    @obj.setter
    def obj(self, value: ManagedObject):
        self._obj = value


class MethodNotFound(InvalidRequest):
    @property
    def receiver(self) -> ManagedObject: ...
    @receiver.setter
    def receiver(self, value: ManagedObject):
        self._receiver = value
    @property
    def method(self) -> str: ...
    @method.setter
    def method(self, value: str):
        self._method = value


class NotEnoughLicenses(vmodl.RuntimeFault): ...


class NotImplemented(vmodl.RuntimeFault): ...


class NotSupported(vmodl.RuntimeFault): ...


class RequestCanceled(vmodl.RuntimeFault): ...


class SecurityError(vmodl.RuntimeFault): ...


class SystemError(vmodl.RuntimeFault):
    @property
    def reason(self) -> str: ...
    @reason.setter
    def reason(self, value: str):
        self._reason = value


class UnexpectedFault(vmodl.RuntimeFault):
    @property
    def faultName(self) -> type: ...
    @faultName.setter
    def faultName(self, value: type):
        self._faultName = value
    @property
    def fault(self) -> vmodl.MethodFault: ...
    @fault.setter
    def fault(self, value: vmodl.MethodFault):
        self._fault = value