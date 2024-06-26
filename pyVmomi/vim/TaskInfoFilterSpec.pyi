# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

class TaskInfoFilterSpec(DynamicData):
   class FilterTaskResults(DynamicData):
      removeAll: Optional[bool] = None
      descriptionIds: list[str] = []
      filterIn: Optional[bool] = None

   filterTaskResults: Optional[FilterTaskResults] = None
