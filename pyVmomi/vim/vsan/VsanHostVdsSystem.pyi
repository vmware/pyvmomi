# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject
from pyVmomi.VmomiSupport import long

from pyVmomi.vim.vsan.VsanVmVdsMigrationSpec import VsanVmVdsMigrationSpec

class VsanHostVdsSystem(ManagedObject):
   def VsanMigrateVmsToVds(self, vmConfigSpecs: list[VsanVmVdsMigrationSpec], vdsUuid: str, timeoutSec: long, revert: Optional[bool]) -> str: ...
   def VsanCompleteMigrateVmsToVds(self, jobId: str, newState: str) -> None: ...
