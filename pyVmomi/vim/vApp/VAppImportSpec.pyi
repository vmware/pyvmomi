# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import ImportSpec
from pyVmomi.vim import ResourceConfigSpec

from pyVmomi.vim.vApp import VAppConfigSpec

class VAppImportSpec(ImportSpec):
   name: str
   vAppConfigSpec: VAppConfigSpec
   resourcePoolSpec: ResourceConfigSpec
   child: list[ImportSpec] = []
