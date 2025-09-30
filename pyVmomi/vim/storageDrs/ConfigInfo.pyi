# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.storageDrs.PodConfigInfo import PodConfigInfo

from pyVmomi.vim.storageDrs.VmConfigInfo import VmConfigInfo

class ConfigInfo(DynamicData):
   podConfig: PodConfigInfo
   vmConfig: list[VmConfigInfo] = []
