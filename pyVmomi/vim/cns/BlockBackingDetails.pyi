# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vim.cns import BackingObjectDetails

class BlockBackingDetails(BackingObjectDetails):
   backingDiskId: Optional[str] = None
   backingDiskUrlPath: Optional[str] = None
   backingDiskPath: Optional[str] = None
   backingDiskObjectId: Optional[str] = None
   usedCapacityInMb: Optional[long] = None
