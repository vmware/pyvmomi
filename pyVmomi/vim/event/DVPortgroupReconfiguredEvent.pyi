# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.dvs import DistributedVirtualPortgroup

from pyVmomi.vim.event import ChangesInfoEventArgument
from pyVmomi.vim.event import DVPortgroupEvent

class DVPortgroupReconfiguredEvent(DVPortgroupEvent):
   configSpec: DistributedVirtualPortgroup.ConfigSpec
   configChanges: Optional[ChangesInfoEventArgument] = None
