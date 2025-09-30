# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.cluster.RuleSpec import RuleSpec

from pyVmomi.vim.storageDrs.AutomationConfig import AutomationConfig

from pyVmomi.vim.storageDrs.IoLoadBalanceConfig import IoLoadBalanceConfig

from pyVmomi.vim.storageDrs.OptionSpec import OptionSpec

from pyVmomi.vim.storageDrs.SpaceLoadBalanceConfig import SpaceLoadBalanceConfig

class PodConfigSpec(DynamicData):
   enabled: Optional[bool] = None
   ioLoadBalanceEnabled: Optional[bool] = None
   defaultVmBehavior: Optional[str] = None
   loadBalanceInterval: Optional[int] = None
   defaultIntraVmAffinity: Optional[bool] = None
   spaceLoadBalanceConfig: Optional[SpaceLoadBalanceConfig] = None
   ioLoadBalanceConfig: Optional[IoLoadBalanceConfig] = None
   automationOverrides: Optional[AutomationConfig] = None
   rule: list[RuleSpec] = []
   option: list[OptionSpec] = []
