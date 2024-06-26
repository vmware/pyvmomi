# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vim import SharesInfo

from pyVmomi.vmodl import DynamicData

class NetworkResourcePool(DynamicData):
   class AllocationInfo(DynamicData):
      limit: Optional[long] = None
      shares: Optional[SharesInfo] = None
      priorityTag: Optional[int] = None

   class ConfigSpec(DynamicData):
      key: str
      configVersion: Optional[str] = None
      allocationInfo: Optional[AllocationInfo] = None
      name: Optional[str] = None
      description: Optional[str] = None

   key: str
   name: Optional[str] = None
   description: Optional[str] = None
   configVersion: str
   allocationInfo: AllocationInfo
