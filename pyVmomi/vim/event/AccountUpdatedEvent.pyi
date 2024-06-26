# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.event import HostEvent

from pyVmomi.vim.host import LocalAccountManager

class AccountUpdatedEvent(HostEvent):
   spec: LocalAccountManager.AccountSpecification
   group: bool
   prevDescription: Optional[str] = None
