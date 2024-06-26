# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import VsanObjectOverallHealth

class VsanFileServiceShareHealthSummary(DynamicData):
   overallHealth: Optional[str] = None
   domainName: Optional[str] = None
   shareUuid: Optional[str] = None
   shareName: Optional[str] = None
   objectHealth: Optional[VsanObjectOverallHealth] = None
   description: Optional[str] = None
   extensible: Optional[bool] = None
