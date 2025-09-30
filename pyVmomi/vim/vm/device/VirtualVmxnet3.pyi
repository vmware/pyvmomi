# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.vm.device.VirtualVmxnet import VirtualVmxnet

class VirtualVmxnet3(VirtualVmxnet):
   class StrictLatencyConfig(DynamicData):
      class DisableOffload(Enum):
         NONE: ClassVar['DisableOffload'] = 'NONE'
         TSO: ClassVar['DisableOffload'] = 'TSO'
         LRO: ClassVar['DisableOffload'] = 'LRO'
         TSO_LRO: ClassVar['DisableOffload'] = 'TSO_LRO'

      allowed: Optional[bool] = None
      measureLatency: Optional[bool] = None
      maxTxQueues: Optional[int] = None
      maxRxQueues: Optional[int] = None
      txDataRingDescSize: Optional[int] = None
      rxDataRingDescSize: Optional[int] = None
      disableOffload: Optional[str] = None

   uptv2Enabled: Optional[bool] = None
   strictLatencyConfig: Optional[StrictLatencyConfig] = None
