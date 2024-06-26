# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.event import CustomFieldEvent
from pyVmomi.vim.event import ManagedEntityEventArgument

class CustomFieldValueChangedEvent(CustomFieldEvent):
   entity: ManagedEntityEventArgument
   fieldKey: int
   name: str
   value: str
   prevState: Optional[str] = None
