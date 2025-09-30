# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl.DynamicData import DynamicData

class VsanSyncingObjectFilter(DynamicData):
   resyncType: Optional[str] = None
   resyncStatus: Optional[str] = None
   numberOfObjects: Optional[long] = None
   offset: Optional[long] = None
   includeDedupObject: Optional[bool] = None
