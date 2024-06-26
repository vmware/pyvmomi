# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import long
from pyVmomi.VmomiSupport import short

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import CpuIdInfo

class CpuPackage(DynamicData):
   class Vendor(Enum):
      unknown: ClassVar['Vendor'] = 'unknown'
      intel: ClassVar['Vendor'] = 'intel'
      amd: ClassVar['Vendor'] = 'amd'
      hygon: ClassVar['Vendor'] = 'hygon'
      arm: ClassVar['Vendor'] = 'arm'

   index: short
   vendor: str
   hz: long
   busHz: long
   description: str
   threadId: list[short] = []
   cpuFeature: list[CpuIdInfo] = []
   family: Optional[short] = None
   model: Optional[short] = None
   stepping: Optional[short] = None
