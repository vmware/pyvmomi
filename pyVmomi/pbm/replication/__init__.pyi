from typing import List
from pyVmomi import ReplicationGroupId, pbm, vmodl
from pyVmomi.VmomiSupport import ManagedObject


class ReplicationManager(ManagedObject):
    def QueryReplicationGroups(self, entities: List[pbm.ServerObjectRef]) -> List[QueryReplicationGroupResult]: ...


class QueryReplicationGroupResult(vmodl.DynamicData):
    @property
    def object(self) -> pbm.ServerObjectRef: ...
    @property
    def replicationGroupId(self) -> ReplicationGroupId: ...
    @property
    def fault(self) -> vmodl.MethodFault: ...