# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.eam import Agency
from pyVmomi.eam import Agent

from pyVmomi.vim import ManagedEntity

from pyVmomi.vmodl import KeyAnyValue

from pyVmomi.eam.issue import Issue

class ExtensibleIssue(Issue):
   typeId: str
   argument: list[KeyAnyValue] = []
   target: Optional[ManagedEntity] = None
   agent: Optional[Agent] = None
   agency: Optional[Agency] = None
