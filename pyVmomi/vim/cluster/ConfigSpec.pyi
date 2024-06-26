# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.cluster import DasConfigInfo
from pyVmomi.vim.cluster import DasVmConfigSpec
from pyVmomi.vim.cluster import DrsConfigInfo
from pyVmomi.vim.cluster import DrsVmConfigSpec
from pyVmomi.vim.cluster import RuleSpec

class ConfigSpec(DynamicData):
   dasConfig: Optional[DasConfigInfo] = None
   dasVmConfigSpec: list[DasVmConfigSpec] = []
   drsConfig: Optional[DrsConfigInfo] = None
   drsVmConfigSpec: list[DrsVmConfigSpec] = []
   rulesSpec: list[RuleSpec] = []
