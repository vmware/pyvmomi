# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vmodl.MethodFault import MethodFault

from pyVmomi.vim.fault.DvsFault import DvsFault

class ImportOperationBulkFault(DvsFault):
   class FaultOnImport(DynamicData):
      entityType: Optional[str] = None
      key: Optional[str] = None
      fault: MethodFault

   importFaults: list[FaultOnImport] = []
