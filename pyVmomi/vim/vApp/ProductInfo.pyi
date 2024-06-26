# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

class ProductInfo(DynamicData):
   key: int
   classId: Optional[str] = None
   instanceId: Optional[str] = None
   name: Optional[str] = None
   vendor: Optional[str] = None
   version: Optional[str] = None
   fullVersion: Optional[str] = None
   vendorUrl: Optional[str] = None
   productUrl: Optional[str] = None
   appUrl: Optional[str] = None
