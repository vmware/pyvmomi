# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import HostSystem

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.vsan.host import AddStoragePoolDiskSpec
from pyVmomi.vim.vsan.host import DiskMapping

class VsanWitnessSpec(DynamicData):
   host: HostSystem
   preferredFaultDomainName: str
   diskMapping: Optional[DiskMapping] = None
   storagePoolSpec: Optional[AddStoragePoolDiskSpec] = None
