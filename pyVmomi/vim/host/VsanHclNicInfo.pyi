# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.host.VsanHclCommonDeviceInfo import VsanHclCommonDeviceInfo

from pyVmomi.vim.host.VsanNicRdmaInfo import VsanNicRdmaInfo

class VsanHclNicInfo(VsanHclCommonDeviceInfo):
   vmknic: Optional[str] = None
   useByVsan: Optional[bool] = None
   rdmaConfig: Optional[VsanNicRdmaInfo] = None
   vsanHostCompatibility: list[str] = []
   nicLinkSpeedInMbps: Optional[int] = None
