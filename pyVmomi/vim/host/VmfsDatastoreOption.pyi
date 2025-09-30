# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.host.DiskPartitionInfo import DiskPartitionInfo

from pyVmomi.vim.host.VmfsDatastoreSpec import VmfsDatastoreSpec

class VmfsDatastoreOption(DynamicData):
   class Info(DynamicData):
      layout: DiskPartitionInfo.Layout
      partitionFormatChange: Optional[bool] = None

   class SingleExtentInfo(Info):
      vmfsExtent: DiskPartitionInfo.BlockRange

   class AllExtentInfo(SingleExtentInfo):
      pass

   class MultipleExtentInfo(Info):
      vmfsExtent: list[DiskPartitionInfo.BlockRange] = []

   info: Info
   spec: VmfsDatastoreSpec
