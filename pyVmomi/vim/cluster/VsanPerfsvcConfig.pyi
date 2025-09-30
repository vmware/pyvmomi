# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.vm.ProfileSpec import ProfileSpec

class VsanPerfsvcConfig(DynamicData):
   enabled: bool
   profile: Optional[ProfileSpec] = None
   diagnosticMode: Optional[bool] = None
   verboseMode: Optional[bool] = None
