# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl.fault import InvalidArgument

class InvalidDasConfigArgument(InvalidArgument):
   class EntryForInvalidArgument(Enum):
      admissionControl: ClassVar['EntryForInvalidArgument'] = 'admissionControl'
      userHeartbeatDs: ClassVar['EntryForInvalidArgument'] = 'userHeartbeatDs'
      vmConfig: ClassVar['EntryForInvalidArgument'] = 'vmConfig'

   entry: Optional[str] = None
   clusterName: Optional[str] = None
