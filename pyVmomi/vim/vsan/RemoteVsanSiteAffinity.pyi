# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.vsan.RemoteVsanSite import RemoteVsanSite

class RemoteVsanSiteAffinity(DynamicData):
   clientSite: Optional[RemoteVsanSite] = None
   serverSite: RemoteVsanSite
