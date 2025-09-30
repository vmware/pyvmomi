# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.host.DiskPartitionInfo import DiskPartitionInfo

from pyVmomi.vim.host.FileSystemVolume import FileSystemVolume

from pyVmomi.vim.host.ScsiDisk import ScsiDisk

class VffsVolume(FileSystemVolume):
   class Specification(DynamicData):
      devicePath: str
      partition: Optional[DiskPartitionInfo.Specification] = None
      majorVersion: int
      volumeName: str

   majorVersion: int
   version: str
   uuid: str
   extent: list[ScsiDisk.Partition] = []
