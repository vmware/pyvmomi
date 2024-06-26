# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import HostSystem
from pyVmomi.vim import ManagedEntity

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.cluster import DasAdmissionControlInfo

class FailoverHostAdmissionControlInfo(DasAdmissionControlInfo):
   class HostStatus(DynamicData):
      host: HostSystem
      status: ManagedEntity.Status

   hostStatus: list[HostStatus] = []
