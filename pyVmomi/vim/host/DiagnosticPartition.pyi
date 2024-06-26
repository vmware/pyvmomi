# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import DiskPartitionInfo
from pyVmomi.vim.host import ScsiDisk

class DiagnosticPartition(DynamicData):
   class StorageType(Enum):
      directAttached: ClassVar['StorageType'] = 'directAttached'
      networkAttached: ClassVar['StorageType'] = 'networkAttached'

   class DiagnosticType(Enum):
      singleHost: ClassVar['DiagnosticType'] = 'singleHost'
      multiHost: ClassVar['DiagnosticType'] = 'multiHost'

   class CreateOption(DynamicData):
      storageType: str
      diagnosticType: str
      disk: ScsiDisk

   class CreateSpec(DynamicData):
      storageType: str
      diagnosticType: str
      id: ScsiDisk.Partition
      partition: DiskPartitionInfo.Specification
      active: Optional[bool] = None

   class CreateDescription(DynamicData):
      layout: DiskPartitionInfo.Layout
      diskUuid: str
      spec: CreateSpec

   storageType: str
   diagnosticType: str
   slots: int
   id: ScsiDisk.Partition
