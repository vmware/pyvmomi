from typing import List
from pyVmomi import DeviceId, sms, vmodl


class AlreadyDone(ReplicationFault): ...


class InvalidFunctionTarget(ReplicationFault): ...


class InvalidReplicationState(ReplicationFault):
    @property
    def desiredState(self) -> List[str]: ...
    @desiredState.setter
    def desiredState(self, value: List[str]):
        self._desiredState = value
    @property
    def currentState(self) -> str: ...
    @currentState.setter
    def currentState(self, value: str):
        self._currentState = value


class NoReplicationTarget(ReplicationFault): ...


class NoValidReplica(ReplicationFault):
    @property
    def deviceId(self) -> DeviceId: ...
    @deviceId.setter
    def deviceId(self, value: DeviceId):
        self._deviceId = value


class PeerNotReachable(ReplicationFault): ...


class ReplicationFault(vmodl.MethodFault): ...


class SyncOngoing(ReplicationFault):
    @property
    def task(self) -> sms.Task: ...
    @task.setter
    def task(self, value: sms.Task):
        self._task = value