# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.KeyValue import KeyValue

from pyVmomi.vim.fault.VimFault import VimFault

class ExtendedFault(VimFault):
   faultTypeId: str
   data: list[KeyValue] = []
