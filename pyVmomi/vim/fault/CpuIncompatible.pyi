# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import HostSystem

from pyVmomi.vim.fault import VirtualHardwareCompatibilityIssue

class CpuIncompatible(VirtualHardwareCompatibilityIssue):
   level: int
   registerName: str
   registerBits: Optional[str] = None
   desiredBits: Optional[str] = None
   host: Optional[HostSystem] = None
