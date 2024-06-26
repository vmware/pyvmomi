# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.cluster import VsanVsanClusterPcapGroup

from pyVmomi.vim.host import VsanVsanPcapResult

class VsanVsanClusterPcapResult(DynamicData):
   pkts: list[str] = []
   groups: list[VsanVsanClusterPcapGroup] = []
   issues: list[str] = []
   hostResults: list[VsanVsanPcapResult] = []
