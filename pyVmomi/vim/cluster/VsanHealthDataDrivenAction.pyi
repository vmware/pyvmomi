# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.cluster import VsanDataDrivenAPIAction
from pyVmomi.vim.cluster import VsanHealthActionBase
from pyVmomi.vim.cluster import VsanHealthConfirmationDialog

class VsanHealthDataDrivenAction(VsanHealthActionBase):
   apiAction: VsanDataDrivenAPIAction
   confirmation: Optional[VsanHealthConfirmationDialog] = None
