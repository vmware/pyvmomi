# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.dvs import VmwareDistributedVirtualSwitch

from pyVmomi.vim.vsan import VsanVdsPgMigrationHostInfo

class VsanVdsPgMigrationSpec(DynamicData):
   vssPgName: str
   dvPgName: str
   vdsPgSetting: VmwareDistributedVirtualSwitch.VmwarePortConfigPolicy
   vdsPgType: str
   hosts: list[VsanVdsPgMigrationHostInfo] = []
   collisionRename: bool
