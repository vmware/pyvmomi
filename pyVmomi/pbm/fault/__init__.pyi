from typing import List
from pyVmomi import pbm, vmodl


class AlreadyExists(PBMFault):
    @property
    def name(self) -> str: ...


class CapabilityProfilePropertyMismatchFault(PropertyMismatchFault):
    @property
    def resourcePropertyInstance(self) -> pbm.capability.PropertyInstance: ...


class CompatibilityCheckFault(PBMFault):
    @property
    def hub(self) -> pbm.placement.PlacementHub: ...


class DefaultProfileAppliesFault(CompatibilityCheckFault): ...


class DuplicateName(PBMFault):
    @property
    def name(self) -> str: ...


class IncompatibleVendorSpecificRuleSet(CapabilityProfilePropertyMismatchFault): ...


class InvalidLogin(PBMFault): ...


class LegacyHubsNotSupported(PBMFault):
    @property
    def hubs(self) -> List[pbm.placement.PlacementHub]: ...


class NoPermission():


    class EntityPrivileges(vmodl.DynamicData):
        @property
        def profileId(self) -> pbm.profile.ProfileId: ...
        @property
        def privilegeIds(self) -> List[str]: ...


class NonExistentHubs(PBMFault):
    @property
    def hubs(self) -> List[pbm.placement.PlacementHub]: ...


class NotFound(PBMFault): ...


class PBMFault(vmodl.MethodFault): ...


class ProfileStorageFault(PBMFault): ...


class PropertyMismatchFault(CompatibilityCheckFault):
    @property
    def capabilityInstanceId(self) -> pbm.capability.CapabilityMetadata.UniqueId: ...
    @property
    def requirementPropertyInstance(self) -> pbm.capability.PropertyInstance: ...


class ResourceInUse(PBMFault):
    @property
    def type(self) -> type: ...
    @property
    def name(self) -> str: ...