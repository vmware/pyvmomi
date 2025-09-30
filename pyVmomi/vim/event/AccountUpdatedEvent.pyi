# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.event.HostEvent import HostEvent

from pyVmomi.vim.host.LocalAccountManager import LocalAccountManager

class AccountUpdatedEvent(HostEvent):
   spec: LocalAccountManager.AccountSpecification
   group: bool
   prevDescription: Optional[str] = None
