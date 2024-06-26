# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.cluster import VsanPerfMetricId
from pyVmomi.vim.cluster import VsanPerfThreshold

class VsanPerfGraph(DynamicData):
   class VsanPerfStatsUnitType(Enum):
      number: ClassVar['VsanPerfStatsUnitType'] = 'number'
      time_ms: ClassVar['VsanPerfStatsUnitType'] = 'time_ms'
      percentage: ClassVar['VsanPerfStatsUnitType'] = 'percentage'
      size_bytes: ClassVar['VsanPerfStatsUnitType'] = 'size_bytes'
      rate_bytes: ClassVar['VsanPerfStatsUnitType'] = 'rate_bytes'
      permille: ClassVar['VsanPerfStatsUnitType'] = 'permille'
      time_s: ClassVar['VsanPerfStatsUnitType'] = 'time_s'
      time_us: ClassVar['VsanPerfStatsUnitType'] = 'time_us'
      time_ns: ClassVar['VsanPerfStatsUnitType'] = 'time_ns'
      VsanPerfStatsUnitType_Unknown: ClassVar['VsanPerfStatsUnitType'] = 'VsanPerfStatsUnitType_Unknown'

   id: str
   metrics: list[VsanPerfMetricId] = []
   unit: str
   threshold: Optional[VsanPerfThreshold] = None
   name: Optional[str] = None
   description: Optional[str] = None
   secondGraph: Optional[VsanPerfGraph] = None
