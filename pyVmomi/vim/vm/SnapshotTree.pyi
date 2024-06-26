# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.vim import VirtualMachine

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.vm import Snapshot

class SnapshotTree(DynamicData):
   snapshot: Snapshot
   vm: VirtualMachine
   name: str
   description: str
   id: int
   createTime: datetime
   state: VirtualMachine.PowerState
   quiesced: bool
   backupManifest: Optional[str] = None
   childSnapshotList: list[SnapshotTree] = []
   replaySupported: Optional[bool] = None
