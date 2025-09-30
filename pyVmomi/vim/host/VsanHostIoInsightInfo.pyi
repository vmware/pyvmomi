# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vim.HostSystem import HostSystem

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.host.VsanIoInsightInfo import VsanIoInsightInfo

class VsanHostIoInsightInfo(DynamicData):
   host: HostSystem
   ioinsightWorldId: Optional[long] = None
   faultMessage: Optional[str] = None
   ioinsightInfo: Optional[VsanIoInsightInfo] = None
