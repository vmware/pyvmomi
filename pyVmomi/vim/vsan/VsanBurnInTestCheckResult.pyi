# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.vsan.VsanBurnInTest import VsanBurnInTest

class VsanBurnInTestCheckResult(DynamicData):
   passedTests: list[VsanBurnInTest] = []
   notPerformedTests: list[VsanBurnInTest] = []
   failedTests: list[VsanBurnInTest] = []
