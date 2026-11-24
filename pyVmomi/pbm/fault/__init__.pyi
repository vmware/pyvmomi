# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import typing as _typing
import pyVmomi.vmodl
import pyVmomi.pbm.capability
import pyVmomi.pbm.placement
import pyVmomi.pbm.profile
import pyVmomi.vmodl.fault



class PBMFault(pyVmomi.vmodl.MethodFault):
   """The super class for all pbm faults."""
   pass


class AlreadyExists(PBMFault):
   """
   An AlreadyExists fault is thrown when an attempt is made to add an element to
   a collection, if the element's key, name, or identifier already exists in
   that collection.
   """
   name: _typing.Optional[str] = None


class CompatibilityCheckFault(PBMFault):
   """
   Super class for all compatibility check faults.
   
   Attributes:
       hub: Placement Hub
   """
   hub: pyVmomi.pbm.placement.PlacementHub


class PropertyMismatchFault(CompatibilityCheckFault):
   """
   Fault used to indicate which property instance in requirements profile that does not
   match.
   
   Attributes:
       capabilityInstanceId: Id of the CapabilityInstance in requirements profile that
           does not match.
       requirementPropertyInstance: The property instance in requirement profile that does not match.
   """
   capabilityInstanceId: pyVmomi.pbm.capability.CapabilityMetadata.UniqueId
   requirementPropertyInstance: pyVmomi.pbm.capability.PropertyInstance


class CapabilityProfilePropertyMismatchFault(PropertyMismatchFault):
   """
   Fault used when a datastore doesnt match the capability profile property instance in requirements profile.
   
   Attributes:
       resourcePropertyInstance: The property instance in the resource profile that does not match.
   """
   resourcePropertyInstance: pyVmomi.pbm.capability.PropertyInstance

class DefaultProfileAppliesFault(CompatibilityCheckFault):
   """
   Warning fault used to indicate that the vendor specific datastore matches the tag in the
   requirements profile that does not have a vendor specific rule set.
   
   In such case,
   an empty blob is sent to the vendor specific datastore and the default profile would apply.
   """
   pass

class DuplicateName(PBMFault):
   """
   A DuplicateName exception is thrown because a name already exists
   in the same name space.
   
   Attributes:
       name: The name that is already bound in the name space.
   """
   name: str

class IncompatibleVendorSpecificRuleSet(CapabilityProfilePropertyMismatchFault):
   """
   Warning fault used to indicate that the vendor specific datastore matches the tag in the
   requirements profile but doesnt match the vendor specific rule set in the requirements profile.
   """
   pass

class InvalidLogin(PBMFault):
   """
   Thrown when login fails due to token not provided or token could not be
   validated.
   """
   pass


class LegacyHubsNotSupported(PBMFault):
   """
   LegacyHubsNotSupported fault is thrown to indicate the legacy hubs that are not supported.
   
   For storage, legacy hubs or datastores are VMFS and NFS datastores.
   
   Attributes:
       hubs: Legacy hubs that are not supported.
           
           Only datastores will be populated in this fault. Datastore clusters
           are not allowed.
   """
   hubs: list[pyVmomi.pbm.placement.PlacementHub] = []


class NoPermission(pyVmomi.vmodl.fault.SecurityError):
   """
   Thrown when an operation is denied because of a privilege
   not held on a storage profile.
   
   Attributes:
       missingPrivileges: List of profile ids and missing privileges for each profile
   """
   class EntityPrivileges(pyVmomi.vmodl.DynamicData):
      profileId: _typing.Optional[pyVmomi.pbm.profile.ProfileId] = None
      privilegeIds: list[str] = []

   missingPrivileges: list[NoPermission.EntityPrivileges] = []


class NonExistentHubs(PBMFault):
   """
   NonExistentHubs is thrown to indicate that some non existent datastores are used.
   
   Attributes:
       hubs: Legacy hubs that do not exist.
   """
   hubs: list[pyVmomi.pbm.placement.PlacementHub] = []

class NotFound(PBMFault):
   """
   A NotFound error occurs when a referenced component of a managed
   object cannot be found.
   
   The referenced component can be a data
   object type (such as a role or permission) or a primitive
   (such as a string).
   
   For example, if the missing referenced component is a data object, such as
   VirtualSwitch, the NotFound error is
   thrown. The NotFound error is also thrown if the data object is found, but the referenced name
   (for example, \"vswitch0\") is not.
   """
   pass

class ProfileStorageFault(PBMFault):
   pass


class ResourceInUse(PBMFault):
   """
   A ResourceInUse fault indicating that some error has occurred because a
   resource was in use.
   
   Information about the resource that is in use may
   be supplied.
   
   Attributes:
       type: Type of resource that is in use.
       name: Name of the instance of the resource that is in use.
   """
   type: _typing.Optional[type] = None
   name: _typing.Optional[str] = None
