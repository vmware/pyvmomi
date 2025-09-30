# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.HostSystem import HostSystem

from pyVmomi.vim.cluster.RuleInfo import RuleInfo

from pyVmomi.vim.fault.VmConfigFault import VmConfigFault

class RuleViolation(VmConfigFault):
   host: Optional[HostSystem] = None
   rule: RuleInfo
