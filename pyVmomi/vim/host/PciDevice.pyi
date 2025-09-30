# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import byte
from pyVmomi.VmomiSupport import short

from pyVmomi.vmodl.DynamicData import DynamicData

class PciDevice(DynamicData):
   id: str
   classId: short
   bus: byte
   slot: byte
   physicalSlot: Optional[int] = None
   slotDescription: Optional[str] = None
   function: byte
   vendorId: short
   subVendorId: short
   vendorName: str
   deviceId: short
   subDeviceId: short
   parentBridge: Optional[str] = None
   deviceName: str
   deviceClassName: Optional[str] = None
