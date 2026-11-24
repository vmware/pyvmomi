# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import typing as _typing
import pyVmomi.vmodl
import pyVmomi.pbm.capability
import pyVmomi.pbm.placement
import pyVmomi.pbm.profile
import pyVmomi.vmodl.fault



class AlreadyExists(PBMFault):
   name: _typing.Optional[str] = None


class CapabilityProfilePropertyMismatchFault(PropertyMismatchFault):
   resourcePropertyInstance: pyVmomi.pbm.capability.PropertyInstance


class CompatibilityCheckFault(PBMFault):
   hub: pyVmomi.pbm.placement.PlacementHub

class DefaultProfileAppliesFault(CompatibilityCheckFault):
   pass

class DuplicateName(PBMFault):
   name: str

class IncompatibleVendorSpecificRuleSet(CapabilityProfilePropertyMismatchFault):
   pass

class InvalidLogin(PBMFault):
   pass


class LegacyHubsNotSupported(PBMFault):
   hubs: list[pyVmomi.pbm.placement.PlacementHub] = []


class NoPermission(pyVmomi.vmodl.fault.SecurityError):
   class EntityPrivileges(pyVmomi.vmodl.DynamicData):
      profileId: _typing.Optional[pyVmomi.pbm.profile.ProfileId] = None
      privilegeIds: list[str] = []

   missingPrivileges: list[EntityPrivileges] = []


class NonExistentHubs(PBMFault):
   hubs: list[pyVmomi.pbm.placement.PlacementHub] = []

class NotFound(PBMFault):
   pass


class PBMFault(pyVmomi.vmodl.MethodFault):
   pass

class ProfileStorageFault(PBMFault):
   pass


class PropertyMismatchFault(CompatibilityCheckFault):
   capabilityInstanceId: pyVmomi.pbm.capability.CapabilityMetadata.UniqueId
   requirementPropertyInstance: pyVmomi.pbm.capability.PropertyInstance


class ResourceInUse(PBMFault):
   type: _typing.Optional[type] = None
   name: _typing.Optional[str] = None
