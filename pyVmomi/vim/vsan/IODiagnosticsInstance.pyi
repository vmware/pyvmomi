# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.vsan import IODiagnosticsInstanceEvent
from pyVmomi.vim.vsan import IODiagnosticsTarget

class IODiagnosticsInstance(DynamicData):
   name: str
   state: str
   events: list[IODiagnosticsInstanceEvent] = []
   targets: list[IODiagnosticsTarget] = []
   startTime: datetime
   endTime: datetime
   recurrenceName: Optional[str] = None
