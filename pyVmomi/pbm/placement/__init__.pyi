# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.pbm
import pyVmomi.vmodl
import pyVmomi.pbm.profile
import pyVmomi.vim.vm.replication



class Requirement(pyVmomi.vmodl.DynamicData):
   """Defines a constraint for placing objects onto `pyVmomi.pbm.placement.PlacementHub`s."""
   pass


class CapabilityConstraintsRequirement(Requirement):
   """
   Requirement type containing capability constraints
   
   Attributes:
       constraints: Capability constraints
   """
   constraints: pyVmomi.pbm.profile.CapabilityConstraints


class CapabilityProfileRequirement(Requirement):
   """
   A Requirement for a particular `pyVmomi.pbm.profile.CapabilityBasedProfile`.
   
   Attributes:
       profileId: Reference to the capability profile being used as a requirement
   """
   profileId: pyVmomi.pbm.profile.ProfileId


class CompatibilityResult(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.pbm.placement.CompatibilityResult` data object
   contains the compatibility result of a placement request.
   
   Attributes:
       hub: The `Datastore` or `StoragePod` under consideration
           as a location for virtual machine files.
       hubInfo: Additional information about `pyVmomi.pbm.placement.CompatibilityResult.hub`
       matchingResources: Resources that match the policy.
           
           If populated, signifies that there are
           specific resources that match the policy for `pyVmomi.pbm.placement.CompatibilityResult.hub`. If null,
           signifies that all resources (for example, hosts connected to the
           datastore or storage pod) are compatible.
       howMany: How many objects of the kind requested can be provisioned on this
           `pyVmomi.pbm.placement.CompatibilityResult.hub`.
       utilization: This field is not populated if there is no size in the query, i.e.
           
           if the request carries only policy and no size requirements, this
           will not be populated.
       warning: Array of faults that describe issues that may affect profile compatibility.
           
           Users should consider these issues before using this `Datastore`
           or `StoragePod` and a connected `Host`s.
       error: Array of faults that prevent this datastore or storage pod from being compatible with the
           specified profile, including if no host connected to this `pyVmomi.pbm.placement.CompatibilityResult.hub` is compatible.
   """
   hub: PlacementHub
   hubInfo: _typing.Optional[PlacementHubInfo] = None
   matchingResources: list[MatchingResources] = []
   howMany: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   utilization: list[ResourceUtilization] = []
   warning: list[pyVmomi.vmodl.MethodFault] = []
   error: list[pyVmomi.vmodl.MethodFault] = []


class MatchingResources(pyVmomi.vmodl.DynamicData):
   """
   Describes the collection of resources (for example, hosts) that satisfy a
   policy, for a specific datastore.
   """
   pass


class MatchingReplicationResources(MatchingResources):
   """
   Describes the collection of replication related resources that satisfy a
   policy, for a specific datastore.
   
   This class is returned only when the policy contains replication capabilities.
   For a storage pod, only those replication groups that are common across
   all datastores in the storage pod are considered compatible.
   
   Attributes:
       replicationGroup: Replication groups that match the policy.
   """
   replicationGroup: list[pyVmomi.vim.vm.replication.ReplicationGroupId] = []


class PlacementHub(pyVmomi.vmodl.DynamicData):
   """
   A `pyVmomi.pbm.placement.PlacementHub` data object identifies a storage location
   where virtual machine files can be placed.
   
   Attributes:
       hubType: Type of the hub.
           
           Currently ManagedObject is the only supported type.
       hubId: Hub identifier; a ManagedObjectReference to a datastore or a storage pod.
   """
   hubType: str
   hubId: str


class PlacementHubInfo(pyVmomi.vmodl.DynamicData):
   """
   Data object to specify additional information related to a `pyVmomi.pbm.placement.PlacementHub`.
   
   Attributes:
       zoneClusters: Indicates `pyVmomi.pbm.ServerObjectRef` of cluster(s) on which a compatible datastore is mounted
           fully on, when compatibility check is invoked with `pyVmomi.pbm.placement.ZoneTopologyRequirement` as input.
           
           Only those clusters which are part of vSphere `AvailabilityZone` are populated here.
   """
   zoneClusters: list[pyVmomi.pbm.ServerObjectRef] = []


class PlacementSolver(pyVmomi.VmomiSupport.ManagedObject):
   """
   The `pyVmomi.pbm.placement.PlacementSolver` data object provides methods to identify
   placement hubs that support the capabilities to store virtual
   machine files.
   
   A placement hub is a datastore or a storage pod.
   A vSphere API `StoragePod` corresponds to Storage DRS in the vSphere Web Client.
   """
   def QueryMatchingHub(self, hubsToSearch: list[PlacementHub], profile: pyVmomi.pbm.profile.ProfileId) -> list[PlacementHub]:
      """
      Deprecated: As of vSphere 2016, use `pyVmomi.pbm.placement.PlacementSolver.checkRequirements`
      instead in order to retrieve both compatible compute and storage location.Finds matching placement hubs for the specified requirements profile.
      
      This
      method returns only those hubs that match the profile. If this method is
      invoked for
      `VVolDefaultProfile`
      profile, then all the VVOL containers are returned as matching.
      
      Args:
          hubsToSearch: Candidate list of hubs, either datastores or storage pods or a
              mix. If this parameter is not specified, the Server uses all
              of the datastores and storage pods.
          profile: Storage requirement profile.
      
      Returns:
          Subset of the `hubsToSearch` list that satisfies the
          profile requirements. A storage pod is returned if and only if all
          its member datastores satisfy the profile requirements, whether
          the hubs list contains any of the member datastores or not. If a
          datastore and its storage pod are in the hubs list, and both
          satisfy the requirements, both are returned.
      
      Raises:
          pyVmomi.pbm.fault.PBMFault: If there is an internal server error.
      """
      ...
   def QueryMatchingHubWithSpec(self, hubsToSearch: list[PlacementHub], createSpec: pyVmomi.pbm.profile.CapabilityBasedProfileCreateSpec) -> list[PlacementHub]:
      """
      Deprecated: As of vSphere 2016, use `pyVmomi.pbm.placement.PlacementSolver.checkRequirements` instead in order to retrieve both compatible compute and storage location.Finds matching placement hubs based on a profile creation specification.
      
      This method returns only those hubs that match the specification.
      
      Args:
          hubsToSearch: Candidate list of hubs, either datastores or storage
              pods or a mix. If this parameter is not specified, the Server uses
              all of the datastores and storage pods for placement compatibility checking.
          createSpec: Storage profile creation specification.
      
      Returns:
          Subset of the `hubsToSearch` list that satisfies the profile
          requirements. A storage pod is returned if and only if all its member datastores
          satisfy the profile requirements, whether the hubs list contains
          any of the member datastores or not. If a datastore and its storage pod
          are in the hubs list, and both satisfy the requirements, both are returned.
      
      Raises:
          pyVmomi.pbm.fault.PBMFault: If there is an internal server error.
      """
      ...
   def CheckCompatibility(self, hubsToSearch: list[PlacementHub], profile: pyVmomi.pbm.profile.ProfileId) -> list[CompatibilityResult]:
      """
      Deprecated: As of vSphere 2016, use `pyVmomi.pbm.placement.PlacementSolver.checkRequirements` instead in order to retrieve compatibility status on both compute and storage
      location.Performs placement compatibility checking based on a storage requirement
      profile.
      
      If compatibility checking for a hub does not produce any errors,
      the hub is considered a viable candidate for virtual machine file storage.
      If this method is invoked for
      `VVolDefaultProfile`
      profile, then all the VVOL containers are returned as matching.
      
      Args:
          hubsToSearch: Candidate list of hubs, either datastores or storage pods or a
              mix. If this parameter is not specified, the Server uses all
              of the datastores and storage pods for placement compatibility
              checking.
          profile: Storage requirement profile.
      
      Returns:
          Array of compatibility result objects. The results array contains
          one entry for each entry in the `hubsToSearch` list. If
          a hubs list is not specified, the results array contains one
          entry for each datastore and storage pod in your vSphere
          environment. Any errors are described in the results array.
          - If there is an invalid argument error, the compatibility
            results will contain `InvalidArgument` faults
            indicating that the profile does not exist or that it does not
            match the requirement type.
          - If there are errors or warnings during compatibility checking,
            the compatibility results will contain faults derived from
            `pyVmomi.pbm.fault.CompatibilityCheckFault`.
          - If this method is invoked for
            `VVolDefaultProfile`
            then the compatibility results will contain faults derived from
            `pyVmomi.pbm.fault.CompatibilityCheckFault` for non-vvol datastores.
      """
      ...
   def CheckCompatibilityWithSpec(self, hubsToSearch: list[PlacementHub], profileSpec: pyVmomi.pbm.profile.CapabilityBasedProfileCreateSpec) -> list[CompatibilityResult]:
      """
      Deprecated: As of vSphere 2016, use `pyVmomi.pbm.placement.PlacementSolver.checkRequirements` instead in order to retrieve compatibility status for both
      compute and storage location.Performs placement compatibility checking based on a storage profile
      specification.
      
      If compatibility checking for a hub does not produce
      any errors, the hub is considered a viable candidate for virtual
      machine file storage.
      
      Args:
          hubsToSearch: Candidate list of hubs, either datastores or storage pods
              or a mix. If this parameter is not specified, the Server uses all of the
              datastores and storage pods for placement compatibility checking.
          profileSpec: Specification for a capability based profile.
      
      Returns:
          Array of compatibility result objects. The results array contains
          one entry for each entry in the `hubsToSearch` list.
          If a hubs list is not specified, the results array contains one entry
          for each datastore and storage pod in your vSphere environment.
          Any errors are described in the results array.
          - If there is an invalid argument error, the compatibility results
            will contain `InvalidArgument` faults indicating that the
            profile does not exist or that it does not match the requirement type.
          - If there are errors or warnings during compatibility checking,
            the compatibility results will contain faults derived from
            `pyVmomi.pbm.fault.CompatibilityCheckFault`.
      """
      ...
   def CheckRequirements(self, hubsToSearch: list[PlacementHub], placementSubjectRef: _typing.Optional[pyVmomi.pbm.ServerObjectRef], placementSubjectRequirement: list[Requirement]) -> list[CompatibilityResult]:
      """
      Performs placement compatibility checking for the specified object to be placed based on its
      specified set of requirements.
      
      If compatibility checking for a hub does not produce any
      errors, the hub is considered a viable candidate for virtual machine storage.
      
      Args:
          hubsToSearch: Candidate list of hubs, either datastores or storage pods
              or a mix. If this parameter is not specified, the Server uses all of the
              datastores and storage pods for placement compatibility checking.
          placementSubjectRef: reference to the object being placed. Should be null when a new
              object is being provisioned. Should be specified when placement compatibility is being checked
              for an existing object. Supported objects are
              `virtualMachine`,
              `virtualMachineAndDisks`,
              `virtualDiskId`,
              `virtualDiskUUID`
          placementSubjectRequirement: Requirements including the policy requirements, compute
              requirements and capacity requirements. It is invalid to specify no requirements. It is also
              invalid to specify duplicate requirements or multiple conflicting requirements such as
              specifying both `pyVmomi.pbm.placement.CapabilityConstraintsRequirement` and
              `pyVmomi.pbm.placement.CapabilityProfileRequirement`.
      
      Returns:
          Array of compatibility result objects. The results array contains
          one entry for each entry in the `hubsToSearch` list.
          If hubs list is not specified, the results array contains one entry
          for each datastore and storage pod in your vSphere environment.
          Any errors are returned in the results array.
          - If there is an invalid argument error, the compatibility results
            will contain `InvalidArgument` faults indicating that the
            profile does not exist or that it does not match the requirement type.
          - If there are errors or warnings during compatibility checking,
            the compatibility results will contain faults derived from
            `pyVmomi.pbm.fault.CompatibilityCheckFault`.
      
      Raises:
          pyVmomi.pbm.fault.PBMFault: If there is an internal server error.
      """
      ...


class ResourceUtilization(pyVmomi.vmodl.DynamicData):
   """
   Describes the resource utilization metrics of a datastore.
   
   These results are not to be treated as a guaranteed availability,
   they are useful to estimate the effects of a change of policy
   or the effects of a provisioning action.
   
   Attributes:
       name: Name of the resource.
       description: Description of the resource.
       availableBefore: Currently available (i.e.
           
           before the provisioning step).
       availableAfter: Available after the provisioning step.
       total: Total resource availability
   """
   name: pyVmomi.pbm.ExtendedElementDescription
   description: pyVmomi.pbm.ExtendedElementDescription
   availableBefore: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   availableAfter: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   total: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class ZoneTopologyRequirement(CapabilityProfileRequirement):
   """
   Defines a zone topology requirement for placing objects onto `pyVmomi.pbm.placement.PlacementHub`s.
   
   It is invalid
   to specify this requirement along with other conflicting requirements and also, it's invalid to
   specify duplicate requirements.
   
   Attributes:
       clusters: References of Cluster server objects belonging to a `AvailabilityZone`.
           
           i.e. each
           referenced cluster must be tagged with a zone as this constraint is intended for scenarios
           where zone-specific behavior is required.
           Cluster which is not associated with any zone is not allowed in the input when using this
           constraint. Other type of server objects such as VirtualMachine are not allowed either.
           This field must be set to a non-empty array of cluster references, otherwise compatibility
           check fails.
   """
   clusters: list[pyVmomi.pbm.ServerObjectRef] = []
