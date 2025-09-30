# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.vsan.FileShareConfig import FileShareConfig

from pyVmomi.vim.vsan.FileShareRuntimeInfo import FileShareRuntimeInfo

class FileShare(DynamicData):
   uuid: str
   config: Optional[FileShareConfig] = None
   runtime: Optional[FileShareRuntimeInfo] = None
