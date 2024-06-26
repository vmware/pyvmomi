# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import DiskDimensions
from pyVmomi.vim.host import MountInfo

class VsanScsiDisk(DynamicData):
   capacity: DiskDimensions.Lba
   usedCapacity: Optional[long] = None
   devicePath: str
   ssd: Optional[bool] = None
   localDisk: Optional[bool] = None
   scsiDiskType: Optional[str] = None
   uuid: str
   operationalState: list[str] = []
   canonicalName: Optional[str] = None
   displayName: Optional[str] = None
   lunType: str
   vendor: Optional[str] = None
   model: Optional[str] = None
   mountInfo: Optional[MountInfo] = None
