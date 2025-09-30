# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.pbm.ServerObjectRef import ServerObjectRef

from pyVmomi.pbm.placement.CompatibilityResult import CompatibilityResult

from pyVmomi.pbm.placement.PlacementHub import PlacementHub

from pyVmomi.pbm.placement.Requirement import Requirement

from pyVmomi.pbm.profile.CapabilityBasedProfileCreateSpec import CapabilityBasedProfileCreateSpec

from pyVmomi.pbm.profile.ProfileId import ProfileId

class PlacementSolver(ManagedObject):
   def QueryMatchingHub(self, hubsToSearch: list[PlacementHub], profile: ProfileId) -> list[PlacementHub]: ...
   def QueryMatchingHubWithSpec(self, hubsToSearch: list[PlacementHub], createSpec: CapabilityBasedProfileCreateSpec) -> list[PlacementHub]: ...
   def CheckCompatibility(self, hubsToSearch: list[PlacementHub], profile: ProfileId) -> list[CompatibilityResult]: ...
   def CheckCompatibilityWithSpec(self, hubsToSearch: list[PlacementHub], profileSpec: CapabilityBasedProfileCreateSpec) -> list[CompatibilityResult]: ...
   def CheckRequirements(self, hubsToSearch: list[PlacementHub], placementSubjectRef: Optional[ServerObjectRef], placementSubjectRequirement: list[Requirement]) -> list[CompatibilityResult]: ...
