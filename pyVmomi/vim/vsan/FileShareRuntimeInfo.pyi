# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vim.KeyValue import KeyValue

from pyVmomi.vmodl.DynamicData import DynamicData

class FileShareRuntimeInfo(DynamicData):
   usedCapacity: Optional[long] = None
   hostname: Optional[str] = None
   address: Optional[str] = None
   vsanObjectUuids: list[str] = []
   accessPoints: list[KeyValue] = []
   managedBy: Optional[str] = None
   fileServerFQDN: Optional[str] = None
