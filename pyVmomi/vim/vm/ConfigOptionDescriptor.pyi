# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.HostSystem import HostSystem

from pyVmomi.vmodl.DynamicData import DynamicData

class ConfigOptionDescriptor(DynamicData):
   key: str
   description: Optional[str] = None
   host: list[HostSystem] = []
   createSupported: bool
   defaultConfigOption: bool
   runSupported: bool
   upgradeSupported: bool
