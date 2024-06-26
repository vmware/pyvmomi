# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.event import GeneralEvent

class ExtendedEvent(GeneralEvent):
   class Pair(DynamicData):
      key: str
      value: str

   eventTypeId: str
   managedObject: ManagedObject
   data: list[Pair] = []
