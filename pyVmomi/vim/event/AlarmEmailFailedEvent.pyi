# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vmodl.MethodFault import MethodFault

from pyVmomi.vim.event.AlarmEvent import AlarmEvent

from pyVmomi.vim.event.ManagedEntityEventArgument import ManagedEntityEventArgument

class AlarmEmailFailedEvent(AlarmEvent):
   entity: ManagedEntityEventArgument
   to: str
   reason: MethodFault
