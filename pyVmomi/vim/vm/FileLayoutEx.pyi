# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.vm import Snapshot

class FileLayoutEx(DynamicData):
   class FileType(Enum):
      config: ClassVar['FileType'] = 'config'
      extendedConfig: ClassVar['FileType'] = 'extendedConfig'
      diskDescriptor: ClassVar['FileType'] = 'diskDescriptor'
      diskExtent: ClassVar['FileType'] = 'diskExtent'
      digestDescriptor: ClassVar['FileType'] = 'digestDescriptor'
      digestExtent: ClassVar['FileType'] = 'digestExtent'
      diskReplicationState: ClassVar['FileType'] = 'diskReplicationState'
      log: ClassVar['FileType'] = 'log'
      stat: ClassVar['FileType'] = 'stat'
      namespaceData: ClassVar['FileType'] = 'namespaceData'
      dataSetsDiskModeStore: ClassVar['FileType'] = 'dataSetsDiskModeStore'
      dataSetsVmModeStore: ClassVar['FileType'] = 'dataSetsVmModeStore'
      nvram: ClassVar['FileType'] = 'nvram'
      snapshotData: ClassVar['FileType'] = 'snapshotData'
      snapshotMemory: ClassVar['FileType'] = 'snapshotMemory'
      snapshotList: ClassVar['FileType'] = 'snapshotList'
      snapshotManifestList: ClassVar['FileType'] = 'snapshotManifestList'
      suspend: ClassVar['FileType'] = 'suspend'
      suspendMemory: ClassVar['FileType'] = 'suspendMemory'
      swap: ClassVar['FileType'] = 'swap'
      uwswap: ClassVar['FileType'] = 'uwswap'
      core: ClassVar['FileType'] = 'core'
      screenshot: ClassVar['FileType'] = 'screenshot'
      ftMetadata: ClassVar['FileType'] = 'ftMetadata'
      guestCustomization: ClassVar['FileType'] = 'guestCustomization'

   class FileInfo(DynamicData):
      key: int
      name: str
      type: str
      size: long
      uniqueSize: Optional[long] = None
      backingObjectId: Optional[str] = None
      accessible: Optional[bool] = None

   class DiskUnit(DynamicData):
      fileKey: list[int] = []

   class DiskLayout(DynamicData):
      key: int
      chain: list[DiskUnit] = []

   class SnapshotLayout(DynamicData):
      key: Snapshot
      dataKey: int
      memoryKey: int
      disk: list[DiskLayout] = []

   file: list[FileInfo] = []
   disk: list[DiskLayout] = []
   snapshot: list[SnapshotLayout] = []
   timestamp: datetime
