# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.vm import FaultToleranceMetaSpec
from pyVmomi.vim.vm import FaultToleranceVMConfigSpec

class FaultToleranceConfigSpec(DynamicData):
   metaDataPath: Optional[FaultToleranceMetaSpec] = None
   secondaryVmSpec: Optional[FaultToleranceVMConfigSpec] = None
   metroFtEnabled: Optional[bool] = None
   metroFtHostGroup: Optional[str] = None
