# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import MethodFault

from pyVmomi.vim.host import ScsiDisk

class StoragePoolDiskInfo(DynamicData):
   disk: ScsiDisk
   vsanUuid: Optional[str] = None
   error: Optional[MethodFault] = None
   isMounted: Optional[bool] = None
   isEncrypted: Optional[bool] = None
   dekId: Optional[str] = None
   diskType: Optional[str] = None
