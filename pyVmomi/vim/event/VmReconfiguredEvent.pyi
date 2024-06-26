# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.event import ChangesInfoEventArgument
from pyVmomi.vim.event import VmEvent

from pyVmomi.vim.vm import ConfigSpec

class VmReconfiguredEvent(VmEvent):
   configSpec: ConfigSpec
   configChanges: Optional[ChangesInfoEventArgument] = None
