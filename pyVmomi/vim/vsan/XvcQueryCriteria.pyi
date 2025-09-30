# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicArray import DynamicArray

from pyVmomi.vmodl.DynamicData import DynamicData

class XvcQueryCriteria(DynamicData):
   property: str
   operator: Optional[str] = None
   comparableValue: Optional[object] = None
   comparableList: Optional[DynamicArray] = None
   ignoreCase: Optional[bool] = None
