# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.sms.storage.BackingConfig import BackingConfig

class StorageLun(DynamicData):
   uuid: str
   vSphereLunIdentifier: str
   vendorDisplayName: str
   capacityInMB: long
   usedSpaceInMB: long
   lunThinProvisioned: bool
   alternateIdentifier: list[str] = []
   drsManagementPermitted: bool
   thinProvisioningStatus: str
   backingConfig: Optional[BackingConfig] = None
