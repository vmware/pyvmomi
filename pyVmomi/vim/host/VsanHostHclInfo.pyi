# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import HostSystem

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import MethodFault

from pyVmomi.vim.host import VsanHclComputeResource
from pyVmomi.vim.host import VsanHclControllerInfo
from pyVmomi.vim.host import VsanHclNicInfo

class VsanHostHclInfo(DynamicData):
   hostname: str
   hclChecked: bool
   releaseName: Optional[str] = None
   error: Optional[MethodFault] = None
   controllers: list[VsanHclControllerInfo] = []
   pnics: list[VsanHclNicInfo] = []
   host: Optional[HostSystem] = None
   computeResource: Optional[VsanHclComputeResource] = None
   vsanHostCompatibility: list[str] = []
