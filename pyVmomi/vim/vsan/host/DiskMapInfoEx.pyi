# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.vsan import DataEfficiencyConfig
from pyVmomi.vim.vsan import DataEncryptionConfig

from pyVmomi.vim.vsan.host import DiskMapping

class DiskMapInfoEx(DynamicData):
   mapping: DiskMapping
   isMounted: bool
   unlockedEncrypted: Optional[bool] = None
   isAllFlash: bool
   isDataEfficiency: Optional[bool] = None
   encryptionInfo: Optional[DataEncryptionConfig] = None
   dataEfficiencyConfig: Optional[DataEfficiencyConfig] = None
   diskgroupCapability: list[str] = []
