# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.event import Event

from pyVmomi.vim.fault import MigrationFault

class SnapshotRevertIssue(MigrationFault):
   snapshotName: Optional[str] = None
   event: list[Event] = []
   errors: bool
