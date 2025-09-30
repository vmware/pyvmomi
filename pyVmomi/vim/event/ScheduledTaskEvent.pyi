# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vim.event.Event import Event

from pyVmomi.vim.event.ManagedEntityEventArgument import ManagedEntityEventArgument

from pyVmomi.vim.event.ScheduledTaskEventArgument import ScheduledTaskEventArgument

class ScheduledTaskEvent(Event):
   scheduledTask: ScheduledTaskEventArgument
   entity: ManagedEntityEventArgument
