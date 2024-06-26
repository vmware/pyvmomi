# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import VirtualMachine

from pyVmomi.vmodl import MethodFault

from pyVmomi.vim.fault import FtIssuesOnHost
from pyVmomi.vim.fault import VmFaultToleranceIssue

class PowerOnFtSecondaryFailed(VmFaultToleranceIssue):
   vm: VirtualMachine
   vmName: str
   hostSelectionBy: FtIssuesOnHost.HostSelectionType
   hostErrors: list[MethodFault] = []
   rootCause: MethodFault
