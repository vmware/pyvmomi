# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import LACPInfo
from pyVmomi.vim.host import PnicTSOInfo
from pyVmomi.vim.host import VirtualNic

class VsanNetworkDiagnosticsHealthInfo(DynamicData):
   vnicInfo: list[VirtualNic] = []
   pnicTSOInfo: list[PnicTSOInfo] = []
   LACPInfo: list[LACPInfo] = []
