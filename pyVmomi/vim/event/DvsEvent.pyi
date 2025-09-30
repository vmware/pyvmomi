# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim.event.Event import Event

class DvsEvent(Event):
   class PortBlockState(Enum):
      unset: ClassVar['PortBlockState'] = 'unset'
      blocked: ClassVar['PortBlockState'] = 'blocked'
      unblocked: ClassVar['PortBlockState'] = 'unblocked'
      unknown: ClassVar['PortBlockState'] = 'unknown'
