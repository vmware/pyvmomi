# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import VsanFileServerHealthSummary
from pyVmomi.vim.host import VsanFileServiceBalanceHealth
from pyVmomi.vim.host import VsanFileServiceRootFsHealth
from pyVmomi.vim.host import VsanFileServiceShareHealthSummary
from pyVmomi.vim.host import VsanResourceHealth

class VsanFileServiceHealthSummary(DynamicData):
   hostname: Optional[str] = None
   overallHealth: Optional[str] = None
   enabled: Optional[bool] = None
   vdfsdStatus: Optional[VsanResourceHealth] = None
   fsvmStatus: Optional[VsanResourceHealth] = None
   rootFsStatus: Optional[VsanFileServiceRootFsHealth] = None
   fileServerHealth: list[VsanFileServerHealthSummary] = []
   fileShareHealth: list[VsanFileServiceShareHealthSummary] = []
   balanceStatus: Optional[VsanFileServiceBalanceHealth] = None
   hostLoadStatus: Optional[VsanResourceHealth] = None
