# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import LocalizableMessage

from pyVmomi.vim.vsan.host import DataInTransitEncryptionInfo

class VsanDitEncryptionHealthSummary(DynamicData):
   hostname: Optional[str] = None
   health: Optional[str] = None
   reason: Optional[LocalizableMessage] = None
   ditEncryptionInfo: Optional[DataInTransitEncryptionInfo] = None
