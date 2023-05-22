from typing import List
from enum import Enum
from pyVmomi import pbm, vmodl
from datetime import datetime
from pyVmomi.VmomiSupport import ManagedObject, NoneType, long
from . import provider


class ProfileManager(ManagedObject):
    def FetchResourceType(self) -> List[ResourceType]: ...
    def FetchVendorInfo(self, resourceType: ResourceType) -> List[pbm.capability.provider.CapabilityObjectSchema.VendorResourceTypeInfo]: ...
    def FetchCapabilityMetadata(self, resourceType: ResourceType, vendorUuid: str) -> List[pbm.capability.provider.CapabilityObjectMetadataPerCategory]: ...
    def FetchCapabilitySchema(self, vendorUuid: str, lineOfService: List[str]) -> List[pbm.capability.provider.CapabilityObjectSchema]: ...
    def Create(self, createSpec: CapabilityBasedProfileCreateSpec) -> ProfileId: ...
    def Update(self, profileId: ProfileId, updateSpec: CapabilityBasedProfileUpdateSpec) -> NoneType: ...
    def Delete(self, profileId: List[ProfileId]) -> List[ProfileOperationOutcome]: ...
    def QueryProfile(self, resourceType: ResourceType, profileCategory: str) -> List[ProfileId]: ...
    def RetrieveContent(self, profileIds: List[ProfileId]) -> List[Profile]: ...
    def QueryAssociatedProfiles(self, entities: List[pbm.ServerObjectRef]) -> List[QueryProfileResult]: ...
    def QueryAssociatedProfile(self, entity: pbm.ServerObjectRef) -> List[ProfileId]: ...
    def QueryAssociatedEntity(self, profile: ProfileId, entityType: str) -> List[pbm.ServerObjectRef]: ...
    def QueryDefaultRequirementProfile(self, hub: pbm.placement.PlacementHub) -> ProfileId: ...
    def ResetDefaultRequirementProfile(self, profile: ProfileId) -> NoneType: ...
    def AssignDefaultRequirementProfile(self, profile: ProfileId, datastores: List[pbm.placement.PlacementHub]) -> NoneType: ...
    def FindApplicableDefaultProfile(self, datastores: List[pbm.placement.PlacementHub]) -> List[Profile]: ...
    def QueryDefaultRequirementProfiles(self, datastores: List[pbm.placement.PlacementHub]) -> List[DefaultProfileInfo]: ...
    def ResetVSanDefaultProfile(self) -> NoneType: ...
    def QuerySpaceStatsForStorageContainer(self, datastore: pbm.ServerObjectRef, capabilityProfileId: List[ProfileId]) -> List[provider.DatastoreSpaceStatistics]: ...
    def QueryAssociatedEntities(self, profiles: List[ProfileId]) -> List[QueryProfileResult]: ...


class CapabilityBasedProfile(Profile):
    @property
    def profileCategory(self) -> str: ...
    @profileCategory.setter
    def profileCategory(self, value: str):
        self._profileCategory = value
    @property
    def resourceType(self) -> ResourceType: ...
    @resourceType.setter
    def resourceType(self, value: ResourceType):
        self._resourceType = value
    @property
    def constraints(self) -> CapabilityConstraints: ...
    @constraints.setter
    def constraints(self, value: CapabilityConstraints):
        self._constraints = value
    @property
    def generationId(self) -> long: ...
    @generationId.setter
    def generationId(self, value: long):
        self._generationId = value
    @property
    def isDefault(self) -> bool: ...
    @isDefault.setter
    def isDefault(self, value: bool):
        self._isDefault = value
    @property
    def systemCreatedProfileType(self) -> str: ...
    @systemCreatedProfileType.setter
    def systemCreatedProfileType(self, value: str):
        self._systemCreatedProfileType = value
    @property
    def lineOfService(self) -> str: ...
    @lineOfService.setter
    def lineOfService(self, value: str):
        self._lineOfService = value


    class ProfileCategoryEnum(Enum):
        REQUIREMENT = "REQUIREMENT"
        RESOURCE = "RESOURCE"
        DATA_SERVICE_POLICY = "DATA_SERVICE_POLICY"


    class SystemCreatedProfileType(Enum):
        VsanDefaultProfile = "VsanDefaultProfile"
        VVolDefaultProfile = "VVolDefaultProfile"
        PmemDefaultProfile = "PmemDefaultProfile"
        VmcManagementProfile = "VmcManagementProfile"
        VsanMaxDefaultProfile = "VsanMaxDefaultProfile"


class CapabilityBasedProfileCreateSpec(vmodl.DynamicData):
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def description(self) -> str: ...
    @description.setter
    def description(self, value: str):
        self._description = value
    @property
    def category(self) -> str: ...
    @category.setter
    def category(self, value: str):
        self._category = value
    @property
    def resourceType(self) -> ResourceType: ...
    @resourceType.setter
    def resourceType(self, value: ResourceType):
        self._resourceType = value
    @property
    def constraints(self) -> CapabilityConstraints: ...
    @constraints.setter
    def constraints(self, value: CapabilityConstraints):
        self._constraints = value


class CapabilityBasedProfileUpdateSpec(vmodl.DynamicData):
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def description(self) -> str: ...
    @description.setter
    def description(self, value: str):
        self._description = value
    @property
    def constraints(self) -> CapabilityConstraints: ...
    @constraints.setter
    def constraints(self, value: CapabilityConstraints):
        self._constraints = value


class CapabilityConstraints(vmodl.DynamicData): ...


class DataServiceToPoliciesMap(vmodl.DynamicData):
    @property
    def dataServicePolicy(self) -> ProfileId: ...
    @dataServicePolicy.setter
    def dataServicePolicy(self, value: ProfileId):
        self._dataServicePolicy = value
    @property
    def parentStoragePolicies(self) -> List[ProfileId]: ...
    @parentStoragePolicies.setter
    def parentStoragePolicies(self, value: List[ProfileId]):
        self._parentStoragePolicies = value
    @property
    def fault(self) -> vmodl.MethodFault: ...
    @fault.setter
    def fault(self, value: vmodl.MethodFault):
        self._fault = value


class DefaultCapabilityBasedProfile(CapabilityBasedProfile):
    @property
    def vvolType(self) -> List[str]: ...
    @vvolType.setter
    def vvolType(self, value: List[str]):
        self._vvolType = value
    @property
    def containerId(self) -> str: ...
    @containerId.setter
    def containerId(self, value: str):
        self._containerId = value


class DefaultProfileInfo(vmodl.DynamicData):
    @property
    def datastores(self) -> List[pbm.placement.PlacementHub]: ...
    @datastores.setter
    def datastores(self, value: List[pbm.placement.PlacementHub]):
        self._datastores = value
    @property
    def defaultProfile(self) -> Profile: ...
    @defaultProfile.setter
    def defaultProfile(self, value: Profile):
        self._defaultProfile = value


class Profile(vmodl.DynamicData):
    @property
    def profileId(self) -> ProfileId: ...
    @profileId.setter
    def profileId(self, value: ProfileId):
        self._profileId = value
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def description(self) -> str: ...
    @description.setter
    def description(self, value: str):
        self._description = value
    @property
    def creationTime(self) -> datetime: ...
    @creationTime.setter
    def creationTime(self, value: datetime):
        self._creationTime = value
    @property
    def createdBy(self) -> str: ...
    @createdBy.setter
    def createdBy(self, value: str):
        self._createdBy = value
    @property
    def lastUpdatedTime(self) -> datetime: ...
    @lastUpdatedTime.setter
    def lastUpdatedTime(self, value: datetime):
        self._lastUpdatedTime = value
    @property
    def lastUpdatedBy(self) -> str: ...
    @lastUpdatedBy.setter
    def lastUpdatedBy(self, value: str):
        self._lastUpdatedBy = value


class ProfileId(vmodl.DynamicData):
    @property
    def uniqueId(self) -> str: ...
    @uniqueId.setter
    def uniqueId(self, value: str):
        self._uniqueId = value


class ProfileOperationOutcome(vmodl.DynamicData):
    @property
    def profileId(self) -> ProfileId: ...
    @profileId.setter
    def profileId(self, value: ProfileId):
        self._profileId = value
    @property
    def fault(self) -> vmodl.MethodFault: ...
    @fault.setter
    def fault(self, value: vmodl.MethodFault):
        self._fault = value


class ProfileType(vmodl.DynamicData):
    @property
    def uniqueId(self) -> str: ...
    @uniqueId.setter
    def uniqueId(self, value: str):
        self._uniqueId = value


class QueryProfileResult(vmodl.DynamicData):
    @property
    def object(self) -> pbm.ServerObjectRef: ...
    @object.setter
    def object(self, value: pbm.ServerObjectRef):
        self._object = value
    @property
    def profileId(self) -> List[ProfileId]: ...
    @profileId.setter
    def profileId(self, value: List[ProfileId]):
        self._profileId = value
    @property
    def fault(self) -> vmodl.MethodFault: ...
    @fault.setter
    def fault(self, value: vmodl.MethodFault):
        self._fault = value


class ResourceType(vmodl.DynamicData):
    @property
    def resourceType(self) -> str: ...
    @resourceType.setter
    def resourceType(self, value: str):
        self._resourceType = value


class SubProfileCapabilityConstraints(CapabilityConstraints):
    @property
    def subProfiles(self) -> List[SubProfileCapabilityConstraints.SubProfile]: ...
    @subProfiles.setter
    def subProfiles(self, value: List[SubProfileCapabilityConstraints.SubProfile]):
        self._subProfiles = value


    class SubProfile(vmodl.DynamicData):
        @property
        def name(self) -> str: ...
        @name.setter
        def name(self, value: str):
            self._name = value
        @property
        def capability(self) -> List[pbm.capability.CapabilityInstance]: ...
        @capability.setter
        def capability(self, value: List[pbm.capability.CapabilityInstance]):
            self._capability = value
        @property
        def forceProvision(self) -> bool: ...
        @forceProvision.setter
        def forceProvision(self, value: bool):
            self._forceProvision = value


class AssociateAndApplyPolicyStatus():


    class PolicyStatus(Enum):
        success = "success"
        failed = "failed"
        invalid = "invalid"


class EntityAssociations():


    class Operation(Enum):
        CREATE = "CREATE"
        REGISTER = "REGISTER"
        RECONFIGURE = "RECONFIGURE"
        MIGRATE = "MIGRATE"
        CLONE = "CLONE"


class IofilterInfo():


    class FilterType(Enum):
        INSPECTION = "INSPECTION"
        COMPRESSION = "COMPRESSION"
        ENCRYPTION = "ENCRYPTION"
        REPLICATION = "REPLICATION"
        CACHE = "CACHE"
        DATAPROVIDER = "DATAPROVIDER"
        DATASTOREIOCONTROL = "DATASTOREIOCONTROL"


class PolicyAssociation():


    class VolumeAllocationType(Enum):
        FullyInitialized = "FullyInitialized"
        ReserveSpace = "ReserveSpace"
        ConserveSpaceWhenPossible = "ConserveSpaceWhenPossible"


class VmAssociations(): ...