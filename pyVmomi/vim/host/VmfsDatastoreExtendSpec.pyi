# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vim.host.DiskPartitionInfo import DiskPartitionInfo

from pyVmomi.vim.host.ScsiDisk import ScsiDisk

from pyVmomi.vim.host.VmfsDatastoreSpec import VmfsDatastoreSpec

class VmfsDatastoreExtendSpec(VmfsDatastoreSpec):
   partition: DiskPartitionInfo.Specification
   extent: list[ScsiDisk.Partition] = []
