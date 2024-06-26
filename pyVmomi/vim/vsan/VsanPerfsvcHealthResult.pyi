# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.cluster import VsanObjectInformation
from pyVmomi.vim.cluster import VsanPerfNodeInformation

class VsanPerfsvcHealthResult(DynamicData):
   statsObjectInfo: Optional[VsanObjectInformation] = None
   statsObjectConsistent: Optional[bool] = None
   statsObjectPolicyConsistent: Optional[bool] = None
   datastoreCompatible: Optional[bool] = None
   enoughFreeSpace: Optional[bool] = None
   remediateAction: Optional[str] = None
   hostResults: list[VsanPerfNodeInformation] = []
   verboseModeStatus: Optional[bool] = None
