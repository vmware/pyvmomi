# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim.fault import VimFault

class CannotMoveFaultToleranceVm(VimFault):
   class MoveType(Enum):
      resourcePool: ClassVar['MoveType'] = 'resourcePool'
      cluster: ClassVar['MoveType'] = 'cluster'

   moveType: str
   vmName: str
