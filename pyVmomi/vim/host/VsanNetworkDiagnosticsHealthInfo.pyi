# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.host.LACPInfo import LACPInfo

from pyVmomi.vim.host.PnicTSOInfo import PnicTSOInfo

from pyVmomi.vim.host.VirtualNic import VirtualNic

class VsanNetworkDiagnosticsHealthInfo(DynamicData):
   vnicInfo: list[VirtualNic] = []
   pnicTSOInfo: list[PnicTSOInfo] = []
   LACPInfo: list[LACPInfo] = []
