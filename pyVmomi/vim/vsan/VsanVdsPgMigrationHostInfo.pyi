# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.HostSystem import HostSystem

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.vsan.VsanVdsPgMigrationVmInfo import VsanVdsPgMigrationVmInfo

class VsanVdsPgMigrationHostInfo(DynamicData):
   host: HostSystem
   hostname: str
   vmknicDevices: list[str] = []
   vmVnics: list[VsanVdsPgMigrationVmInfo] = []
