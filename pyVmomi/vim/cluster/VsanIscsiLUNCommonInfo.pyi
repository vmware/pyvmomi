# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData

class VsanIscsiLUNCommonInfo(DynamicData):
   class VsanIscsiLUNStatus(Enum):
      Online: ClassVar['VsanIscsiLUNStatus'] = 'Online'
      Offline: ClassVar['VsanIscsiLUNStatus'] = 'Offline'
      VsanIscsiLUNStatus_Unknown: ClassVar['VsanIscsiLUNStatus'] = 'VsanIscsiLUNStatus_Unknown'

   lunId: Optional[int] = None
   alias: Optional[str] = None
   lunSize: long
   status: Optional[str] = None
