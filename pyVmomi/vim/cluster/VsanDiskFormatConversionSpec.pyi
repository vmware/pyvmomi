# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.vsan import DataEfficiencyConfig
from pyVmomi.vim.vsan import DataEncryptionConfig

class VsanDiskFormatConversionSpec(DynamicData):
   dataEfficiencyConfig: Optional[DataEfficiencyConfig] = None
   dataEncryptionConfig: Optional[DataEncryptionConfig] = None
   skipHostRemediation: Optional[bool] = None
   allowDataMovement: Optional[bool] = None
