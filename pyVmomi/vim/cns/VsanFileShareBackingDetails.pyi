# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import KeyValue

from pyVmomi.vim.cns import FileBackingDetails

from pyVmomi.vim.vsan import FileShareNetPermission

class VsanFileShareBackingDetails(FileBackingDetails):
   name: Optional[str] = None
   accessPoints: list[KeyValue] = []
   permission: list[FileShareNetPermission] = []
