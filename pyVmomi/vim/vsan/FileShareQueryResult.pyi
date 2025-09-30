# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.vsan.FileShare import FileShare

class FileShareQueryResult(DynamicData):
   fileShares: list[FileShare] = []
   nextOffset: Optional[str] = None
   totalShareCount: Optional[long] = None
   maxShareCount: Optional[long] = None
