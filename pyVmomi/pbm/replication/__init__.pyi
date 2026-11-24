# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.pbm
import pyVmomi.vmodl
import pyVmomi.vim.vm.replication



class QueryReplicationGroupResult(pyVmomi.vmodl.DynamicData):
   object: pyVmomi.pbm.ServerObjectRef
   replicationGroupId: _typing.Optional[pyVmomi.vim.vm.replication.ReplicationGroupId] = None
   fault: _typing.Optional[pyVmomi.vmodl.MethodFault] = None


class ReplicationManager(pyVmomi.VmomiSupport.ManagedObject):
   def QueryReplicationGroups(self, entities: list[pyVmomi.pbm.ServerObjectRef]) -> list[QueryReplicationGroupResult]: ...
