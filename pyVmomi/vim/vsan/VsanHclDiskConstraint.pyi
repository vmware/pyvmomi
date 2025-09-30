# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.vsan.VsanHclDeviceConstraint import VsanHclDeviceConstraint

from pyVmomi.vim.vsan.VsanHclMinFwConstraint import VsanHclMinFwConstraint

class VsanHclDiskConstraint(DynamicData):
   productId: str
   vendor: str
   constraints: list[VsanHclMinFwConstraint] = []
   pcieConstraints: list[VsanHclDeviceConstraint] = []
   partNumber: Optional[str] = None
