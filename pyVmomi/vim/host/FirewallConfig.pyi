# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import FirewallInfo
from pyVmomi.vim.host import Ruleset

class FirewallConfig(DynamicData):
   class RuleSetConfig(DynamicData):
      rulesetId: str
      enabled: bool
      allowedHosts: Optional[Ruleset.IpList] = None

   rule: list[RuleSetConfig] = []
   defaultBlockingPolicy: FirewallInfo.DefaultPolicy
