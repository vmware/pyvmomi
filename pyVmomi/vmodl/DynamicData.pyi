# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import DataObject

from pyVmomi.vmodl import DynamicProperty

class DynamicData(DataObject):
   dynamicType: Optional[str] = None
   dynamicProperty: list[DynamicProperty] = []
