# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vim.DistributedVirtualSwitch import DistributedVirtualSwitch

from pyVmomi.vim.HostSystem import HostSystem

from pyVmomi.vim.vsan.VsanNetworkConfigBaseIssue import VsanNetworkConfigBaseIssue

class VsanNetworkConfigVswitchWithNoRedundancyIssue(VsanNetworkConfigBaseIssue):
   host: HostSystem
   vswitchName: Optional[str] = None
   vds: Optional[DistributedVirtualSwitch] = None
   numPnics: long
