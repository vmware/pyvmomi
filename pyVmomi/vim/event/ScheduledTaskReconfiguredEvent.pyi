# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.event.ChangesInfoEventArgument import ChangesInfoEventArgument

from pyVmomi.vim.event.ScheduledTaskEvent import ScheduledTaskEvent

class ScheduledTaskReconfiguredEvent(ScheduledTaskEvent):
   configChanges: Optional[ChangesInfoEventArgument] = None
