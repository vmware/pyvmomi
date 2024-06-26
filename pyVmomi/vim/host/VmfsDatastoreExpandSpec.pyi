# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vim.host import DiskPartitionInfo
from pyVmomi.vim.host import ScsiDisk
from pyVmomi.vim.host import VmfsDatastoreSpec

class VmfsDatastoreExpandSpec(VmfsDatastoreSpec):
   partition: DiskPartitionInfo.Specification
   extent: ScsiDisk.Partition
