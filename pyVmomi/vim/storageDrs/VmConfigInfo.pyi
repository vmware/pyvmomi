# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import VirtualMachine

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.storageDrs import VirtualDiskAntiAffinityRuleSpec
from pyVmomi.vim.storageDrs import VirtualDiskRuleSpec

class VmConfigInfo(DynamicData):
   vm: Optional[VirtualMachine] = None
   enabled: Optional[bool] = None
   behavior: Optional[str] = None
   intraVmAffinity: Optional[bool] = None
   intraVmAntiAffinity: Optional[VirtualDiskAntiAffinityRuleSpec] = None
   virtualDiskRules: list[VirtualDiskRuleSpec] = []
