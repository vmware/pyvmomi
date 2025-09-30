# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vim.VirtualMachine import VirtualMachine

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vmodl.MethodFault import MethodFault

class VsanVcsaDeploymentProgress(DynamicData):
   phase: str
   progressPct: long
   message: str
   success: bool
   error: Optional[MethodFault] = None
   updateCounter: long
   taskId: Optional[str] = None
   vm: Optional[VirtualMachine] = None
