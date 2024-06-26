# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vmodl import DynamicData

class VsanCapability(DynamicData):
   target: Optional[ManagedObject] = None
   capabilities: list[str] = []
   statuses: list[str] = []
