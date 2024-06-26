# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import DiskDimensions
from pyVmomi.vim.host import ScsiLun

from pyVmomi.vim.vsan.host import VsanDiskInfo

class ScsiDisk(ScsiLun):
   class Partition(DynamicData):
      diskName: str
      partition: int

   class ScsiDiskType(Enum):
      native512: ClassVar['ScsiDiskType'] = 'native512'
      emulated512: ClassVar['ScsiDiskType'] = 'emulated512'
      native4k: ClassVar['ScsiDiskType'] = 'native4k'
      SoftwareEmulated4k: ClassVar['ScsiDiskType'] = 'SoftwareEmulated4k'
      unknown: ClassVar['ScsiDiskType'] = 'unknown'

   capacity: DiskDimensions.Lba
   devicePath: str
   ssd: Optional[bool] = None
   localDisk: Optional[bool] = None
   physicalLocation: list[str] = []
   emulatedDIXDIFEnabled: Optional[bool] = None
   vsanDiskInfo: Optional[VsanDiskInfo] = None
   scsiDiskType: Optional[str] = None
   usedByMemoryTiering: Optional[bool] = None
