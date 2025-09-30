# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.cns.AccessControlSpec import AccessControlSpec

from pyVmomi.vim.vsan.FileShareNetPermission import FileShareNetPermission

class NFSAccessControlSpec(AccessControlSpec):
   netPermission: FileShareNetPermission
   delete: Optional[bool] = None
