# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.cluster.VsanVsanClusterPcapGroup import VsanVsanClusterPcapGroup

from pyVmomi.vim.host.VsanVsanPcapResult import VsanVsanPcapResult

class VsanVsanClusterPcapResult(DynamicData):
   pkts: list[str] = []
   groups: list[VsanVsanClusterPcapGroup] = []
   issues: list[str] = []
   hostResults: list[VsanVsanPcapResult] = []
