# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.event import PermissionEvent
from pyVmomi.vim.event import RoleEventArgument

class PermissionUpdatedEvent(PermissionEvent):
   role: RoleEventArgument
   propagate: bool
   prevRole: Optional[RoleEventArgument] = None
   prevPropagate: Optional[bool] = None
