# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import typing as _typing
import pyVmomi.sms
import pyVmomi.vmodl
import pyVmomi.sms.storage.replication



class ReplicationFault(pyVmomi.vmodl.MethodFault):
   """Base class for all Replication faults."""
   pass

class AlreadyDone(ReplicationFault):
   """
   Thrown if the object is already at the desired state.
   
   This is always a warning.
   """
   pass

class InvalidFunctionTarget(ReplicationFault):
   """
   Thrown if the function is called at the wrong end of the replication (i.e.
   
   the failing function should be tried at the opposite end of replication).
   """
   pass


class InvalidReplicationState(ReplicationFault):
   """
   Thrown if the replication group is not in the correct state.
   
   Attributes:
       desiredState: States where the operation would have been successful.
       currentState: Current state.
   """
   desiredState: list[str] = []
   currentState: str

class NoReplicationTarget(ReplicationFault):
   """This exception is set if the replication target is not yet available."""
   pass


class NoValidReplica(ReplicationFault):
   """
   This exception is thrown when there is no valid replica
   to be used in recovery.
   
   This may happen when a Virtual Volume
   is created on the source domain, but the replica is yet to
   be copied to the target.
   
   Attributes:
       deviceId: Identifier of the device which does not have a valid
           replica.
           
           This is the identifier on the target site.
           This may not be set if the ReplicationGroup does not
           have even a single valid replica.
   """
   deviceId: _typing.Optional[pyVmomi.sms.storage.replication.DeviceId] = None

class PeerNotReachable(ReplicationFault):
   """
   This exception is set if the replication peer is not reachable.
   
   For prepareFailover, it is the target that is not reachable.
   For other functions, it is the source that is not reachable.
   """
   pass


class SyncOngoing(ReplicationFault):
   """
   Throw if an synchronization is ongoing.
   
   Attributes:
       task: Task identifier of the ongoing sync (@see sms.TaskInfo#key).
   """
   task: pyVmomi.sms.Task
