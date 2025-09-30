# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.vsan.cluster.ConfigInfo import ConfigInfo

class VsanClusterConfig(DynamicData):
   config: ConfigInfo
   name: str
   hosts: list[str] = []
   toBeDeleted: Optional[bool] = None
