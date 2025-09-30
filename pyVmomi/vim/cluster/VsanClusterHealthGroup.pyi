# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.cluster.VsanClusterHealthResultBase import VsanClusterHealthResultBase

from pyVmomi.vim.cluster.VsanClusterHealthTest import VsanClusterHealthTest

class VsanClusterHealthGroup(DynamicData):
   groupId: str
   groupName: str
   groupHealth: str
   groupTests: list[VsanClusterHealthTest] = []
   groupDetails: list[VsanClusterHealthResultBase] = []
   inProgress: Optional[bool] = None
