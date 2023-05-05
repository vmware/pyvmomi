from typing import List
from pyVmomi import DeviceId, sms, vmodl


class AlreadyDone(ReplicationFault): ...


class InvalidFunctionTarget(ReplicationFault): ...


class InvalidReplicationState(ReplicationFault):
    @property
    def desiredState(self) -> List[str]: ...
    @property
    def currentState(self) -> str: ...


class NoReplicationTarget(ReplicationFault): ...


class NoValidReplica(ReplicationFault):
    @property
    def deviceId(self) -> DeviceId: ...


class PeerNotReachable(ReplicationFault): ...


class ReplicationFault(vmodl.MethodFault): ...


class SyncOngoing(ReplicationFault):
    @property
    def task(self) -> sms.Task: ...