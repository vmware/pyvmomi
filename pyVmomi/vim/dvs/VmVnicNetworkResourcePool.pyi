# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vim import VirtualMachine

from pyVmomi.vmodl import DynamicData

class VmVnicNetworkResourcePool(DynamicData):
   class ResourceAllocation(DynamicData):
      reservationQuota: Optional[long] = None

   class ConfigSpec(DynamicData):
      operation: str
      key: Optional[str] = None
      configVersion: Optional[str] = None
      allocationInfo: Optional[ResourceAllocation] = None
      name: Optional[str] = None
      description: Optional[str] = None

   class VnicAllocatedResource(DynamicData):
      vm: VirtualMachine
      vnicKey: str
      reservation: Optional[long] = None

   class RuntimeInfo(DynamicData):
      key: str
      name: Optional[str] = None
      capacity: Optional[int] = None
      usage: Optional[int] = None
      available: Optional[int] = None
      status: str
      allocatedResource: list[VnicAllocatedResource] = []

   key: str
   name: Optional[str] = None
   description: Optional[str] = None
   configVersion: str
   allocationInfo: Optional[ResourceAllocation] = None
