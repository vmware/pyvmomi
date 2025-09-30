# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.cluster.DasConfigInfo import DasConfigInfo

from pyVmomi.vim.cluster.DasVmConfigInfo import DasVmConfigInfo

from pyVmomi.vim.cluster.DrsConfigInfo import DrsConfigInfo

from pyVmomi.vim.cluster.DrsVmConfigInfo import DrsVmConfigInfo

from pyVmomi.vim.cluster.RuleInfo import RuleInfo

class ConfigInfo(DynamicData):
   dasConfig: DasConfigInfo
   dasVmConfig: list[DasVmConfigInfo] = []
   drsConfig: DrsConfigInfo
   drsVmConfig: list[DrsVmConfigInfo] = []
   rule: list[RuleInfo] = []
