from typing import List
from pyVmomi import eam, vim, vmodl


class DisabledClusterFault(EamAppFault):
    @property
    def disabledComputeResource(self) -> List[vim.ComputeResource]: ...
    @disabledComputeResource.setter
    def disabledComputeResource(self, value: List[vim.ComputeResource]):
        self._disabledComputeResource = value


class EamAppFault(EamRuntimeFault): ...


class EamFault(vmodl.MethodFault): ...


class EamIOFault(EamRuntimeFault): ...


class EamRuntimeFault(vmodl.RuntimeFault): ...


class EamServiceNotInitialized(EamRuntimeFault): ...


class EamSystemFault(EamRuntimeFault): ...


class InvalidAgencyScope(EamFault):
    @property
    def unknownComputeResource(self) -> List[vim.ComputeResource]: ...
    @unknownComputeResource.setter
    def unknownComputeResource(self, value: List[vim.ComputeResource]):
        self._unknownComputeResource = value


class InvalidAgentConfiguration(EamFault):
    @property
    def invalidAgentConfiguration(self) -> eam.Agent.ConfigInfo: ...
    @invalidAgentConfiguration.setter
    def invalidAgentConfiguration(self, value: eam.Agent.ConfigInfo):
        self._invalidAgentConfiguration = value
    @property
    def invalidField(self) -> str: ...
    @invalidField.setter
    def invalidField(self, value: str):
        self._invalidField = value


class InvalidLogin(EamRuntimeFault): ...


class InvalidState(EamAppFault): ...


class InvalidUrl(EamFault):
    @property
    def url(self) -> str: ...
    @url.setter
    def url(self, value: str):
        self._url = value
    @property
    def malformedUrl(self) -> bool: ...
    @malformedUrl.setter
    def malformedUrl(self, value: bool):
        self._malformedUrl = value
    @property
    def unknownHost(self) -> bool: ...
    @unknownHost.setter
    def unknownHost(self, value: bool):
        self._unknownHost = value
    @property
    def connectionRefused(self) -> bool: ...
    @connectionRefused.setter
    def connectionRefused(self, value: bool):
        self._connectionRefused = value
    @property
    def responseCode(self) -> int: ...
    @responseCode.setter
    def responseCode(self, value: int):
        self._responseCode = value


class InvalidVibPackage(EamRuntimeFault): ...


class NoConnectionToVCenter(EamRuntimeFault): ...


class NotAuthorized(EamRuntimeFault): ...