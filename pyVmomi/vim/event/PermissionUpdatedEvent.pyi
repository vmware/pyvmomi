# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.event.PermissionEvent import PermissionEvent

from pyVmomi.vim.event.RoleEventArgument import RoleEventArgument

class PermissionUpdatedEvent(PermissionEvent):
   role: RoleEventArgument
   propagate: bool
   prevRole: Optional[RoleEventArgument] = None
   prevPropagate: Optional[bool] = None
