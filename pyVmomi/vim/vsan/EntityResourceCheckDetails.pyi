# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData

class EntityResourceCheckDetails(DynamicData):
   name: Optional[str] = None
   uuid: Optional[str] = None
   isNew: Optional[bool] = None
   capacity: Optional[long] = None
   postOperationCapacity: Optional[long] = None
   usedCapacity: Optional[long] = None
   postOperationUsedCapacity: Optional[long] = None
   additionalRequiredCapacity: Optional[long] = None
   maxComponents: Optional[long] = None
   components: Optional[long] = None
