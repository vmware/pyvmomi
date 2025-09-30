# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.host.FirewallInfo import FirewallInfo

from pyVmomi.vim.host.Ruleset import Ruleset

class FirewallConfig(DynamicData):
   class RuleSetConfig(DynamicData):
      rulesetId: str
      enabled: bool
      allowedHosts: Optional[Ruleset.IpList] = None

   rule: list[RuleSetConfig] = []
   defaultBlockingPolicy: FirewallInfo.DefaultPolicy
