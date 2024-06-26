# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import MethodFault

class VsanKmsHealth(DynamicData):
   serverName: str
   health: str
   error: Optional[MethodFault] = None
   trustHealth: Optional[str] = None
   certHealth: Optional[str] = None
   certExpireDate: Optional[datetime] = None
