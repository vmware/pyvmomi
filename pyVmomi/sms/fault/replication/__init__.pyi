# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import typing as _typing
import pyVmomi.sms
import pyVmomi.vmodl
import pyVmomi.sms.storage.replication


class AlreadyDone(ReplicationFault):
   pass

class InvalidFunctionTarget(ReplicationFault):
   pass


class InvalidReplicationState(ReplicationFault):
   desiredState: list[str] = []
   currentState: str

class NoReplicationTarget(ReplicationFault):
   pass


class NoValidReplica(ReplicationFault):
   deviceId: _typing.Optional[pyVmomi.sms.storage.replication.DeviceId] = None

class PeerNotReachable(ReplicationFault):
   pass


class ReplicationFault(pyVmomi.vmodl.MethodFault):
   pass


class SyncOngoing(ReplicationFault):
   task: pyVmomi.sms.Task
