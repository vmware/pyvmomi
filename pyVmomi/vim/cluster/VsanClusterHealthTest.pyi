# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.cluster.VsanClusterHealthAction import VsanClusterHealthAction

from pyVmomi.vim.cluster.VsanClusterHealthResultBase import VsanClusterHealthResultBase

from pyVmomi.vim.cluster.VsanHealthCorrelation import VsanHealthCorrelation

from pyVmomi.vim.cluster.VsanHistoricalHealthTest import VsanHistoricalHealthTest

class VsanClusterHealthTest(DynamicData):
   testId: Optional[str] = None
   testName: Optional[str] = None
   testDescription: Optional[str] = None
   testShortDescription: Optional[str] = None
   testHealthyEntities: Optional[int] = None
   testAllEntities: Optional[int] = None
   testHealth: Optional[str] = None
   testDetails: list[VsanClusterHealthResultBase] = []
   testActions: list[VsanClusterHealthAction] = []
   historicalResults: list[VsanHistoricalHealthTest] = []
   testCorrelation: Optional[VsanHealthCorrelation] = None
   reducedScore: Optional[int] = None
   category: Optional[str] = None
   riskIfNotFix: Optional[str] = None
   lastStatusChangeTime: Optional[datetime] = None
