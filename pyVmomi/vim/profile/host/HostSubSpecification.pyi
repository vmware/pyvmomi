# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.VmomiSupport import binary
from pyVmomi.VmomiSupport import byte

from pyVmomi.vmodl import DynamicData

class HostSubSpecification(DynamicData):
   name: str
   createdTime: datetime
   data: list[byte] = []
   binaryData: Optional[binary] = None
