# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.cluster.RuleInfo import RuleInfo

from pyVmomi.vim.option.OptionValue import OptionValue

from pyVmomi.vim.storageDrs.AutomationConfig import AutomationConfig

from pyVmomi.vim.storageDrs.IoLoadBalanceConfig import IoLoadBalanceConfig

from pyVmomi.vim.storageDrs.SpaceLoadBalanceConfig import SpaceLoadBalanceConfig

class PodConfigInfo(DynamicData):
   class Behavior(Enum):
      manual: ClassVar['Behavior'] = 'manual'
      automated: ClassVar['Behavior'] = 'automated'

   enabled: bool
   ioLoadBalanceEnabled: bool
   defaultVmBehavior: str
   loadBalanceInterval: Optional[int] = None
   defaultIntraVmAffinity: Optional[bool] = None
   spaceLoadBalanceConfig: Optional[SpaceLoadBalanceConfig] = None
   ioLoadBalanceConfig: Optional[IoLoadBalanceConfig] = None
   automationOverrides: Optional[AutomationConfig] = None
   rule: list[RuleInfo] = []
   option: list[OptionValue] = []
