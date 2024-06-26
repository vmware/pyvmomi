# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.event import DvsEvent
from pyVmomi.vim.event import HostEventArgument

class DvsHostStatusUpdated(DvsEvent):
   hostMember: HostEventArgument
   oldStatus: Optional[str] = None
   newStatus: Optional[str] = None
   oldStatusDetail: Optional[str] = None
   newStatusDetail: Optional[str] = None
