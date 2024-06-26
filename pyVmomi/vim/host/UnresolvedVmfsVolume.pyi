# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import UnresolvedVmfsExtent

class UnresolvedVmfsVolume(DynamicData):
   class ResolveStatus(DynamicData):
      resolvable: bool
      incompleteExtents: Optional[bool] = None
      multipleCopies: Optional[bool] = None

   extent: list[UnresolvedVmfsExtent] = []
   vmfsLabel: str
   vmfsUuid: str
   totalBlocks: int
   resolveStatus: ResolveStatus
