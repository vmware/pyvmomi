# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.event.Event import Event

from pyVmomi.vim.fault.MigrationFault import MigrationFault

class SnapshotRevertIssue(MigrationFault):
   snapshotName: Optional[str] = None
   event: list[Event] = []
   errors: bool
