# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vmodl.LocalizableMessage import LocalizableMessage

from pyVmomi.vim.vsan.host.DataInTransitEncryptionInfo import DataInTransitEncryptionInfo

class VsanDitEncryptionHealthSummary(DynamicData):
   hostname: Optional[str] = None
   health: Optional[str] = None
   reason: Optional[LocalizableMessage] = None
   ditEncryptionInfo: Optional[DataInTransitEncryptionInfo] = None
