# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.ext.ManagedByInfo import ManagedByInfo

from pyVmomi.vim.vApp.EntityConfigInfo import EntityConfigInfo

from pyVmomi.vim.vApp.VmConfigInfo import VmConfigInfo

class VAppConfigInfo(VmConfigInfo):
   entityConfig: list[EntityConfigInfo] = []
   annotation: str
   instanceUuid: Optional[str] = None
   managedBy: Optional[ManagedByInfo] = None
