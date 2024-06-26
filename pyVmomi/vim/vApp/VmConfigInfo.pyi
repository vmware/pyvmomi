# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.vApp import IPAssignmentInfo
from pyVmomi.vim.vApp import OvfSectionInfo
from pyVmomi.vim.vApp import ProductInfo
from pyVmomi.vim.vApp import PropertyInfo

class VmConfigInfo(DynamicData):
   product: list[ProductInfo] = []
   property: list[PropertyInfo] = []
   ipAssignment: IPAssignmentInfo
   eula: list[str] = []
   ovfSection: list[OvfSectionInfo] = []
   ovfEnvironmentTransport: list[str] = []
   installBootRequired: bool
   installBootStopDelay: int
