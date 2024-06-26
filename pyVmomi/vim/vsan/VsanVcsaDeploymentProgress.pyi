# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vim import VirtualMachine

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import MethodFault

class VsanVcsaDeploymentProgress(DynamicData):
   phase: str
   progressPct: long
   message: str
   success: bool
   error: Optional[MethodFault] = None
   updateCounter: long
   taskId: Optional[str] = None
   vm: Optional[VirtualMachine] = None
