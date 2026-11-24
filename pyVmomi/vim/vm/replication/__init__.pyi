# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import pyVmomi.vmodl



class DeviceGroupId(pyVmomi.vmodl.DynamicData):
   """
   Identifier of a replication device group.
   
   Attributes:
       id: ID of the device group.
   """
   id: str


class FaultDomainId(pyVmomi.vmodl.DynamicData):
   """
   Represents the identity of a replication fault domain.
   
   Fault domains IDs are globally
   unique.
   
   Attributes:
       id: ID of the fault domain.
   """
   id: str


class ReplicationGroupId(pyVmomi.vmodl.DynamicData):
   """
   The identity of a replication group.
   
   A following well-known ReplicationGroupId
   
   {
   
   faultDomainId: 
   
   deviceGroupId: ffffffff-ffff-ffff-ffff-ffffffffffff
   
   }
   
   means that VASA provider can create a new ReplicationGroupId
   on demand (this feature may not be supported in the first
   vSphere release that supports VVol replication).
   
   Attributes:
       faultDomainId: ID of the fault domain to which the group belongs.
           
           Combined with the fault
           domain id, the group id is unique. A group may (or may not) have the same
           id in all the fault domains.
       deviceGroupId: Id of the replication device group.
           
           A group may have the same (or different) id in each fault
           domain.
   """
   faultDomainId: FaultDomainId
   deviceGroupId: DeviceGroupId


class ReplicationSpec(pyVmomi.vmodl.DynamicData):
   """
   Attributes:
       replicationGroupId: Replication Group id
   """
   replicationGroupId: ReplicationGroupId
