from pyVmomi import vmodl
from pyVmomi.VmomiSupport import ManagedObject, PropertyPath


class HostCommunication(vmodl.RuntimeFault): ...


class HostNotConnected(HostCommunication): ...


class HostNotReachable(HostCommunication): ...


class InvalidArgument(vmodl.RuntimeFault):
    @property
    def invalidProperty(self) -> PropertyPath: ...


class InvalidRequest(vmodl.RuntimeFault): ...


class InvalidType(InvalidRequest):
    @property
    def argument(self) -> PropertyPath: ...


class ManagedObjectNotFound(vmodl.RuntimeFault):
    @property
    def obj(self) -> ManagedObject: ...


class MethodNotFound(InvalidRequest):
    @property
    def receiver(self) -> ManagedObject: ...
    @property
    def method(self) -> str: ...


class NotEnoughLicenses(vmodl.RuntimeFault): ...


class NotImplemented(vmodl.RuntimeFault): ...


class NotSupported(vmodl.RuntimeFault): ...


class RequestCanceled(vmodl.RuntimeFault): ...


class SecurityError(vmodl.RuntimeFault): ...


class SystemError(vmodl.RuntimeFault):
    @property
    def reason(self) -> str: ...


class UnexpectedFault(vmodl.RuntimeFault):
    @property
    def faultName(self) -> type: ...
    @property
    def fault(self) -> vmodl.MethodFault: ...