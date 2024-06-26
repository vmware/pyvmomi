# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

class VsanPerfThreshold(DynamicData):
   class VsanPerfThresholdDirectionType(Enum):
      upper: ClassVar['VsanPerfThresholdDirectionType'] = 'upper'
      lower: ClassVar['VsanPerfThresholdDirectionType'] = 'lower'
      VsanPerfThresholdDirectionType_Unknown: ClassVar['VsanPerfThresholdDirectionType'] = 'VsanPerfThresholdDirectionType_Unknown'

   direction: str
   yellow: Optional[str] = None
   red: Optional[str] = None
