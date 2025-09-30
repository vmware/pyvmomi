# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.vApp.IPAssignmentInfo import IPAssignmentInfo

from pyVmomi.vim.vApp.OvfSectionSpec import OvfSectionSpec

from pyVmomi.vim.vApp.ProductSpec import ProductSpec

from pyVmomi.vim.vApp.PropertySpec import PropertySpec

class VmConfigSpec(DynamicData):
   product: list[ProductSpec] = []
   property: list[PropertySpec] = []
   ipAssignment: Optional[IPAssignmentInfo] = None
   eula: list[str] = []
   ovfSection: list[OvfSectionSpec] = []
   ovfEnvironmentTransport: list[str] = []
   installBootRequired: Optional[bool] = None
   installBootStopDelay: Optional[int] = None
