# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vim.HostSystem import HostSystem

from pyVmomi.vim.vsan.VsanConfigBaseIssue import VsanConfigBaseIssue

class VsanConfigNotAllDisksClaimedIssue(VsanConfigBaseIssue):
   host: HostSystem
   disks: list[str] = []
