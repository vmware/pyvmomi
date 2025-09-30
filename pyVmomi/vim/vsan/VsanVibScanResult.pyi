# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.HostSystem import HostSystem

from pyVmomi.vmodl.DynamicData import DynamicData

class VsanVibScanResult(DynamicData):
   host: HostSystem
   vibName: str
   vibVersion: str
   existingVersion: Optional[str] = None
   maintenanceModeRequired: bool
   rebootRequired: bool
   meetsSystemReq: bool
   pkgDepsMetByHost: bool
