# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vmodl.MethodFault import MethodFault

from pyVmomi.vim.vsan.host.DiskMapping import DiskMapping

from pyVmomi.vim.vsan.host.DiskResult import DiskResult

class DiskMapResult(DynamicData):
   mapping: DiskMapping
   diskResult: list[DiskResult] = []
   error: Optional[MethodFault] = None
