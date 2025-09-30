# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.cluster.DasAdmissionControlPolicy import DasAdmissionControlPolicy

from pyVmomi.vim.cluster.SlotPolicy import SlotPolicy

class FailoverLevelAdmissionControlPolicy(DasAdmissionControlPolicy):
   failoverLevel: int
   slotPolicy: Optional[SlotPolicy] = None
