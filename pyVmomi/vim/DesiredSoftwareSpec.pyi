# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

class DesiredSoftwareSpec(DynamicData):
   class BaseImageSpec(DynamicData):
      version: str

   class VendorAddOnSpec(DynamicData):
      name: str
      version: str

   class ComponentSpec(DynamicData):
      name: str
      version: Optional[str] = None

   baseImageSpec: BaseImageSpec
   vendorAddOnSpec: Optional[VendorAddOnSpec] = None
   components: list[ComponentSpec] = []
   removedComponents: list[str] = []
