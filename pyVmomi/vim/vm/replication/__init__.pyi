# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import pyVmomi.vmodl



class DeviceGroupId(pyVmomi.vmodl.DynamicData):
   id: str


class FaultDomainId(pyVmomi.vmodl.DynamicData):
   id: str


class ReplicationGroupId(pyVmomi.vmodl.DynamicData):
   faultDomainId: FaultDomainId
   deviceGroupId: DeviceGroupId


class ReplicationSpec(pyVmomi.vmodl.DynamicData):
   replicationGroupId: ReplicationGroupId
