# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import VsanHostIoInsightInfo

class VsanIoInsightInstance(DynamicData):
   runName: str
   state: Optional[str] = None
   startTime: Optional[datetime] = None
   endTime: Optional[datetime] = None
   hostsIoInsightInfo: list[VsanHostIoInsightInfo] = []
   hostUuids: list[str] = []
   vmUuids: list[str] = []
