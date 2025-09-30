# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vim.HostSystem import HostSystem

from pyVmomi.vim.fault.MigrationFault import MigrationFault

class MigrationFeatureNotSupported(MigrationFault):
   atSourceHost: bool
   failedHostName: str
   failedHost: HostSystem
