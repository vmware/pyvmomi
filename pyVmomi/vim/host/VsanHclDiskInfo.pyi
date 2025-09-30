# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vmodl.MethodFault import MethodFault

class VsanHclDiskInfo(DynamicData):
   deviceName: str
   model: Optional[str] = None
   isSsd: Optional[bool] = None
   vsanDisk: bool
   issues: list[MethodFault] = []
   remediableIssues: list[str] = []
   uuid: Optional[str] = None
   capacity: Optional[long] = None
   vsanCompatibility: list[str] = []
