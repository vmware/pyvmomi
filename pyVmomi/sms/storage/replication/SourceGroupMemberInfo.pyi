# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.sms.storage.replication.DeviceId import DeviceId

from pyVmomi.sms.storage.replication.ReplicaId import ReplicaId

from pyVmomi.vim.vm.replication.FaultDomainId import FaultDomainId

class SourceGroupMemberInfo(DynamicData):
   class TargetDeviceId(DynamicData):
      domainId: FaultDomainId
      deviceId: ReplicaId

   deviceId: DeviceId
   targetId: list[TargetDeviceId] = []
