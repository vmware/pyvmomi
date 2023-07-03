from typing import List
from pyVmomi import pbm, vim, vmodl
from pyVmomi.VmomiSupport import ManagedObject


class ReplicationManager(ManagedObject):
    def QueryReplicationGroups(self, entities: List[pbm.ServerObjectRef]) -> List[QueryReplicationGroupResult]: ...


class QueryReplicationGroupResult(vmodl.DynamicData):
    @property
    def object(self) -> pbm.ServerObjectRef: ...
    @object.setter
    def object(self, value: pbm.ServerObjectRef):
        self._object = value
    @property
    def replicationGroupId(self) -> vim.vm.replication.ReplicationGroupId: ...
    @replicationGroupId.setter
    def replicationGroupId(self, value: vim.vm.replication.ReplicationGroupId):
        self._replicationGroupId = value
    @property
    def fault(self) -> vmodl.MethodFault: ...
    @fault.setter
    def fault(self, value: vmodl.MethodFault):
        self._fault = value