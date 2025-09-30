# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.cluster.VsanDataDrivenAPIAction import VsanDataDrivenAPIAction

from pyVmomi.vim.cluster.VsanHealthActionBase import VsanHealthActionBase

from pyVmomi.vim.cluster.VsanHealthConfirmationDialog import VsanHealthConfirmationDialog

class VsanHealthDataDrivenAction(VsanHealthActionBase):
   apiAction: VsanDataDrivenAPIAction
   confirmation: Optional[VsanHealthConfirmationDialog] = None
