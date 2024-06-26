# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import Description

from pyVmomi.vmodl import DynamicData

class VirtualDeviceGroups(DynamicData):
   class DeviceGroup(DynamicData):
      groupInstanceKey: int
      deviceInfo: Optional[Description] = None

   class VendorDeviceGroup(DeviceGroup):
      deviceGroupName: str

   deviceGroup: list[DeviceGroup] = []
