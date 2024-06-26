# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import KeyAnyValue
from pyVmomi.vmodl import MethodFault

from pyVmomi.vim.event import Event

class EventEx(Event):
   eventTypeId: str
   severity: Optional[str] = None
   message: Optional[str] = None
   arguments: list[KeyAnyValue] = []
   objectId: Optional[str] = None
   objectType: Optional[type] = None
   objectName: Optional[str] = None
   fault: Optional[MethodFault] = None
