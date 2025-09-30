# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.cluster.VsanClusterHealthExternalLink import VsanClusterHealthExternalLink

from pyVmomi.vim.cluster.VsanClusterHealthResultBase import VsanClusterHealthResultBase

from pyVmomi.vim.cluster.VsanClusterHealthResultTable import VsanClusterHealthResultTable

from pyVmomi.vim.cluster.VsanHealthTroubleshooting import VsanHealthTroubleshooting

class VsanClusterHealthResultWithRemediation(VsanClusterHealthResultBase):
   issueDescription: Optional[str] = None
   issueDetail: list[VsanClusterHealthResultTable] = []
   troubleshooting: Optional[VsanHealthTroubleshooting] = None
   additionalResources: list[VsanClusterHealthExternalLink] = []
