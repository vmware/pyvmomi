# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.vim import HostSystem

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import KeyAnyValue

class VsanNetworkDiagnostics(DynamicData):
   host: HostSystem
   eventTypeId: str
   severity: str
   createdTime: datetime
   arguments: list[KeyAnyValue] = []
