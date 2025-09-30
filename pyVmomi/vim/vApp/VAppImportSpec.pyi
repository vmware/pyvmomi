# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.ImportSpec import ImportSpec

from pyVmomi.vim.ResourceConfigSpec import ResourceConfigSpec

from pyVmomi.vim.vApp.VAppConfigSpec import VAppConfigSpec

class VAppImportSpec(ImportSpec):
   name: str
   vAppConfigSpec: VAppConfigSpec
   resourcePoolSpec: ResourceConfigSpec
   child: list[ImportSpec] = []
