# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.host import VsanHclCommonDeviceInfo
from pyVmomi.vim.host import VsanNicRdmaInfo

class VsanHclNicInfo(VsanHclCommonDeviceInfo):
   vmknic: Optional[str] = None
   useByVsan: Optional[bool] = None
   rdmaConfig: Optional[VsanNicRdmaInfo] = None
   vsanHostCompatibility: list[str] = []
   nicLinkSpeedInMbps: Optional[int] = None
