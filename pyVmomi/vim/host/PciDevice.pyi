# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import byte
from pyVmomi.VmomiSupport import short

from pyVmomi.vmodl import DynamicData

class PciDevice(DynamicData):
   id: str
   classId: short
   bus: byte
   slot: byte
   function: byte
   vendorId: short
   subVendorId: short
   vendorName: str
   deviceId: short
   subDeviceId: short
   parentBridge: Optional[str] = None
   deviceName: str
   deviceClassName: Optional[str] = None
