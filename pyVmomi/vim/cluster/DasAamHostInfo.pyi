# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.cluster.DasAamNodeState import DasAamNodeState

from pyVmomi.vim.cluster.DasHostInfo import DasHostInfo

class DasAamHostInfo(DasHostInfo):
   hostDasState: list[DasAamNodeState] = []
   primaryHosts: list[str] = []
