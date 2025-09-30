# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.vApp.IPAssignmentInfo import IPAssignmentInfo

from pyVmomi.vim.vApp.OvfSectionInfo import OvfSectionInfo

from pyVmomi.vim.vApp.ProductInfo import ProductInfo

from pyVmomi.vim.vApp.PropertyInfo import PropertyInfo

class VmConfigInfo(DynamicData):
   product: list[ProductInfo] = []
   property: list[PropertyInfo] = []
   ipAssignment: IPAssignmentInfo
   eula: list[str] = []
   ovfSection: list[OvfSectionInfo] = []
   ovfEnvironmentTransport: list[str] = []
   installBootRequired: bool
   installBootStopDelay: int
