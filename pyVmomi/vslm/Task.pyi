# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import NoReturn
from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vslm import TaskInfo

class Task(ManagedObject):
   def QueryResult(self) -> Optional[object]: ...
   def QueryInfo(self) -> TaskInfo: ...
   def Cancel(self) -> NoReturn: ...
