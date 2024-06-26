# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.sms.storage.replication import DeviceId
from pyVmomi.sms.storage.replication import ReplicaId

from pyVmomi.vim.vm.replication import FaultDomainId

class SourceGroupMemberInfo(DynamicData):
   class TargetDeviceId(DynamicData):
      domainId: FaultDomainId
      deviceId: ReplicaId

   deviceId: DeviceId
   targetId: list[TargetDeviceId] = []
