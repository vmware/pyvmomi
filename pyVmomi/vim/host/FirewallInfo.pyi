# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import Ruleset

class FirewallInfo(DynamicData):
   class DefaultPolicy(DynamicData):
      incomingBlocked: Optional[bool] = None
      outgoingBlocked: Optional[bool] = None

   defaultPolicy: DefaultPolicy
   ruleset: list[Ruleset] = []
