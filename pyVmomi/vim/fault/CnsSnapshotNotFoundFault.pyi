# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.cns import SnapshotId
from pyVmomi.vim.cns import VolumeId

from pyVmomi.vim.fault import CnsFault

class CnsSnapshotNotFoundFault(CnsFault):
   volumeId: Optional[VolumeId] = None
   SnapshotId: SnapshotId
