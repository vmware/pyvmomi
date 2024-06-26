# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.vsan import IODiagnosticsTarget

class VsanIOTripAnalyzerRecurrence(DynamicData):
   name: Optional[str] = None
   targets: list[IODiagnosticsTarget] = []
   startTime: datetime
   endTime: Optional[datetime] = None
   duration: long
   interval: long
   status: str
