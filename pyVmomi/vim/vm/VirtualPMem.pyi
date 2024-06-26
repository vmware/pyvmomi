# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

class VirtualPMem(DynamicData):
   class SnapshotMode(Enum):
      independent_persistent: ClassVar['SnapshotMode'] = 'independent_persistent'
      independent_eraseonrevert: ClassVar['SnapshotMode'] = 'independent_eraseonrevert'

   snapshotMode: Optional[str] = None
