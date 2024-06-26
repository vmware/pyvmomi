# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.vsan.host import DiskMapInfoEx
from pyVmomi.vim.vsan.host import StoragePoolInfo
from pyVmomi.vim.vsan.host import VsanDirectStorage
from pyVmomi.vim.vsan.host import VsanManagedPMemInfo

class VsanManagedDisksInfo(DynamicData):
   vSANDirectDisks: list[VsanDirectStorage] = []
   vSANDiskMapInfo: list[DiskMapInfoEx] = []
   vSANPMemInfo: Optional[VsanManagedPMemInfo] = None
   storagePools: list[StoragePoolInfo] = []
