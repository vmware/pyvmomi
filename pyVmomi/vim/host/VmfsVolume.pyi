# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import FileSystemVolume
from pyVmomi.vim.host import ForceMountedInfo
from pyVmomi.vim.host import ScsiDisk

from pyVmomi.vim.option import LongOption

class VmfsVolume(FileSystemVolume):
   class Specification(DynamicData):
      extent: ScsiDisk.Partition
      blockSizeMb: Optional[int] = None
      majorVersion: int
      volumeName: str
      blockSize: Optional[int] = None
      unmapGranularity: Optional[int] = None
      unmapPriority: Optional[str] = None
      unmapBandwidthSpec: Optional[UnmapBandwidthSpec] = None

   class UnmapBandwidthSpec(DynamicData):
      policy: str
      fixedValue: long
      dynamicMin: long
      dynamicMax: long

   class UnmapPriority(Enum):
      none: ClassVar['UnmapPriority'] = 'none'
      low: ClassVar['UnmapPriority'] = 'low'

   class UnmapBandwidthPolicy(Enum):
      fixed: ClassVar['UnmapBandwidthPolicy'] = 'fixed'
      dynamic: ClassVar['UnmapBandwidthPolicy'] = 'dynamic'

   class ConfigOption(DynamicData):
      blockSizeOption: int
      unmapGranularityOption: list[int] = []
      unmapBandwidthFixedValue: Optional[LongOption] = None
      unmapBandwidthDynamicMin: Optional[LongOption] = None
      unmapBandwidthDynamicMax: Optional[LongOption] = None
      unmapBandwidthIncrement: Optional[long] = None
      unmapBandwidthUltraLow: Optional[long] = None

   blockSizeMb: int
   blockSize: Optional[int] = None
   unmapGranularity: Optional[int] = None
   unmapPriority: Optional[str] = None
   unmapBandwidthSpec: Optional[UnmapBandwidthSpec] = None
   maxBlocks: int
   majorVersion: int
   version: str
   uuid: str
   extent: list[ScsiDisk.Partition] = []
   vmfsUpgradable: bool
   forceMountedInfo: Optional[ForceMountedInfo] = None
   ssd: Optional[bool] = None
   local: Optional[bool] = None
   scsiDiskType: Optional[str] = None
