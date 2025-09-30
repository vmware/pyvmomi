# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.cns.SnapshotId import SnapshotId

from pyVmomi.vim.cns.VolumeId import VolumeId

from pyVmomi.vim.cns.VolumeSource import VolumeSource

class SnapshotVolumeSource(VolumeSource):
   volumeId: Optional[VolumeId] = None
   snapshotId: Optional[SnapshotId] = None
