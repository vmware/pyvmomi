# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import MethodFault

from pyVmomi.vim.vsan.host import DiskMapping
from pyVmomi.vim.vsan.host import DiskResult

class DiskMapResult(DynamicData):
   mapping: DiskMapping
   diskResult: list[DiskResult] = []
   error: Optional[MethodFault] = None
