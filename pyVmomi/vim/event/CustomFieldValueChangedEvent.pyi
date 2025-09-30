# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.event.CustomFieldEvent import CustomFieldEvent

from pyVmomi.vim.event.ManagedEntityEventArgument import ManagedEntityEventArgument

class CustomFieldValueChangedEvent(CustomFieldEvent):
   entity: ManagedEntityEventArgument
   fieldKey: int
   name: str
   value: str
   prevState: Optional[str] = None
