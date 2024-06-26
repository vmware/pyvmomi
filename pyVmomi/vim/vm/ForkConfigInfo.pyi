# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

class ForkConfigInfo(DynamicData):
   class ChildType(Enum):
      none: ClassVar['ChildType'] = 'none'
      persistent: ClassVar['ChildType'] = 'persistent'
      nonpersistent: ClassVar['ChildType'] = 'nonpersistent'

   parentEnabled: Optional[bool] = None
   childForkGroupId: Optional[str] = None
   parentForkGroupId: Optional[str] = None
   childType: Optional[str] = None
