# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import KeyValue

from pyVmomi.vim.fault import OvfConsumerCallbackFault

class OvfConsumerFault(OvfConsumerCallbackFault):
   errorKey: str
   message: str
   params: list[KeyValue] = []
