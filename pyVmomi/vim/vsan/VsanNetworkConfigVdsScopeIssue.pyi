# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vim.DistributedVirtualSwitch import DistributedVirtualSwitch

from pyVmomi.vim.HostSystem import HostSystem

from pyVmomi.vim.vsan.VsanNetworkConfigBaseIssue import VsanNetworkConfigBaseIssue

class VsanNetworkConfigVdsScopeIssue(VsanNetworkConfigBaseIssue):
   vds: DistributedVirtualSwitch
   memberHosts: list[HostSystem] = []
   nonMemberHosts: list[HostSystem] = []
