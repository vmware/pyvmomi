# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.cluster.StorageComplianceResult import StorageComplianceResult

from pyVmomi.vim.host.VsanObjectHealth import VsanObjectHealth

class VsanObjectOverallHealth(DynamicData):
   objectHealthDetail: list[VsanObjectHealth] = []
   objectsComplianceDetail: list[StorageComplianceResult] = []
   objectVersionCompliance: Optional[bool] = None
   objectFormatChangeRequiredUuids: list[str] = []
   objectsRelayoutBytes: Optional[long] = None
   globalDedupStoreHealth: Optional[str] = None
