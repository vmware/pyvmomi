# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

class FcoeConfig(DynamicData):
   class VlanRange(DynamicData):
      vlanLow: int
      vlanHigh: int

   class FcoeCapabilities(DynamicData):
      priorityClass: bool
      sourceMacAddress: bool
      vlanRange: bool

   class FcoeSpecification(DynamicData):
      underlyingPnic: str
      priorityClass: Optional[int] = None
      sourceMac: Optional[str] = None
      vlanRange: list[VlanRange] = []

   priorityClass: int
   sourceMac: str
   vlanRange: list[VlanRange] = []
   capabilities: FcoeCapabilities
   fcoeActive: bool
