# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import VsanVmdkLoadTestSpec

class VsanVmdkLoadTestResult(DynamicData):
   success: bool
   faultMessage: Optional[str] = None
   spec: VsanVmdkLoadTestSpec
   actualDurationSec: Optional[int] = None
   totalBytes: Optional[long] = None
   iops: Optional[long] = None
   tputBps: Optional[long] = None
   avgLatencyUs: Optional[long] = None
   maxLatencyUs: Optional[long] = None
   numIoAboveLatencyThreshold: Optional[long] = None
