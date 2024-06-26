# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import DistributedVirtualSwitch
from pyVmomi.vim import VirtualMachine

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.vsan import VsanVdsPgMigrationSpec

class VsanVdsMigrationPlan(DynamicData):
   vdsSpec: DistributedVirtualSwitch.CreateSpec
   pgs: list[VsanVdsPgMigrationSpec] = []
   inaccessibleVms: list[VirtualMachine] = []
   infraVms: list[VirtualMachine] = []
