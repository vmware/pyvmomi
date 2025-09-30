# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.cns.SnapshotId import SnapshotId

from pyVmomi.vim.cns.VolumeId import VolumeId

class SnapshotDeleteSpec(DynamicData):
   volumeId: VolumeId
   snapshotId: SnapshotId
