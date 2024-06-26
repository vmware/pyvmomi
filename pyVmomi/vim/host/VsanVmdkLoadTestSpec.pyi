# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vim import VirtualDiskManager

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import VsanVmdkIOLoadSpec

class VsanVmdkLoadTestSpec(DynamicData):
   vmdkCreateSpec: Optional[VirtualDiskManager.FileBackedVirtualDiskSpec] = None
   vmdkIOSpec: Optional[VsanVmdkIOLoadSpec] = None
   vmdkIOSpecSequence: list[VsanVmdkIOLoadSpec] = []
   stepDurationSec: Optional[long] = None
