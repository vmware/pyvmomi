# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim.fault.ReplicationVmFault import ReplicationVmFault

class ReplicationVmInProgressFault(ReplicationVmFault):
   class Activity(Enum):
      fullSync: ClassVar['Activity'] = 'fullSync'
      delta: ClassVar['Activity'] = 'delta'

   requestedActivity: str
   inProgressActivity: str
