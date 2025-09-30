# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.event.VmEvent import VmEvent

from pyVmomi.vim.vm.Message import Message

class VmMessageEvent(VmEvent):
   message: str
   messageInfo: list[Message] = []
