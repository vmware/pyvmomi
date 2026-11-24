# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import datetime as _datetime
import typing as _typing
import pyVmomi.vim
import pyVmomi.vmodl
import pyVmomi.sms.provider
import pyVmomi.vim.vm.replication



class DeviceId(pyVmomi.vmodl.DynamicData):
   pass


class FailoverParam(pyVmomi.vmodl.DynamicData):
   class ReplicationGroupData(pyVmomi.vmodl.DynamicData):
      groupId: pyVmomi.vim.vm.replication.ReplicationGroupId
      pitId: _typing.Optional[PointInTimeReplicaId] = None

   class PolicyAssociation(pyVmomi.vmodl.DynamicData):
      id: DeviceId
      policyId: str
      datastore: pyVmomi.vim.Datastore

   isPlanned: bool
   checkOnly: bool
   replicationGroupsToFailover: list[ReplicationGroupData] = []
   policyAssociations: list[PolicyAssociation] = []


class FailoverSuccessResult(GroupOperationResult):
   class RecoveredDiskInfo(pyVmomi.vmodl.DynamicData):
      deviceKey: int
      dsUrl: str
      diskPath: str

   class RecoveredDevice(pyVmomi.vmodl.DynamicData):
      targetDeviceId: _typing.Optional[ReplicaId] = None
      recoveredDeviceId: _typing.Optional[DeviceId] = None
      sourceDeviceId: DeviceId
      info: list[str] = []
      datastore: pyVmomi.vim.Datastore
      recoveredDiskInfo: list[RecoveredDiskInfo] = []
      error: _typing.Optional[pyVmomi.vmodl.MethodFault] = None
      warnings: list[pyVmomi.vmodl.MethodFault] = []

   newState: str
   pitId: _typing.Optional[PointInTimeReplicaId] = None
   pitIdBeforeFailover: _typing.Optional[PointInTimeReplicaId] = None
   recoveredDeviceInfo: list[RecoveredDevice] = []
   timeStamp: _typing.Optional[_datetime.datetime] = None


class FaultDomainInfo(pyVmomi.vim.vm.replication.FaultDomainId):
   name: _typing.Optional[str] = None
   description: _typing.Optional[str] = None
   storageArrayId: _typing.Optional[str] = None
   children: list[pyVmomi.vim.vm.replication.FaultDomainId] = []
   provider: _typing.Optional[pyVmomi.sms.provider.Provider] = None


class GroupErrorResult(GroupOperationResult):
   error: list[pyVmomi.vmodl.MethodFault] = []


class GroupInfo(pyVmomi.vmodl.DynamicData):
   groupId: pyVmomi.vim.vm.replication.ReplicationGroupId


class GroupOperationResult(pyVmomi.vmodl.DynamicData):
   groupId: pyVmomi.vim.vm.replication.ReplicationGroupId
   warning: list[pyVmomi.vmodl.MethodFault] = []


class PointInTimeReplicaId(pyVmomi.vmodl.DynamicData):
   id: str


class PromoteParam(pyVmomi.vmodl.DynamicData):
   isPlanned: bool
   replicationGroupsToPromote: list[pyVmomi.vim.vm.replication.ReplicationGroupId] = []


class QueryPointInTimeReplicaParam(pyVmomi.vmodl.DynamicData):
   class ReplicaQueryIntervalParam(pyVmomi.vmodl.DynamicData):
      fromDate: _typing.Optional[_datetime.datetime] = None
      toDate: _typing.Optional[_datetime.datetime] = None
      number: _typing.Optional[int] = None

   replicaTimeQueryParam: _typing.Optional[ReplicaQueryIntervalParam] = None
   pitName: _typing.Optional[str] = None
   tags: list[str] = []
   preferDetails: _typing.Optional[bool] = None


class QueryPointInTimeReplicaSuccessResult(GroupOperationResult):
   class PointInTimeReplicaInfo(pyVmomi.vmodl.DynamicData):
      id: PointInTimeReplicaId
      pitName: str
      timeStamp: _datetime.datetime
      tags: list[str] = []

   replicaInfo: list[PointInTimeReplicaInfo] = []


class QueryPointInTimeReplicaSummaryResult(GroupOperationResult):
   class ReplicaIntervalQueryResult(pyVmomi.vmodl.DynamicData):
      fromDate: _datetime.datetime
      toDate: _datetime.datetime
      number: int

   intervalResults: list[ReplicaIntervalQueryResult] = []

class QueryReplicationGroupSuccessResult(GroupOperationResult):
   rgInfo: GroupInfo


class QueryReplicationPeerResult(pyVmomi.vmodl.DynamicData):
   sourceDomain: pyVmomi.vim.vm.replication.FaultDomainId
   targetDomain: list[pyVmomi.vim.vm.replication.FaultDomainId] = []
   error: list[pyVmomi.vmodl.MethodFault] = []
   warning: list[pyVmomi.vmodl.MethodFault] = []


class RecoveredTargetGroupMemberInfo(TargetGroupMemberInfo):
   recoveredDeviceId: _typing.Optional[DeviceId] = None


class ReplicaId(pyVmomi.vmodl.DynamicData):
   id: str

class ReplicationState:
   pass


class ReverseReplicationSuccessResult(GroupOperationResult):
   newGroupId: pyVmomi.vim.vm.replication.DeviceGroupId


class SourceGroupInfo(GroupInfo):
   class ReplicationTargetInfo(pyVmomi.vmodl.DynamicData):
      targetGroupId: pyVmomi.vim.vm.replication.ReplicationGroupId
      replicationAgreementDescription: _typing.Optional[str] = None

   name: _typing.Optional[str] = None
   description: _typing.Optional[str] = None
   state: str
   replica: list[ReplicationTargetInfo] = []
   memberInfo: list[SourceGroupMemberInfo] = []


class SourceGroupMemberInfo(pyVmomi.vmodl.DynamicData):
   class TargetDeviceId(pyVmomi.vmodl.DynamicData):
      domainId: pyVmomi.vim.vm.replication.FaultDomainId
      deviceId: ReplicaId

   deviceId: DeviceId
   targetId: list[TargetDeviceId] = []


class SyncReplicationGroupSuccessResult(GroupOperationResult):
   timeStamp: _datetime.datetime
   pitId: _typing.Optional[PointInTimeReplicaId] = None
   pitName: _typing.Optional[str] = None


class TargetGroupInfo(GroupInfo):
   class TargetToSourceInfo(pyVmomi.vmodl.DynamicData):
      sourceGroupId: pyVmomi.vim.vm.replication.ReplicationGroupId
      replicationAgreementDescription: _typing.Optional[str] = None

   sourceInfo: TargetToSourceInfo
   state: str
   devices: list[TargetGroupMemberInfo] = []
   isPromoteCapable: _typing.Optional[bool] = None
   name: _typing.Optional[str] = None


class TargetGroupMemberInfo(pyVmomi.vmodl.DynamicData):
   replicaId: ReplicaId
   sourceId: DeviceId
   targetDatastore: pyVmomi.vim.Datastore

class TestFailoverParam(FailoverParam):
   pass

class VVolId(DeviceId):
   id: str

class VirtualDiskId(DeviceId):
   diskId: str

class VirtualDiskKey(DeviceId):
   vmInstanceUUID: str
   deviceKey: int


class VirtualDiskMoId(DeviceId):
   vcUuid: _typing.Optional[str] = None
   vmMoid: str
   diskKey: str


class VirtualMachineFilePath(VirtualMachineId):
   vcUuid: _typing.Optional[str] = None
   dsUrl: str
   vmxPath: str

class VirtualMachineId(DeviceId):
   pass


class VirtualMachineMoId(VirtualMachineId):
   vcUuid: _typing.Optional[str] = None
   vmMoid: str

class VirtualMachineUUID(VirtualMachineId):
   vmInstanceUUID: str
