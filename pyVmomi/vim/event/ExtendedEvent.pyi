# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.event.GeneralEvent import GeneralEvent

class ExtendedEvent(GeneralEvent):
   class Pair(DynamicData):
      key: str
      value: str

   eventTypeId: str
   managedObject: ManagedObject
   data: list[Pair] = []
