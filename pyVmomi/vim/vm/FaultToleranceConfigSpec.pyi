# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.vm.FaultToleranceMetaSpec import FaultToleranceMetaSpec

from pyVmomi.vim.vm.FaultToleranceVMConfigSpec import FaultToleranceVMConfigSpec

class FaultToleranceConfigSpec(DynamicData):
   metaDataPath: Optional[FaultToleranceMetaSpec] = None
   secondaryVmSpec: Optional[FaultToleranceVMConfigSpec] = None
   metroFtEnabled: Optional[bool] = None
   metroFtHostGroup: Optional[str] = None
