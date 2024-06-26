# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.cluster import RuleInfo

class VmHostRuleInfo(RuleInfo):
   vmGroupName: Optional[str] = None
   affineHostGroupName: Optional[str] = None
   antiAffineHostGroupName: Optional[str] = None
