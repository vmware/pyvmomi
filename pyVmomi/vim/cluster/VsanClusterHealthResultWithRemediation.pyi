# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.cluster import VsanClusterHealthExternalLink
from pyVmomi.vim.cluster import VsanClusterHealthResultBase
from pyVmomi.vim.cluster import VsanClusterHealthResultTable
from pyVmomi.vim.cluster import VsanHealthTroubleshooting

class VsanClusterHealthResultWithRemediation(VsanClusterHealthResultBase):
   issueDescription: Optional[str] = None
   issueDetail: list[VsanClusterHealthResultTable] = []
   troubleshooting: Optional[VsanHealthTroubleshooting] = None
   additionalResources: list[VsanClusterHealthExternalLink] = []
