# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.storageDrs import PodConfigInfo
from pyVmomi.vim.storageDrs import VmConfigInfo

class ConfigInfo(DynamicData):
   podConfig: PodConfigInfo
   vmConfig: list[VmConfigInfo] = []
