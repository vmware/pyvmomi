# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.cluster.DasConfigInfo import DasConfigInfo

from pyVmomi.vim.cluster.DasVmConfigSpec import DasVmConfigSpec

from pyVmomi.vim.cluster.DrsConfigInfo import DrsConfigInfo

from pyVmomi.vim.cluster.DrsVmConfigSpec import DrsVmConfigSpec

from pyVmomi.vim.cluster.RuleSpec import RuleSpec

class ConfigSpec(DynamicData):
   dasConfig: Optional[DasConfigInfo] = None
   dasVmConfigSpec: list[DasVmConfigSpec] = []
   drsConfig: Optional[DrsConfigInfo] = None
   drsVmConfigSpec: list[DrsVmConfigSpec] = []
   rulesSpec: list[RuleSpec] = []
