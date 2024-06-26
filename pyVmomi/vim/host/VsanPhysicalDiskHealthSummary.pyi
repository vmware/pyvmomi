# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import MethodFault

from pyVmomi.vim.host import VsanPhysicalDiskHealth
from pyVmomi.vim.host import VsanResourceHealth

class VsanPhysicalDiskHealthSummary(DynamicData):
   overallHealth: str
   heapsWithIssues: list[VsanResourceHealth] = []
   slabsWithIssues: list[VsanResourceHealth] = []
   disks: list[VsanPhysicalDiskHealth] = []
   componentsWithIssues: list[VsanResourceHealth] = []
   hostname: Optional[str] = None
   hostDedupScope: Optional[int] = None
   error: Optional[MethodFault] = None
