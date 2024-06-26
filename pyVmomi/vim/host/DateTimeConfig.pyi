# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import NtpConfig
from pyVmomi.vim.host import PtpConfig

class DateTimeConfig(DynamicData):
   timeZone: Optional[str] = None
   ntpConfig: Optional[NtpConfig] = None
   ptpConfig: Optional[PtpConfig] = None
   protocol: Optional[str] = None
   enabled: Optional[bool] = None
   disableEvents: Optional[bool] = None
   disableFallback: Optional[bool] = None
   resetToFactoryDefaults: Optional[bool] = None
