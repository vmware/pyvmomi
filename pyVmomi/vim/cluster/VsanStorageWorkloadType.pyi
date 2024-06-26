# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import VsanVmdkLoadTestSpec

class VsanStorageWorkloadType(DynamicData):
   specs: list[VsanVmdkLoadTestSpec] = []
   typeId: str
   name: str
   description: str
   duration: Optional[long] = None
