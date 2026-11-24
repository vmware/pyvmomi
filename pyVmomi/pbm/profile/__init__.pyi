# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from . import provider as provider

import datetime as _datetime
import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.pbm
import pyVmomi.vmodl
import pyVmomi.pbm.capability
import pyVmomi.pbm.placement
import pyVmomi.pbm.capability.provider
import pyVmomi.pbm.profile.provider



class CapabilityBasedProfile(Profile):
   class ProfileCategoryEnum(pyVmomi.VmomiSupport.Enum):
      REQUIREMENT: _typing.ClassVar['ProfileCategoryEnum'] = 'REQUIREMENT'
      RESOURCE: _typing.ClassVar['ProfileCategoryEnum'] = 'RESOURCE'
      DATA_SERVICE_POLICY: _typing.ClassVar['ProfileCategoryEnum'] = 'DATA_SERVICE_POLICY'

   class SystemCreatedProfileType(pyVmomi.VmomiSupport.Enum):
      VsanDefaultProfile: _typing.ClassVar['SystemCreatedProfileType'] = 'VsanDefaultProfile'
      VVolDefaultProfile: _typing.ClassVar['SystemCreatedProfileType'] = 'VVolDefaultProfile'
      PmemDefaultProfile: _typing.ClassVar['SystemCreatedProfileType'] = 'PmemDefaultProfile'
      VmcManagementProfile: _typing.ClassVar['SystemCreatedProfileType'] = 'VmcManagementProfile'
      VsanMaxDefaultProfile: _typing.ClassVar['SystemCreatedProfileType'] = 'VsanMaxDefaultProfile'
      VsanEsaAutoManagedRaidProfile: _typing.ClassVar['SystemCreatedProfileType'] = 'VsanEsaAutoManagedRaidProfile'

   profileCategory: str
   resourceType: ResourceType
   constraints: CapabilityConstraints
   generationId: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   isDefault: bool
   systemCreatedProfileType: _typing.Optional[str] = None
   lineOfService: _typing.Optional[str] = None
   k8sCompliantName: _typing.Optional[str] = None
   otherK8sCompliantNames: list[str] = []


class CapabilityBasedProfileCreateSpec(pyVmomi.vmodl.DynamicData):
   name: str
   description: _typing.Optional[str] = None
   category: _typing.Optional[str] = None
   resourceType: ResourceType
   constraints: CapabilityConstraints
   k8sCompliantName: _typing.Optional[str] = None


class CapabilityBasedProfileUpdateSpec(pyVmomi.vmodl.DynamicData):
   name: _typing.Optional[str] = None
   description: _typing.Optional[str] = None
   constraints: _typing.Optional[CapabilityConstraints] = None


class CapabilityConstraints(pyVmomi.vmodl.DynamicData):
   pass


class DataServiceToPoliciesMap(pyVmomi.vmodl.DynamicData):
   dataServicePolicy: ProfileId
   parentStoragePolicies: list[ProfileId] = []
   fault: _typing.Optional[pyVmomi.vmodl.MethodFault] = None

class DefaultCapabilityBasedProfile(CapabilityBasedProfile):
   vvolType: list[str] = []
   containerId: str


class DefaultProfileInfo(pyVmomi.vmodl.DynamicData):
   datastores: list[pyVmomi.pbm.placement.PlacementHub] = []
   defaultProfile: _typing.Optional[Profile] = None
   methodFault: _typing.Optional[pyVmomi.vmodl.MethodFault] = None


class Profile(pyVmomi.vmodl.DynamicData):
   profileId: ProfileId
   name: str
   description: _typing.Optional[str] = None
   creationTime: _datetime.datetime
   createdBy: str
   lastUpdatedTime: _datetime.datetime
   lastUpdatedBy: str


class ProfileId(pyVmomi.vmodl.DynamicData):
   uniqueId: str


class ProfileK8sCompliantNameSpec(pyVmomi.vmodl.DynamicData):
   profileId: str
   k8sCompliantName: str
   otherK8sCompliantNames: list[str] = []


class ProfileManager(pyVmomi.VmomiSupport.ManagedObject):
   def FetchResourceType(self) -> list[ResourceType]: ...
   def FetchVendorInfo(self, resourceType: _typing.Optional[ResourceType]) -> list[pyVmomi.pbm.capability.provider.CapabilityObjectSchema.VendorResourceTypeInfo]: ...
   def FetchCapabilityMetadata(self, resourceType: _typing.Optional[ResourceType], vendorUuid: _typing.Optional[str]) -> list[pyVmomi.pbm.capability.provider.CapabilityObjectMetadataPerCategory]: ...
   def FetchCapabilitySchema(self, vendorUuid: _typing.Optional[str], lineOfService: list[str]) -> list[pyVmomi.pbm.capability.provider.CapabilityObjectSchema]: ...
   def Create(self, createSpec: CapabilityBasedProfileCreateSpec) -> ProfileId: ...
   def Update(self, profileId: ProfileId, updateSpec: CapabilityBasedProfileUpdateSpec) -> None: ...
   def Delete(self, profileId: list[ProfileId]) -> list[ProfileOperationOutcome]: ...
   def QueryProfile(self, resourceType: ResourceType, profileCategory: _typing.Optional[str]) -> list[ProfileId]: ...
   def RetrieveContent(self, profileIds: list[ProfileId]) -> list[Profile]: ...
   def QueryAssociatedProfiles(self, entities: list[pyVmomi.pbm.ServerObjectRef]) -> list[QueryProfileResult]: ...
   def QueryAssociatedProfile(self, entity: pyVmomi.pbm.ServerObjectRef) -> list[ProfileId]: ...
   def QueryAssociatedEntity(self, profile: ProfileId, entityType: _typing.Optional[str]) -> list[pyVmomi.pbm.ServerObjectRef]: ...
   def QueryDefaultRequirementProfile(self, hub: pyVmomi.pbm.placement.PlacementHub) -> _typing.Optional[ProfileId]: ...
   def ResetDefaultRequirementProfile(self, profile: _typing.Optional[ProfileId]) -> None: ...
   def AssignDefaultRequirementProfile(self, profile: ProfileId, datastores: list[pyVmomi.pbm.placement.PlacementHub]) -> None: ...
   def FindApplicableDefaultProfile(self, datastores: list[pyVmomi.pbm.placement.PlacementHub]) -> list[Profile]: ...
   def QueryDefaultRequirementProfiles(self, datastores: list[pyVmomi.pbm.placement.PlacementHub]) -> list[DefaultProfileInfo]: ...
   def ResetVSanDefaultProfile(self) -> None: ...
   def QuerySpaceStatsForStorageContainer(self, datastore: pyVmomi.pbm.ServerObjectRef, capabilityProfileId: list[ProfileId]) -> list[pyVmomi.pbm.profile.provider.DatastoreSpaceStatistics]: ...
   def QueryAssociatedEntities(self, profiles: list[ProfileId]) -> list[QueryProfileResult]: ...


class ProfileOperationOutcome(pyVmomi.vmodl.DynamicData):
   profileId: ProfileId
   fault: _typing.Optional[pyVmomi.vmodl.MethodFault] = None


class ProfileType(pyVmomi.vmodl.DynamicData):
   uniqueId: str


class QueryProfileResult(pyVmomi.vmodl.DynamicData):
   object: pyVmomi.pbm.ServerObjectRef
   profileId: list[ProfileId] = []
   fault: _typing.Optional[pyVmomi.vmodl.MethodFault] = None


class ResourceType(pyVmomi.vmodl.DynamicData):
   resourceType: str

class ResourceTypeEnum:
   pass


class SubProfileCapabilityConstraints(CapabilityConstraints):
   class SubProfile(pyVmomi.vmodl.DynamicData):
      name: str
      capability: list[pyVmomi.pbm.capability.CapabilityInstance] = []
      forceProvision: _typing.Optional[bool] = None

   subProfiles: list[SubProfile] = []
