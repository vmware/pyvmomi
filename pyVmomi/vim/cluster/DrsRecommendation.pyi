# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.cluster import DrsMigration

class DrsRecommendation(DynamicData):
   class ReasonCode(Enum):
      fairnessCpuAvg: ClassVar['ReasonCode'] = 'fairnessCpuAvg'
      fairnessMemAvg: ClassVar['ReasonCode'] = 'fairnessMemAvg'
      jointAffin: ClassVar['ReasonCode'] = 'jointAffin'
      antiAffin: ClassVar['ReasonCode'] = 'antiAffin'
      hostMaint: ClassVar['ReasonCode'] = 'hostMaint'

   key: str
   rating: int
   reason: str
   reasonText: str
   migrationList: list[DrsMigration] = []
