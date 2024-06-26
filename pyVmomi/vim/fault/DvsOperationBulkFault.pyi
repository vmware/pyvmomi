# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vim import HostSystem

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import MethodFault

from pyVmomi.vim.fault import DvsFault

class DvsOperationBulkFault(DvsFault):
   class FaultOnHost(DynamicData):
      host: HostSystem
      fault: MethodFault

   hostFault: list[FaultOnHost] = []
