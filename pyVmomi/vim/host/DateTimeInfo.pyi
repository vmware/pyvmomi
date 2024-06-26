# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import DateTimeSystem
from pyVmomi.vim.host import NtpConfig
from pyVmomi.vim.host import PtpConfig

class DateTimeInfo(DynamicData):
   class Protocol(Enum):
      ntp: ClassVar['Protocol'] = 'ntp'
      ptp: ClassVar['Protocol'] = 'ptp'

   timeZone: DateTimeSystem.TimeZone
   systemClockProtocol: Optional[str] = None
   ntpConfig: Optional[NtpConfig] = None
   ptpConfig: Optional[PtpConfig] = None
   enabled: Optional[bool] = None
   disableEvents: Optional[bool] = None
   disableFallback: Optional[bool] = None
   inFallbackState: Optional[bool] = None
   serviceSync: Optional[bool] = None
   lastSyncTime: Optional[datetime] = None
   remoteNtpServer: Optional[str] = None
   ntpRunTime: Optional[long] = None
   ptpRunTime: Optional[long] = None
   ntpDuration: Optional[str] = None
   ptpDuration: Optional[str] = None
