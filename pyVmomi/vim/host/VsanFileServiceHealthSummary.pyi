# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.host.VsanFileServerHealthSummary import VsanFileServerHealthSummary

from pyVmomi.vim.host.VsanFileServiceBalanceHealth import VsanFileServiceBalanceHealth

from pyVmomi.vim.host.VsanFileServiceRootFsHealth import VsanFileServiceRootFsHealth

from pyVmomi.vim.host.VsanFileServiceShareHealthSummary import VsanFileServiceShareHealthSummary

from pyVmomi.vim.host.VsanResourceHealth import VsanResourceHealth

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
