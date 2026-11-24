# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import datetime as _datetime
import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.pbm
import pyVmomi.vmodl
import pyVmomi.pbm.capability
import pyVmomi.pbm.profile



class ComplianceManager(pyVmomi.VmomiSupport.ManagedObject):
   """
   The `pyVmomi.pbm.compliance.ComplianceManager` provides methods to verify the compliance
   of virtual machine and virtual disk requirement profiles.
   
   When you provision
   a virtual machine on a matching datastore, the Server sends the profile
   to the storage provider. When you perform a compliance check, the storage
   provider compares the requirements with its capabilities,
   returns the results to the Server, and the Server returns the results
   to your client. The Server maintains the compliance results for retrieval
   at a later time.
   
   You can check the compliance of one or more virtual machines and/or virtual disks.
   You can also perform a rollup compliance check, in which the Server checks the
   compliance of a virtual machine and all of its virtual disks.
   """
   def CheckCompliance(self, entities: list[pyVmomi.pbm.ServerObjectRef], profile: _typing.Optional[pyVmomi.pbm.profile.ProfileId]) -> list[ComplianceResult]:
      """
      Checks compliance of the profiles associated with one or more
      virtual machines and/or virtual disks.
      
      The Server stores the compliance results for all of the storage entities
      associated with the virtual machines and disks. You can call the
      `pyVmomi.pbm.compliance.ComplianceManager.fetchComplianceResult` method
      to retrieve the stored results. However, for storage entities placed on vSAN,
      both fetchComplianceResult and checkCompliance methods have the same
      behaviour of recomputing the compliance.
      
      Args:
          entities: One or more references to storage entities.
              You can specify virtual machines and virtual disks
              A maximum of 1000 virtual machines and/or virtual disks can be specified
              in a call. The results of calling the checkCompliance API with
              more than a 1000 entities is undefined.
              - If the list of entities also contains datastores, the Server
                will ignore the datastores.
              - If the list contains valid and invalid entities, the Server ignores
                the invalid entities and returns results for the valid entities.
                Invalid entities are entities that are not in the vCenter inventory.
              - If the list contains only datastores, the method throws
                an `InvalidArgument` fault.
              - If the list contains virtual machines and disks and the entities
                are invalid or have been deleted by the time of the request, the method
                throws an `InvalidArgument` fault.
                
              If an entity does not have an associated storage profile, the entity
              is removed from the list.
          profile: Not used. If specified, the Server ignores the value.
              The Server uses the profiles associated with the specified entities.
      
      Returns:
          Result of the compliance check. The returned array contains one
          result object for each entity specified in the method call.
      
      Raises:
          pyVmomi.pbm.fault.PBMFault: If there is an internal server error.
      """
      ...
   def FetchComplianceResult(self, entities: list[pyVmomi.pbm.ServerObjectRef], profile: _typing.Optional[pyVmomi.pbm.profile.ProfileId]) -> list[ComplianceResult]:
      """
      Retrieves the latest version of `pyVmomi.pbm.compliance.ComplianceResult` objects that are
      available for the specified entities.
      
      Args:
          entities: One or more references to storage entities.
              A maximum of 1000 virtual machines and/or virtual disks can be specified
              in a call. The results of calling the fetchComplianceResult API with
              more than a 1000 entities is undefined.
              - If the list of entities also contains datastores, the Server
                will ignore the datastores.
              - If the list contains valid and invalid entities, the Server ignores
                the invalid entities and returns results for the valid entities.
                Invalid entities are entities that are not in the vCenter inventory.
              - If the list contains only datastores, the method throws
                an `InvalidArgument` fault.
          profile: Not used. if specified, the Server ignores the value.
              The Server uses the profiles associated with the specified entities.
      
      Returns:
          Array of compliance results. The returned array contains
          one result object for each entity specified in the method call.
      
      Raises:
          pyVmomi.pbm.fault.PBMFault: If there is an internal server error.
      """
      ...
   def CheckRollupCompliance(self, entity: list[pyVmomi.pbm.ServerObjectRef]) -> list[RollupComplianceResult]:
      """
      Checks rollup compliance of virtual machines and returns the results to your
      client.
      
      For a specified virtual machine, a rollup compliance check verifies
      the storage requirements of the virtual machine and its virtual disks as
      compared with the storage provider capabilities.
      
      The Server stores the compliance results for all of the storage entities
      associated with the virtual machines. You can call the
      `pyVmomi.pbm.compliance.ComplianceManager.fetchRollupComplianceResult` method
      to retrieve the stored results. However, for storage entities placed on vSAN,
      both fetchRollupComplianceResult and checkRollupCompliance methods have the
      same behaviour of recomputing the compliance.
      
      Args:
          entity: One or more references to virtual machines.
              A maximum of 1000 virtual machines can be specified
              in a call. The results of calling the checkRollupCompliance API with
              more than a 1000 entities is undefined.
      
      Returns:
          Result of the rollup compliance check. The returned array
          contains one rollup compliance result for each virtual machine.
          A rollup compliance result object includes the overall compliance
          status that represents the collective compliance status for the
          virtual machine and its virtual disks.
      
      Raises:
          pyVmomi.pbm.fault.PBMFault: If there is an internal server error.
      """
      ...
   def FetchRollupComplianceResult(self, entity: list[pyVmomi.pbm.ServerObjectRef]) -> list[RollupComplianceResult]:
      """
      Retrieves the rollup compliance (`pyVmomi.pbm.compliance.RollupComplianceResult`)
      of the given virtual machines if present.
      
      The returned rollup compliance
      result may be old. Invoke checkRollupCompliance API to compute and retrieve the
      latest rollup compliance result. For storage entities placed on vSAN the
      returned compliance is always the latest.
      
      Args:
          entity: One or more virtual machines.
              A maximum of 1000 virtual machines can be specified
              in a call. The results of calling the fetchRollupComplianceResult API with
              more than a 1000 entity objects is undefined.
      
      Returns:
          Rollup compliance results for the given virtual machines.
      
      Raises:
          pyVmomi.pbm.fault.PBMFault: If there is an internal server error.
      """
      ...
   def QueryByRollupComplianceStatus(self, status: str) -> list[pyVmomi.pbm.ServerObjectRef]:
      """
      Returns the virtual machines for the given rollup compliance status.
      
      Args:
          status: `pyVmomi.pbm.compliance.ComplianceResult.ComplianceStatus`
      
      Returns:
          Array of VirtualMachine entities
      
      Raises:
          pyVmomi.vmodl.fault.InvalidArgument: If the given status parameter is invalid or incorrect format.
          pyVmomi.pbm.fault.PBMFault: If there is an internal service error.
      """
      ...


class ComplianceResult(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.pbm.compliance.ComplianceResult` data object describes the results of profile compliance
   checking for a virtual machine or virtual disk.
   
   Attributes:
       checkTime: Time when the compliance was checked.
       entity: Virtual machine or virtual disk for which compliance was checked.
       profile: Requirement profile with which the compliance was checked.
       complianceTaskStatus: Status of the current running compliance operation.
           
           If there is no
           compliance check operation triggered, this indicates the last compliance
           task status. `complianceTaskStatus` is a string value that
           corresponds to one of the
           `pyVmomi.pbm.compliance.ComplianceResult.ComplianceTaskStatus` values.
       complianceStatus: Status of the compliance operation.
           
           `complianceStatus` is a
           string value that corresponds to one of the
           `pyVmomi.pbm.compliance.ComplianceResult.ComplianceStatus` values.
           
           When you perform compliance checking on an entity whose associated profile
           contains more than one subprofile (
           `pyVmomi.pbm.profile.CapabilityBasedProfile` .
           `pyVmomi.pbm.profile.CapabilityBasedProfile.constraints`), a compliant
           result for any one of the subprofiles will produce a compliant result
           for the operation.
       mismatch: Set to true if there is a profile version mismatch between the Storage
           Profile Server and the storage provider.
           
           If you receive a result that
           indicates a mismatch, you must use the vSphere API to update the profile
           associated with the virtual machine or virtual disk.
       violatedPolicies: Values for capabilities that are known to be non-compliant with the specified constraints.
       errorCause: This property is set if the compliance task fails with errors.
           
           There can be
           more than one error since a policy containing multiple blobs can return
           multiple failures, one for each blob.
       operationalStatus: Additional information on the effects of backend resources and
           operations on the storage object.
       info: Informational localized messages provided by the VASA provider in
           addition to the `violatedPolicy`.
   """
   class ComplianceStatus(pyVmomi.VmomiSupport.Enum):
      """
      The `pyVmomi.pbm.compliance.ComplianceResult.ComplianceStatus`
      enumeration type defines the set of status values
      for compliance operations.
      
      See `pyVmomi.pbm.compliance.ComplianceResult` and
      `pyVmomi.pbm.compliance.RollupComplianceResult`.
      
      Attributes:
          compliant: Entity is in compliance.
          nonCompliant: Entity is out of compliance.
          unknown: Compliance status of the entity is not known.
          notApplicable: Compliance computation is not applicable for this entity,
              because it does not have any storage requirements that
              apply to the object-based datastore on which this entity is placed.
          outOfDate: This is the same as `pyVmomi.pbm.compliance.ComplianceResult.mismatch`
              variable.
              
              Compliance status becomes out-of-date when the profile
              associated with the entity is edited and not applied. The compliance
              status will remain in out-of-date compliance status until the latest
              policy is applied to the entity.
      """
      compliant: _typing.ClassVar['ComplianceResult.ComplianceStatus'] = 'compliant'
      nonCompliant: _typing.ClassVar['ComplianceResult.ComplianceStatus'] = 'nonCompliant'
      unknown: _typing.ClassVar['ComplianceResult.ComplianceStatus'] = 'unknown'
      notApplicable: _typing.ClassVar['ComplianceResult.ComplianceStatus'] = 'notApplicable'
      outOfDate: _typing.ClassVar['ComplianceResult.ComplianceStatus'] = 'outOfDate'

   class ComplianceTaskStatus(pyVmomi.VmomiSupport.Enum):
      """
      The `pyVmomi.pbm.compliance.ComplianceResult.ComplianceTaskStatus`
      enumeration type defines the set of task status for compliance
      operations.
      
      See `pyVmomi.pbm.compliance.ComplianceResult` and
      `pyVmomi.pbm.compliance.RollupComplianceResult`.
      
      Attributes:
          inProgress: Compliance calculation is in progress.
          success: Compliance calculation has succeeded.
          failed: Compliance calculation failed due to some exception.
      """
      inProgress: _typing.ClassVar['ComplianceResult.ComplianceTaskStatus'] = 'inProgress'
      success: _typing.ClassVar['ComplianceResult.ComplianceTaskStatus'] = 'success'
      failed: _typing.ClassVar['ComplianceResult.ComplianceTaskStatus'] = 'failed'

   checkTime: _datetime.datetime
   entity: pyVmomi.pbm.ServerObjectRef
   profile: _typing.Optional[pyVmomi.pbm.profile.ProfileId] = None
   complianceTaskStatus: _typing.Optional[str] = None
   complianceStatus: str
   mismatch: bool
   violatedPolicies: list[PolicyStatus] = []
   errorCause: list[pyVmomi.vmodl.MethodFault] = []
   operationalStatus: _typing.Optional[OperationalStatus] = None
   info: _typing.Optional[pyVmomi.pbm.ExtendedElementDescription] = None


class FetchEntityHealthStatusSpec(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.pbm.compliance.FetchEntityHealthStatusSpec` data object contains
   the arguments required for
   `pyVmomi.pbm.compliance.ComplianceManager.fetchEntityHealthStatusExt`.
   
   Attributes:
       objectRef: `pyVmomi.pbm.ServerObjectRef` for which the healthStatus is required
       backingId: BackingId for the ServerObjectRef
           BackingId is mandatory for FCD on vSAN
   """
   objectRef: pyVmomi.pbm.ServerObjectRef
   backingId: _typing.Optional[str] = None


class OperationalStatus(pyVmomi.vmodl.DynamicData):
   """
   Additional information on the effects of backend resources and
   operations on the storage object.
   
   Attributes:
       healthy: Whether the object is currently affected by the failure of backend
           storage resources.
           
           Optional property.
       operationETA: Estimated completion time of a backend operation affecting the object.
           
           If set, then \"transitional\" will be true.
           Optional property.
       operationProgress: Percent progress of a backend operation affecting the object.
           
           If set, then \"transitional\" will be true.
           Optional property.
       transitional: Whether an object is undergoing a backend operation that may affect
           its performance.
           
           This may be a rebalancing the resources of a healthy
           object or recovery tasks for an unhealthy object.
           Optional property.
   """
   healthy: _typing.Optional[bool] = None
   operationETA: _typing.Optional[_datetime.datetime] = None
   operationProgress: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   transitional: _typing.Optional[bool] = None


class PolicyStatus(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.pbm.compliance.PolicyStatus` data object provides information
   when compliance checking produces non-compliant results.
   
   See
   `pyVmomi.pbm.compliance.ComplianceResult`.`pyVmomi.pbm.compliance.ComplianceResult.violatedPolicies`.
   
   Attributes:
       expectedValue: Expected storage capability values of profile policies defined
           by a storage provider.
       currentValue: Current storage requirement values of the profile policies
           specified for the virtual machine or virtual disk.
   """
   expectedValue: pyVmomi.pbm.capability.CapabilityInstance
   currentValue: _typing.Optional[pyVmomi.pbm.capability.CapabilityInstance] = None


class RollupComplianceResult(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.pbm.compliance.RollupComplianceResult` data object identifies the virtual machine
   for which rollup compliance was checked, and it contains the overall status
   and a list of compliance result objects.
   
   Attributes:
       oldestCheckTime: Indicates the earliest time that compliance was checked for any
           of the entities in the rollup compliance check.
           
           The compliance
           check time for a single entity is represented in the
           `pyVmomi.pbm.compliance.ComplianceResult`.`pyVmomi.pbm.compliance.ComplianceResult.checkTime`
           property. If the `pyVmomi.pbm.compliance.ComplianceResult.checkTime`
           property is unset for any of the objects in the `results`
           array, the `oldestCheckTime` property will be unset.
       entity: Virtual machine for which the rollup compliance was checked.
       overallComplianceStatus: Overall compliance status of the virtual machine and its virtual disks.
           
           `overallComplianceStatus` is a string value that
           corresponds to one of the
           `pyVmomi.pbm.compliance.ComplianceResult`.`pyVmomi.pbm.compliance.ComplianceResult.complianceStatus`
           values.
           
           The overall compliance status is determined by the following rules, applied in the order
           listed:
           - If all the entities are `compliant`, the overall status is
             `compliant`.
           - Else if any entity's status is `outOfDate`, the overall status is
             `outOfDate`.
           - Else if any entity's status is `nonCompliant`, the overall status is
             `nonCompliant`.
           - Else if any entity's status is `unknown`, the overall status is
             `unknown`.
           - Else if any entity's status is `notApplicable`, the overall status is
             `notApplicable`.
       overallComplianceTaskStatus: Overall compliance task status of the virtual machine and its virtual
           disks.
           
           `overallComplianceTaskStatus` is a string value that
           corresponds to one of the `pyVmomi.pbm.compliance.ComplianceResult`.
           `pyVmomi.pbm.compliance.ComplianceResult.complianceTaskStatus` values.
       result: Individual compliance results that make up the rollup.
       errorCause: This property is set if the overall compliance task fails with some error.
           
           This
           property indicates the causes of error. If there are multiple failures, it stores
           these failure in this array.
       profileMismatch: True if and only if `pyVmomi.pbm.compliance.ComplianceResult`.
           
           `pyVmomi.pbm.compliance.ComplianceResult.mismatch` is true for at least one
           entity in the rollup compliance check.
   """
   oldestCheckTime: _datetime.datetime
   entity: pyVmomi.pbm.ServerObjectRef
   overallComplianceStatus: str
   overallComplianceTaskStatus: _typing.Optional[str] = None
   result: list[ComplianceResult] = []
   errorCause: list[pyVmomi.vmodl.MethodFault] = []
   profileMismatch: bool
