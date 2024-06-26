# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim.fault import VmConfigFault

class NumVirtualCpusIncompatible(VmConfigFault):
   class Reason(Enum):
      recordReplay: ClassVar['Reason'] = 'recordReplay'
      faultTolerance: ClassVar['Reason'] = 'faultTolerance'

   reason: str
   numCpu: int
