# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

class VsanPerfMetricId(DynamicData):
   class VsanPerfSummaryType(Enum):
      average: ClassVar['VsanPerfSummaryType'] = 'average'
      maximum: ClassVar['VsanPerfSummaryType'] = 'maximum'
      minimum: ClassVar['VsanPerfSummaryType'] = 'minimum'
      latest: ClassVar['VsanPerfSummaryType'] = 'latest'
      summation: ClassVar['VsanPerfSummaryType'] = 'summation'
      none: ClassVar['VsanPerfSummaryType'] = 'none'
      VsanPerfSummaryType_Unknown: ClassVar['VsanPerfSummaryType'] = 'VsanPerfSummaryType_Unknown'

   class VsanPerfStatsType(Enum):
      absolute: ClassVar['VsanPerfStatsType'] = 'absolute'
      delta: ClassVar['VsanPerfStatsType'] = 'delta'
      rate: ClassVar['VsanPerfStatsType'] = 'rate'
      VsanPerfStatsType_Unknown: ClassVar['VsanPerfStatsType'] = 'VsanPerfStatsType_Unknown'

   label: str
   group: Optional[str] = None
   rollupType: Optional[str] = None
   statsType: Optional[str] = None
   name: Optional[str] = None
   description: Optional[str] = None
   metricsCollectInterval: Optional[int] = None
