# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.cluster import RuleSpec

from pyVmomi.vim.storageDrs import AutomationConfig
from pyVmomi.vim.storageDrs import IoLoadBalanceConfig
from pyVmomi.vim.storageDrs import OptionSpec
from pyVmomi.vim.storageDrs import SpaceLoadBalanceConfig

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
