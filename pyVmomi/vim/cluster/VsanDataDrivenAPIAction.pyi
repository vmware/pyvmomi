# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import KeyValue

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import LocalizableMessage

class VsanDataDrivenAPIAction(DynamicData):
   actionId: str
   actionLabel: LocalizableMessage
   actionDescription: LocalizableMessage
   enabled: bool
   parameters: list[KeyValue] = []
