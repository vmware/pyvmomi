# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.dvs.DistributedVirtualPortgroup import DistributedVirtualPortgroup

from pyVmomi.vim.event.ChangesInfoEventArgument import ChangesInfoEventArgument

from pyVmomi.vim.event.DVPortgroupEvent import DVPortgroupEvent

class DVPortgroupReconfiguredEvent(DVPortgroupEvent):
   configSpec: DistributedVirtualPortgroup.ConfigSpec
   configChanges: Optional[ChangesInfoEventArgument] = None
