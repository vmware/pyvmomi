# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vim.VirtualDiskManager import VirtualDiskManager

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.host.VsanVmdkIOLoadSpec import VsanVmdkIOLoadSpec

class VsanVmdkLoadTestSpec(DynamicData):
   vmdkCreateSpec: Optional[VirtualDiskManager.FileBackedVirtualDiskSpec] = None
   vmdkIOSpec: Optional[VsanVmdkIOLoadSpec] = None
   vmdkIOSpecSequence: list[VsanVmdkIOLoadSpec] = []
   stepDurationSec: Optional[long] = None
