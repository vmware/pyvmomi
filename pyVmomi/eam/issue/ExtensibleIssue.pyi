# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.eam.Agency import Agency

from pyVmomi.eam.Agent import Agent

from pyVmomi.vim.ManagedEntity import ManagedEntity

from pyVmomi.vmodl.KeyAnyValue import KeyAnyValue

from pyVmomi.eam.issue.Issue import Issue

class ExtensibleIssue(Issue):
   typeId: str
   argument: list[KeyAnyValue] = []
   target: Optional[ManagedEntity] = None
   agent: Optional[Agent] = None
   agency: Optional[Agency] = None
