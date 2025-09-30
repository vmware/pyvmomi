# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.vsan.VipDVswitchConfig import VipDVswitchConfig

from pyVmomi.vim.vsan.VipNetworkConfig import VipNetworkConfig

from pyVmomi.vim.vsan.VipVswitchConfig import VipVswitchConfig

class VipConfigSpec(DynamicData):
   enabled: Optional[bool] = None
   v4NetworkConfig: Optional[VipNetworkConfig] = None
   v6NetworkConfig: Optional[VipNetworkConfig] = None
   vswitchConfig: Optional[VipVswitchConfig] = None
   distributedSwitchConfig: Optional[VipDVswitchConfig] = None
