# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.cluster.AttemptedVmInfo import AttemptedVmInfo

from pyVmomi.vim.cluster.NotAttemptedVmInfo import NotAttemptedVmInfo

from pyVmomi.vim.cluster.Recommendation import Recommendation

class PowerOnVmResult(DynamicData):
   attempted: list[AttemptedVmInfo] = []
   notAttempted: list[NotAttemptedVmInfo] = []
   recommendations: list[Recommendation] = []
