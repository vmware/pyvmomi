# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.vm import Snapshot

class FileLayout(DynamicData):
   class DiskLayout(DynamicData):
      key: int
      diskFile: list[str] = []

   class SnapshotLayout(DynamicData):
      key: Snapshot
      snapshotFile: list[str] = []

   configFile: list[str] = []
   logFile: list[str] = []
   disk: list[DiskLayout] = []
   snapshot: list[SnapshotLayout] = []
   swapFile: Optional[str] = None
