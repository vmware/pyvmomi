# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

class ProductSpec(DynamicData):
   name: Optional[str] = None
   vendor: Optional[str] = None
   version: Optional[str] = None
   build: Optional[str] = None
   forwardingClass: Optional[str] = None
   bundleId: Optional[str] = None
   bundleUrl: Optional[str] = None
