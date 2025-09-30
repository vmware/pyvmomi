# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vim.HostSystem import HostSystem

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vmodl.MethodFault import MethodFault

from pyVmomi.vim.fault.DvsFault import DvsFault

class DvsOperationBulkFault(DvsFault):
   class FaultOnHost(DynamicData):
      host: HostSystem
      fault: MethodFault

   hostFault: list[FaultOnHost] = []
