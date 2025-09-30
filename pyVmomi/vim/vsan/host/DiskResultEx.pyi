# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.MethodFault import MethodFault

from pyVmomi.vim.vsan.host.DiskResult import DiskResult

class DiskResultEx(DiskResult):
   vsanDirectTagged: bool
   storagePoolDiskState: Optional[str] = None
   storagePoolDiskError: Optional[MethodFault] = None
   isCapacityFlash: Optional[bool] = None
