# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vim import DistributedVirtualSwitch
from pyVmomi.vim import HostSystem

from pyVmomi.vim.vsan import VsanNetworkConfigBaseIssue

class VsanNetworkConfigVswitchWithNoRedundancyIssue(VsanNetworkConfigBaseIssue):
   host: HostSystem
   vswitchName: Optional[str] = None
   vds: Optional[DistributedVirtualSwitch] = None
   numPnics: long
