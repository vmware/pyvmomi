from typing import List
from pyVmomi import pbm, vim, vmodl
from pyVmomi.VmomiSupport import ManagedObject, long


class PlacementSolver(ManagedObject):
    def QueryMatchingHub(self, hubsToSearch: List[PlacementHub], profile: pbm.profile.ProfileId) -> List[PlacementHub]: ...
    def QueryMatchingHubWithSpec(self, hubsToSearch: List[PlacementHub], createSpec: pbm.profile.CapabilityBasedProfileCreateSpec) -> List[PlacementHub]: ...
    def CheckCompatibility(self, hubsToSearch: List[PlacementHub], profile: pbm.profile.ProfileId) -> List[CompatibilityResult]: ...
    def CheckCompatibilityWithSpec(self, hubsToSearch: List[PlacementHub], profileSpec: pbm.profile.CapabilityBasedProfileCreateSpec) -> List[CompatibilityResult]: ...
    def CheckRequirements(self, hubsToSearch: List[PlacementHub], placementSubjectRef: pbm.ServerObjectRef, placementSubjectRequirement: List[Requirement]) -> List[CompatibilityResult]: ...


class CapabilityConstraintsRequirement(Requirement):
    @property
    def constraints(self) -> pbm.profile.CapabilityConstraints: ...
    @constraints.setter
    def constraints(self, value: pbm.profile.CapabilityConstraints):
        self._constraints = value


class CapabilityProfileRequirement(Requirement):
    @property
    def profileId(self) -> pbm.profile.ProfileId: ...
    @profileId.setter
    def profileId(self, value: pbm.profile.ProfileId):
        self._profileId = value


class CompatibilityResult(vmodl.DynamicData):
    @property
    def hub(self) -> PlacementHub: ...
    @hub.setter
    def hub(self, value: PlacementHub):
        self._hub = value
    @property
    def matchingResources(self) -> List[MatchingResources]: ...
    @matchingResources.setter
    def matchingResources(self, value: List[MatchingResources]):
        self._matchingResources = value
    @property
    def howMany(self) -> long: ...
    @howMany.setter
    def howMany(self, value: long):
        self._howMany = value
    @property
    def utilization(self) -> List[ResourceUtilization]: ...
    @utilization.setter
    def utilization(self, value: List[ResourceUtilization]):
        self._utilization = value
    @property
    def warning(self) -> List[vmodl.MethodFault]: ...
    @warning.setter
    def warning(self, value: List[vmodl.MethodFault]):
        self._warning = value
    @property
    def error(self) -> List[vmodl.MethodFault]: ...
    @error.setter
    def error(self, value: List[vmodl.MethodFault]):
        self._error = value


class MatchingReplicationResources(MatchingResources):
    @property
    def replicationGroup(self) -> List[vim.vm.replication.ReplicationGroupId]: ...
    @replicationGroup.setter
    def replicationGroup(self, value: List[vim.vm.replication.ReplicationGroupId]):
        self._replicationGroup = value


class MatchingResources(vmodl.DynamicData): ...


class PlacementHub(vmodl.DynamicData):
    @property
    def hubType(self) -> str: ...
    @hubType.setter
    def hubType(self, value: str):
        self._hubType = value
    @property
    def hubId(self) -> str: ...
    @hubId.setter
    def hubId(self, value: str):
        self._hubId = value


class Requirement(vmodl.DynamicData): ...


class ResourceUtilization(vmodl.DynamicData):
    @property
    def name(self) -> pbm.ExtendedElementDescription: ...
    @name.setter
    def name(self, value: pbm.ExtendedElementDescription):
        self._name = value
    @property
    def description(self) -> pbm.ExtendedElementDescription: ...
    @description.setter
    def description(self, value: pbm.ExtendedElementDescription):
        self._description = value
    @property
    def availableBefore(self) -> long: ...
    @availableBefore.setter
    def availableBefore(self, value: long):
        self._availableBefore = value
    @property
    def availableAfter(self) -> long: ...
    @availableAfter.setter
    def availableAfter(self, value: long):
        self._availableAfter = value
    @property
    def total(self) -> long: ...
    @total.setter
    def total(self, value: long):
        self._total = value