# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.cluster.VsanClusterHealthResultBase import VsanClusterHealthResultBase

from pyVmomi.vim.cluster.VsanClusterHealthResultColumnInfo import VsanClusterHealthResultColumnInfo

from pyVmomi.vim.cluster.VsanClusterHealthResultRow import VsanClusterHealthResultRow

class VsanClusterHealthResultTable(VsanClusterHealthResultBase):
   columns: list[VsanClusterHealthResultColumnInfo] = []
   rows: list[VsanClusterHealthResultRow] = []
