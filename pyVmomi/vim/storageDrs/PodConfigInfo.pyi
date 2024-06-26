# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.cluster import RuleInfo

from pyVmomi.vim.option import OptionValue

from pyVmomi.vim.storageDrs import AutomationConfig
from pyVmomi.vim.storageDrs import IoLoadBalanceConfig
from pyVmomi.vim.storageDrs import SpaceLoadBalanceConfig

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
