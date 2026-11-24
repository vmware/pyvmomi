# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.pbm
import pyVmomi.vmodl
import pyVmomi.pbm.profile
import pyVmomi.vim.vm.replication



class CapabilityConstraintsRequirement(Requirement):
   constraints: pyVmomi.pbm.profile.CapabilityConstraints


class CapabilityProfileRequirement(Requirement):
   profileId: pyVmomi.pbm.profile.ProfileId


class CompatibilityResult(pyVmomi.vmodl.DynamicData):
   hub: PlacementHub
   hubInfo: _typing.Optional[PlacementHubInfo] = None
   matchingResources: list[MatchingResources] = []
   howMany: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   utilization: list[ResourceUtilization] = []
   warning: list[pyVmomi.vmodl.MethodFault] = []
   error: list[pyVmomi.vmodl.MethodFault] = []


class MatchingReplicationResources(MatchingResources):
   replicationGroup: list[pyVmomi.vim.vm.replication.ReplicationGroupId] = []


class MatchingResources(pyVmomi.vmodl.DynamicData):
   pass


class PlacementHub(pyVmomi.vmodl.DynamicData):
   hubType: str
   hubId: str


class PlacementHubInfo(pyVmomi.vmodl.DynamicData):
   zoneClusters: list[pyVmomi.pbm.ServerObjectRef] = []


class PlacementSolver(pyVmomi.VmomiSupport.ManagedObject):
   def QueryMatchingHub(self, hubsToSearch: list[PlacementHub], profile: pyVmomi.pbm.profile.ProfileId) -> list[PlacementHub]: ...
   def QueryMatchingHubWithSpec(self, hubsToSearch: list[PlacementHub], createSpec: pyVmomi.pbm.profile.CapabilityBasedProfileCreateSpec) -> list[PlacementHub]: ...
   def CheckCompatibility(self, hubsToSearch: list[PlacementHub], profile: pyVmomi.pbm.profile.ProfileId) -> list[CompatibilityResult]: ...
   def CheckCompatibilityWithSpec(self, hubsToSearch: list[PlacementHub], profileSpec: pyVmomi.pbm.profile.CapabilityBasedProfileCreateSpec) -> list[CompatibilityResult]: ...
   def CheckRequirements(self, hubsToSearch: list[PlacementHub], placementSubjectRef: _typing.Optional[pyVmomi.pbm.ServerObjectRef], placementSubjectRequirement: list[Requirement]) -> list[CompatibilityResult]: ...


class Requirement(pyVmomi.vmodl.DynamicData):
   pass


class ResourceUtilization(pyVmomi.vmodl.DynamicData):
   name: pyVmomi.pbm.ExtendedElementDescription
   description: pyVmomi.pbm.ExtendedElementDescription
   availableBefore: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   availableAfter: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   total: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class ZoneTopologyRequirement(CapabilityProfileRequirement):
   clusters: list[pyVmomi.pbm.ServerObjectRef] = []
