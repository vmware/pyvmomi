# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim.HostSystem import HostSystem

from pyVmomi.vmodl.MethodFault import MethodFault

from pyVmomi.vim.fault.VmFaultToleranceIssue import VmFaultToleranceIssue

class FtIssuesOnHost(VmFaultToleranceIssue):
   class HostSelectionType(Enum):
      user: ClassVar['HostSelectionType'] = 'user'
      vc: ClassVar['HostSelectionType'] = 'vc'
      drs: ClassVar['HostSelectionType'] = 'drs'

   host: HostSystem
   hostName: str
   errors: list[MethodFault] = []
