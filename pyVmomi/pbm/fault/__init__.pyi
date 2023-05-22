from typing import List
from pyVmomi import pbm, vmodl


class AlreadyExists(PBMFault):
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value


class CapabilityProfilePropertyMismatchFault(PropertyMismatchFault):
    @property
    def resourcePropertyInstance(self) -> pbm.capability.PropertyInstance: ...
    @resourcePropertyInstance.setter
    def resourcePropertyInstance(self, value: pbm.capability.PropertyInstance):
        self._resourcePropertyInstance = value


class CompatibilityCheckFault(PBMFault):
    @property
    def hub(self) -> pbm.placement.PlacementHub: ...
    @hub.setter
    def hub(self, value: pbm.placement.PlacementHub):
        self._hub = value


class DefaultProfileAppliesFault(CompatibilityCheckFault): ...


class DuplicateName(PBMFault):
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value


class IncompatibleVendorSpecificRuleSet(CapabilityProfilePropertyMismatchFault): ...


class InvalidLogin(PBMFault): ...


class LegacyHubsNotSupported(PBMFault):
    @property
    def hubs(self) -> List[pbm.placement.PlacementHub]: ...
    @hubs.setter
    def hubs(self, value: List[pbm.placement.PlacementHub]):
        self._hubs = value


class NoPermission():


    class EntityPrivileges(vmodl.DynamicData):
        @property
        def profileId(self) -> pbm.profile.ProfileId: ...
        @profileId.setter
        def profileId(self, value: pbm.profile.ProfileId):
            self._profileId = value
        @property
        def privilegeIds(self) -> List[str]: ...
        @privilegeIds.setter
        def privilegeIds(self, value: List[str]):
            self._privilegeIds = value


class NonExistentHubs(PBMFault):
    @property
    def hubs(self) -> List[pbm.placement.PlacementHub]: ...
    @hubs.setter
    def hubs(self, value: List[pbm.placement.PlacementHub]):
        self._hubs = value


class NotFound(PBMFault): ...


class PBMFault(vmodl.MethodFault): ...


class ProfileStorageFault(PBMFault): ...


class PropertyMismatchFault(CompatibilityCheckFault):
    @property
    def capabilityInstanceId(self) -> pbm.capability.CapabilityMetadata.UniqueId: ...
    @capabilityInstanceId.setter
    def capabilityInstanceId(self, value: pbm.capability.CapabilityMetadata.UniqueId):
        self._capabilityInstanceId = value
    @property
    def requirementPropertyInstance(self) -> pbm.capability.PropertyInstance: ...
    @requirementPropertyInstance.setter
    def requirementPropertyInstance(self, value: pbm.capability.PropertyInstance):
        self._requirementPropertyInstance = value


class ResourceInUse(PBMFault):
    @property
    def type(self) -> type: ...
    @type.setter
    def type(self, value: type):
        self._type = value
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value