# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.pbm
import pyVmomi.vmodl
import pyVmomi.vim.vm.replication



class QueryReplicationGroupResult(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.pbm.replication.QueryReplicationGroupResult` data object
   identifies a virtual machine, or a virtual disk and lists the identifier(s) for the associated
   replication group.
   
   Attributes:
       object: Reference to the virtual machine or virtual disk on which the query was performed.
           
           If the
           query was performed for a virtual machine and all it's disks, this will reference each disk
           and the virtual machine config individually.
       replicationGroupId: Replication group identifier which is associated with `object`.
       fault: Fault associated with the query, if there is one.
   """
   object: pyVmomi.pbm.ServerObjectRef
   replicationGroupId: _typing.Optional[pyVmomi.vim.vm.replication.ReplicationGroupId] = None
   fault: _typing.Optional[pyVmomi.vmodl.MethodFault] = None


class ReplicationManager(pyVmomi.VmomiSupport.ManagedObject):
   """
   The `pyVmomi.pbm.replication.ReplicationManager` provides methods dealing with replication aspects of virtual
   machine and virtual disk requirement profiles.
   """
   def QueryReplicationGroups(self, entities: list[pyVmomi.pbm.ServerObjectRef]) -> list[QueryReplicationGroupResult]:
      """
      Returns identifiers for replication groups associated with virtual machines, virtual
      disks or virtual machines and all their disks.
      
      If the query is performed for a virtual machine
      and all it's disks `virtualMachineAndDisks`, an entry per
      disk and one for the virtual machine config will be returned.
      
      Args:
          entities: Array of server object references. Valid types are
              `virtualMachine`,
              `virtualMachineAndDisks`,
              `virtualDiskId`,
              `virtualDiskUUID`
      
      Returns:
          Array of query result objects. Each `pyVmomi.pbm.replication.QueryReplicationGroupResult`
          object identifies a virtual machine, or virtual disk and contains the replication group id
          associated with that entity, if any. It also describes the fault, if there is an error associated
          with one of the entities.
      
      Raises:
          pyVmomi.pbm.fault.PBMFault: If there is an internal service error.
      """
      ...
