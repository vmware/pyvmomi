# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.vApp import IPAssignmentInfo
from pyVmomi.vim.vApp import OvfSectionSpec
from pyVmomi.vim.vApp import ProductSpec
from pyVmomi.vim.vApp import PropertySpec

class VmConfigSpec(DynamicData):
   product: list[ProductSpec] = []
   property: list[PropertySpec] = []
   ipAssignment: Optional[IPAssignmentInfo] = None
   eula: list[str] = []
   ovfSection: list[OvfSectionSpec] = []
   ovfEnvironmentTransport: list[str] = []
   installBootRequired: Optional[bool] = None
   installBootStopDelay: Optional[int] = None
