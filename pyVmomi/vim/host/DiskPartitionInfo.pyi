# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import byte
from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import DiskDimensions

class DiskPartitionInfo(DynamicData):
   class PartitionFormat(Enum):
      gpt: ClassVar['PartitionFormat'] = 'gpt'
      mbr: ClassVar['PartitionFormat'] = 'mbr'
      unknown: ClassVar['PartitionFormat'] = 'unknown'

   class Type(Enum):
      none: ClassVar['Type'] = 'none'
      vmfs: ClassVar['Type'] = 'vmfs'
      linuxNative: ClassVar['Type'] = 'linuxNative'
      linuxSwap: ClassVar['Type'] = 'linuxSwap'
      extended: ClassVar['Type'] = 'extended'
      ntfs: ClassVar['Type'] = 'ntfs'
      vmkDiagnostic: ClassVar['Type'] = 'vmkDiagnostic'
      vffs: ClassVar['Type'] = 'vffs'

   class Partition(DynamicData):
      partition: int
      startSector: long
      endSector: long
      type: str
      guid: Optional[str] = None
      logical: bool
      attributes: byte
      partitionAlignment: Optional[long] = None

   class BlockRange(DynamicData):
      partition: Optional[int] = None
      type: str
      start: DiskDimensions.Lba
      end: DiskDimensions.Lba

   class Specification(DynamicData):
      partitionFormat: Optional[str] = None
      chs: Optional[DiskDimensions.Chs] = None
      totalSectors: Optional[long] = None
      partition: list[Partition] = []

   class Layout(DynamicData):
      total: Optional[DiskDimensions.Lba] = None
      partition: list[BlockRange] = []

   deviceName: str
   spec: Specification
   layout: Layout
