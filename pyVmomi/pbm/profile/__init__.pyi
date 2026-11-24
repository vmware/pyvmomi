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



class Profile(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.pbm.profile.Profile` data object is the base object
   for storage capability profiles.
   
   This object defines metadata
   for the profile. The derived capability profile represents the
   user's intent for selection and configuration of storage resources
   and/or services that support deployment of virtual machines
   and virtual disks.
   
   Attributes:
       profileId: Unique identifier for the profile.
       description: Profile description.
       creationTime: Time stamp of profile creation.
       createdBy: User name of the profile creator.
           
           Set during creation time.
       lastUpdatedTime: Time stamp of latest modification to the profile.
       lastUpdatedBy: Name of the user performing the latest modification of the profile.
   """
   profileId: ProfileId
   name: str
   description: _typing.Optional[str] = None
   creationTime: _datetime.datetime
   createdBy: str
   lastUpdatedTime: _datetime.datetime
   lastUpdatedBy: str


class CapabilityBasedProfile(Profile):
   """
   The `pyVmomi.pbm.profile.CapabilityBasedProfile` data object defines
   capability-based profiles.
   
   A capability-based profile is derived
   from tag-based storage capabilities or from vSAN storage capabilities.
   
   Attributes:
       profileCategory: Indicates whether the profile is requirement
           profile, a resource profile or a data service profile.
           
           The `profileCategory`
           is a string value that corresponds to one of the
           `pyVmomi.pbm.profile.CapabilityBasedProfile.ProfileCategoryEnum` values.
           - REQUIREMENT profile - Defines the storage constraints applied
             to virtual machine placement. Requirements are defined by
             the user and can be associated with virtual machines and virtual
             disks. During provisioning, you can use a requirements profile
             for compliance and placement checking to support
             selection and configuration of resources.
           - RESOURCE profile - Specifies system-defined storage capabilities.
             You cannot modify a resource profile. You cannot associate a resource
             profile with vSphere entities, use it during provisioning, or target
             entities for resource selection or configuration.
             This type of profile gives the user visibility into the capabilities
             supported by the storage provider.
           - DATA_SERVICE_POLICY - Indicates a data service policy that can
             be embedded into another storage policy. Policies of this type can't
             be assigned to Virtual Machines or Virtual Disks. This policy cannot
             be used for compliance checking.
       resourceType: Type of the target resource to which the capability information applies.
           
           A fixed enum that defines resource types for which capabilities can be defined
           see `pyVmomi.pbm.profile.ResourceType`, `pyVmomi.pbm.profile.ResourceTypeEnum`
       constraints: Subprofiles that describe storage requirements or storage provider capabilities,
           depending on the profile category (REQUIREMENT or RESOURCE).
       generationId: Generation ID is used to communicate the current version of the profile to VASA
           providers.
           
           It is only applicable to REQUIREMENT profile types. Every time a
           requirement profile is edited, the Server will increment the generationId. You
           do not need to set the generationID. When an object is created (or
           reconfigured), the Server will send the requirement profile content, profile ID and
           the generationID to VASA provider.
       isDefault: Not supported in this release.
       systemCreatedProfileType: Indicates the type of system pre-created default profile.
           
           This will be set only for system pre-created default profiles. And
           this is not set for RESOURCE profiles.
       lineOfService: This property is set only for data service policy.
           
           Indicates the line of service
           `pyVmomi.pbm.capability.provider.LineOfServiceInfo.LineOfServiceEnum` of the data service policy.
       k8sCompliantName: Indicates compliant name to be used as K8s `StorageClass` name when this policy is used
           for K8s workloads.
           
           It essentially maps Storage Policy to corresponding `StorageClass`
           name across Supervisor clusters within a vCenter server.
           When this policy is assigned to a K8s `Namespace`, then a `StorageClass` with name
           `.K8sCompliantName` and optionally a WaitForFirstConsumer(WFFC) `StorageClass`
           with the name '`.K8sCompliantName`-latebinding' gets created. Duplicating both K8s
           compliant name and latebinding K8s compliant name across storage profiles in a vCenter is not
           allowed, i.e. it shouldn't match with `pyVmomi.pbm.profile.CapabilityBasedProfile.k8sCompliantName` and
           `pyVmomi.pbm.profile.CapabilityBasedProfile.otherK8sCompliantNames` of any other profile.
           Once the value for this field is set, it can't be changed. This name is RFC 1123 compliant.
           For new storage policy being created, compliant name will automatically be generated and
           populated based on policy name if it's not provided in the profile createSpec.
           For pre-existing storage policies in the Brownfield setup, K8s compliant name would be set
           during the vCenter upgrade.
       otherK8sCompliantNames: Indicates the reserved K8s compliant names other than `pyVmomi.pbm.profile.CapabilityBasedProfile.k8sCompliantName` for a profile.
           
           These names shouldn't be used as a K8s `StorageClass`'s name associated with any other
           profiles.
           Note that, it doesn't indicate that `StorageClass` with following names actually exists,
           i.e. it's not a profile->K8s `StorageClass` association data. These are used to keep
           track of all the reserved K8s compliant names which can't be used for any other profile and
           used to avoid any K8s compliant name collision when a profile is being created.
           It can include the following:
           1\\. K8s compliant name to be used for a WaitForFirstConsumer(WFFC) `StorageClass` which
           is in the format '`pyVmomi.pbm.profile.CapabilityBasedProfile.k8sCompliantName`-latebinding'.
           2\\. Name of all the `StorageClass`s except the one set in `pyVmomi.pbm.profile.CapabilityBasedProfile.k8sCompliantName` if
           it's a Brownfield profile associated with multiple K8s `StorageClass`s.
           For a new storage policy being created, WFFC `StorageClass` name is automatically
           generated and populated here. So a newly created profile will always have
           '`pyVmomi.pbm.profile.CapabilityBasedProfile.k8sCompliantName` -latebinding' as a `pyVmomi.pbm.profile.CapabilityBasedProfile.otherK8sCompliantNames`. Whereas for
           a Brownfield profile, WFFC `StorageClass` name is reserved only if it's not already
           taken by a different profile.
   """
   class ProfileCategoryEnum(pyVmomi.VmomiSupport.Enum):
      """
      The `pyVmomi.pbm.profile.CapabilityBasedProfile.ProfileCategoryEnum`
      enumerated type defines the profile categories for a capability-based
      storage profile.
      
      See
      `pyVmomi.pbm.profile.CapabilityBasedProfile`.
      
      Attributes:
          REQUIREMENT: Indicates a storage requirement.
              
              Requirements are based on
              storage capabilities.
          RESOURCE: Indicates a storage capability.
              
              Storage capabilities
              are defined by storage providers.
          DATA_SERVICE_POLICY: Indicates a data service policy that can be embedded into
              another storage policy.
              
              Policies of this type can't be assigned to
              Virtual Machines or Virtual Disks.
      """
      REQUIREMENT: _typing.ClassVar['CapabilityBasedProfile.ProfileCategoryEnum'] = 'REQUIREMENT'
      RESOURCE: _typing.ClassVar['CapabilityBasedProfile.ProfileCategoryEnum'] = 'RESOURCE'
      DATA_SERVICE_POLICY: _typing.ClassVar['CapabilityBasedProfile.ProfileCategoryEnum'] = 'DATA_SERVICE_POLICY'

   class SystemCreatedProfileType(pyVmomi.VmomiSupport.Enum):
      """
      System pre-created profile types.
      
      Attributes:
          VsanDefaultProfile: Indicates the system pre-created editable VSAN default profile.
          VVolDefaultProfile: Indicates the system pre-created non-editable default profile
              for VVOL datastores.
          PmemDefaultProfile: Indicates the system pre-created non-editable default profile
              for PMem datastores
          VmcManagementProfile: Indicates the system pre-created non-editable VMC default profile.
          VsanMaxDefaultProfile: Indicates the system pre-created non-editable VSANMAX default profile.
          VsanEsaAutoManagedRaidProfile: Indicates the new system pre-created non-editable vSAN ESA default
              profile.
      """
      VsanDefaultProfile: _typing.ClassVar['CapabilityBasedProfile.SystemCreatedProfileType'] = 'VsanDefaultProfile'
      VVolDefaultProfile: _typing.ClassVar['CapabilityBasedProfile.SystemCreatedProfileType'] = 'VVolDefaultProfile'
      PmemDefaultProfile: _typing.ClassVar['CapabilityBasedProfile.SystemCreatedProfileType'] = 'PmemDefaultProfile'
      VmcManagementProfile: _typing.ClassVar['CapabilityBasedProfile.SystemCreatedProfileType'] = 'VmcManagementProfile'
      VsanMaxDefaultProfile: _typing.ClassVar['CapabilityBasedProfile.SystemCreatedProfileType'] = 'VsanMaxDefaultProfile'
      VsanEsaAutoManagedRaidProfile: _typing.ClassVar['CapabilityBasedProfile.SystemCreatedProfileType'] = 'VsanEsaAutoManagedRaidProfile'

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
   """
   The `pyVmomi.pbm.profile.CapabilityBasedProfileCreateSpec` describes storage requirements.
   
   Use this data object to create a `pyVmomi.pbm.profile.CapabilityBasedProfile`.
   
   Attributes:
       name: Name of the capability based profile to be created.
           
           The maximum length of the name is 80 characters.
       description: Text description associated with the profile.
       category: Category specifies the type of policy to be created.
           
           This can be REQUIREMENT from
           `pyVmomi.pbm.profile.CapabilityBasedProfile.ProfileCategoryEnum`
           or null when creating a storage policy. And it can be DATA_SERVICE_POLICY from
           `pyVmomi.pbm.profile.CapabilityBasedProfile.ProfileCategoryEnum`
           when creating a data service policy. RESOURCE from `pyVmomi.pbm.profile.CapabilityBasedProfile.ProfileCategoryEnum`
           is not allowed as resource profile is created by the system.
       resourceType: Specifies the type of resource to which the profile applies.
           
           The only legal value is STORAGE - deprecated.
       constraints: Set of subprofiles that define the storage requirements.
           
           A subprofile corresponds to a rule set in the vSphere Web Client.
       k8sCompliantName: Indicates compliant name to be used as K8s `StorageClass` name when this policy is used
           for K8s workloads.
           
           If compliant name is specified, and it's not RFC 1123 compliant, then
           policy creation would fail.
           Duplicating the compliant name across storage profiles in a vCenter is not allowed. If either
           there is already a K8s `StorageClass` with this name or WaitForForFirstConsumer
           `StorageClass` with the name '`pyVmomi.pbm.profile.CapabilityBasedProfileCreateSpec.k8sCompliantName`-latebinding', then the policy
           creation would fail.
           Compliant name will automatically be generated and populated based on policy name if it's not
           provided.
   """
   name: str
   description: _typing.Optional[str] = None
   category: _typing.Optional[str] = None
   resourceType: ResourceType
   constraints: CapabilityConstraints
   k8sCompliantName: _typing.Optional[str] = None


class CapabilityBasedProfileUpdateSpec(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.pbm.profile.CapabilityBasedProfileUpdateSpec` data object
   contains data that you use to update a storage profile.
   
   Attributes:
       name: Specifies a new profile name.
       description: Specifies a new profile description.
       constraints: Specifies one or more subprofiles.
           
           A subprofile defines one or more
           storage requirements.
   """
   name: _typing.Optional[str] = None
   description: _typing.Optional[str] = None
   constraints: _typing.Optional[CapabilityConstraints] = None


class CapabilityConstraints(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.pbm.profile.CapabilityConstraints` data object is the base
   object for capability subprofile constraints.
   """
   pass


class DataServiceToPoliciesMap(pyVmomi.vmodl.DynamicData):
   """
   DataServiceToProfilesMap maps the data service policy to the parent storage policies
   if referred.
   
   This is returned from the API call
   `ProfileManager#queryParentStoragePolicies(ProfileId[])`
   
   Attributes:
       dataServicePolicy: Denotes a Data Service Policy Id.
       parentStoragePolicies: Storage Policies that refer to the Data Service Policy given by
           `pyVmomi.pbm.profile.DataServiceToPoliciesMap.dataServicePolicy`.
       fault: The fault is set in case of error conditions and this property will
           have the reason.
   """
   dataServicePolicy: ProfileId
   parentStoragePolicies: list[ProfileId] = []
   fault: _typing.Optional[pyVmomi.vmodl.MethodFault] = None

class DefaultCapabilityBasedProfile(CapabilityBasedProfile):
   """
   Not supported in this release.
   
   Attributes:
       vvolType: Not supported in this release.
       containerId: Not supported in this release.
   """
   vvolType: list[str] = []
   containerId: str


class DefaultProfileInfo(pyVmomi.vmodl.DynamicData):
   """
   Data structure that stores the default profile for datastores.
   
   Attributes:
       datastores: Datastores
       defaultProfile: Default requirements profile.
           
           It is set to null if the datastores are not associated with any default profile.
       methodFault: NoPermission fault if default profile is not permitted.
   """
   datastores: list[pyVmomi.pbm.placement.PlacementHub] = []
   defaultProfile: _typing.Optional[Profile] = None
   methodFault: _typing.Optional[pyVmomi.vmodl.MethodFault] = None


class ProfileId(pyVmomi.vmodl.DynamicData):
   """
   Profile unique identifier.
   
   Attributes:
       uniqueId: Unique identifier of the profile.
   """
   uniqueId: str


class ProfileK8sCompliantNameSpec(pyVmomi.vmodl.DynamicData):
   """
   The data object defines the K8s compliant name(s) for a Storage Profile.
   
   Attributes:
       profileId: Profile unique identifier
       k8sCompliantName: K8s compliant name matching `CapabilityBasedProfile.k8sCompliantName`.
       otherK8sCompliantNames: Other K8s compliant names for a profile matching
           `CapabilityBasedProfile.otherK8sCompliantNames`.
           
           These are mutually exclusive with
           `pyVmomi.pbm.profile.ProfileK8sCompliantNameSpec.k8sCompliantName`.
   """
   profileId: str
   k8sCompliantName: str
   otherK8sCompliantNames: list[str] = []


class ProfileManager(pyVmomi.VmomiSupport.ManagedObject):
   """
   The `pyVmomi.pbm.profile.ProfileManager` supports operations on virtual machine storage profiles.
   
   A Storage Policy API profile consists of a set of subprofiles.
   A subprofile corresponds to a rule set in the vSphere Web Client.
   
   Virtual machine storage profiles specify the storage requirements
   for virtual machine files. You use the vSphere Web Client to define virtual machine
   storage profiles. The requirements
   (`pyVmomi.pbm.profile.CapabilityBasedProfile`.`pyVmomi.pbm.profile.CapabilityBasedProfile.constraints`)
   impose constraints on the placement of virtual machine files.
   
   The Storage Policy Server also supports datastore profiles. Datastore profiles
   define storage capabilities. Storage capabilities are resources defined by
   storage providers. Storage requirements are based on storage capabilities.
   When you associate a storage profile with a virtual machine or virtual disk,
   the Server sends the profile to the storage provider. When you perform compliance
   checking (`pyVmomi.pbm.compliance.ComplianceManager`), the storage provider
   compares the requirements with the capabilities.
   
   The `pyVmomi.pbm.profile.ProfileManager` supports the following operations on
   virtual machine storage profiles.
   - Create, update, and delete storage profiles.
   - Retrieve profile data based on specified criteria.
   - Retrieve storage vendor data.
     
   The following figure shows the set of data objects that comprise
   a storage profile specification (`pyVmomi.pbm.profile.CapabilityBasedProfileCreateSpec`).
   You pass a storage profile specification to the Storage Policy Server
   when you call the following methods:
   - `pyVmomi.pbm.profile.ProfileManager`.`pyVmomi.pbm.profile.ProfileManager.create`
   - `pyVmomi.pbm.placement.PlacementSolver`.`pyVmomi.pbm.placement.PlacementSolver.checkCompatibilityWithSpec`
   - `pyVmomi.pbm.placement.PlacementSolver`.`pyVmomi.pbm.placement.PlacementSolver.queryMatchingHubWithSpec`
   <!-- -->
        +---------------------------------+
        |  PbmCapabilityProfileCreateSpec |
        |                            name |     +-------------------------+
        |                     description |     |  PbmProfileResourceType |
        |                    resourceType ------|    resourceType=STORAGE |
        |                     constraints ---   +-------------------------+
        +---------------------------------+ |
                                            |
                                            |
               +------------------------------------+
               | PbmCapabilitySubProfileConstraints |
               |                        subprofiles ---
               +------------------------------------+ |
                                                      | 1..n
                                                      |
                                 +-------------------------+
                                 | PbmCapabilitySubProfile |
                                 |                    name |
                                 |          forceProvision |
                                 |              capability ---
                                 +-------------------------+ |
                                                             | 1..n            +-------------------------------+
                                                             |                 | PbmCapabilityMetadataUniqueId |
                                           +-----------------------+           |                            id |
                                           | PbmCapabilityInstance |           |                     namespace |
                                           |                    id ------------+-------------------------------+
                                           |            constraint ---
                                           +-----------------------+ |
                                                                     | 1..n
                                                                     |                +-------------------------------+
                                          +---------------------------------+         | PbmCapabilityPropertyInstance |
                                          | PbmCapabilityConstraintInstance |  1..n   |                            id |
                                          |                propertyInstance ----------|                         value |
                                          +---------------------------------+         +-------------------------------+
   """
   def FetchResourceType(self) -> list[ResourceType]:
      """
      Retrieves information about various resource types registered with the system.
      
      Returns:
          Array of resource types.
      """
      ...
   def FetchVendorInfo(self, resourceType: _typing.Optional[ResourceType]) -> list[pyVmomi.pbm.capability.provider.CapabilityObjectSchema.VendorResourceTypeInfo]:
      """
      Retrieve information about various capability metadata owners/vendors
      registered with the system, the resource type for which they are registered,
      and schema namespaces to which they belong.
      
      Args:
          resourceType: Specifies the resource type. The Server supports the STORAGE resource
              type only. If not specified, server defaults to STORAGE resource type. Any other
              `resourceType` is considered invalid.
      
      Returns:
          Vendor and namespace information.
      """
      ...
   def FetchCapabilityMetadata(self, resourceType: _typing.Optional[ResourceType], vendorUuid: _typing.Optional[str]) -> list[pyVmomi.pbm.capability.provider.CapabilityObjectMetadataPerCategory]:
      """
      Retrieves capability metadata.
      
      Each capability metadata object has a unique identifier
      (`pyVmomi.pbm.capability.CapabilityMetadata`.`pyVmomi.pbm.capability.CapabilityMetadata.id`).
      The identifier object (`pyVmomi.pbm.capability.CapabilityMetadata.UniqueId`)
      contains the unique ID and it identifies the namespace to which
      the capability metadata object belongs.
      
      Each registered namespace is required to be globally unique.
      You can associate a capability metadata object with a unique vendor and
      resource type by using the namespace and the
      `pyVmomi.pbm.capability.provider.CapabilityObjectSchema.VendorResourceTypeInfo`
      data returned by the `pyVmomi.pbm.profile.ProfileManager.fetchVendorInfo` method.
      
      Args:
          resourceType: Type of profile resource. The Server supports the \"STORAGE\" resource
              type only. If not specified, this method will return capability metadata for the storage
              resources. Any other `resourceType` is considered invalid.
          vendorUuid: Unique identifier for the vendor/owner of capability
              metadata. The specified vendor ID must match
              `pyVmomi.pbm.capability.provider.CapabilityObjectSchema.VendorInfo`.`pyVmomi.pbm.capability.provider.CapabilityObjectSchema.VendorInfo.vendorUuid`.
              If omitted, the Server searches all capability metadata registered with the system. If a
              `vendorUuid` unknown to the Server is specified, empty results will be returned.
      
      Returns:
          Array of capability metadata objects, classified by category
          (`pyVmomi.pbm.capability.provider.CapabilityObjectMetadataPerCategory`.`pyVmomi.pbm.capability.provider.CapabilityObjectMetadataPerCategory.subCategory`).
      """
      ...
   def FetchCapabilitySchema(self, vendorUuid: _typing.Optional[str], lineOfService: list[str]) -> list[pyVmomi.pbm.capability.provider.CapabilityObjectSchema]:
      """
      Returns the capability schema objects registered in the system.
      
      Args:
          vendorUuid: Unique identifier for the vendor/owner of capability metadata.
              If omitted, the server searches all capability metadata registered
              with the system. The specified vendor ID must match
              `pyVmomi.pbm.capability.provider.CapabilityObjectSchema.VendorInfo`.`pyVmomi.pbm.capability.provider.CapabilityObjectSchema.VendorInfo.vendorUuid`.
          lineOfService: Optional line of service that must match `pyVmomi.pbm.capability.provider.LineOfServiceInfo.LineOfServiceEnum`.
              If specified, the capability schema objects
              are returned for the given lineOfServices. If null, then all
              capability schema objects that may or may not have data service capabilities
              are returned.
      
      Returns:
          Array of `pyVmomi.pbm.capability.provider.CapabilityObjectSchema`
      
      Raises:
          pyVmomi.pbm.fault.PBMFault: If there is an internal server error.
      """
      ...
   def Create(self, createSpec: CapabilityBasedProfileCreateSpec) -> ProfileId:
      """
      Creates a capability-based storage profile.
      
      A capability-based profile
      contains requirements that are derived from tag-defined capabilities
      or from VMware VSAN capabilities.
      - Use the vSphere Web Client to define tags for capabilities.
      - VSAN storage capabilities are system-defined.
        
      A profile is a collection of subprofiles
      (`pyVmomi.pbm.profile.SubProfileCapabilityConstraints.SubProfile`).
      A subprofile references storage capabilities and defines requirements
      based on those capabilities.
      
      To define a storage requirement, you specify constraint property instance values
      (`pyVmomi.pbm.capability.PropertyInstance`) that use Storage Policy API builtin
      types (`pyVmomi.pbm.capability.types.BuiltinTypesEnum`) to create expressions
      for compliance checking.
      
      The profile specification contains lists of constraint property instances
      (`pyVmomi.pbm.profile.CapabilityBasedProfileCreateSpec`.`pyVmomi.pbm.profile.CapabilityBasedProfileCreateSpec.constraints`.`pyVmomi.pbm.profile.SubProfileCapabilityConstraints.subProfiles`[].`pyVmomi.pbm.profile.SubProfileCapabilityConstraints.SubProfile.capability`[].`pyVmomi.pbm.capability.CapabilityInstance.constraint`[].`pyVmomi.pbm.capability.ConstraintInstance.propertyInstance`[]).
      The constraints are based on storage capabilities described in metadata
      (`pyVmomi.pbm.capability.PropertyMetadata`) and in the datastore profiles.
      
      Args:
          createSpec: Capability-based profile specification.
      
      Returns:
          Identifier for the new profile.
      
      Raises:
          pyVmomi.vmodl.fault.InvalidArgument: if
              `pyVmomi.pbm.profile.CapabilityBasedProfileCreateSpec` is invalid.
          pyVmomi.pbm.fault.ProfileStorageFault: if there is an error in persisting the profile.
          pyVmomi.pbm.fault.DuplicateName: if a profile with the same name or K8s compliant name already exists.
      """
      ...
   def Update(self, profileId: ProfileId, updateSpec: CapabilityBasedProfileUpdateSpec) -> None:
      """
      Updates a storage profile.
      
      Args:
          profileId: Profile identifier.
          updateSpec: Capability-based update specification.
      
      Raises:
          pyVmomi.vmodl.fault.InvalidArgument: if the Server does not recognize `pyVmomi.pbm.profile.ProfileId`.
          pyVmomi.pbm.fault.ProfileStorageFault: in case of internal service error.
      """
      ...
   def Delete(self, profileId: list[ProfileId]) -> list[ProfileOperationOutcome]:
      """
      Deletes one or more profiles.
      
      If the method successfully deletes a
      profile, its identifier is no longer valid.
      
      Args:
          profileId: Array of profile identifiers.
      
      Returns:
          Array of result objects, one for each profile specified in the
          call to the `PbmDelete` method.
          
          The result object contains the profile ID and, if an error
          occurred, it also describes the fault. The method can return one
          of the following faults if the profile cannot be deleted:
          - `pyVmomi.vmodl.fault.InvalidArgument` - Profile is not
            recognized by the system.
          - `pyVmomi.pbm.fault.ProfileStorageFault` - Internal service
            error.
          - `pyVmomi.pbm.fault.ResourceInUse` - Profile is still associated
            with an entity.
      """
      ...
   def QueryProfile(self, resourceType: ResourceType, profileCategory: _typing.Optional[str]) -> list[ProfileId]:
      """
      Returns requirement profile ids or resource profile ids, or both.
      
      Args:
          resourceType: Type of resource. You can specify only STORAGE.
          profileCategory: Profile category. The string value must correspond
              to one of the `pyVmomi.pbm.profile.CapabilityBasedProfile.ProfileCategoryEnum` values.
              If you do not specify a profile category, the method returns profiles in all
              categories.
      
      Returns:
          Array of storage profile identifiers.
      
      Raises:
          pyVmomi.vmodl.fault.InvalidArgument: if the Server does not recognize the specified
              resourceType or profileCategory.
      """
      ...
   def RetrieveContent(self, profileIds: list[ProfileId]) -> list[Profile]:
      """
      Returns one or more storage profiles.
      
      Args:
          profileIds: Array of storage profile identifiers.
      
      Returns:
          Array of storage profiles.
      
      Raises:
          pyVmomi.vmodl.fault.InvalidArgument: if the Server does not recognize any of the profileIds.
      """
      ...
   def QueryAssociatedProfiles(self, entities: list[pyVmomi.pbm.ServerObjectRef]) -> list[QueryProfileResult]:
      """
      Returns profiles associated with the specified entities.
      
      Args:
          entities: Array of server object references.
      
      Returns:
          Array of query result objects. Each `pyVmomi.pbm.profile.QueryProfileResult`
          object identifies a virtual machine, virtual disk, or datastore
          and it contains a list of the profiles associated with that entity.
          It also describes the fault, if there is an error associated
          with one of the profiles.
      
      Raises:
          pyVmomi.pbm.fault.PBMFault: If there is an internal server error.
      """
      ...
   def QueryAssociatedProfile(self, entity: pyVmomi.pbm.ServerObjectRef) -> list[ProfileId]:
      """
      Returns identifiers for profiles associated with a virtual machine,
      virtual disk, or datastore.
      
      Args:
          entity: Reference to a virtual machine, virtual disk, or datastore.
      
      Returns:
          Array of profiles associated with the entity.
      
      Raises:
          pyVmomi.pbm.fault.PBMFault: If there is an internal server error.
      """
      ...
   def QueryAssociatedEntity(self, profile: ProfileId, entityType: _typing.Optional[str]) -> list[pyVmomi.pbm.ServerObjectRef]:
      """
      Retrieves entities associated with the specified profile.
      
      Args:
          profile: Profile identifier.
          entityType: If specified, the method returns only those entities
              which match the type. The `entityType` string value must match
              one of the `pyVmomi.pbm.ServerObjectRef.ObjectType` values.
              If not specified, the method returns all entities associated with the profile.
      
      Returns:
          Array of entities associated with the profile.
      
      Raises:
          pyVmomi.pbm.fault.PBMFault: If there is an internal server error.
      """
      ...
   def QueryDefaultRequirementProfile(self, hub: pyVmomi.pbm.placement.PlacementHub) -> _typing.Optional[ProfileId]:
      """
      Returns the default requirement profile ID for the given datastore.
      
      For
      legacy hub the API returns `null`.
      
      Args:
          hub: Placement hub (i.e. datastore).
      
      Returns:
          Profile Id of the Default Requirement Profile. For legacy hub the
          API returns `null`.
      
      Raises:
          pyVmomi.vmodl.fault.InvalidArgument: If hub is invalid (does not denote a datastore).
          pyVmomi.pbm.fault.NonExistentHubs: If hub is non existent.
          pyVmomi.pbm.fault.PBMFault: Internal service error.
      """
      ...
   def ResetDefaultRequirementProfile(self, profile: _typing.Optional[ProfileId]) -> None:
      """
      Deprecated: since it is not supported.Not supported in this release.
      
      Args:
          profile: Profile to reset.
      """
      ...
   def AssignDefaultRequirementProfile(self, profile: ProfileId, datastores: list[pyVmomi.pbm.placement.PlacementHub]) -> None:
      """
      Assign the given profile as the default profile for the given datastores.
      
      This is an atomic operation. Either all the datastores will be assigned
      the default profile or none will be.
      In addition to StorageProfile.Update privilege, it requires
      Datastore.UpdateVirtualMachineFiles privilege on the given datastores to
      change the default profile for the datastores. Otherwise a NoPermission
      fault is thrown.
      
      Args:
          profile: The profile that needs to be made default profile.
          datastores: The datastores for which the profile needs to be made as default profile.
      
      Raises:
          pyVmomi.vmodl.fault.InvalidArgument: If one of the hub is not a datastore or profile cannot be
              used as default requirement profile for any of the hub.
          pyVmomi.pbm.fault.LegacyHubsNotSupported: If any of the hub in datastores argument is legacy (VMFS
              or NFS) datastores.
          pyVmomi.pbm.fault.NonExistentHubs: If any of the hub in datastores argument is non existent.
          pyVmomi.pbm.fault.PBMFault: Internal service error
      """
      ...
   def FindApplicableDefaultProfile(self, datastores: list[pyVmomi.pbm.placement.PlacementHub]) -> list[Profile]:
      """
      Returns the profiles that can be made as default profile for all the given datastores.
      
      A profile can be made as a default profile for a datastore only if it contains a ruleset
      from the namespace the datastore belongs to.
      
      Args:
          datastores: Datastores for which the default profile is found out. Note that
              the datastore pods/clusters are not supported.
      
      Returns:
          Profile[]
          Returns all the requirements profiles that can be made as default profile for the given datastores.
          If no profile can be made as default for all datastores, then an empty array is returned.
          Note that the profiles returned may or may not be compatible with the datastores.
      
      Raises:
          pyVmomi.pbm.fault.LegacyHubsNotSupported: If any of the hubs in datastores argument are legacy (VMFS or NFS) datastores.
          pyVmomi.pbm.fault.NonExistentHubs: If any of the hubs in datastores argument are non existent.
          pyVmomi.pbm.fault.PBMFault: Internal service error.
          pyVmomi.vmodl.fault.InvalidArgument: If the datastores argument contains a non-datastore, example storage pod.
      """
      ...
   def QueryDefaultRequirementProfiles(self, datastores: list[pyVmomi.pbm.placement.PlacementHub]) -> list[DefaultProfileInfo]:
      """
      Returns the default profiles for the given datastores.
      
      For legacy
      datastores we set `DefaultProfileInfo.defaultProfile` to
      `null`.
      
      Args:
          datastores: The datastores for which the default profiles are requested. For
              legacy datastores we set
              `DefaultProfileInfo.defaultProfile` to `null`.
      
      Returns:
          DefaultProfileInfo Default profile information.
      
      Raises:
          pyVmomi.vmodl.fault.InvalidArgument: If one of the datastore is invalid (does not denote a
              datastore).
          pyVmomi.pbm.fault.NonExistentHubs: If any of the datastore in datastores argument are non
              existent.
          pyVmomi.pbm.fault.PBMFault: Internal service error.
      """
      ...
   def ResetVSanDefaultProfile(self) -> None:
      """Resets the system pre-created VSAN default profile to factory defaults."""
      ...
   def QuerySpaceStatsForStorageContainer(self, datastore: pyVmomi.pbm.ServerObjectRef, capabilityProfileId: list[ProfileId]) -> list[pyVmomi.pbm.profile.provider.DatastoreSpaceStatistics]:
      """
      Retrieves space statistics of a datastore.
      
      Args:
          datastore: Entity for which space statistics are being requested i.e datastore.
          capabilityProfileId: \\- capability profile Ids.
              If omitted, the statistics for the container
              as a whole would be returned.
      
      Returns:
          Array of Space stats of datastore for each capabilityProfileId.
      
      Raises:
          pyVmomi.vmodl.fault.InvalidArgument: \\- Thrown if the input datastore parameter is null
              or its type is not datastore or its key is empty.
          pyVmomi.pbm.fault.PBMFault: \\- Thrown if server internal error occurred or
              if storage container does not support the profile.
      """
      ...
   def QueryAssociatedEntities(self, profiles: list[ProfileId]) -> list[QueryProfileResult]:
      """
      Returns the virtual machine and disks that are associated with the given
      storage policies.
      
      If the profiles parameter is empty, then this API returns
      all the virtual machine and disks that are associated with some storage
      policy.
      
      Args:
          profiles: Storage policy array.
      
      Returns:
          Array of QueryProfileResult
      
      Raises:
          pyVmomi.pbm.fault.PBMFault: If there is an internal service error.
      """
      ...


class ProfileOperationOutcome(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.pbm.profile.ProfileOperationOutcome` data object describes the result
   of a `pyVmomi.pbm.profile.ProfileManager` operation.
   
   If there was an
   error during the operation, the object identifies the fault.
   
   Attributes:
       profileId: Identifies the profile specified for the operation.
       fault: One of the `pyVmomi.pbm.fault.PBMFault` objects.
   """
   profileId: ProfileId
   fault: _typing.Optional[pyVmomi.vmodl.MethodFault] = None


class ProfileType(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.pbm.profile.ProfileType` identifier is defined by storage providers
   to distinguish between different types of profiles plugged into the system.
   
   An example of a system supported profile type is \"CapabilityBasedProfileType\"
   which will be the type used for all capability-based profiles created by
   the system using capability metadata information published to the system.
   
   For internal use only.
   
   Attributes:
       uniqueId: Unique type identifier for this profile type.
           
           eg \"CapabilityBased\", or other.
   """
   uniqueId: str


class QueryProfileResult(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.pbm.profile.QueryProfileResult` data object
   identifies a virtual machine, virtual disk, or datastore
   and it lists the identifier(s) for the associated profile(s).
   
   Attributes:
       object: Reference to the virtual machine, virtual disk, or
           datastore on which the query was performed.
       profileId: Array of identifiers for profiles which are associated with `object`.
       fault: Fault associated with the query, if there is one.
   """
   object: pyVmomi.pbm.ServerObjectRef
   profileId: list[ProfileId] = []
   fault: _typing.Optional[pyVmomi.vmodl.MethodFault] = None


class ResourceType(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.pbm.profile.ResourceType` data object defines the vSphere resource type
   that is supported for profile management.
   
   Attributes:
       resourceType: Type of resource to which capability information applies.
           
           `resourceType` is a string value that corresponds to
           a `pyVmomi.pbm.profile.ResourceTypeEnum` enumeration value.
           Only the STORAGE resource type is supported.
   """
   resourceType: str

class ResourceTypeEnum:
   """
   The `pyVmomi.pbm.profile.ResourceTypeEnum` enumerated type defines the set of resource
   types that are supported for profile management.
   
   See `pyVmomi.pbm.profile.ResourceType`.
   """
   pass


class SubProfileCapabilityConstraints(CapabilityConstraints):
   """
   The `pyVmomi.pbm.profile.SubProfileCapabilityConstraints` data object defines a group
   of storage subprofiles.
   
   Subprofile usage depends on the type of profile
   (`pyVmomi.pbm.profile.CapabilityBasedProfile`.`pyVmomi.pbm.profile.CapabilityBasedProfile.profileCategory`).
   - For a REQUIREMENTS profile, each subprofile defines storage requirements.
     A Storage Policy API requirements subprofile corresponds to a vSphere Web Client
     rule set.
   - For a RESOURCE profile, each subprofile defines storage capabilities.
     Storage capabilities are read-only.
   
   Attributes:
       subProfiles: Aggregation of one or more subprofiles.
           
           The relationship among all subprofiles is \"OR\". When you perform
           compliance checking on a profile that contains more than one subprofile,
           a non-compliant result for any one of the subprofiles will produce a
           non-compliant result for the operation.
   """
   class SubProfile(pyVmomi.vmodl.DynamicData):
      """
      A `pyVmomi.pbm.profile.SubProfileCapabilityConstraints.SubProfile`
      is a section within a profile that aggregates one or more capability
      instances.
      
      Capability instances define storage constraints.
      
      All constraints within a subprofile are ANDed by default.
      When you perform compliance checking on a virtual machine or virtual
      disk, all of the constraints must be satisfied by the storage capabilities.
      
      Attributes:
          name: Subprofile name.
          capability: List of capability instances.
          forceProvision: Indicates whether the source policy profile allows creating a virtual machine
              or virtual disk that may be non-compliant.
      """
      name: str
      capability: list[pyVmomi.pbm.capability.CapabilityInstance] = []
      forceProvision: _typing.Optional[bool] = None

   subProfiles: list[SubProfileCapabilityConstraints.SubProfile] = []
