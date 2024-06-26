# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import QualifiedName
from pyVmomi.vim.host import SystemIdentificationInfo

class SystemInfo(DynamicData):
   vendor: str
   model: str
   uuid: str
   otherIdentifyingInfo: list[SystemIdentificationInfo] = []
   serialNumber: Optional[str] = None
   qualifiedName: list[QualifiedName] = []
   vvolHostNQN: Optional[QualifiedName] = None
   vvolHostId: Optional[str] = None
   bootCommandLine: Optional[str] = None
