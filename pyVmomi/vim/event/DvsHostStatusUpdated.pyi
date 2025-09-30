# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.event.DvsEvent import DvsEvent

from pyVmomi.vim.event.HostEventArgument import HostEventArgument

class DvsHostStatusUpdated(DvsEvent):
   hostMember: HostEventArgument
   oldStatus: Optional[str] = None
   newStatus: Optional[str] = None
   oldStatusDetail: Optional[str] = None
   newStatusDetail: Optional[str] = None
