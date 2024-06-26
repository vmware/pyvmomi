# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.dvs import DistributedVirtualPort

from pyVmomi.vim.event import DvsEvent

class DvsPortLinkUpEvent(DvsEvent):
   portKey: str
   runtimeInfo: Optional[DistributedVirtualPort.RuntimeInfo] = None
