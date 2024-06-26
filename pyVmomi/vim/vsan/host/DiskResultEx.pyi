# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import MethodFault

from pyVmomi.vim.vsan.host import DiskResult

class DiskResultEx(DiskResult):
   vsanDirectTagged: bool
   storagePoolDiskState: Optional[str] = None
   storagePoolDiskError: Optional[MethodFault] = None
   isCapacityFlash: Optional[bool] = None
