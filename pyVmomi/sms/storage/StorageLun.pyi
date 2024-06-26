# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData

from pyVmomi.sms.storage import BackingConfig

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
