# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.event import VmEvent

from pyVmomi.vim.vm import Message

class VmMessageWarningEvent(VmEvent):
   message: str
   messageInfo: list[Message] = []
