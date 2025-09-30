# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.host.ScsiDisk import ScsiDisk

class UnresolvedVmfsExtent(DynamicData):
   class UnresolvedReason(Enum):
      diskIdMismatch: ClassVar['UnresolvedReason'] = 'diskIdMismatch'
      uuidConflict: ClassVar['UnresolvedReason'] = 'uuidConflict'

   device: ScsiDisk.Partition
   devicePath: str
   vmfsUuid: str
   isHeadExtent: bool
   ordinal: int
   startBlock: int
   endBlock: int
   reason: str
