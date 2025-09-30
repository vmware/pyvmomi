# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.Datacenter import Datacenter

from pyVmomi.vim.ManagedEntity import ManagedEntity

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.fault.MigrationFault import MigrationFault

class DatacenterMismatch(MigrationFault):
   class Argument(DynamicData):
      entity: ManagedEntity
      inputDatacenter: Optional[Datacenter] = None

   invalidArgument: list[Argument] = []
   expectedDatacenter: Datacenter
