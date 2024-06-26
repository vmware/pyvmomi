# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.vsan.host import VsanObjectSyncState
from pyVmomi.vim.vsan.host import VsanSyncingObjectRecoveryDetails

class VsanSyncingObjectQueryResult(DynamicData):
   totalObjectsToSync: Optional[long] = None
   totalBytesToSync: Optional[long] = None
   totalRecoveryETA: Optional[long] = None
   objects: list[VsanObjectSyncState] = []
   syncingObjectRecoveryDetails: Optional[VsanSyncingObjectRecoveryDetails] = None
