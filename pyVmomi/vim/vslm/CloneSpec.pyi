# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.KeyValue import KeyValue

from pyVmomi.vim.vslm.MigrateSpec import MigrateSpec

class CloneSpec(MigrateSpec):
   name: str
   keepAfterDeleteVm: Optional[bool] = None
   metadata: list[KeyValue] = []
