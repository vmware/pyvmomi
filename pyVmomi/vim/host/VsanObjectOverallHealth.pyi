# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.cluster import StorageComplianceResult

from pyVmomi.vim.host import VsanObjectHealth

class VsanObjectOverallHealth(DynamicData):
   objectHealthDetail: list[VsanObjectHealth] = []
   objectsComplianceDetail: list[StorageComplianceResult] = []
   objectVersionCompliance: Optional[bool] = None
   objectFormatChangeRequiredUuids: list[str] = []
   objectsRelayoutBytes: Optional[long] = None
