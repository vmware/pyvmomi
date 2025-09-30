# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.cluster.VmOrchestrationInfo import VmOrchestrationInfo

from pyVmomi.vim.option.ArrayUpdateSpec import ArrayUpdateSpec

class VmOrchestrationSpec(ArrayUpdateSpec):
   info: Optional[VmOrchestrationInfo] = None
