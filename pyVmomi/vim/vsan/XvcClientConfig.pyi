# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.vsan.DatastoreSpec import DatastoreSpec

from pyVmomi.vim.vsan.XVCClientInfo import XVCClientInfo

class XvcClientConfig(DatastoreSpec):
   xvcClusters: list[XVCClientInfo] = []
