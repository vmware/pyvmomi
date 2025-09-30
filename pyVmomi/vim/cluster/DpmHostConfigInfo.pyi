# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.HostSystem import HostSystem

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.cluster.DpmConfigInfo import DpmConfigInfo

class DpmHostConfigInfo(DynamicData):
   key: HostSystem
   enabled: Optional[bool] = None
   behavior: Optional[DpmConfigInfo.DpmBehavior] = None
