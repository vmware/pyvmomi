# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.host import DiskPartitionInfo
from pyVmomi.vim.host import ScsiDisk
from pyVmomi.vim.host import VmfsDatastoreSpec
from pyVmomi.vim.host import VmfsVolume

class VmfsDatastoreCreateSpec(VmfsDatastoreSpec):
   partition: DiskPartitionInfo.Specification
   vmfs: VmfsVolume.Specification
   extent: list[ScsiDisk.Partition] = []
