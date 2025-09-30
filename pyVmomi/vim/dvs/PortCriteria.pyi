# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.HostSystem import HostSystem

from pyVmomi.vim.ManagedEntity import ManagedEntity

from pyVmomi.vmodl.DynamicData import DynamicData

class PortCriteria(DynamicData):
   connected: Optional[bool] = None
   active: Optional[bool] = None
   uplinkPort: Optional[bool] = None
   nsxPort: Optional[bool] = None
   scope: Optional[ManagedEntity] = None
   portgroupKey: list[str] = []
   inside: Optional[bool] = None
   portKey: list[str] = []
   host: list[HostSystem] = []
