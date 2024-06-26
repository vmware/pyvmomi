# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import KeyValue

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.cluster import StorageComplianceResult

class VsanObjectInformation(DynamicData):
   directoryName: Optional[str] = None
   vsanObjectUuid: Optional[str] = None
   vsanHealth: Optional[str] = None
   policyAttributes: list[KeyValue] = []
   spbmProfileUuid: Optional[str] = None
   spbmProfileGenerationId: Optional[str] = None
   spbmComplianceResult: Optional[StorageComplianceResult] = None
