# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.cluster import DasConfigInfo
from pyVmomi.vim.cluster import DasVmConfigInfo
from pyVmomi.vim.cluster import DrsConfigInfo
from pyVmomi.vim.cluster import DrsVmConfigInfo
from pyVmomi.vim.cluster import RuleInfo

class ConfigInfo(DynamicData):
   dasConfig: DasConfigInfo
   dasVmConfig: list[DasVmConfigInfo] = []
   drsConfig: DrsConfigInfo
   drsVmConfig: list[DrsVmConfigInfo] = []
   rule: list[RuleInfo] = []
