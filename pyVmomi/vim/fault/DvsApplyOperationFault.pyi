# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import MethodFault

from pyVmomi.vim.fault import DvsFault

class DvsApplyOperationFault(DvsFault):
   class FaultOnObject(DynamicData):
      objectId: str
      type: type
      fault: MethodFault

   objectFault: list[FaultOnObject] = []
